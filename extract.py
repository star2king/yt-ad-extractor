#!/usr/bin/env python3
"""
YouTube 广告（当前播放视频）提取器
✅ 支持：
  python extract.py debug.json
  python extract.py   （手动粘贴）
"""

import json
import sys

def extract_real_video(data: dict) -> str | None:
    return (
        data.get("addocid")
        or data.get("addebug_videoId")
        or data.get("docid")
    )

def main():
    # 情况 1：传了文件名
    if len(sys.argv) == 2:
        path = sys.argv[1]
        try:
            with open(path, "r", encoding="utf-8") as f:
                raw_text = f.read()
        except Exception as e:
            print(f"❌ 无法读取文件：{e}")
            sys.exit(1)

    # 情况 2：没传参数 → 从 stdin
    else:
        print("📋 请粘贴 YouTube 调试信息（粘贴完 Ctrl+Z 回车）：")
        raw_text = sys.stdin.read()

    try:
        data = json.loads(raw_text)
    except json.JSONDecodeError:
        print("❌ JSON 解析失败")
        sys.exit(1)

    video_id = extract_real_video(data)
    if not video_id:
        print("❌ 未找到广告 / 播放视频")
        sys.exit(1)

    print("\n✅ 当前播放视频地址：")
    print(f"https://www.youtube.com/watch?v={video_id}")

if __name__ == "__main__":
    main()