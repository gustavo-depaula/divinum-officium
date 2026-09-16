# [pt-BR][markup] The Gloria Patri and Requiem have no `*` flex markers

**Labels:** bug, good first issue

`horas/Portugues/Psalterium/Common/Prayers.txt`

The `*` marks the mid-verse pause for chant pointing. **The Gloria Patri is said after nearly every psalm — this is the single most-repeated text in the Office.**

`[Gloria]` — Latin:
```
V. Glória Patri, et Fílio, * et Spirítui Sancto.
R. Sicut erat in princípio, et nunc, et semper, * et in sǽcula sæculórum. Amen.
```
Portuguese (no `*` on either line):
```
V. Glória ao Pai, e ao Filho e ao Espírito Santo.
R. Como era no princípio, agora e sempre, e por todos os séculos dos séculos. Amém.
```

`[Requiem]` — Latin has `Réquiem ætérnam * dona eis, Dómine.` / `Et lux perpétua * lúceat eis.`; the Portuguese has neither marker.

### Tasks
- [ ] Add `*` to both lines of `[Gloria]`
- [ ] Add `*` to both lines of `[Requiem]`


<sub>Found by an automated pt-BR translation audit of `web/www/{horas,missa}/Portugues/**` against the Latin at the same relative path. Every item below was verified against the source files.</sub>
