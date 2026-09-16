# [pt-BR][typography] Trailing whitespace, double spaces and space before punctuation

**Labels:** good first issue

Mechanical scan of `horas/Portugues` + `missa/Portugues`:

- **551 lines** with trailing whitespace
- **218 lines** with a double space mid-line
- **30 lines** with a space before `,` `.` `;` `:` `!` `?`

Verified examples of the last: `horas/.../Psalmorum/Psalm84.txt:14` (`justiça :`), `Psalm106.txt:31`, `Psalm118.txt:174` (`Senhor :`), `missa/Portugues/Sancti/08-21.txt:13`. Also `horas/.../Psalmorum/Psalm15.txt:1` — double space after the `‡` marker before `(2)`.

### Tasks
- [ ] Strip trailing whitespace corpus-wide
- [ ] Collapse mid-line double spaces (check each — some may be intentional column alignment)
- [ ] Remove spaces before punctuation


<sub>Found by an automated pt-BR translation audit of `web/www/{horas,missa}/Portugues/**` against the Latin at the same relative path. Every item below was verified against the source files.</sub>
