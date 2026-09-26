# Frontend HTML Practice

A small introductory HTML exercise for learning page structure and navigation between static files.

This repository captures an early learning stage. It is not a finished portfolio site or a production-ready frontend application.

## Files

| File | Current purpose |
| --- | --- |
| `index.html` | Home page with shared navigation and heading examples |
| `blog_list.html` | Blog placeholder with a small inline CSS experiment |
| `about_me.html` | Reserved About Me page; currently empty |

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

## Current limitations

- `about_me.html` has not been implemented.
- The Blog page contains placeholder content rather than posts.
- Styling is an inline experiment and includes a `front-size` declaration that browsers ignore; the valid CSS property is `font-size`.
- The pages do not yet define language, character encoding, responsive viewport metadata, or accessibility landmarks beyond the basic navigation element.
- There is no automated test, formatter, deployment, or dependency setup.

## Suggested learning steps

1. Add a valid HTML document to `about_me.html` and keep navigation consistent across pages.
2. Add `lang`, UTF-8 charset, and responsive viewport metadata.
3. Correct the invalid CSS property and move shared styles into a stylesheet.
4. Add meaningful page content and accessible link or heading labels.
5. Validate the pages with an HTML validator and test keyboard navigation.
6. Add a lightweight deployment only after the static pages are complete.

## Scope

The source is intentionally framework-free so that HTML structure, relative links, and basic CSS behavior remain visible. Later application work is represented by the more complete projects linked from the owner's GitHub profile.