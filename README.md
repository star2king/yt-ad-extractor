markdown
# YouTube Ad Video Extractor 🎯

从浏览器复制的 YouTube 调试信息中，  
**精准提取当前正在播放的广告 / 视频链接**。

> ✅ 适用于 Network / Console 复制的 JSON  
> ✅ 不依赖 YouTube API  
> ✅ Windows / macOS / Linux 通用

---

## 使用方法（几种方法，建议手动粘贴，如自动化再考虑文件读取）

### 从文件读取（推荐 ✅）
bash

python extract.py debug_sample.json

纯文本
### 手动粘贴（交互式）
bash

python extract.py

纯文本
然后粘贴调试信息，结束按：

- Windows：`Ctrl + Z` → 回车
- macOS / Linux：`Ctrl + D`

---

## 示例输出
text

✅ 当前播放视频地址：

https://www.youtube.com/watch?v=X5t_kJXbem8

纯文本
---

## 提取规则（已验证）

优先级如下：

1. `addocid`
2. `addebug_videoId`
3. `docid`（备用）

---

## 适用场景

- 浏览器调试分析
- 广告视频识别
- 播放链路研究

---

## 许可证

MIT