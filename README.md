# PrimeLink Technologies

A responsive, static ICT company website using HTML5, CSS3 and vanilla JavaScript. Open `index.html` directly; no build, installation, database or backend is needed. The redesigned site uses a dark navy visual identity, realistic technology imagery and a connected service ecosystem.

## Files

- `index.html`: all website sections, metadata and enquiry form.
- `css/style.css`: brand variables, layouts, responsive rules and reduced-motion support.
- `js/script.js`: mobile navigation, active section indication, keyboard-accessible environment tabs, contextual enquiries, validation and WhatsApp message preparation.
- `assets/logo/primelink.webp`: unchanged horizontal logo cropped from `media/logo.jpg`.
- `assets/logo/favicon.png`: cropped original brand symbol.
- `assets/logo/primelink-roundel.webp`: unchanged circular logo cropped from the original brand sheet, used in the header, footer and connected ecosystem.
- `assets/images/*.webp`: optimized hero and eight coordinated technology service images. The hero has two responsive sizes; the service images are lazy-loaded and reused in the environment panels.
- `assets/images/infrastructure.svg`: preserved original vector illustration from the previous design.
- `media/logo.jpg`: original brand image, preserved.
- `build_site.py`: development-only HTML generator; not required to run or deploy. If editing HTML directly, do not rerun the generator unless those edits are also incorporated there.
- `site_components.py`: shared static HTML components and service/environment data for the optional generator. Run `python build_site.py` only when regenerating the checked-in HTML during development.
- `verify_chrome.py`: development-only checks using Python and locally installed Chrome. Run `python verify_chrome.py` on Windows to check all seven requested viewport widths, local links, menu behavior, environment tabs and WhatsApp validation. Preview files are written to the ignored `qa-output` directory. Python is not used by the website.

## Brand

The supplied brand image establishes a deep navy wordmark and layered medium-blue/cyan symbol. The redesign extends the original navy `#092b43` into a midnight background `#061321`, with secondary blue `#205979`, action blue and lighter cyan `#68d1f0` for readable highlights on dark surfaces. The original circular logo was cropped and proportionally displayed without recoloring or redrawing. System sans-serif typography keeps the site fast and consistent with the wordmark. The brief's `image_5.png` was not present in the workspace; the provided logo and written design direction guided the design.

The technology visuals are original AI-generated conceptual illustrations, not photographs of company installations, product listings or endorsements. They share navy lighting and realistic materials. The optimized image set is approximately 620 KB. The original hero artwork and QA previews stay in the ignored `qa-output` directory and are not needed for deployment.

## Publish on GitHub Pages

1. Sign in to GitHub and create a public repository. To use the supplied site address, create or use `portfolio.github.io` under the `johnbett068` account. Back up any existing site before replacing its files.
2. Use **Add file → Upload files**, or Git, to upload `index.html`, `css`, `js`, `assets`, and `media` to the repository root. Keep folder names and capitalization intact. Commit to `main`.
3. Open repository **Settings → Pages**.
4. Under **Build and deployment**, choose **Deploy from a branch**, then **main** and **/(root)**. Save.
5. Wait for the Pages deployment to finish, then open the address shown in Settings. With the account and repository above, it is `https://johnbett068.github.io/portfolio.github.io/`.

All local asset links are relative and support a GitHub Pages project path. If you use a different address, update the canonical URL, `og:url`, and `og:image` in `index.html` (and in the optional generator). No build command or custom workflow is required. The deployment files can also be hosted on any static web server.

## Enquiries

The form validates required fields and prepares an encoded WhatsApp message addressed to `254720394517`. It opens WhatsApp in a new tab; the visitor must review and press Send there. It does not claim delivery, submit to a server or save personal details in browser storage. A visible fallback link appears if the tab is blocked. Telephone, email and direct WhatsApp links work independently of the form. A connection and a WhatsApp account are needed to send the enquiry.

## Accessibility and performance

Semantic sections, a skip link, visible keyboard focus, labelled fields, accessible menu state, Escape-to-close navigation, reduced-motion support and responsive layouts are included. Environment tabs support arrow keys, Home and End; all panels remain available if JavaScript is disabled. Service links preselect the enquiry service, and environment links add context without overwriting an existing message. Connection animations are finite and respect reduced motion.

There are no third-party scripts, fonts, trackers or runtime dependencies. The hero uses responsive WebP images with high fetch priority; images below the fold are lazy-loaded with explicit dimensions. The site needs no build, backend, CDN or external image provider. No Lighthouse score is claimed without a measured audit.
