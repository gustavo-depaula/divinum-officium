# [pt-BR][missing] Office: the 12 Commons are title-and-Mass-only stubs

**Labels:** enhancement, help wanted

In `horas/Portugues/Commune/`, the Divine Office is missing from every Common — Vespers, Invitatorium, all 9 Matins lessons and responsories, Lauds and the minor hours. Only Mass-proper sections and the title survive.

Missing sections per file (verified against `horas/Latin/Commune/`):

| File | Missing / total Latin sections |
|---|---|
| `C8.txt` | 92 / 109 |
| `C4.txt` | 62 / 75 |
| `C2.txt` | 56 / 69 |
| `C3.txt` | 55 / 69 |
| `C1.txt` | **53 / 54** |
| `C12.txt` | **53 / 54** |
| `C9.txt` | 53 / 60 |
| `C10.txt` | 52 / 54 |
| `C11.txt` | 51 / 64 |
| `C6.txt` | 50 / 70 |
| `C5.txt` | 45 / 57 |
| `C7.txt` | 39 / 44 |

`C1.txt` is literally 2 lines against 357 in the Latin.

### Tasks
- [ ] `C1.txt` Commune Apostolorum
- [ ] `C2.txt` — [ ] `C3.txt` — [ ] `C4.txt` — [ ] `C5.txt` — [ ] `C6.txt`
- [ ] `C7.txt` — [ ] `C8.txt` — [ ] `C9.txt` — [ ] `C10.txt` — [ ] `C11.txt` — [ ] `C12.txt`
- [ ] Commune variant files (`C*a`, `C*b`, `Votiva/`, `aliquibus locis/`)
**Reminder on impact:** `setupstring` (`web/cgi-bin/DivinumOfficium/SetupString.pl:548`) layers a translation on top of `$langfb` (default **English**), then Latin. Every gap below renders as English to a Portuguese user, silently.



<sub>Found by an automated pt-BR translation audit of `web/www/{horas,missa}/Portugues/**` against the Latin at the same relative path.</sub>
