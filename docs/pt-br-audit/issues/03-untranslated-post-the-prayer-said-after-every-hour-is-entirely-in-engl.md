# [pt-BR][untranslated] `[Post]` — the prayer said after EVERY Hour — is entirely in English

**Labels:** bug

`horas/Portugues/Psalterium/Common/Prayers.txt`, section `[Post]`.

This is the *Sacrosanctae* prayer recited at the end of every single Hour. The body is English; only `R. Amém` and the `/:e em silêncio:/` rubric are Portuguese.

```
v. To the Most Holy and undivided Trinity, to the Manhood of our Lord Jesus Christ
   Crucified, to the fruitful Virginity of the most blessed and most glorious Mary...
R. Amém
_
V. Blessed be the womb of the Virgin Mary which bore the Son of the Eternal Father.
R. And blessed be the paps which gave suck to Christ our Lord.
_
/:e em silêncio:/ Pai nosso. /:e o:/ Ave Maria.
```

Latin source (`horas/Latin/Psalterium/Common/Prayers.txt`, `[Post]`):

```
v. Sacrosánctæ et indivíduæ Trinitáti, crucifíxi Dómini nostri Jesu Christi humanitáti,
   beatíssimæ et gloriosíssimæ sempérque Vírginis Maríæ fœcúndæ integritáti...
R. Amen.
_
V. Beáta víscera Maríæ Vírginis, quæ portavérunt ætérni Patris Fílium.
R. Et beáta úbera, quæ lactavérunt Christum Dóminum.
```

### Tasks
- [ ] Translate the `[Post]` section into pt-BR

**Why this is user-visible:** `setupstring` (`web/cgi-bin/DivinumOfficium/SetupString.pl:548`) layers a translation on top of `$langfb` (default **English**), which layers on Latin. So anything missing or wrong in Portuguese silently renders as English rather than failing loudly.



<sub>Found by an automated pt-BR translation audit of `web/www/{horas,missa}/Portugues/**` against the Latin at the same relative path. Every item below was verified against the source files.</sub>
