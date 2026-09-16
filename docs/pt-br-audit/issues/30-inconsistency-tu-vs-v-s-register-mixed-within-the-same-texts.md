# [pt-BR][inconsistency] `tu` vs `vós` register mixed within the same texts

**Labels:** bug

The corpus addresses God as `Vós` almost everywhere. A few high-traffic places slip into `tu`.

### Tasks
- [ ] `horas/.../Common/Prayers.txt:49` — `R. E com o teu espírito`. This is the response to *Dominus vobiscum*, the most frequently repeated versicle in the Office. Should be `E com o vosso espírito`.
- [ ] `horas/Portugues/Commune/C6.txt:11` — the collect addresses God as `tu/teu/Ti` while every other collect in the same file uses `Vós/vosso`
- [ ] `horas/.../Common/Prayers.txt:244` — `salva-nos hoje com o teu poder ... observemos a tua justiça` in the same prayer that has the `pobras` typo

> The archaic `vós` register itself is deliberate and correct for this corpus — only the inconsistency is the defect.


<sub>Found by an automated pt-BR translation audit of `web/www/{horas,missa}/Portugues/**` against the Latin at the same relative path. Every item below was verified against the source files.</sub>
