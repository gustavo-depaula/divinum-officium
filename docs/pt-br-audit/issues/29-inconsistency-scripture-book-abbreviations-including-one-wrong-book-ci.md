# [pt-BR][inconsistency] Scripture-book abbreviations, including one wrong-book citation

**Labels:** bug

### Wrong book (a real citation error)
`Sb` is the abbreviation for *Sabedoria* (Wisdom), but it is also used for Latin `Eccli` (*Ecclesiasticus/Eclesiástico*, a different book) in ~31 places. Elsewhere the corpus uses `Ecl` for the same book (11x).

- [ ] Audit every `Sb` citation; where the Latin says `Eccli`, change to `Eclo`
- [ ] `missa/Portugues/Tempora/Pasc7-5.txt:29` and `Pasc7-5t.txt` — Psalm 12 (Latin `Ps 12:1`) is cited as `Sb 12:1`. Wrong book.

### Internal inconsistency
- [ ] `Sl` (1,273x) vs `Ps` (14x) for Psalms — standardise on `Sl`
- [ ] `Mt.` with trailing dot (7x) vs `Mt` (29x)
- [ ] `Dn` vs `Dan`; `Ecl` vs `Sb`; `Jn` vs `Jo` for John (`Jn` also reads as Jonas — genuinely ambiguous)
- [ ] `missa/Portugues/Tempora/Pasc0-0.txt` — Introitus cited as `Sl. 1:38; 1:18; 1:5-6`, a corrupted rendering of `Sl 138:18; 138:5-6`
- [ ] The `V. Ps NN:N ...` leaked-Latin-citation pattern (missing `!` tag, stray `V.` marker) in `Nat1-0`, `Epi1-0`, `Epi3-0`, `Pent03-0r`, `Quadp3-5`

> Localised abbreviations themselves are correct — `Sl` for `Ps` is proper Portuguese. Only the wrong book and the inconsistency need fixing.


<sub>Found by an automated pt-BR translation audit of `web/www/{horas,missa}/Portugues/**` against the Latin at the same relative path. Every item below was verified against the source files.</sub>
