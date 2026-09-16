# [pt-BR][missing] `Sancti/Brasilia` is absent — including Nossa Senhora Aparecida, patroness of Brazil

**Labels:** enhancement, help wanted

All five `Sancti/` subdirectories are 100% absent from Portuguese:

| Subdirectory | Latin files |
|---|---|
| **`Sancti/Brasilia`** | **10** |
| `Sancti/Urbis` | 141 |
| `Sancti/Bavaria` (+ Monacensis, Passaviensis, Spirensis, Ratisbonensis) | 96 |
| `Sancti/Neerlandia` (+ Ultrajectum, Groningen) | 57 |
| `Sancti/aliquibus locis` | 42 |

`Sancti/Brasilia` is the one that matters most for a Brazilian edition — it carries the proper feasts of Brazil, including **Nossa Senhora Aparecida**, the country's patroness. `horas/Latin/Tempora/Brasilia` and `missa`'s equivalents are likewise untranslated.

### Tasks
- [ ] **`horas/Portugues/Sancti/Brasilia/` (10 files) — highest priority for a pt-BR edition**
- [ ] `horas/Portugues/Tempora/Brasilia/`
- [ ] `Sancti/aliquibus locis/` (42)
- [ ] `Sancti/Urbis/` (141)
- [ ] `Sancti/Bavaria/` and `Sancti/Neerlandia/` (lower priority — local German/Dutch calendars)
**Reminder on impact:** `setupstring` (`web/cgi-bin/DivinumOfficium/SetupString.pl:548`) layers a translation on top of `$langfb` (default **English**), then Latin. Every gap below renders as English to a Portuguese user, silently.



<sub>Found by an automated pt-BR translation audit of `web/www/{horas,missa}/Portugues/**` against the Latin at the same relative path.</sub>
