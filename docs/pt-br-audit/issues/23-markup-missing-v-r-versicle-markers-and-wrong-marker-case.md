# [pt-BR][markup] Missing `V.`/`R.` versicle markers and wrong marker case

**Labels:** bug

### Missing `V.`/`R.` where the Latin has them
- [ ] `missa/Portugues/Sancti/06-29.txt:29` (Ss. Peter & Paul) — the `V.` before the Graduale's second verse is dropped, merging it into the antiphon
- [ ] Broader sweep: 468 lines corpus-wide where the Latin line at the same position starts with `V.`/`R.`/`v.`/`R.br.` and the Portuguese does not. Needs triage — some are legitimate structural differences.

### Wrong marker case
- [ ] `horas/Portugues/Psalterium/Special/Minor Special.txt:2,19,36,53,58` — hymn/chapter incipits use capital `V.` where the corpus (and `Major Special.txt`, and the Latin) use lower-case `v.`. Capital `V.`/`R.` is reserved for versicle/response pairs.

### Broken reverse-lookup keys
- [ ] `horas/Portugues/Psalterium/Revtrans.txt` — `[Antest]` should be `[Antes]` and its value is missing the `$` prefix; `[After]` is an untranslated English key that should be `[Depois]` mapping to `$Post`. Both break the Ante/Post navigation shown at the start and end of every Hour.


<sub>Found by an automated pt-BR translation audit of `web/www/{horas,missa}/Portugues/**` against the Latin at the same relative path. Every item below was verified against the source files.</sub>
