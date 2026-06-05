这是大陆程序员大辉为了下载油管广告视频而做的小程序，
第一个程序，很简单，以后再设计高级的
（Written by Da Hui, a software developer based in mainland China,  this project is aimed at extracting YouTube ad videos.  It represents my first step into tool-building, kept deliberately simple,  with more sophisticated versions planned ahead.）
# YouTube Ad Video Extractor 🎯

从浏览器复制的 YouTube 调试信息中，  
**精准提取当前正在播放的广告 / 视频链接**。  
(Extract the currently playing ad/video URL directly from YouTube debugging information copied from the browser.)

> ✅ 适用于 Network / Console 复制的 JSON  
> (Applicable to JSON copied from Network / Console)
>
> ✅ 不依赖 YouTube API  
> (Does not rely on the YouTube API)
>
> ✅ Windows / macOS / Linux 通用  
> (Works across Windows / macOS / Linux)

---

## 使用方法（几种方法，建议手动粘贴，如自动化再考虑文件读取）
(Usage — multiple methods; manual paste is recommended, use file input only when automating)

### 从文件读取（推荐 ✅）
(Read from a file — recommended)

bash
python extract.py debug_sample.json


### 手动粘贴（交互式）
(Manual paste — interactive mode)

bash
python extract.py


然后粘贴调试信息，结束按：  
(Paste the debugging information, then finish by pressing:)

- Windows：`Ctrl + Z` → 回车 (Enter)
- macOS / Linux：`Ctrl + D`

---

## 示例输出
(Example Output)

text
✅ 当前播放视频地址：
(Currently playing video URL:)

https://www.youtube.com/watch?v=X5t_kJXbem8


---

## 提取规则（已验证）
(Extraction Rules — verified)

优先级如下：  
(The priority order is as follows:)

1. `addocid`
2. `addebug_videoId`
3. `docid`（备用）  
   (fallback)

---

## 适用场景
(Use Cases)

- 浏览器调试分析  
  (Browser debugging & analysis)
- 广告视频识别  
  (Ad video identification)
- 播放链路研究  
  (Playback pipeline research)

---

## 许可证
(License)

MIT
