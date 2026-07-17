#!/usr/bin/env python3
"""Check URLs stored in source YAML files without requiring third-party packages."""

from __future__ import annotations

import re
import sys
import time
import urllib.error
import urllib.request
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE_FILES = [
    ROOT / "sources" / "sources.yaml",
    ROOT / "sources" / "community-tutorials.yaml",
]
URL_RE = re.compile(r"https?://[^\s\]\[\)\(\}\{\"']+")


@dataclass
class Result:
    url: str
    status: str
    detail: str


def extract_urls() -> list[str]:
    urls: set[str] = set()
    for path in SOURCE_FILES:
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        for match in URL_RE.findall(text):
            urls.add(match.rstrip(".,;:"))
    return sorted(urls)


def check_url(url: str) -> Result:
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": "Mozilla/5.0 WorkBuddy-Guide-Source-Audit/1.0",
            "Accept": "text/html,application/xhtml+xml,application/json;q=0.9,*/*;q=0.8",
        },
        method="GET",
    )
    try:
        with urllib.request.urlopen(request, timeout=25) as response:
            code = int(response.getcode() or 0)
            if 200 <= code < 400:
                return Result(url, "ok", str(code))
            return Result(url, "warning", str(code))
    except urllib.error.HTTPError as exc:
        code = int(exc.code)
        if code in {404, 410}:
            return Result(url, "broken", str(code))
        if code in {401, 403, 429}:
            return Result(url, "warning", f"{code}（可能限制自动访问）")
        return Result(url, "warning", str(code))
    except (urllib.error.URLError, TimeoutError) as exc:
        return Result(url, "warning", f"网络或超时：{exc}")
    except Exception as exc:  # noqa: BLE001 - audit should report unexpected failures
        return Result(url, "warning", f"检查异常：{exc}")


def main() -> int:
    urls = extract_urls()
    if not urls:
        print("# 来源链接检查\n\n未找到可检查的 URL。")
        return 1

    results: list[Result] = []
    for index, url in enumerate(urls, start=1):
        results.append(check_url(url))
        if index < len(urls):
            time.sleep(0.25)

    ok = [result for result in results if result.status == "ok"]
    warnings = [result for result in results if result.status == "warning"]
    broken = [result for result in results if result.status == "broken"]

    print("# WorkBuddy Guide 来源链接检查")
    print()
    print(f"- 检查链接：{len(results)}")
    print(f"- 正常：{len(ok)}")
    print(f"- 警告：{len(warnings)}")
    print(f"- 确认失效：{len(broken)}")
    print()

    if broken:
        print("## 确认失效")
        print()
        for result in broken:
            print(f"- `{result.detail}` {result.url}")
        print()

    if warnings:
        print("## 需要人工复核")
        print()
        for result in warnings:
            print(f"- `{result.detail}` {result.url}")
        print()

    print("## 说明")
    print()
    print("401、403、429 或网络超时不等于页面失效，可能只是站点限制自动访问，需要人工打开确认。")
    print("只有明确返回 404 或 410 时，本脚本才把链接判定为失效。")

    return 1 if broken else 0


if __name__ == "__main__":
    sys.exit(main())
