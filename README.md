# YTV for Claude Code

将 YouTube 字幕（json3 格式）自动转换为高质量**双语（英文 + 中文）SRT 字幕**的 Claude Code 工作区。

## 功能概览

- 输入 YouTube 自动生成或手动上传的英文字幕（`.en.json3`）
- 经过 7 步 AI 流水线，输出中英双语 `.srt` 字幕文件
- 可选读取视频章节信息（`.info.json`）自动插入章节标题
- 由两个 Claude Code Skill 驱动：
  - [`format-and-translate`](https://github.com/inceptiongt/format-and-translate-subtitle-plugin)：主流水线，协调全部 7 个步骤
  - [`baoyu-translate`](https://github.com/JimLiu/baoyu-skills#baoyu-translate)：高质量 AI 翻译

## 快速开始

### 前置条件

- [Claude Code](https://claude.ai/code) 已安装并登录
- [Bun](https://bun.sh) 运行时已安装（`bun --version` 验证）
- 已使用 [yt-dlp](https://github.com/yt-dlp/yt-dlp) 等工具下载视频字幕

### 下载字幕

使用 yt-dlp 下载英文字幕及视频信息：

```bash
yt-dlp --write-sub --write-auto-sub --sub-lang en \
       --write-info-json --skip-download \
       --sub-format json3 \
       -o "%(title)s/%(title)s_%(uploader)s_%(id)s_%(upload_date)s" \
       "<YouTube URL>"
```

下载完成后目录结构示例：

```
VideoTitle/
├── VideoTitle_Author_xxxxx_20251001.en.json3      # 英文字幕（必需）
├── VideoTitle_Author_xxxxx_20251001.info.json     # 视频信息（可选，含章节）
└── VideoTitle_Author_xxxxx_20251001.jpg           # 封面（不使用）
```

### 运行转换

在 Claude Code 中执行：

```
/format-and-translate <en_json_path> [info_json_path]
```

**示例：**

```
/format-and-translate "Amsterdam_s_Map_Explained/Amsterdam_s_Map_Explained_Daniel_Steiner_w1fzg9GC5UU_20251001.en.json3"
```

中间文件和最终字幕默认输出到 `<视频目录>/Subtitle/`。

## 工作流说明

| 步骤 | 类型 | 描述 |
|------|------|------|
| Step 1 | 代码 | 解析 json3，清洗字幕，生成带序号的 Markdown |
| Step 2 | AI + 代码 | 按句意确定段落边界（`[end]` 标记） |
| Step 3 | 代码 | 合并为格式化 JSON |
| Step 4 | 代码 | 整合章节标题（来自 info.json） |
| Step 5 | AI | 调用 `baoyu-translate` 翻译为中文 |
| Step 6 | AI + 代码 | 双语句级对齐 |
| Step 7 | 代码 | 生成最终双语 SRT（中文在上，英文在下） |

### 高级用法

指定执行特定步骤范围（适合断点续传）：

```
/format-and-translate video.en.json3 --steps 5-7
/format-and-translate video.en.json3 --steps 5
```

指定中间文件输出目录：

```
/format-and-translate video.en.json3 --debug-dir /tmp/output/
```

## 项目结构

```
YTV_for_claude_code/
├── .claude/
│   └── skills/
│       ├── format-and-translate/   # 字幕转换主流水线
│       └── baoyu-translate/        # AI 翻译技能
├── skills-lock.json                # 技能版本锁定
├── <VideoTitle>/                   # 每个视频一个目录
│   ├── *.en.json3                  # 英文字幕（输入）
│   ├── *.info.json                 # 视频信息（可选）
│   └── Subtitle/                   # 输出目录（自动创建）
│       ├── 1.en.indexed.md
│       ├── ...
│       ├── 7.final.srt             # 最终双语字幕
│       └── statistics.md           # 处理统计摘要
└── README.md
```

## 输出格式

`7.final.srt` 每条字幕中文在上、英文在下：

```
1
00:00:00,560 --> 00:00:06,160
阿姆斯特丹的地图和荷兰所有其他城市完全不同。
Amsterdam's map is completely different from all other Dutch cities.

2
00:00:06,160 --> 00:00:10,400
我来解释一下原因。
Let me explain why.
```

## 已安装技能版本

| 技能 | 来源 | 版本 |
|------|------|------|
| `format-and-translate` | `inceptiongt/format-and-translate-subtitle-plugin` | 1.0.0 |
| `baoyu-translate` | `jimliu/baoyu-skills` | 1.59.0 |
