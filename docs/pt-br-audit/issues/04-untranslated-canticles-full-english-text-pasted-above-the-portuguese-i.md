# [pt-BR][untranslated] Canticles: full English text pasted above the Portuguese, in 32 files

**Labels:** bug, help wanted

In `horas/Portugues/Psalterium/Psalmorum/`, 32 canticle files contain a complete English (Douay-Rheims) block **followed by** a separate Portuguese block. The English is what renders first.

Affected: `Psalm225.txt`, `Psalm226.txt`, `Psalm234.txt`, and every file `Psalm240`-`Psalm268` except `Psalm252` (which does not exist).

Notable cases:
- **`Psalm234.txt`** (Athanasian Creed, *Quicumque*): English at lines 1-40; the Portuguese at lines 43-82 is complete and correct. Just delete the English block and fix the verse labels.
- **`Psalm226.txt`** (Canticle of Moses, Deut 32): English at lines 1-66 — and see the separate issue for its incomplete Portuguese.
- **`Psalm225.txt`**: different shape — verses 3:5-3:12 (lines 8-19) and 3:13b-3:14b (lines 21-23) are left in English *interleaved* with correct Portuguese verses.

Files verified pure Portuguese with correct line counts (no action needed): `Psalm210`-`Psalm224` (except 225/226), `Psalm231`-`Psalm233`, `Psalm269`-`Psalm273`.

### Tasks
- [ ] `Psalm234.txt` — remove English block (lines 1-40)
- [ ] `Psalm226.txt` — remove English block (lines 1-66)
- [ ] `Psalm225.txt` — translate the interleaved English verses at lines 8-19 and 21-23
- [ ] `Psalm240`-`Psalm268` (29 files) — remove the English block from each, keeping the Portuguese



<sub>Found by an automated pt-BR translation audit of `web/www/{horas,missa}/Portugues/**` against the Latin at the same relative path. Every item below was verified against the source files.</sub>
