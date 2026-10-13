#!/usr/bin/env python3
"""Central African Republic: Constitution of the Seventh Republic (promulgated 30 August 2023), from the
Digithèque de matériaux juridiques et politiques (MJP, Université de Perpignan), a reputable academic transcription
of the Journal officiel (JORCA/ES n° 9 of 4 September 2023). No official online source could be reached.
Usage: python3 cf_fetch.py [--no-download]"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cf_text as T  # noqa

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW = os.path.join(os.path.dirname(REPO), "_raw", "cf")
RETRIEVED = os.environ.get("LC_RETRIEVED", "2026-10-13")
URL = "https://mjp.univ-perp.fr/constit/cf2023.htm"


def main():
    dest = os.path.join(RAW, "cf2023.htm")
    if "--no-download" not in sys.argv:
        import urllib3
        urllib3.disable_warnings()
        T.fetch(URL, dest, delay=3, verify=False)  # the server sends an incomplete TLS certificate chain
    lines = T.html_lines(dest)
    st = [i for i, x in enumerate(lines) if x == "Préambule."][1]  # skip table of contents and editorial note
    en = next(i for i, x in enumerate(lines) if x.startswith("Pour obtenir davantage d'informations"))
    lines = lines[st + 1:en]
    # "Titre II. Des ..." / "Chapitre premier. De ..." -> division headings; "Article 12." -> article
    lines = [re.sub(r"^(Titre|Chapitre|Section)\s+([IVXLC]+|premier|unique|\d+)\.\s*", lambda m: m.group(1).upper() + " " + m.group(2).upper() + " - ", x)
             for x in lines]
    out = []
    for x in lines:
        out += [x, ""]
    body = ["## Préambule", ""] + T.structure(out, "fr")
    meta = {"title": "Constitution de la République centrafricaine", "identifier": "Constitution de la VIIe République, promulguée le 30 août 2023",
            "type": "constitution", "jurisdiction": "cf", "language": "fr", "date": "2023-08-30", "status": "in_force",
            "source": URL, "gazette": "Journal officiel de la République centrafricaine, JORCA/ES n° 9, 4 septembre 2023",
            "retrieved": RETRIEVED,
            "note": "Non-official transcription by the Digithèque MJP (Université de Perpignan); MJP's editorial introduction omitted"}
    T.write_md(os.path.join(REPO, "constitution", "constitution-2023.md"), meta, meta["title"], body)
    print("OK", sum(1 for x in body if x.startswith("#") and "Article" in x), "articles")


if __name__ == "__main__":
    main()
