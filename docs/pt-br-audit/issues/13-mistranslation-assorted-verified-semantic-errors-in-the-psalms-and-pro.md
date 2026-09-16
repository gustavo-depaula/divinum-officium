# [pt-BR][mistranslation] Assorted verified semantic errors in the psalms and propers

**Labels:** bug

Individually small, each verified against the Latin.

### Tasks
- [ ] `horas/.../Psalmorum/Psalm105.txt:34` — Latin `servierunt sculptilibus eorum` (perfect, "they served their idols", a confession of past sin) is rendered as future `servirão os seus ídolos`
- [ ] `horas/.../Psalmorum/Psalm16.txt:15` (`16:14b`) — Latin `a paucis de terra dívide eos in vita eórum` asks God to separate the psalmist *from the wicked*; the Portuguese invents `separai os bons ... que são poucos` ("separate the good, who are few"), reversing who is separated from whom
- [ ] `horas/.../Psalmorum/Psalm50.txt:5` (`50:6`) — mixes vós-conjugation (`sejais`, `vençais`) with tu-conjugation `fores`; should be `fordes`
- [ ] `horas/.../Common/Prayers.txt` `[Requiem]` — the response `Entre os esplendores da luz perpétua` drops the verb of `Et lux perpétua lúceat eis` ("and may perpetual light shine upon them"); the Latin's second single-line form is also absent
- [ ] `missa/Portugues/Sancti/07-07.txt:10` — `[Oratio]` uses a generic collect with an unfilled `B. N.` placeholder instead of the proper collect of Ss. Cyril and Methodius; the saints' names are missing entirely
- [ ] `missa/Portugues/Ordo/Prefationes.txt:35` `[Pasch]` — the variable clause ("on this night/day, when Christ our Passover was sacrificed") is collapsed into a literal `...` ellipsis instead of being translated
- [ ] `horas/.../Common/Translate.txt` — `[Aperi]` and `[Qui cum Patre]` labels duplicate other entries' wording (wrong body part `lábios` vs `boca`; wrong person `convosco` vs `com o Pai`), which also causes duplicate-key collisions in `Revtrans.txt`


<sub>Found by an automated pt-BR translation audit of `web/www/{horas,missa}/Portugues/**` against the Latin at the same relative path. Every item below was verified against the source files.</sub>
