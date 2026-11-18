# Imported Mastery Academy website

## Scope
- Preserve the imported Framer site's HTML, CSS, assets, and existing structure.
- This is a static export, not the original Framer editing project.

## Running on Replit
- Run workflow: **Start application**.
- Command: `python3 server.py`.
- The server binds to `0.0.0.0:5000` by default; `PORT` may override it.
- No package installation, build step, database, or secrets are required.
- Only the homepage, stylesheet, and assets are served. Workspace files and the
  source ZIP are not public. JavaScript modules use the correct MIME type.

## External dependencies
- The imported page still includes third-party tracking scripts and links to
  external services. Running the export does not transfer ownership of those
  services or guarantee that their endpoints work.
- Check contact actions and other external integrations separately before using
  this export as a replacement for the original live site.

## Setup verification
- Confirmed the homepage renders in the browser and the proxied URL responds.
- All 72 local resource paths referenced directly by the HTML exist.
- Styles and module scripts return their expected content types.
- Configuration files, source ZIP, and directory listings return 404.
- The unchanged export reports Google Tag Manager / Facebook script errors,
  duplicate Hotjar tracking, and recoverable React hydration warnings.
- Its Cloudflare analytics POST to `/cdn-cgi/rum` has no local backend and
  returns 501. No analytics or form backend has been invented for the export.
- Contact submissions and other external interactions have not been tested.
