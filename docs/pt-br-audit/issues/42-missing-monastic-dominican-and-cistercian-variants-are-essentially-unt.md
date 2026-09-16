# [pt-BR][missing] Monastic, Dominican and Cistercian variants are essentially untranslated

**Labels:** enhancement

The religious-order variants of the Office have almost no Portuguese at all. Lower priority than the Roman books, but recorded for completeness.

| Directory | Latin files | Portuguese files |
|---|---|---|
| `horas/*/SanctiM` (Monastic) | 278 | **2** |
| `horas/*/TemporaM` | 266 | 0 |
| `horas/*/CommuneM` | 55 | **1** |
| `horas/*/TemporaOP` (Dominican) | 427 | 0 |
| `horas/*/SanctiOP` | 124 | 0 |
| `horas/*/CommuneOP` | 28 | 0 |
| `horas/*/SanctiCist` (Cistercian) | 192 | 0 |
| `horas/*/TemporaCist` | 172 | 0 |
| `horas/*/CommuneCist` | 59 | 0 |

### Tasks
- [ ] Decide whether the pt-BR edition should cover the order variants at all
- [ ] If yes, Monastic first (`SanctiM`/`TemporaM`/`CommuneM`), then Dominican, then Cistercian


<sub>Found by an automated pt-BR translation audit of `web/www/{horas,missa}/Portugues/**` against the Latin at the same relative path.</sub>
