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
- Local resource paths referenced directly by the HTML were checked at setup.
- Styles and module scripts return their expected content types.
- Configuration files, source ZIP, and directory listings return 404.
- Removed captured tracking runtimes, duplicate TikTok initialization, duplicate
  Hotjar scripts, and a captured Google Tag Manager internal-function call that
  caused uncaught browser errors. The normal tracker bootstrap snippets remain.
- Removed the production-only Cloudflare beacon rather than inventing a local
  analytics endpoint.
- Desktop and mobile homepage renders were checked after the fix. Non-script
  HTML was compared against the original ZIP and is unchanged.
- Recoverable React hydration warnings and a blocked original-domain Framer
  editor iframe remain; the exported site renders despite these limitations.
- Contact submissions and other external interactions have not been tested.

## Regression checks
- Run `python3 -m unittest discover -s tests -v`.
- Checks prevent captured tracker runtimes, duplicate initialization, and calls
  to private Google Tag Manager internals from being restored accidentally.
