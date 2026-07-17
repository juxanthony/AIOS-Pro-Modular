#!/usr/bin/env python3
"""检查 knowledge/ 下各文件的「最后核对」日期，列出过期或未标注的文件。

用法（在仓库根目录运行）:
    python automation/scripts/stale_check.py            # 默认阈值 180 天
    python automation/scripts/stale_check.py --days 90  # 自定义阈值

依据 MEMORY.md 第 4 节: 超过 6 个月未核对的领域文件，引用时须提醒可能过期。
"""

import re
import sys
from datetime import date, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
KNOWLEDGE = ROOT / "knowledge"
DATE_RE = re.compile(r"最后核对:\s*(\d{4}-\d{2}-\d{2})")


def main() -> None:
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

    days = 180
    if "--days" in sys.argv:
        days = int(sys.argv[sys.argv.index("--days") + 1])

    today = date.today()
    stale, unmarked, fresh = [], [], []

    for f in sorted(KNOWLEDGE.rglob("*.md")):
        rel = f.relative_to(ROOT)
        m = DATE_RE.search(f.read_text(encoding="utf-8"))
        if not m:
            if f.name != "README.md":  # README 是目录说明，不要求核对日期
                unmarked.append(rel)
            continue
        checked = datetime.strptime(m.group(1), "%Y-%m-%d").date()
        age = (today - checked).days
        (stale if age > days else fresh).append((rel, age))

    print(f"knowledge/ freshness report (threshold: {days} days, today: {today})\n")
    if stale:
        print(f"[STALE] {len(stale)} file(s) need re-check:")
        for rel, age in sorted(stale, key=lambda x: -x[1]):
            print(f"  {age:>4}d  {rel}")
    if unmarked:
        print(f"[UNMARKED] {len(unmarked)} file(s) missing 最后核对 field:")
        for rel in unmarked:
            print(f"        {rel}")
    print(f"[FRESH] {len(fresh)} file(s) within threshold")
    if not stale and not unmarked:
        print("\nAll good — nothing to do.")


if __name__ == "__main__":
    main()
