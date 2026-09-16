# [pt-BR][mistranslation] Misereatur at Mass addresses the wrong grammatical person

**Labels:** bug

`missa/Portugues/Ordo/Prayers.txt`, section `[Misereatur]`.

Latin is first-person plural throughout:
```
v. Misereátur nostri omnípotens Deus, et dimíssis peccátis nostris, perdúcat nos ad vitam ætérnam. Amen.
```

English matches ("have mercy on **us**, forgive **us** our sins, and bring **us** to everlasting life").

Portuguese switches to second-person plural:
```
v. Que o Deus omnipotente se compadeça de vós, perdoe os vossos pecados e vos conduza à vida eterna.
```

This is the Misereatur said in response to the Confiteor. As written, the congregation asks mercy for *you* rather than *us*.

### Tasks
- [ ] Rewrite as first-person plural: `...se compadeça de nós, perdoe os nossos pecados e nos conduza à vida eterna.`


<sub>Found by an automated pt-BR translation audit of `web/www/{horas,missa}/Portugues/**` against the Latin at the same relative path. Every item below was verified against the source files.</sub>
