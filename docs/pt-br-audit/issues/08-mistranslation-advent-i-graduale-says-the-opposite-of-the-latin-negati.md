# [pt-BR][mistranslation] Advent I Graduale says the opposite of the Latin (negation misplaced)

**Labels:** bug

`missa/Portugues/Tempora/Adv1-0.txt`, sections `[Graduale]` (line 23) and `[GradualeF]` (line 30).

Latin (`missa/Latin/Tempora/Adv1-0.txt`):
```
Univérsi, qui te exspéctant, non confundéntur, Dómine.
```
"All **who wait for Thee** shall **not** be confounded, O Lord."

Portuguese:
```
Senhor, aqueles que em Vós não esperam serão confundidos.
```
"Lord, those who do **not** hope in You **shall be** confounded."

The negation has migrated from the main verb into the relative clause, inverting the sense from a promise to the faithful into a threat against the faithless. Present in both `[Graduale]` and `[GradualeF]`.

### Tasks
- [ ] `Adv1-0.txt:23` → e.g. `Senhor, todos os que esperam em Vós não serão confundidos.`
- [ ] `Adv1-0.txt:30` — same fix in `[GradualeF]`


<sub>Found by an automated pt-BR translation audit of `web/www/{horas,missa}/Portugues/**` against the Latin at the same relative path. Every item below was verified against the source files.</sub>
