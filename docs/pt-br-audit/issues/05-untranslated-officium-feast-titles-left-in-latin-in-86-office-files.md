# [pt-BR][untranslated] `[Officium]` feast titles left in Latin in ~86 Office files

**Labels:** bug, good first issue

Across `horas/Portugues/{Sancti,Commune,Tempora}`, 86 files have an `[Officium]` title that is byte-identical to the Latin (36 in `Sancti/`, 18 in `Commune/`, 32 in `Tempora/`). Sibling files *do* translate the title, so this is inconsistent rather than deliberate.

Verified examples:
- `horas/Portugues/Sancti/03-19.txt:2` — `S. Joseph Sponsi B.M.V. Confessoris`
- `horas/Portugues/Commune/C5b.txt:2` — `Commune Abbatis`
- `horas/Portugues/Sancti/06-28r.txt:2` — `In Vigilia Ss. Petri et Pauli Apostolorum`
- `missa/Portugues/Sancti/01-18.txt:2` — `Cathedræ S. Petri Romæ`

**This one does affect the calendar.** `SetupString.pl:629-640` overwrites field 0 of `[Rank]` with the translation's `[Officium]` value, so an untranslated `[Officium]` shows a Latin feast name in the calendar and rank display.

> For the avoidance of doubt: a *missing* `[Rank]` section is **not** a defect — English ships `[Rank]` in only 67 of 454 Sancti files, Spanish 64/445, Italian 64/447, and `SetupString.pl` always takes `[Rank]` from the base layer anyway. Only the `[Officium]` title needs fixing.

### Tasks
- [ ] Translate the 36 Latin `[Officium]` titles in `horas/Portugues/Sancti/`
- [ ] Translate the 18 in `horas/Portugues/Commune/`
- [ ] Translate the 32 in `horas/Portugues/Tempora/`


<sub>Found by an automated pt-BR translation audit of `web/www/{horas,missa}/Portugues/**` against the Latin at the same relative path. Every item below was verified against the source files.</sub>
