# [pt-BR][markup] `Psalm226.txt` / `Psalm234.txt` use a verse format found nowhere else in the corpus

**Labels:** bug

The Portuguese blocks in these two files use a bare verse number **alone on its own line**, with the verse text on the following one or two lines:

```
1
Escutai, ó céus, que eu vou falar, *
ouça a terra as palavras da minha boca.
2
Sejam como a chuva os meus pensamentos *
```

The corpus format is one line per verse with a `chapter:verse` prefix:
```
3:57 Bendizei o Senhor, todas as obras do Senhor: * louvai-O e aclamai-O...
```

`Psalm226.txt`'s final line is worse still — the label is glued to the text: `12Só o Senhor o conduzia, *`.

**`Psalm226.txt` is also drastically incomplete**: its Portuguese carries verse labels `1`-`12` only, i.e. **12 of the Latin's 65 verses** (~82% of the Canticle of Moses absent).

### Tasks
- [ ] `Psalm226.txt` — reformat to `32:N` prefixes, one line per verse
- [ ] `Psalm226.txt` — translate the missing verses (Latin `32:13` through `32:65`)
- [ ] `Psalm234.txt` — reformat the Portuguese block (lines 43-82) to corpus style


<sub>Found by an automated pt-BR translation audit of `web/www/{horas,missa}/Portugues/**` against the Latin at the same relative path. Every item below was verified against the source files.</sub>
