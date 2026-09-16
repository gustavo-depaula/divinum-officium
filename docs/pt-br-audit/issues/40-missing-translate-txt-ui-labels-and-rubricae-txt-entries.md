# [pt-BR][missing] `Translate.txt` UI labels and `Rubricae.txt` entries

**Labels:** enhancement, good first issue

`horas/Portugues/Psalterium/Common/Translate.txt` holds the interface labels. It is missing ~52 keys that the Latin has, so those labels fall back to English in the UI.

### Tasks
- [ ] Missing standalone labels and aliases (enumerate against `horas/Latin/Psalterium/Common/Translate.txt`)
- [ ] The whole `Preces` label block
- [ ] Lower-priority Appendix and refectory keys
- [ ] `horas/Portugues/Psalterium/Common/Rubricae.txt` — missing `[Pater totum secreto]` and `[Preces flexis genibus]`
- [ ] Fix `Avé Maria` → `Ave Maria` while in this file
- [ ] Fix the `[Aperi]` / `[Qui cum Patre]` duplicate-wording bug (see the mistranslation issue)


<sub>Found by an automated pt-BR translation audit of `web/www/{horas,missa}/Portugues/**` against the Latin at the same relative path.</sub>
