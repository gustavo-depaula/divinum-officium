# Brazilian Portuguese translation audit

Catalogue of defects and gaps in `web/www/horas/Portugues/**` and
`web/www/missa/Portugues/**`, produced by an automated audit that compared every
Portuguese file against the Latin at the same relative path (and against the
English, Spanish and Italian editions where that helped tell a real defect from a
house convention).

**715 findings** were collected and grouped into the 42 issue drafts below.

## Why gaps are user-visible

`setupstring` (`web/cgi-bin/DivinumOfficium/SetupString.pl:548`) layers a
translation on top of `$langfb`, which **defaults to English**, which in turn
layers on Latin. Anything missing from a Portuguese file therefore renders as
**English**, silently — it does not fall back to Latin and it does not fail
loudly. This is why so much foreign text shows up while praying.

## Coverage

| | Latin files | Portuguese files | Latin files with no PT counterpart |
|---|---|---|---|
| Office (`horas`) | 4,973 | 597 | 4,378 |
| Mass (`missa`) | 1,066 | 566 | 503 |

Plus 6,303 sections present in Latin but absent from a Portuguese file that does
exist (excluding `[Rule]` and `[Missa]`, which are machine-parsed directives and
not translatable).

## Findings by category

| category | count |
|---|---|
| pt-pt-variant | 164 |
| untranslated | 142 |
| markup | 108 |
| missing-text | 106 |
| typo | 84 |
| typography | 71 |
| inconsistency | 17 |
| mistranslation | 17 |
| encoding | 6 |

## Issue drafts

| # | Title | Labels |
|---|---|---|
| 1 | [[pt-BR][untranslated] Holy Week & Triduum Mass files are verbatim copies of the English files](issues/01-untranslated-holy-week-triduum-mass-files-are-verbatim-copies-of-the-e.md) | bug, help wanted |
| 2 | [[pt-BR][untranslated] 48 more Portuguese files are near-verbatim copies of their English counterparts](issues/02-untranslated-48-more-portuguese-files-are-near-verbatim-copies-of-thei.md) | bug, help wanted |
| 3 | [[pt-BR][untranslated] `[Post]` — the prayer said after EVERY Hour — is entirely in English](issues/03-untranslated-post-the-prayer-said-after-every-hour-is-entirely-in-engl.md) | bug |
| 4 | [[pt-BR][untranslated] Canticles: full English text pasted above the Portuguese, in 32 files](issues/04-untranslated-canticles-full-english-text-pasted-above-the-portuguese-i.md) | bug, help wanted |
| 5 | [[pt-BR][untranslated] `[Officium]` feast titles left in Latin in ~86 Office files](issues/05-untranslated-officium-feast-titles-left-in-latin-in-86-office-files.md) | bug, good first issue |
| 6 | [[pt-BR][untranslated] Isolated Latin/English passages left inside otherwise-translated files](issues/06-untranslated-isolated-latin-english-passages-left-inside-otherwise-tra.md) | bug |
| 7 | [[pt-BR][mistranslation] Easter Sunday rubric says purple vestments instead of white](issues/07-mistranslation-easter-sunday-rubric-says-purple-vestments-instead-of-w.md) | bug, good first issue |
| 8 | [[pt-BR][mistranslation] Advent I Graduale says the opposite of the Latin (negation misplaced)](issues/08-mistranslation-advent-i-graduale-says-the-opposite-of-the-latin-negati.md) | bug |
| 9 | [[pt-BR][mistranslation] `raca` corrupted to `faca` ("knife") in the Gospel of Pentecost V](issues/09-mistranslation-raca-corrupted-to-faca-knife-in-the-gospel-of-pentecost.md) | bug, good first issue |
| 10 | [[pt-BR][mistranslation] Misereatur at Mass addresses the wrong grammatical person](issues/10-mistranslation-misereatur-at-mass-addresses-the-wrong-grammatical-pers.md) | bug |
| 11 | [[pt-BR][mistranslation] Vexilla Regis: `Regnávit a ligno Deus` rendered in the future tense](issues/11-mistranslation-vexilla-regis-regn-vit-a-ligno-deus-rendered-in-the-fut.md) | bug |
| 12 | [[pt-BR][mistranslation] Psalm 87: verse 13 is a duplicate of verse 12, shifting the rest of the psalm](issues/12-mistranslation-psalm-87-verse-13-is-a-duplicate-of-verse-12-shifting-t.md) | bug |
| 13 | [[pt-BR][mistranslation] Assorted verified semantic errors in the psalms and propers](issues/13-mistranslation-assorted-verified-semantic-errors-in-the-psalms-and-pro.md) | bug |
| 14 | [[pt-BR][typo] Corrupted words in the daily core prayers](issues/14-typo-corrupted-words-in-the-daily-core-prayers.md) | bug, good first issue |
| 15 | [[pt-BR][typo] `passa- das` — broken hyphenation from a bad import, in 21+ files](issues/15-typo-passa-das-broken-hyphenation-from-a-bad-import-in-21-files.md) | bug, good first issue |
| 16 | [[pt-BR][typo] Missing space after a colon glues two words together (~40 instances)](issues/16-typo-missing-space-after-a-colon-glues-two-words-together-40-instances.md) | bug, good first issue |
| 17 | [[pt-BR][markup] Psalm verse numbering diverges from the Latin in 84 files](issues/17-markup-psalm-verse-numbering-diverges-from-the-latin-in-84-files.md) | bug |
| 18 | [[pt-BR][markup] The Gloria Patri and Requiem have no `*` flex markers](issues/18-markup-the-gloria-patri-and-requiem-have-no-flex-markers.md) | bug, good first issue |
| 19 | [[pt-BR][markup] The Te Deum has no `*` flex markers, in both copies](issues/19-markup-the-te-deum-has-no-flex-markers-in-both-copies.md) | bug, good first issue |
| 20 | [[pt-BR][markup] Four canticles have no `*`/`†` pause markers at all](issues/20-markup-four-canticles-have-no-pause-markers-at-all.md) | bug |
| 21 | [[pt-BR][markup] `Psalm226.txt` / `Psalm234.txt` use a verse format found nowhere else in the corpus](issues/21-markup-psalm226-txt-psalm234-txt-use-a-verse-format-found-nowhere-else.md) | bug |
| 22 | [[pt-BR][markup] Broken `$` directives and a dangling `@` include](issues/22-markup-broken-directives-and-a-dangling-include.md) | bug |
| 23 | [[pt-BR][markup] Missing `V.`/`R.` versicle markers and wrong marker case](issues/23-markup-missing-v-r-versicle-markers-and-wrong-marker-case.md) | bug |
| 24 | [[pt-BR][typography] Unbalanced and nested-same-level guillemets (335 lines, 213 files)](issues/24-typography-unbalanced-and-nested-same-level-guillemets-335-lines-213-f.md) | bug, help wanted |
| 25 | [[pt-BR][typography] Trailing whitespace, double spaces and space before punctuation](issues/25-typography-trailing-whitespace-double-spaces-and-space-before-punctuat.md) | good first issue |
| 26 | [[pt-BR][encoding] U+FFFD replacement characters in two Holy Week files](issues/26-encoding-u-fffd-replacement-characters-in-two-holy-week-files.md) | bug, good first issue |
| 27 | [[pt-BR][orthography] European Portuguese spellings throughout the corpus (~1,000 occurrences)](issues/27-orthography-european-portuguese-spellings-throughout-the-corpus-1-000-.md) | enhancement, help wanted |
| 28 | [[pt-BR][orthography] Pre-reform archaisms that are wrong in both pt-BR and pt-PT](issues/28-orthography-pre-reform-archaisms-that-are-wrong-in-both-pt-br-and-pt-p.md) | enhancement |
| 29 | [[pt-BR][inconsistency] Scripture-book abbreviations, including one wrong-book citation](issues/29-inconsistency-scripture-book-abbreviations-including-one-wrong-book-ci.md) | bug |
| 30 | [[pt-BR][inconsistency] `tu` vs `vós` register mixed within the same texts](issues/30-inconsistency-tu-vs-v-s-register-mixed-within-the-same-texts.md) | bug |
| 31 | [[pt-BR][missing] Office: the entire temporal cycle is untranslated](issues/31-missing-office-the-entire-temporal-cycle-is-untranslated.md) | enhancement, help wanted |
| 32 | [[pt-BR][missing] Office: the 12 Commons are title-and-Mass-only stubs](issues/32-missing-office-the-12-commons-are-title-and-mass-only-stubs.md) | enhancement, help wanted |
| 33 | [[pt-BR][missing] Office Sancti: 187 feasts have no file, and 264 of 298 existing files are stubs](issues/33-missing-office-sancti-187-feasts-have-no-file-and-264-of-298-existing-.md) | enhancement, help wanted |
| 34 | [[pt-BR][missing] `Sancti/Brasilia` is absent — including Nossa Senhora Aparecida, patroness of Brazil](issues/34-missing-sancti-brasilia-is-absent-including-nossa-senhora-aparecida-pa.md) | enhancement, help wanted |
| 35 | [[pt-BR][missing] Mass Sancti: 174 feasts have no Portuguese file](issues/35-missing-mass-sancti-174-feasts-have-no-portuguese-file.md) | enhancement, help wanted |
| 36 | [[pt-BR][missing] Mass Sancti: sections missing from files that do exist](issues/36-missing-mass-sancti-sections-missing-from-files-that-do-exist.md) | enhancement, help wanted |
| 37 | [[pt-BR][missing] Mass Tempora: stub files and missing sections](issues/37-missing-mass-tempora-stub-files-and-missing-sections.md) | enhancement, help wanted |
| 38 | [[pt-BR][missing] Psalterium Special: Terce/Sext/None, Preces and the Litany are absent](issues/38-missing-psalterium-special-terce-sext-none-preces-and-the-litany-are-a.md) | enhancement, help wanted |
| 39 | [[pt-BR][missing] Canticles with verses silently dropped](issues/39-missing-canticles-with-verses-silently-dropped.md) | bug, help wanted |
| 40 | [[pt-BR][missing] `Translate.txt` UI labels and `Rubricae.txt` entries](issues/40-missing-translate-txt-ui-labels-and-rubricae-txt-entries.md) | enhancement, good first issue |
| 41 | [[pt-BR][missing] Mass Ordinary: Suffragium, Coronatio, Advent preface, and 6 Ordo variants](issues/41-missing-mass-ordinary-suffragium-coronatio-advent-preface-and-6-ordo-v.md) | enhancement, help wanted |
| 42 | [[pt-BR][missing] Monastic, Dominican and Cistercian variants are essentially untranslated](issues/42-missing-monastic-dominican-and-cistercian-variants-are-essentially-unt.md) | enhancement |

## Reproducing / filing

`issues.json` holds the same 42 drafts as `{title, body, labels}` objects, ready
to POST to `/repos/{owner}/{repo}/issues`.

`findings.json` holds all 715 raw findings with file, line, section, the Latin
source line, the offending Portuguese, the problem and a suggested fix.

`VERIFICATION.md` records which subagent claims were checked by hand, which were
confirmed, and which were **rejected as false positives** — read it before
trusting any single finding.
