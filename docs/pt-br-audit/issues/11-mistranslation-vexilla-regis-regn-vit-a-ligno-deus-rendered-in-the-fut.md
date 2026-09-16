# [pt-BR][mistranslation] Vexilla Regis: `Regnávit a ligno Deus` rendered in the future tense

**Labels:** bug

`horas/Portugues/Psalterium/Special/Major Special.txt:773`

```
"Deus reinará pelo lenho."
```

Latin (`Major Special.txt:1342` and `:1385`):
```
Regnávit a ligno Deus.
```

`Regnávit` is perfect — "God **has reigned** from the wood". The Portuguese future "reinará" ("will reign") reverses the theological point of this verse (an antiphon drawn from Ps 95:10, central to Passiontide).

The line also uses straight ASCII `"` quotes where the surrounding corpus uses `« »`.

### Tasks
- [ ] `Major Special.txt:773` → `«Deus reinou pelo lenho.»`


<sub>Found by an automated pt-BR translation audit of `web/www/{horas,missa}/Portugues/**` against the Latin at the same relative path. Every item below was verified against the source files.</sub>
