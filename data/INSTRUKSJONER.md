# Instructions: adding a new lesson (for Claude)

When Marco sends photos of book pages and/or notebook pages (with or without text like "new lesson"), follow these steps **without asking questions first**:

1. **Read the current database**: `project_read claude/norsk-database.md` (sections 0–5) and `claude/norsk-verbliste.md` (section 6, verbs).
2. **Skip repeats**: notebook pages show "N/26" in the top bar, and book pages show a page number. Pages already listed in the **Lesson log** (section 0) are skipped. Don't add entries that already exist (match on the Norsk word); just add the new source to the existing row's Kilde.
3. **Extract from the photos**:
   - Book pages: words/phrases Marco **highlighted, underlined, circled or annotated**, plus his handwritten translations. Also the chapter's *Ordliste* and *Ord og uttrykk* pages, and any grammar box.
   - Notebook pages: everything he wrote (words, translations, rules, example sentences). Use the date written on the page, or `N pX` (page number in the top bar), as Kilde.
   - If Marco wrote an answer/sentence with a mistake, add the corrected version and note it.
4. **Fill in each word** (bokmål): gender/article, all forms, English meaning, an example (from the book if possible), Kilde, tags (`kapN`, part of speech, topic).
   - Check forms on **naob.no** for words where gender or inflection is uncertain (irregular verbs, ei/en nouns, unusual plurals). WebFetch e.g. `https://naob.no/ordbok/<word>`.
   - Formats: noun = `best. sg – ubest. pl – best. pl`; verb = `presens – preteritum – har perfektum`; adjective = `m/f – n – pl/best`.
5. **Append** to the right section:
   - `1a/1b/…` vocabulary per chapter (create `1x. Kapittel N – <title>` if new), `1c` notebook words
   - `2.` expressions (5 columns: Norsk | English | Eksempel | Kilde | Tag)
   - `3.` grammar: new rule = new `### G<next number>. <title> *(kilde)*` with the rule, exceptions and examples
   - `4.` pronunciation (Oslo vs Bergen) when relevant
   - `5.` unreadable/uncertain handwriting: list it there and ask Marco at the end
   - `6.` verbliste: new verbs to drill go here (6 columns: Infinitiv | Presens | Preteritum | Perfektum | English | Gruppe). Gruppe is exactly one of: `svak -et`, `svak -te`, `svak -de`, `svak -dde`, `sterk`, `uregelmessig`, `modal`, `s-verb`. A verb learned in class goes in section 1 (with example) as usual; add it to section 6 too if it isn't there.
   - Add a row to the **Lesson log**.
6. **Keep the table formats exactly as they are** (6 columns in sections 1 and 6, 5 in section 2, `### G` headings): the study app parses them. The app balances random picks across ord / uttrykk / verb / grammatikk (weights 4/3/2/1), so the big verb list never dominates.
7. **Save**: `project_write` the changed file(s) whole: `claude/norsk-database.md` and/or `claude/norsk-verbliste.md`.
8. **Update the study app** (artifact "Norsk øvingsapp", slug in the line below): rebuild it with the new database text embedded (`read_artifact` → replace the content of `<script id="db" type="text/markdown">` with the new markdown (database file + a blank line + verbliste file, concatenated) → `publish_version` with slug + base_version).
   App slug: `3c479463-1542-464e-82fe-ee6046f11196`
9. **GitHub** (repo `norsk-laering`, owner EdgarSawtelle, once Marco has created it): attach it with `add_repo` (access "push"), copy the updated `data/*.md` files into the clone, commit ("Time <dato>") and push to `main`. The GitHub Action rebuilds `docs/index.html` + `docs/norsk-anki.txt`. If the app template changed, update `app/template.html` too. The repo's `scripts/build.py` can also be used to build the artifact page: `python3 scripts/build.py` → `docs/index.html`.
10. **Reply briefly**: how many words, expressions and rules were added, any grammar points worth explaining (clear, B1 level, with exceptions), and the uncertain items as questions.

## Marco's preferences (from the project instructions)
B1 level · bokmål · clear, direct explanations with exceptions · pronunciation notes for Oslo/Bergen · English translations · all forms of each word.
