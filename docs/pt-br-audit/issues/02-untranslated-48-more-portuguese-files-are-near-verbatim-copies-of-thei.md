# [pt-BR][untranslated] 48 more Portuguese files are near-verbatim copies of their English counterparts

**Labels:** bug, help wanted

A corpus-wide sweep (comparing each `Portugues/**` file with `English/**` at the same relative path, flagging files where >60% of distinct lines are byte-identical to English) found **56 files / 3,782 lines** total. The 8 Holy Week files are tracked separately; the remaining 48 are listed below.

### Tasks
- [ ] `horas/Portugues/Psalterium/Psalmi/Psalmi major.txt` — 411 lines, 63% identical to English
- [ ] `horas/Portugues/Psalterium/Special/Preces.txt` — 25 lines, **100%** identical to English
- [ ] `missa/Portugues/Tempora/Pent01-0.txt` — 34 lines, 64%
- [ ] `missa/Portugues/Sancti/07-16.txt` — 33 lines, 62%
- [ ] `missa/Portugues/Tempora/Pent03-0.txt` — 27 lines, 70%
- [ ] `horas/Portugues/Psalterium/Psalmorum/Psalm248.txt` — 23 lines, 65%
- [ ] `horas/Portugues/Psalterium/Psalmorum/Psalm245.txt` — 18 lines, 61%
- [ ] `horas/Portugues/Psalterium/Psalmorum/Psalm246.txt` — 17 lines, 65%
- [ ] `missa/Portugues/Sancti/01-18r.txt`, `09-24.txt`, `07-02cc.txt`, `01-14cc.txt`, `08-29cc.txt`, `11-24o.txt`, `08-22cc.txt` — 10-14 lines each
- [ ] `horas/Portugues/Commune/C7b.txt` — 11 lines
- [ ] `missa/Portugues/Ordo/Suffragium.txt` — 11 lines, 83%
- [ ] `horas/Portugues/Sancti/10-15.txt`, `07-21r.txt`, `12-02.txt`, `03-12.txt`, `12-04.txt`, `05-04.txt` and ~27 further small Sancti files

The full machine-readable list is reproducible with the sweep described above.

**Why this is user-visible:** `setupstring` (`web/cgi-bin/DivinumOfficium/SetupString.pl:548`) layers a translation on top of `$langfb` (default **English**), which layers on Latin. So anything missing or wrong in Portuguese silently renders as English rather than failing loudly.



<sub>Found by an automated pt-BR translation audit of `web/www/{horas,missa}/Portugues/**` against the Latin at the same relative path. Every item below was verified against the source files.</sub>
