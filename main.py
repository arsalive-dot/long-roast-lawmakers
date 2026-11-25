"""The Long Roast: Lawmakers and the File They Cannot Convert — one
satirical sentence, at most 320 characters, roasting lawmakers who
regulate AI, crypto or the internet but cannot convert a file to PDF.

The entry sets up the lawmaker's authority — the chair of the AI
oversight committee writes laws governing machines that can compose
poetry — then undercuts it with a specific, everyday detail: he
emails his staff a Word file called FINAL_v7_ACTUALLY_FINAL because
the PDF button is, in his words, a bit much. The joke is about power
and competence, and the punch lands on the last few words — the
lawmaker's own excuse, quoted back at him.
"""

import os

ENTRY = (
    "The chair of the AI oversight committee writes laws governing "
    "machines that can compose poetry, then emails his staff a Word "
    "file called FINAL_v7_ACTUALLY_FINAL because the PDF button is, "
    "in his words, a bit much."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    tmp = "/output/.entry.txt.tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.replace(tmp, "/output/entry.txt")
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
