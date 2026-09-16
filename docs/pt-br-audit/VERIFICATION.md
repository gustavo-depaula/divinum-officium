# Lead verification of subagent claims (checked directly against files)

## CONFIRMED
- Psalm verse-number drift. Latin `Psalm20` starts at `20:2`, English at `20:2`,
  Portuguese at `20:1`. `Psalm22` has `22:4` twice in Latin AND English (split
  half-verse); Portuguese renumbers past it. Portuguese-only defect. CONFIRMED.
- Psalm87.txt: PT line 13 is a near-verbatim duplicate of PT line 12 (ending
  changed to "no túmulo"); the real v.13 content is shifted onto line 14 and
  everything after is off by one. CONFIRMED against Latin and English.
- `Major Special.txt:773` `"Deus reinará pelo lenho."` (future) mistranslates
  `Regnávit a ligno Deus` (perfect, Latin line 1342/1385). CONFIRMED.
- `Major Special.txt:877` `Ao Pao e ao Paráclito` — `Pao` is a dropped-letter
  corruption of `Pai`. CONFIRMED.
- `Ressucitado`/`Ressucitou` at Major Special.txt:820,824,833,878 — missing `s`,
  should be `Ressuscitado`/`Ressuscitou`. CONFIRMED (4 occurrences).
- Holy Week / Sorrows Mass files are near-VERBATIM COPIES OF THE ENGLISH FILES,
  not merely "containing English". Measured line-diff vs English/:
  Quad6-5t 17/370 lines differ, Quad6-6t 63/780, Quad6-5r 25/330, Quad6-0r 38/212,
  Quad5-5 26/156, Quad6-4r 54/272, Quad6-6r 186/686. CONFIRMED.
  Corpus-wide sweep found 56 such files, 3,782 lines total (see
  findings/zz-verified-by-lead.jsonl).

## REJECTED — do not file
- "[Rank] section entirely absent in Portuguese degrades calendar/rank display."
  FALSE POSITIVE. Two independent reasons:
  1. Omitting [Rank] is the NORM for translations, not a Portuguese anomaly:
     English has [Rank] in only 67 of 454 Sancti files, Spanish 64/445,
     Italian 64/447. Portuguese 0/298 is the same design, taken further.
  2. web/cgi-bin/DivinumOfficium/SetupString.pl:629-640 ALWAYS takes [Rank] from
     the base (fallback→Latin) layer and only overwrites field 0 with the
     translation's [Officium]. A translation's own [Rank] is discarded whenever
     the base has one. So a missing [Rank] cannot degrade anything.
  The real defect in this area is the untranslated [Officium] titles, which DO
  feed Rank field 0. File that instead.
- "Other languages have the Holy Week t/r variant files as 1-line
  `@Tempora/XXXX` redirects, so Portuguese should be too." FALSE. English
  Quad6-6t.txt is 781 lines, Italiano 781, Latin Quad6-5t 388. They are full
  files. Do not put the redirect suggestion in the issue.
- ASCII `...` vs `…`. Not a defect: `…` (U+2026) appears nowhere in the
  Portuguese or Latin corpus, so `...` is the established convention.
- `«»` guillemets. Not a pt-PT defect: they are the dominant quote style in
  horas/Portugues (37 files vs 2 using `“”`). Only genuinely UNBALANCED or
  NESTED-same-level guillemets are defects.
- `genuflectir`. Attested standard Portuguese, used consistently 24x. Not a variant.

## CONFIRMED (batch 2 — Mass Ordinary)
- `missa/Portugues/Ordo/Prayers.txt` [Misereatur]: Latin is first-person plural
  (`Misereátur NOSTRI ... peccátis NOSTRIS, perdúcat NOS`), English likewise
  ("mercy on us ... forgive us ... bring us"). Portuguese says
  "se compadeça de VÓS, perdoe os VOSSOS pecados e VOS conduza" — second person.
  Wrong grammatical person in the Misereatur after the Confiteor. CONFIRMED, high.
- `missa/Portugues/Ordo/Post.txt:3`: "o Papa Leão XIII uma indulgência de um ano"
  has no verb; `concedeu` is missing. CONFIRMED. Same line also has pt-PT
  "Acção de graças" in the line-1 heading (→ "Ação de graças").

## DOWNGRADED — needs investigation, do NOT file as a confident bug
- "`&Ultimaev` missing from Propers.txt ⇒ the Last Gospel is lost."
  Latin `Ordo/Propers.txt` has `&Ultimaev`; Portuguese does not. BUT all six
  translations that ship this file lack it (Bohemice, Cesky-Schaller, Italiano,
  Polski, Portugues, Ukrainian — only Latin has it), so it is not a pt-BR defect.
  Also Propers.txt contains NO `[Section]` headers, so the whole file is
  `__preamble`, and SetupString.pl CONCATENATES `__preamble` with the base layer
  rather than letting the top layer win. So `&Ultimaev` may well still reach the
  renderer from Latin. Runtime impact unverified. Mention in the tracking issue
  as an open question for upstream, not as a pt-BR bug.

## CONFIRMED (batch 3 — Psalterium core, the most-repeated texts in the app)
- `Prayers.txt` [Gloria] — the Gloria Patri, said after nearly every psalm:
  Latin `Glória Patri, et Fílio, * et Spirítui Sancto` / `...et semper, * et in
  sǽcula...`; Portuguese has NO `*` on either line. CONFIRMED, high.
- `Prayers.txt` [Requiem]: PT missing `*` on both lines. ALSO the R. is a loose
  paraphrase — "Entre os esplendores da luz perpétua" drops the verb of
  `Et lux perpétua lúceat eis` ("and may perpetual light shine upon them"), and
  PT lacks the Latin's second single-line form entirely.
- `Prayers.txt:62` [Indulgentiam], said daily at Prime: "Que o Senhor + cruz
  omnipotente e misericordioso..." — the word "cruz" has been typed next to the
  `+` cross glyph, producing nonsense. CONFIRMED, high.
- `Prayers.txt:244`: "pensamentos, palavras e pobras" → `obras`. CONFIRMED.
- `Prayers.txt:49`: `R. E com o teu espírito` — "tu" register against the corpus's
  "vós". CONFIRMED.
- `Prayers.txt` [Post], said after EVERY Hour: body is entirely ENGLISH
  ("To the Most Holy and undivided Trinity...", "Blessed be the womb..."), with
  only "R. Amém" and the `/:e em silêncio:/` rubric in Portuguese. CONFIRMED, high.
- `missa/Portugues/Sancti/02-02.txt:29`: "na Vasa presença" → "na vossa presença".
  CONFIRMED.
- `missa/Portugues/Sancti/01-18.txt` is a 2-line stub (title only) vs 45 Latin
  lines. CONFIRMED.

## CORRECTED — subagent overstated
- "11-02.txt (All Souls) and its entire octave (22 files) have no Portuguese
  version at all." PARTLY WRONG. Portuguese HAS 11-02m1.txt, 11-02m2.txt and
  11-02m3.txt (the 2nd and 3rd Masses). MISSING are 11-02.txt (the principal
  All Souls Mass), 11-02oct.txt and 11-02t.txt. File it that way: the main
  All Souls Mass is missing while the alternate Masses are present.

## CONFIRMED (batch 4 — canticles). Subagent corrected my briefing leads; it was right.
- My brief said Psalm226.txt and Psalm234.txt were "wholly English". WRONG, and the
  subagent corrected it. Both files have an English block followed by a separate
  Portuguese block:
  - Psalm234.txt (Athanasian Creed): English lines 1-40, then a COMPLETE and correct
    Portuguese translation, lines 43-82.
  - Psalm226.txt (Canticle of Moses, Deut 32): English lines 1-66 (labelled
    `32:1`..`32:65`), then Portuguese from line 68.
- Psalm226.txt is worse than the subagent reported: the Portuguese part carries only
  verse labels 1..12, i.e. 12 of the Latin's 65 verses (~82% absent), not "1-17".
- Psalm226/Psalm234 Portuguese blocks also use a FORMAT FOUND NOWHERE ELSE in the
  corpus: a bare verse number alone on its own line, with the verse text on the
  following one or two lines. The corpus format is `32:1 text * text` — one line,
  `chapter:verse` prefix. Psalm226's last line is `12Só o Senhor o conduzia, *`
  with the label glued to the text. This will mis-render. Markup, high.
- Psalm232.txt:6 — the MAGNIFICAT, sung at Vespers daily: `1:49 Grandes maravilhas
  fês em mim o Omnipotente` — `fês` is not a Portuguese word (→ `fez`), and
  `Omnipotente` is the pt-PT form. CONFIRMED, high.
- `Cãntico` (tilde) for `Cântico` (circumflex) in the headers of Psalm216, 220, 221,
  222, 223. CONFIRMED, 5 files.
