# [pt-BR][markup] Four canticles have no `*`/`†` pause markers at all

**Labels:** bug

`horas/Portugues/Psalterium/Psalmorum/Psalm245.txt`, `Psalm246.txt`, `Psalm247.txt`, `Psalm248.txt` (the Habacuc and Sophonias canticles).

The Portuguese is written as unbroken prose with **zero** `*` or `†` markers, while the Latin has 11-15 per file. This breaks chant pointing entirely.

### Tasks
- [ ] `Psalm245.txt` — insert pause markers matching the Latin
- [ ] `Psalm246.txt`
- [ ] `Psalm247.txt`
- [ ] `Psalm248.txt`
- [ ] Also `Psalm223.txt:17` and `Psalm269.txt:6` — individual missing `*`
- [ ] Also `horas/.../Psalmorum/Psalm16.txt:1` (`16:1a`) — Latin splits the verse with `*`; the Portuguese uses a semicolon and no marker


<sub>Found by an automated pt-BR translation audit of `web/www/{horas,missa}/Portugues/**` against the Latin at the same relative path. Every item below was verified against the source files.</sub>
