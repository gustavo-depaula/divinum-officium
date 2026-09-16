# [pt-BR][missing] Canticles with verses silently dropped

**Labels:** bug, help wanted

Canticle files whose Portuguese omits verses that exist in the Latin. These render as a short canticle with no indication anything is missing.

### Tasks
- [ ] `Psalm226.txt` — **48+ of 65 verses absent** (see the markup issue for the format problem in the same file)
- [ ] `Psalm264.txt` — omits Latin `26:5` (x2), `26:6`, `26:10`, `26:11` — 4 of 12 verses dropped (around lines 28-29 and 39-40)
- [ ] `Psalm265.txt` — ends at `66:14`; the final two verses `66:15`-`66:16` are absent
- [ ] `Psalm260.txt:31-38` — verse `13:16` is absent and the surrounding labels are corrupted (an orphan `15` label with no text, `17`/`18` mislabelled, no verse 18 exists in the canticle)
- [ ] `Psalm267.txt` — verse `33:17` mislabelled `16` (real v16 merged into the v15 paragraph); final verse `33:18` absent


<sub>Found by an automated pt-BR translation audit of `web/www/{horas,missa}/Portugues/**` against the Latin at the same relative path.</sub>
