# [pt-BR][typo] Corrupted words in the daily core prayers

**Labels:** bug, good first issue

Each verified against the Latin and the surrounding text. These are in texts said every day.

### Tasks
- [ ] `horas/.../Common/Prayers.txt:62` `[Indulgentiam]` (said daily at Prime) — `Que o Senhor + cruz omnipotente e misericordioso...`: the **word** `cruz` has been typed next to the `+` cross glyph, producing nonsense. Latin: `Indulgéntiam, + absolutiónem et remissiónem peccatórum nostrórum tríbuat nobis omnípotens et miséricors Dóminus.`
- [ ] `horas/.../Common/Prayers.txt:244` — `mas sempre por pensamentos, palavras e pobras` → `obras`
- [ ] `horas/.../Psalmorum/Psalm232.txt:6` — **the Magnificat**, sung at Vespers daily: `Grandes maravilhas fês em mim o Omnipotente` — `fês` is not a Portuguese word → `fez`
- [ ] `horas/.../Special/Major Special.txt:877` — `Ao Pao e ao Paráclito` → `Ao Pai e ao Paráclito`
- [ ] `horas/.../Special/Major Special.txt:820,824,833,878` — `Ressucitou`/`Ressucitado` → `Ressuscitou`/`Ressuscitado` (4 occurrences, missing `s`)
- [ ] `missa/Portugues/Sancti/02-02.txt:29` — `na Vasa presença` → `na vossa presença`
- [ ] `missa/Portugues/Ordo/Post.txt:3` — sentence has no verb: `o Papa Leão XIII uma indulgência de um ano` → `o Papa Leão XIII concedeu uma indulgência de um ano`
- [ ] `horas/.../Psalmorum/Psalm216,220,221,222,223.txt:1` — header reads `Cãntico` (tilde) instead of `Cântico` (circumflex), 5 files


<sub>Found by an automated pt-BR translation audit of `web/www/{horas,missa}/Portugues/**` against the Latin at the same relative path. Every item below was verified against the source files.</sub>
