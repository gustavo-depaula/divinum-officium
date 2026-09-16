# [pt-BR][missing] Office: the entire temporal cycle is untranslated

**Labels:** enhancement, help wanted

`horas/Portugues/Tempora` has 43 files totalling ~117 lines. `horas/Latin/Tempora` has 639. **Every existing Portuguese file is a title-only stub** — none contains any actual Office content.

Coverage by season (PT files present / Latin files):

| Season | Coverage | Note |
|---|---|---|
| Advent | 3 / 55 | stubs |
| Christmas | 2 / 27 | stubs |
| Epiphany & after | 4 / 50 | stubs |
| Septuagesima | 1 / 21 | the one file has 2 of 37 sections |
| **Lent** | **0 / 39** | 100% absent |
| **Passiontide & Holy Week** | **0 / 25** | 100% absent, incl. Palm Sunday |
| Easter | 21 / 85 | all 2-line title stubs |
| After Pentecost | 12 / 335 | 96% absent |

### Tasks
- [ ] Advent (`Adv*`)
- [ ] Christmas (`Nat*`)
- [ ] Epiphany and Sundays after (`Epi*`)
- [ ] Septuagesima (`Quadp*`)
- [ ] Lent (`Quad1*`-`Quad4*`)
- [ ] Passiontide and Holy Week (`Quad5*`, `Quad6*`)
- [ ] Easter (`Pasc*`)
- [ ] After Pentecost (`Pent*`, `081*`-`115*`)
**Reminder on impact:** `setupstring` (`web/cgi-bin/DivinumOfficium/SetupString.pl:548`) layers a translation on top of `$langfb` (default **English**), then Latin. Every gap below renders as English to a Portuguese user, silently.



<sub>Found by an automated pt-BR translation audit of `web/www/{horas,missa}/Portugues/**` against the Latin at the same relative path.</sub>
