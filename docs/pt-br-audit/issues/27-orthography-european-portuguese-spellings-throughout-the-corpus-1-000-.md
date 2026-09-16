# [pt-BR][orthography] European Portuguese spellings throughout the corpus (~1,000 occurrences)

**Labels:** enhancement, help wanted

The corpus is served as the Portuguese edition but is written in **European Portuguese** orthography. These are the pre-1990-agreement consonant clusters that Brazilian Portuguese dropped in 1943.

Corpus-wide counts over `horas/Portugues` + `missa/Portugues`:

| pt-PT form | pt-BR form | occurrences | files |
|---|---|---|---|
| `omnipotente` | `onipotente` | 362 | 221 |
| `rect-` (recto, recta, rectidão) | `ret-` | 103 | 73 |
| `protecção` | `proteção` | 89 | 79 |
| `Baptis-` / `baptiz-` | `Batis-` / `batiz-` | 124 | 43 |
| `Unigénito` | `Unigênito` | 70 | 42 |
| `protector` | `protetor` | 67 | 48 |
| `demónio` | `demônio` | 55 | 41 |
| `Egipto` | `Egito` | 53 | 26 |
| `há-de` / `hei-de` / `hão-de` | `há de` / `hei de` / `hão de` | 88 | 70 |
| `connosco` | `conosco` | 40 | 25 |
| `fact-` | `fat-` | 28 | 24 |
| `acção` | `ação` | 25 | 23 |
| `adop-` | `ado-` | 21 | 14 |
| `afect-` | `afet-` | 20 | 20 |
| `objecto` | `objeto` | 15 | 14 |
| `género` | `gênero` | 13 | 12 |
| `quotidian-` | `cotidian-` | 10 | 9 |
| `excepto` | `exceto` | 4 | 4 |

`missa/Portugues/Tempora` alone already contains `ação` 440 times against `acção` 5 — so the corpus is internally inconsistent as well as non-Brazilian.

### Tasks
- [ ] Decide the policy first: is this edition pt-BR, pt-PT, or should it be split into two (`Portugues` / `Portugues-Brasil`)? **Everything below depends on that answer.**
- [ ] If pt-BR: mechanical sweep per row above, most-frequent first
- [ ] `horas/.../Common/Translate.txt` — UI label `Avé Maria` → `Ave Maria`


<sub>Found by an automated pt-BR translation audit of `web/www/{horas,missa}/Portugues/**` against the Latin at the same relative path. Every item below was verified against the source files.</sub>
