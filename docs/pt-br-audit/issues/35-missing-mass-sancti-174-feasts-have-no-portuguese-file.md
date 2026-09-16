# [pt-BR][missing] Mass Sancti: 174 feasts have no Portuguese file

**Labels:** enhancement, help wanted

174 of the Latin `missa/Latin/Sancti/` files have no Portuguese counterpart (verified with `comm`).

Verified high-impact gaps:
- **`11-02.txt` — the principal Mass of All Souls' Day is missing**, along with `11-02oct.txt` and `11-02t.txt`. (Portuguese *does* have `11-02m1/m2/m3.txt`, the 2nd and 3rd Masses — so All Souls renders with the alternate Masses but not the main one.)
- **The entire Assumption octave** — 23 August files, `08-11oct` through `08-dom-oct`
- `12-29.txt` (St Thomas of Canterbury) — 2-line stub, zero proper texts
- `01-18.txt` (Chair of St Peter at Rome) — 2-line stub, title only, against 45 lines of Latin; the Mass renders empty

### Tasks
- [ ] `11-02.txt` All Souls (principal Mass) + `11-02oct` + `11-02t`
- [ ] Assumption octave (23 files)
- [ ] `01-18.txt`, `12-29.txt`
- [ ] January — [ ] February — [ ] March — [ ] April — [ ] May — [ ] June
- [ ] July — [ ] August — [ ] September — [ ] October — [ ] November — [ ] December
**Reminder on impact:** `setupstring` (`web/cgi-bin/DivinumOfficium/SetupString.pl:548`) layers a translation on top of `$langfb` (default **English**), then Latin. Every gap below renders as English to a Portuguese user, silently.



<sub>Found by an automated pt-BR translation audit of `web/www/{horas,missa}/Portugues/**` against the Latin at the same relative path.</sub>
