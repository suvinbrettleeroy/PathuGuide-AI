# PathGuide logo assets

Source: `PathGuide Logo.png`, supplied by the project owner (1254 × 1254 px). `pathguide-logo-master.png` is an untouched copy of it. Keep it for regenerating the other files.

| File | Used for |
|---|---|
| `pathguide-logo-128.webp`, `-256.webp`, `-512.webp` | The badge on every page (navbar, footers, load and page-transition curtains, admin sidebar and top bar, laptop screen on the admin login). The browser picks a size through `srcset`. |
| `favicon-32.png`, `favicon-192.png` | Browser tab and Android icons (linked from `base.html` and `admin_dashboard.html`) |
| `apple-touch-icon.png` | iOS home-screen icon (180 px, white background) |

The WebP files are circular cut-outs of the master (centre 622.5, 638.5; radius 616 px) with an anti-aliased edge and transparent corners.

- Markup: `templates/partials/pg_logo.html` (macro `pg_logo`)
- Size, halo, orbit, sheen and hover motion: `static/css/brand.css`

To change the logo, regenerate these files from a new master and keep the same file names.
