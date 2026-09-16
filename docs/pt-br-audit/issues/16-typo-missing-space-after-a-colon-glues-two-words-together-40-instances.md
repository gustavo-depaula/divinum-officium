# [pt-BR][typo] Missing space after a colon glues two words together (~40 instances)

**Labels:** bug, good first issue

Pattern: a colon introducing direct speech with no following space.

Examples:
- `horas/.../Psalmorum/Psalm34.txt` — `dizei à minha alma:eu sou a tua salvação`
- `horas/.../Psalmorum/Psalm72.txt:13` — `Disse:foi portanto...`
- `horas/.../Psalmorum/Psalm105.txt:32,34,47`, `Psalm78.txt:10`, `Psalm82.txt:11`, `Psalm86.txt:5`, `Psalm103.txt:25`, `Psalm118.txt:82`, `Psalm128.txt:7`, `Psalm139.txt:7`, `Psalm140.txt:9`, `Psalm141.txt:7`

28 further instances across `Psalm31`, `34`, `38`-`41`, `44`, `54`, `61`, `63`, `65`, `67`, `69`, `70`, `72`.

### Tasks
- [ ] Regex sweep for `:[^ \n]` in `horas/Portugues/Psalterium/Psalmorum/` and insert the missing space


<sub>Found by an automated pt-BR translation audit of `web/www/{horas,missa}/Portugues/**` against the Latin at the same relative path. Every item below was verified against the source files.</sub>
