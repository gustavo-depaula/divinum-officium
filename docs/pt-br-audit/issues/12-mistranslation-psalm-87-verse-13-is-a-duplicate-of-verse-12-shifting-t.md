# [pt-BR][mistranslation] Psalm 87: verse 13 is a duplicate of verse 12, shifting the rest of the psalm

**Labels:** bug

`horas/Portugues/Psalterium/Psalmorum/Psalm87.txt`

Line 13 is a near-verbatim duplicate of line 12, with only the ending swapped:

```
87:12 Acaso publicará alguém na sepultura a vossa misericórdia, * e a vossa verdade na perdição?
87:13 Acaso publicará alguém na sepultura a vossa misericórdia, * e a vossa verdade no túmulo?
87:14 Porventura vossas maravilhas serão conhecidas nas trevas, * e a vossa justiça na terra do esquecimento.
```

Latin:
```
87:12 Numquid narrábit áliquis in sepúlcro misericórdiam tuam, * et veritátem tuam in perditióne?
87:13 Numquid cognoscéntur in ténebris mirabília tua, * et justítia tua in terra obliviónis?
87:14 Et ego ad te, Dómine, clamávi: * et mane orátio mea prævéniet te.
```

The real verse 13 has been pushed onto line 14, and **every verse from there to the end of the psalm is off by one**.

### Tasks
- [ ] Delete the spurious duplicate at line 13
- [ ] Renumber the remainder of the psalm to match the Latin


<sub>Found by an automated pt-BR translation audit of `web/www/{horas,missa}/Portugues/**` against the Latin at the same relative path. Every item below was verified against the source files.</sub>
