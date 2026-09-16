# [pt-BR][missing] Psalterium Special: Terce/Sext/None, Preces and the Litany are absent

**Labels:** enhancement, help wanted

### `horas/Portugues/Psalterium/Special/Minor Special.txt`
Missing ~115-139 of the Latin's sections: the entire set of capitula, short responsories and versicles for **Terce, Sext and None across every season**. Only the 3 fixed hymns and Compline survive.

### `horas/Portugues/Psalterium/Special/Major Special.txt`
Missing ~104-116 sections.

### `horas/Portugues/Psalterium/Special/Preces.txt`
Only **1 of 10** Latin sections present at all. Absent: the full **Litany of the Saints** (`[Litania]`, `[LitaniaM]`, `[LitaniaT]` — 181 Latin lines) and every ferial/Sunday Preces set (Laudes, Vespera, Completorium, primae, secundae). The one section that is present is in English (tracked separately).

### `horas/Portugues/Psalterium/Special/Matutinum Special.txt`
No Portuguese file at all.

### `horas/Portugues/Psalterium/Psalmi/Psalmi minor.txt`
Four entire Hours' antiphon sets missing — `[Prima]`, `[Sexta]`, `[Nona]`, `[Completorium]`. The file starts at `[Tertia]`.

### Tasks
- [ ] `Minor Special.txt` — Terce/Sext/None capitula, responsories, versicles
- [ ] `Major Special.txt` — missing sections
- [ ] `Preces.txt` — Litany of the Saints
- [ ] `Preces.txt` — ferial and Sunday Preces sets
- [ ] `Matutinum Special.txt` — create
- [ ] `Psalmi minor.txt` — Prima, Sexta, Nona, Completorium
**Reminder on impact:** `setupstring` (`web/cgi-bin/DivinumOfficium/SetupString.pl:548`) layers a translation on top of `$langfb` (default **English**), then Latin. Every gap below renders as English to a Portuguese user, silently.



<sub>Found by an automated pt-BR translation audit of `web/www/{horas,missa}/Portugues/**` against the Latin at the same relative path.</sub>
