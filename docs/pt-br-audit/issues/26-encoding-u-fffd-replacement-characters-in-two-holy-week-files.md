# [pt-BR][encoding] U+FFFD replacement characters in two Holy Week files

**Labels:** bug, good first issue

A full-corpus sweep found exactly **8 U+FFFD occurrences in 2 files**.

`missa/Portugues/Tempora/Quad6-6t.txt`:
- line 198 — `!Jon� 3:1-10` → `Jonæ`
- line 260 — `Fr�fationis` → `Præfationis`
- lines 763, 764 — `allel�ja` → `allelúja`
- line 767 — `Pl�ceat` → `Placeat`

`missa/Portugues/Tempora/Quad1-3.txt`:
- line 2 — `Feria Quarta Quatuor Temporum Quadrigeism�` — both mojibake **and** a typo; should read `Quadragesimæ`

### Tasks
- [ ] Fix the 5 occurrences in `Quad6-6t.txt`
- [ ] Fix `Quad1-3.txt:2` (spelling and character)


<sub>Found by an automated pt-BR translation audit of `web/www/{horas,missa}/Portugues/**` against the Latin at the same relative path. Every item below was verified against the source files.</sub>
