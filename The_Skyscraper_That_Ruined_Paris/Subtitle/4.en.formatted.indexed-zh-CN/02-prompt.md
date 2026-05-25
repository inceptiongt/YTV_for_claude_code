# Translation Prompt — Shared Context

## Task
Translate an English YouTube documentary subtitle file into zh-CN (Simplified Chinese). This is a **refined/publication-quality** translation.

## Style & Audience
- **Style**: conversational, storytelling — smooth and engaging, like a well-produced Chinese documentary narration
- **Audience**: general Chinese viewers (no specialist knowledge assumed)
- **Humor**: preserve the presenter's light, self-deprecating humor and dry wit

## CRITICAL Format Rules (MUST follow exactly)
1. Every `[N]` numbered line must appear **on its own line** in the output — do NOT merge multiple numbers onto one line, do NOT split one number across multiple lines
2. Preserve all `[N]` index prefixes exactly as in the source
3. Translate all `# Chapter Heading` lines
4. Blank lines between sections must be preserved
5. Lines beginning with `>>` are expert interview quotes — translate them, keep the `>>` marker
6. `[snorts]` → `[笑]` (or `[嗤之以鼻]` if more natural in context)
7. Output format must be **identical in structure** to the input

## Proper Noun Corrections (ASR errors → correct translations)
The source was auto-transcribed from speech; many proper nouns are garbled. Use these corrected translations:

| Garbled ASR | Correct entity | Chinese |
|------------|---------------|---------|
| Tormon Panass / Mont Panas / Montanas / Torm Pan | Tour Montparnasse | 蒙帕纳斯大厦 |
| Osman | Baron Haussmann | 奥斯曼男爵 |
| Jagard Stang | Valéry Giscard d'Estaing | 瓦勒里·吉斯卡尔·德斯坦 |
| Lafon | La Défense | 拉德芳斯 |
| tour triangler | Tour Triangle | 三角塔楼 |
| Bazani / Pasani | Edgar Pisani | 埃德加·皮萨尼 |
| Perry | Paris | 巴黎 (when clearly meant as "Paris") |
| G manassess | Gare Montparnasse | 蒙帕纳斯火车站 |
| Maine Montanas plan | Maine-Montparnasse plan | 缅因-蒙帕纳斯计划 |
| Tuttle / Tuttles | Wy Tuttle (real-estate developer) | 怀·塔特尔（Wy Tuttle） |
| Straight Hour News | Straight Arrow News | 直箭新闻 |
| Newvel AOM | Nouvelle AOM | 新AOM建筑事务所 |
| devivver | je ne sais quoi / unique character | 独特气质 |
| unblenmished | unblemished | 无可挑剔 |
| neocclassical | neoclassical | 新古典主义 |
| Regent Streets | Regent Street | 摄政街 |

## Key Terminology
| English | Chinese |
|---------|---------|
| slip forming | 滑模施工 |
| Mansard roof | 孟莎屋顶 |
| piles / foundation piles | 桩基 |
| stratum of clay | 黏土层 |
| concrete core | 混凝土核心筒 |
| steel superstructure | 钢结构上部框架 |
| cladding | 外墙覆层 |
| hydraulic jacks | 液压千斤顶 |
| sky gardens | 空中花园 |
| transparent glazing | 透明玻璃幕墙 |
| facade | 立面 |

## Translation Principles
- **Rewrite, don't word-for-word translate**: produce natural Chinese as if a skilled Chinese writer had written it
- **Accuracy**: facts, numbers, and logic must match exactly
- **Short, punchy sentences**: the presenter style uses short punchy sentences — replicate in Chinese
- **First person**: presenter speaks in first person; keep that voice
- **Expert quotes** (>>) are slightly more formal register than presenter narration
- **Sponsor segment** (lines 30–45): keep bright, friendly promotional tone
