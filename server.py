"""Serve the imported site without exposing workspace or configuration files."""

import mimetypes
import os
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parent
mimetypes.add_type("text/javascript", ".mjs")
mimetypes.add_type("font/woff2", ".woff2")


class SiteHandler(SimpleHTTPRequestHandler):
    def send_head(self):
        path = unquote(urlsplit(self.path).path)
        target = (ROOT / path.lstrip("/")).resolve()
        public_file = target in {ROOT / "index.html", ROOT / "styles.css"}
        public_asset = target.is_relative_to(ROOT / "assets")
        if path == "/":
            return super().send_head()
        if not (public_file or public_asset) or not target.is_file():
            self.send_error(404, "File not found")
            return None
        return super().send_head()

    def guess_type(self, path):
        # The export includes extensionless JavaScript tracking bundles.
        if Path(path).is_relative_to(ROOT / "assets" / "js"):
            return "text/javascript"
        return super().guess_type(path)

    def end_headers(self):
        self.send_header("Cache-Control", "no-cache")
        self.send_header("X-Content-Type-Options", "nosniff")
        super().end_headers()


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "5000"))
    handler = partial(SiteHandler, directory=str(ROOT))
    server = ThreadingHTTPServer(("0.0.0.0", port), handler)
    print(f"Serving imported site on port {port}", flush=True)
    server.serve_forever()
