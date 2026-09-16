# [pt-BR][typo] `passa- das` — broken hyphenation from a bad import, in 21+ files

**Labels:** bug, good first issue

A line-break hyphenation artifact from a PDF/OCR import was copy-pasted across nearly every Lenten feria file:

```
Esquecei-Vos, Senhor, das nossas iniquidades passa- das, apressai-Vos em revestir-nos...
```

`passa- das` should be `passadas`.

Affected files in `missa/Portugues/Tempora/`: `Quad1-1`, `Quad1-5`, `Quad2-1`, `Quad2-3`, `Quad2-5`, `Quad3-1`, `Quad3-3`, `Quad3-3t`, `Quad3-5`, `Quad3-5t`, `Quad4-1`, `Quad4-3`, `Quad4-3t`, `Quad4-5`, `Quad4-5t`, `Quad5-3`, `Quad5-3t`, `Quad5-5Feria`, `Quad6-1`, `Quadp3-3`, `Quadp3-5`.

### Tasks
- [ ] Fix all occurrences of `passa- das` → `passadas`
- [ ] Sweep the corpus for the general pattern `[a-zà-ú]- [a-zà-ú]` to catch other imports of the same kind


<sub>Found by an automated pt-BR translation audit of `web/www/{horas,missa}/Portugues/**` against the Latin at the same relative path. Every item below was verified against the source files.</sub>
