# [pt-BR][missing] Office Sancti: 187 feasts have no file, and 264 of 298 existing files are stubs

**Labels:** enhancement, help wanted

`horas/Portugues/Sancti/` has 298 files averaging under 6 lines each. `horas/Latin/Sancti/` has 832 top-level files.

- **187** Latin files have no Portuguese counterpart at all
- Of the 298 that exist, **264 are title+collect stubs** with 2 sections or fewer
- Only 34 have any further content — and **none** has actual antiphons, hymns, lessons or responsories

Sample verified month breakdowns:
- **December**: 30 of 45 Latin files missing; 13 of the 15 present are stubs
- **August**: 27 of 62 missing; 33 of 35 present are stubs

### Tasks
- [ ] January — [ ] February — [ ] March — [ ] April — [ ] May — [ ] June
- [ ] July — [ ] August — [ ] September — [ ] October — [ ] November — [ ] December
**Reminder on impact:** `setupstring` (`web/cgi-bin/DivinumOfficium/SetupString.pl:548`) layers a translation on top of `$langfb` (default **English**), then Latin. Every gap below renders as English to a Portuguese user, silently.



<sub>Found by an automated pt-BR translation audit of `web/www/{horas,missa}/Portugues/**` against the Latin at the same relative path.</sub>
