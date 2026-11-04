#!/usr/bin/env python3
"""Build the study app and the Anki file from the markdown database.

Usage:  python3 scripts/build.py
Reads:  data/norsk-database.md, data/norsk-verbliste.md, app/template.html
Writes: docs/index.html (the app, for GitHub Pages) and docs/norsk-anki.txt (Anki import file)
"""
import html, re, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = [ROOT / "data/norsk-database.md", ROOT / "data/norsk-verbliste.md"]
md = "\n\n".join(p.read_text(encoding="utf-8") for p in DATA if p.exists())
if "</script" in md.lower():
    raise SystemExit("The database must not contain '</script'")

# 1) app
tpl = (ROOT / "app/template.html").read_text(encoding="utf-8")
(ROOT / "docs").mkdir(exist_ok=True)
(ROOT / "docs/index.html").write_text(tpl.replace("__DB__", md), encoding="utf-8")

# 2) Anki file (tab separated: front, back, tags)
def inline(s):
    s = html.escape(s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
    s = re.sub(r"~~(.+?)~~", r"<s>\1</s>", s)
    s = re.sub(r"\*(.+?)\*", r"<i>\1</i>", s)
    return re.sub(r"`(.+?)`", r"<code>\1</code>", s)

def cells(line):
    return [c.strip() for c in line.strip().strip("|").split("|")]

rows, sec = [], ""
lines = md.split("\n")
i = 0
while i < len(lines):
    L = lines[i]
    if L.startswith("## "):
        sec = L[3:].strip(); i += 1; continue
    if re.match(r"^### G\d+", L):
        title = re.sub(r"\s*\*\(.+?\)\*", "", L[4:].strip()); body = []; i += 1
        while i < len(lines) and not re.match(r"^#{2,3} ", lines[i]) and lines[i].strip() != "---":
            if lines[i].strip() and not re.match(r"^\|[-\s|]+\|$", lines[i].strip()):
                body.append(inline(lines[i].strip().lstrip("- ")))
            i += 1
        rows.append((inline(title), "<br>".join(body), "norsk grammatikk"))
        continue
    if L.startswith("|") and i + 1 < len(lines) and re.match(r"^\|[-\s|]+\|$", lines[i + 1].strip()):
        n = len(cells(L)); i += 2
        while i < len(lines) and lines[i].startswith("|"):
            c = cells(lines[i]); i += 1
            if sec.startswith("1") and n == 6:
                back = inline(c[2]) + (f"<br><small>{inline(c[1])}</small>" if c[1] else "") + (f"<br><i>{inline(c[3])}</i>" if c[3] else "")
                rows.append((inline(c[0]), back, "norsk ord " + c[5]))
            elif sec.startswith("2") and n == 5:
                rows.append((inline(c[0]), inline(c[1]) + (f"<br><i>{inline(c[2])}</i>" if c[2] else ""), "norsk uttrykk " + c[4]))
            elif sec.startswith("6") and n == 6:
                rows.append((inline(c[0]), f"{inline(c[4])}<br>{inline(c[1])} – {inline(c[2])} – {inline(c[3])}<br><small>{inline(c[5])}</small>", "norsk verbliste " + c[5].replace(" ", "")))
        continue
    i += 1

out = "#separator:tab\n#html:true\n#tags column:3\n" + "\n".join("\t".join(x.replace("\t", " ") for x in r) for r in rows) + "\n"
(ROOT / "docs/norsk-anki.txt").write_text(out, encoding="utf-8")
print(f"Built docs/index.html and docs/norsk-anki.txt ({len(rows)} cards)")
