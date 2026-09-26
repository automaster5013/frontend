from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit


ROOT = Path(__file__).resolve().parent.parent
PAGES = ("index.html", "blog_list.html", "about_me.html")


class DocumentValidator(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.lang = ""
        self.charset = ""
        self.has_viewport = False
        self.title_parts: list[str] = []
        self.in_title = False
        self.main_count = 0
        self.h1_count = 0
        self.has_labelled_nav = False
        self.has_stylesheet = False
        self.links: list[tuple[str, str]] = []
        self.ids: set[str] = set()

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        if tag == "html":
            self.lang = values.get("lang") or ""
        elif tag == "meta":
            self.charset = (values.get("charset") or self.charset).lower()
            self.has_viewport = self.has_viewport or (
                values.get("name") == "viewport" and bool(values.get("content"))
            )
        elif tag == "title":
            self.in_title = True
        elif tag == "main":
            self.main_count += 1
        elif tag == "h1":
            self.h1_count += 1
        elif tag == "nav":
            self.has_labelled_nav = self.has_labelled_nav or bool(values.get("aria-label"))
        elif tag == "link":
            self.has_stylesheet = self.has_stylesheet or (
                values.get("rel") == "stylesheet" and values.get("href") == "./styles.css"
            )
        elif tag == "a":
            self.links.append((values.get("href") or "", values.get("aria-current") or ""))

        if values.get("id"):
            self.ids.add(values["id"] or "")

    def handle_endtag(self, tag: str) -> None:
        if tag == "title":
            self.in_title = False

    def handle_data(self, data: str) -> None:
        if self.in_title:
            self.title_parts.append(data)


def validate_page(filename: str) -> list[str]:
    path = ROOT / filename
    parser = DocumentValidator()
    parser.feed(path.read_text(encoding="utf-8"))
    errors: list[str] = []

    checks = {
        "html lang must be 'ko'": parser.lang == "ko",
        "UTF-8 charset is required": parser.charset == "utf-8",
        "responsive viewport metadata is required": parser.has_viewport,
        "a non-empty title is required": bool("".join(parser.title_parts).strip()),
        "exactly one main element is required": parser.main_count == 1,
        "exactly one h1 is required": parser.h1_count == 1,
        "navigation must have an accessible label": parser.has_labelled_nav,
        "the shared stylesheet must be linked": parser.has_stylesheet,
        "main-content target is required": "main-content" in parser.ids,
    }
    errors.extend(message for message, valid in checks.items() if not valid)

    current_links = [href for href, current in parser.links if current == "page"]
    if current_links != [f"./{filename}"]:
        errors.append("exactly one aria-current link must identify this page")

    for href, _ in parser.links:
        target = urlsplit(href)
        if target.scheme or target.netloc or not target.path:
            continue
        resolved = (path.parent / target.path).resolve()
        if not resolved.is_relative_to(ROOT) or not resolved.is_file():
            errors.append(f"local link does not resolve: {href}")

    return errors


def main() -> None:
    failures: list[str] = []
    for page in PAGES:
        failures.extend(f"{page}: {message}" for message in validate_page(page))

    css = (ROOT / "styles.css").read_text(encoding="utf-8")
    if "front-size" in css:
        failures.append("styles.css: invalid front-size property remains")

    if failures:
        raise SystemExit("\n".join(failures))

    print(f"PASS: validated {len(PAGES)} HTML pages and their local navigation")


if __name__ == "__main__":
    main()
