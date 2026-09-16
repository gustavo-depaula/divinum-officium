# [pt-BR][untranslated] Isolated Latin/English passages left inside otherwise-translated files

**Labels:** bug

Individual sections left untranslated inside files that are otherwise in Portuguese.

### Tasks
- [ ] `missa/Portugues/Sancti/10-17.txt:42-44` — an entire alternate Tractus (Ps 83:3-4) is still in Latin
- [ ] `horas/Portugues/Psalterium/Psalmi/Psalmi major.txt:93-147` — a contiguous block of 27 antiphons (Day4 Laudes2 through Day6 Vespera) is in English
- [ ] `horas/Portugues/Psalterium/Psalmi/Psalmi major.txt:68` — a single isolated English antiphon inside an otherwise-correct section
- [ ] `horas/Portugues/Psalterium/Psalmi/Psalmi minor.txt:70` — the literal English word `missing` is sitting in an antiphon-text field (the Latin source leaves it empty)
- [ ] `horas/Portugues/Psalterium/Special/Preces.txt:2-25` — the whole `[Preces feriales Prima]` section, all 24 V./R. lines, is in English
- [ ] `missa/Portugues/Tempora/Pent18-0.txt` — `Eccli` left untranslated where the corpus norm is `Ecl` (11x)


<sub>Found by an automated pt-BR translation audit of `web/www/{horas,missa}/Portugues/**` against the Latin at the same relative path. Every item below was verified against the source files.</sub>
