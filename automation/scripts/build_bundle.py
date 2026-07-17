#!/usr/bin/env python3
"""AIOS Pro 跨平台打包脚本。

把 system/ 六件套（按启动顺序）与指定引擎拼成单个 Markdown 文件，
输出到 dist/，供上传 Claude Projects / ChatGPT GPTs / Gemini Gems，
或作为 Ollama Modelfile 的 SYSTEM 段。

用法（在仓库根目录运行）:
    python automation/scripts/build_bundle.py core          # 只打包 system 六件套
    python automation/scripts/build_bundle.py teaching      # system + 教学引擎
    python automation/scripts/build_bundle.py --all         # core + 每个引擎各一包
    python automation/scripts/build_bundle.py --list        # 列出可用引擎

仅用 Python 标准库，无需安装任何依赖。
"""

import sys
from datetime import datetime
from pathlib import Path

# system 文件按 SYSTEM.md 规定的启动顺序拼接
SYSTEM_ORDER = [
    "SYSTEM.md",
    "IDENTITY.md",
    "RULES.md",
    "MEMORY.md",
    "THINKING.md",
    "SELF_IMPROVEMENT.md",
]

ROOT = Path(__file__).resolve().parents[2]
DIST = ROOT / "dist"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8").strip()


def section(rel_name: str, content: str) -> str:
    return f"\n\n<!-- ========== FILE: {rel_name} ========== -->\n\n{content}"


def build(engine: str | None) -> Path:
    name = engine or "core"
    parts = []
    included = []

    for fname in SYSTEM_ORDER:
        p = ROOT / "system" / fname
        parts.append(section(f"system/{fname}", read(p)))
        included.append(f"system/{fname}")

    if engine:
        p = ROOT / "engines" / f"{engine}.md"
        if not p.exists():
            sys.exit(f"[ERROR] engine not found: engines/{engine}.md "
                     f"(use --list to see available engines)")
        parts.append(section(f"engines/{engine}.md", read(p)))
        included.append(f"engines/{engine}.md")

    stamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    header = (
        f"# AIOS Pro Bundle · {name}\n\n"
        f"> 生成时间: {stamp} · 生成工具: automation/scripts/build_bundle.py\n"
        f"> 包含: {', '.join(included)}\n"
        f"> 使用方式: 上传后对 AI 说「请阅读全文并遵守其中协议，然后开始工作」。\n"
        f"> ⚠️ 本文件含私密层信息（IDENTITY 等），只上传到你本人的账号，不公开分享。\n"
    )

    DIST.mkdir(exist_ok=True)
    out = DIST / f"aios_{name}.md"
    out.write_text(header + "".join(parts) + "\n", encoding="utf-8")
    return out


def available_engines() -> list[str]:
    return sorted(p.stem for p in (ROOT / "engines").glob("*.md")
                  if p.name != "README.md")


def main() -> None:
    # Windows 控制台默认编码可能不是 UTF-8，安全重配置，失败也不影响打包
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

    args = sys.argv[1:]
    if not args or args[0] in ("-h", "--help"):
        print(__doc__)
        return
    if args[0] == "--list":
        print("available engines:")
        for e in available_engines():
            print(f"  {e}")
        return

    targets: list[str | None]
    if args[0] == "--all":
        targets = [None] + list(available_engines())
    elif args[0] == "core":
        targets = [None]
    else:
        targets = [args[0]]

    for t in targets:
        out = build(t)
        size_kb = out.stat().st_size / 1024
        print(f"[OK] {out.relative_to(ROOT)}  ({size_kb:.1f} KB)")


if __name__ == "__main__":
    main()
