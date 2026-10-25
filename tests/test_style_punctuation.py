from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
TEXT_SUFFIXES = {".md", ".svg", ".json", ".yml", ".yaml", ".py", ".html", ".txt"}
FORBIDDEN = {
    chr(0x2014): "em dash",
    chr(0x2013): "en dash",
}


class PublicTextStyleTests(unittest.TestCase):
    def test_typographic_dashes_are_not_used(self):
        violations = []

        for path in ROOT.rglob("*"):
            if not path.is_file() or path.suffix.lower() not in TEXT_SUFFIXES:
                continue
            if any(part in {".git", "dist", "__pycache__"} for part in path.parts):
                continue

            text = path.read_text(encoding="utf-8")
            for line_number, line in enumerate(text.splitlines(), start=1):
                for glyph, label in FORBIDDEN.items():
                    if glyph in line:
                        violations.append(
                            f"{path.relative_to(ROOT)}:{line_number}: {label}"
                        )

        self.assertEqual(
            violations,
            [],
            "Use periods, colons, commas, or parentheses instead of typographic dashes:\n"
            + "\n".join(violations),
        )


if __name__ == "__main__":
    unittest.main()
