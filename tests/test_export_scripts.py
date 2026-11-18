"""Regression checks for tracking code captured by the site exporter."""

import unittest
from html.parser import HTMLParser
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class ScriptParser(HTMLParser):
    def __init__(self, html):
        super().__init__()
        self.scripts = []
        self.active = None
        self.feed(html)

    def handle_starttag(self, tag, attrs):
        if tag == "script":
            self.active = {"attrs": dict(attrs), "body": ""}
            self.scripts.append(self.active)

    def handle_data(self, data):
        if self.active is not None:
            self.active["body"] += data

    def handle_endtag(self, tag):
        if tag == "script":
            self.active = None


class ExportScriptTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.scripts = ScriptParser((ROOT / "index.html").read_text()).scripts
        cls.inline = "\n".join(script["body"] for script in cls.scripts)

    def test_no_captured_tag_manager_internal_calls(self):
        self.assertNotIn('google_tag_manager["rm"]', self.inline)

    def test_each_tracker_has_one_bootstrap(self):
        self.assertEqual(self.inline.count('fbq("init",'), 1)
        self.assertEqual(self.inline.count('a.load("CHAO8OJC77UEQOU9GK40")'), 1)
        self.assertEqual(self.inline.count("a._hjSettings={"), 1)

    def test_no_preloaded_tracking_runtime_or_cloudflare_beacon(self):
        for script in self.scripts:
            attrs = script["attrs"]
            src = attrs.get("src", "")
            self.assertFalse(src.startswith(("https://static.hotjar.com/",
                                             "https://script.hotjar.com/")))
            self.assertNotIn("data-cf-beacon", attrs)
            if src:
                self.assertEqual(src, "assets/js/script_main.DBd7kMom.mjs")

    def test_framer_application_still_loads(self):
        bundles = [s for s in self.scripts
                   if s["attrs"].get("data-framer-bundle") == "main"]
        self.assertEqual(len(bundles), 1)
        self.assertTrue((ROOT / bundles[0]["attrs"]["src"]).is_file())


if __name__ == "__main__":
    unittest.main()
