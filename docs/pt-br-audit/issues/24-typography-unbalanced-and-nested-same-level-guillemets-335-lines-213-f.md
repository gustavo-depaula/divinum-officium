# [pt-BR][typography] Unbalanced and nested-same-level guillemets (335 lines, 213 files)

**Labels:** bug, help wanted

A corpus-wide sweep of `horas/Portugues` and `missa/Portugues` for lines where `«` and `»` counts differ, or where a line opens `«` more than once, found **335 lines across 213 files**.

Two distinct problems:
1. **Nested same level** — an inner quotation reuses `«` instead of `“ ”`:
   ```
   «Se algum de vós tiver um amigo, e for à meia-noite encontrá-lo, dizendo-lhe: «Empresta-me três pães...
   ```
2. **Unclosed** — a `«` with no matching `»` on the line.

Worst offenders: `missa/Portugues/Tempora/Quad6-0t.txt` (16 lines), `Quad6-0.txt` (9), `Quad6-6.txt` (8), `Tempora/093-6.txt` (6), `Pasc7-6.txt` (4), `Pasc7-6t.txt` (4), `horas/Portugues/Psalterium/Common/Rubricae.txt` (3), `Quad1-3.txt` (3), `Quad6-3/4/5.txt` (3 each), `Quad1-6.txt` (3).

> **Needs triage, not a blind sweep.** Some single-`«` lines are legitimate continuations of a quotation spanning several verses. Only genuine nesting and genuine non-closure should be changed.

> Note for the fixer: `« »` is the **correct** house style here (37 files use it vs 2 using `“ ”`), and ASCII `...` is also correct — `…` (U+2026) appears nowhere in the Portuguese or Latin corpus. Neither is a defect.

### Tasks
- [ ] Triage the 335 flagged lines
- [ ] Convert genuine inner quotations to `“ ”`
- [ ] Close genuinely unclosed quotations


<sub>Found by an automated pt-BR translation audit of `web/www/{horas,missa}/Portugues/**` against the Latin at the same relative path. Every item below was verified against the source files.</sub>
