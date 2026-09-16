# [pt-BR][untranslated] Holy Week & Triduum Mass files are verbatim copies of the English files

**Labels:** bug, help wanted

The Portuguese files for the most solemn liturgies of the year were seeded from the **English** files and never translated. They are not "partly English" — they are near-verbatim copies.

Measured by diffing each against `missa/English/Tempora/<same name>`:

| File | PT lines | lines differing from English |
|---|---|---|
| `missa/Portugues/Tempora/Quad6-6t.txt` (Easter Vigil) | 780 | 63 |
| `missa/Portugues/Tempora/Quad6-6r.txt` (Easter Vigil, alt) | 686 | 186 |
| `missa/Portugues/Tempora/Quad6-5t.txt` (Good Friday) | 370 | **17** |
| `missa/Portugues/Tempora/Quad6-5r.txt` (Good Friday, alt) | 330 | 25 |
| `missa/Portugues/Tempora/Quad6-4r.txt` (Holy Thursday) | 272 | 54 |
| `missa/Portugues/Tempora/Quad6-0r.txt` (Palm Sunday) | 212 | 38 |
| `missa/Portugues/Tempora/Quad5-5.txt` (Our Lady of Sorrows) | 156 | 26 |
| `missa/Portugues/Tempora/Quad6-4.txt` (Holy Thursday, main) | — | `[Communicantes]` lines 214-224 only |

The differing lines are mostly the `[Officium]` title and `$`/`@` directives.

### Tasks
- [ ] `Quad6-6t.txt` — translate the Easter Vigil (Blessing of Fire, Exsultet, Prophecies, Blessing of Font, Litany, Mass, Vespers)
- [ ] `Quad6-6r.txt` — same, alternate rite
- [ ] `Quad6-5t.txt` — Good Friday (Lessons, Passion, Great Intercessions, Adoration of the Cross, Mass of the Presanctified)
- [ ] `Quad6-5r.txt` — same, alternate rite
- [ ] `Quad6-4r.txt` — Holy Thursday Mandatum + Mass proper
- [ ] `Quad6-0r.txt` — Palm Sunday Blessing of Palms + Mass proper
- [ ] `Quad5-5.txt` — Our Lady of Sorrows, including the full Stabat Mater sequence
- [ ] `Quad6-4.txt:214-224` — the `[Communicantes]` Canon insert, which is English with a Latin fragment spliced in ("Virgin Mary Genetrícis ejúsdem Dei et Dómini nostri Jesu Christi: sed and of the blessed Apostles")

> Note: these are **not** one-line `@Tempora/...` redirects in other languages — `English/Tempora/Quad6-6t.txt` is itself 781 lines. They need real translations.

**Why this is user-visible:** `setupstring` (`web/cgi-bin/DivinumOfficium/SetupString.pl:548`) layers a translation on top of `$langfb` (default **English**), which layers on Latin. So anything missing or wrong in Portuguese silently renders as English rather than failing loudly.



<sub>Found by an automated pt-BR translation audit of `web/www/{horas,missa}/Portugues/**` against the Latin at the same relative path. Every item below was verified against the source files.</sub>
