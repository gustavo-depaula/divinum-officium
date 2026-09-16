# [pt-BR][markup] Broken `$` directives and a dangling `@` include

**Labels:** bug

### `$Deo Gratias` with a capital G (6 occurrences)
The canonical prayer name is `[Deo gratias]` (lower-case `g`) in both `missa/Portugues/Ordo/Prayers.txt:122` and `horas/Portugues/Psalterium/Common/Prayers.txt:87`. Perl hash keys are case-sensitive, so `$Deo Gratias` will not resolve.

- [ ] `missa/Portugues/Tempora/Adv3-6.txt:16,31,46,61`
- [ ] `missa/Portugues/Tempora/Adv3-3.txt:16`
- [ ] `missa/Portugues/Tempora/Pasc7-6t.txt:81`

### Dangling include
`missa/Portugues/Tempora/Pent02-0.txt:71`:
```
@Tempora/Pent04-1:Postcommunio
```
`Pent04-1.txt` has **no** `[Postcommunio]` section (verified: 0 matches). The digits are transposed — `Pent01-4.txt` does have one. The sibling file `Pent02-0r.txt` has the correct reference.

- [ ] `Pent02-0.txt:71` → `@Tempora/Pent01-4:Postcommunio`

### Missing section header
- [ ] `missa/Portugues/Tempora/Pasc7-3.txt:29` — the `[OratioL1]` header is missing entirely; its (correctly translated) collect text is orphaned inside the preceding `[GradualeL1]` section, breaking the Ember Wednesday Pentecost-vigil structure


<sub>Found by an automated pt-BR translation audit of `web/www/{horas,missa}/Portugues/**` against the Latin at the same relative path. Every item below was verified against the source files.</sub>
