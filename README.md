# Central African Republic (CF) — législation en Markdown

Part of [LawCodex](https://github.com/LawCodex): the legislation of every country as plain Markdown in git.

**Minimal repository: the Constitution of the Central African Republic** (French version; French and Sango are
the official languages).

Retrieved 2026-10-13.

<!-- COUNTS -->
| Directory | Files |
|---|---|
| `constitution/` | 1 |
| **Total** | **1** |
<!-- /COUNTS -->

## Contents

```
constitution/constitution-2023.md   Constitution of the Seventh Republic, approved by referendum on 30 July 2023
                                    and promulgated on 30 August 2023 (JORCA/ES n° 9, 4 September 2023)
```

## Source

| Document | URL |
|---|---|
| Constitution of 2023 — Digithèque de matériaux juridiques et politiques (Jean-Pierre Maury, Université de Perpignan) | https://mjp.univ-perp.fr/constit/cf2023.htm |

**This is not an official source.** The Digithèque MJP is a long-standing academic collection of constitutional
texts; its transcription cites the *Journal officiel de la République centrafricaine* (JORCA/ES n° 9 of
4 September 2023) as source. The same transcription is what FAOLEX (FAO) archives for this Constitution. MJP's
editorial introduction (historical note and referendum results) is not reproduced; only the constitutional text
is. Minor typos of the transcription (e.g. "responsable d son destin") are kept as is. The MJP server sends an
incomplete TLS certificate chain, so the script downloads it without certificate verification.

## Not covered / known gaps

* **No official online source of Central African law could be reached.** The Presidency, Secrétariat général du
  Gouvernement, National Assembly, Constitutional Court and Journal officiel domains (presidence.cf, sgg.cf,
  assembleenationale.cf, cour-constitutionnelle.cf, journalofficiel.cf) did not answer, and the Internet Archive
  holds no usable copies of legal texts from them. gouv.cf and primature.cf publish no legislation (the Prime
  Minister's "décrets / législations" category is empty).
* The Ministry of Justice website (justice.gouv.cf) publishes four texts (Code de la famille, Code de justice
  militaire, loi portant organisation judiciaire, statut des juges administratifs) but only as scanned images
  without a text layer: not OCRed.
* No laws, ordinances or codes are included; no Sango version.

## Copyright

The Constitution is an official text of the Central African Republic; official texts of a legislative nature are
excluded from copyright protection (OAPI Bangui Agreement, Annex VII). Transcription credited to the Digithèque
MJP. The Markdown conversion is provided as is; the authoritative text is the one published in the *Journal
officiel de la République centrafricaine*.

## Regenerating

```sh
python3 scripts/cf_fetch.py    # downloads the page to ../_raw/cf/ and writes the Markdown
python3 scripts/cf_readme.py   # updates the counts table
```
