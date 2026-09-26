# Frontend HTML Practice

A small introductory HTML exercise for learning page structure and navigation between static files.

This repository captures an early learning stage. It is not a finished portfolio site or a production-ready frontend application.

## Files

| File | Current purpose |
| --- | --- |
| `index.html` | Responsive home page and learning goals |
| `blog_list.html` | Accessible empty state for future learning posts |
| `about_me.html` | Project scope and practiced frontend concepts |
| `styles.css` | Shared responsive layout, focus states, and visual design |
| `scripts/validate_html.py` | Dependency-free HTML structure and local-link validation |

The Home, Blog, and About Me links use relative paths so the pages can be browsed without a framework or build step.

## Run locally

You can open `index.html` directly in a browser. To serve the directory over HTTP, run:

```bash
python -m http.server 8000
```

Then visit:

```text
http://localhost:8000/index.html
```

Stop the development server with `Ctrl+C`.

## Verification

Run the dependency-free validator with Python 3.9 or newer:

```bash
python scripts/validate_html.py
```

It checks language and viewport metadata, page titles, main landmarks, H1 cardinality, labelled navigation, the current-page link, the shared stylesheet, and every local link. GitHub Actions runs the same validation for pull requests and pushes to `main`.

## Current scope

- The Blog intentionally remains an accessible empty state until the first real learning post is written.
- The site has no JavaScript, framework, package dependency, form, backend, analytics, or production deployment.
- Automated validation covers document contracts and local links; keyboard navigation and visual layout still require browser review.

## Scope

The source is intentionally framework-free so that HTML structure, relative links, responsive CSS, and focus behavior remain visible. Later application work is represented by the more complete projects linked from the owner's GitHub profile.
