# [pt-BR][markup] Psalm verse numbering diverges from the Latin in 84 files

**Labels:** bug

The Latin psalter repeats or skips verse numbers wherever a long Vulgate verse is split across two printed/chant lines, and it often does not start at verse 1. **English, Spanish and Italian all follow the Latin numbering exactly. Portuguese renumbers sequentially from 1.**

Verified examples:

`Psalm20.txt` — Latin and English both start at `20:2`; Portuguese starts at `20:1` and is off by one for the whole psalm.

`Psalm22.txt` — Latin and English both print `22:4` **twice** (the split half-verse `Virga tua, et báculus tuus`); Portuguese renumbers it `22:5` and continues shifted.

`Psalm45.txt` — Latin and English start at `45:2`; Portuguese at `45:1`.

The *text* is correct and complete; only the printed prefix diverges. But these prefixes key the verse-range and optional-verse machinery, so the drift is not merely cosmetic.

### Affected files (84)
`Psalm16, 20, 21, 22, 24, 26, 27, 28, 29, 30, 31, 33, 34, 35, 36, 37, 38, 39, 40, 41, 43, 45, 46, 47, 48, 49, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 63, 64, 65, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 82, 83, 84, 85, 86, 89, 91, 96, 97, 98, 100, 101, 102, 103, 104, 105, 107, 108, 112, 128, 137, 139, 140, 141, 143, 223, 245, 250, 260, 267, 269`

### Tasks
- [ ] Realign every file's verse prefixes to the Latin at the same relative path (mechanically checkable: the sequence of prefixes should match Latin line-for-line)
- [ ] `Psalm137.txt:7` — verse translating Latin `137:6` is labelled `137:5`, duplicating the previous line's number


<sub>Found by an automated pt-BR translation audit of `web/www/{horas,missa}/Portugues/**` against the Latin at the same relative path. Every item below was verified against the source files.</sub>
