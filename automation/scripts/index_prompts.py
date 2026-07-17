#!/usr/bin/env python3
"""扫描 prompts/ 目录，自动重建 prompts/README.md 的「当前索引」表。

用法（在仓库根目录运行）:
    python automation/scripts/index_prompts.py           # 重建索引并写回
    python automation/scripts/index_prompts.py --check   # 只检查是否过期，不写回

索引写在 README 的 <!-- INDEX:START --> 与 <!-- INDEX:END --> 标记之间。
状态规则: 「使用记录: 0 次」 → 骨架；有使用记录 → 在用。
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PROMPTS = ROOT / "prompts"
README = PROMPTS / "README.md"

TITLE_RE = re.compile(r"^#\s+(P-[A-Z]-\d{3})\s*·\s*(.+?)\s*$", re.M)
USAGE_RE = re.compile(r"使用记录:\s*(\d+)")


def collect() -> list[tuple[str, str, str]]:
    rows = []
    for f in sorted(PROMPTS.glob("*/P-*.md")):
        text = f.read_text(encoding="utf-8")
        m = TITLE_RE.search(text)
        if not m:
            print(f"[WARN] no title found, skipped: {f.relative_to(ROOT)}")
            continue
        code, name = m.group(1), m.group(2)
        um = USAGE_RE.search(text)
        status = "在用" if um and int(um.group(1)) > 0 else "骨架"
        rows.append((code, name, status))
    rows.sort(key=lambda r: r[0])
    return rows


def render(rows: list[tuple[str, str, str]]) -> str:
    lines = ["| 编号 | 名称 | 状态 |", "|---|---|---|"]
    lines += [f"| {c} | {n} | {s} |" for c, n, s in rows]
    return "\n".join(lines)


def main() -> None:
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

    rows = collect()
    table = render(rows)
    text = README.read_text(encoding="utf-8")

    pattern = re.compile(r"(<!-- INDEX:START -->\n).*?(\n<!-- INDEX:END -->)", re.S)
    if not pattern.search(text):
        sys.exit("[ERROR] markers <!-- INDEX:START/END --> not found in prompts/README.md")

    new_text = pattern.sub(lambda m: m.group(1) + table + m.group(2), text)

    if "--check" in sys.argv:
        if new_text == text:
            print(f"[OK] index up to date ({len(rows)} prompts)")
        else:
            sys.exit(f"[STALE] index out of date, run without --check to fix")
        return

    README.write_text(new_text, encoding="utf-8")
    print(f"[OK] index rebuilt: {len(rows)} prompts -> prompts/README.md")


if __name__ == "__main__":
    main()
