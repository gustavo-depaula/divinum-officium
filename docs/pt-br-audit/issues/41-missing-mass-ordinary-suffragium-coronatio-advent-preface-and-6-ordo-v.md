# [pt-BR][missing] Mass Ordinary: Suffragium, Coronatio, Advent preface, and 6 Ordo variants

**Labels:** enhancement, help wanted

### `missa/Portugues/Ordo/Suffragium.txt`
- [ ] All 3 implemented sections (`Oratio`/`Secreta`/`Postcommunio Maria1`) contain only the heading plus `$Per eundem` — **the entire prayer body text is missing**
- [ ] 8 of the 9 Latin commemoration groups are absent altogether (Maria2, Maria3, Ecclesiæ, Papa, Sanctorum, Spiritu, Vivis — 24 sections)

### `missa/Portugues/Commune/Coronatio.txt`
- [ ] Missing Oratio, Lectio, Tractus, Offertorium, Secreta, Postcommunio and the leading `@Commune/C4b` include. Only Graduale, Evangelium and Communio exist.

### `missa/Portugues/Ordo/Prefationes.txt`
- [ ] The **Advent preface** (`[Adv]`) is completely absent — Advent Masses have no proper preface in Portuguese

### Ordo variants with no Portuguese file
- [ ] `Ordo67.txt` — [ ] `OrdoA.txt` — [ ] `OrdoM.txt` — [ ] `OrdoN.txt` — [ ] `OrdoOP.txt` — [ ] `OrdoS.txt`
**Reminder on impact:** `setupstring` (`web/cgi-bin/DivinumOfficium/SetupString.pl:548`) layers a translation on top of `$langfb` (default **English**), then Latin. Every gap below renders as English to a Portuguese user, silently.



<sub>Found by an automated pt-BR translation audit of `web/www/{horas,missa}/Portugues/**` against the Latin at the same relative path.</sub>
