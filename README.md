# Norsk læring (B1, bokmål)

My Norwegian study database (words, expressions, grammar rules, verbs), plus a study app with flashcards, exercises, verb drills and Anki export.

## What's in here

| Folder | What it is |
|---|---|
| `data/norsk-database.md` | Words, expressions, grammar rules, pronunciation (sections 0–5) |
| `data/norsk-verbliste.md` | Verb list with all forms (section 6) |
| `data/INSTRUKSJONER.md` | How new lessons are added (for Claude) |
| `app/template.html` | The study app (the data gets inserted at `__DB__`) |
| `scripts/build.py` | Builds `docs/index.html` (the app) and `docs/norsk-anki.txt` (Anki file) |
| `docs/` | The built app. GitHub Pages serves this folder. |
| `.github/workflows/build.yml` | Rebuilds `docs/` automatically every time `data/` changes |

## One-time setup

1. **Create the repo**: on github.com → **New repository** → name it `norsk-laering` → **Create repository** (don't add a README).
2. **Upload the files**: on the empty repo page, click **uploading an existing file**. Unzip `norsk-laering.zip` on your computer and drag **everything inside the folder** in, including the hidden `.github` folder (on Mac, press `Cmd+Shift+.` in Finder to show it) → **Commit changes**.
3. **Allow the build to save files**: **Settings → Actions → General → Workflow permissions** → choose **Read and write permissions** → **Save**.
4. **Turn on the website**: **Settings → Pages** → Source: **Deploy from a branch** → Branch: **main**, folder **/docs** → **Save**.
   After a minute the app is live at `https://<your-username>.github.io/norsk-laering/`.

> GitHub Pages is free for **public** repos. A private repo needs a paid plan (GitHub Pro) for Pages.

## After each lesson (updating)

**Option A: Claude does it (easiest).** Tell Claude "push to GitHub" after a lesson. Claude updates `data/` and pushes. The workflow rebuilds the app.

**Option B: by hand, in the browser.**
1. Download the updated `norsk-database.md` / `norsk-verbliste.md` from the claude.ai project.
2. In the repo, open the `data` folder → **Add file → Upload files** → drag in the files (they replace the old ones) → **Commit changes**.
3. Wait about 1 minute (watch the **Actions** tab). The app and the Anki file are rebuilt automatically.

**Option C: on your computer, with git.**
```bash
cp ~/Downloads/norsk-*.md data/
git add data && git commit -m "Ny time" && git push
```
To build locally instead: `python3 scripts/build.py`, then open `docs/index.html`.

## Anki

On the GitHub Pages site, the **Anki** tab has a **Last ned Anki-fil** button (all cards). You can also download `docs/norsk-anki.txt` directly. In Anki: **File → Import** → pick the file. Tags are included (`kap5`, `verb`, `verbliste`, `sterk` …), so you can filter the deck afterwards.

## Sources

Textbook examples are short quotes for personal study. The verb list is based on *238 norske verb* (grammatikk.com, Kjell H. Ullestad), checked and corrected.
