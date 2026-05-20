# Translation Prompt

## Task
Translate an English YouTube video subtitle file to Simplified Chinese (zh-CN).

## Source Context
- **Genre**: Sports/engineering documentary narration (The B1M channel)
- **Topic**: Buffalo Bills' new NFL stadium (New Highmark) — architecture, engineering, cost, fan experience
- **Tone**: Conversational, enthusiastic, UK English, narrator speaks directly to audience
- **Style target**: Conversational Chinese — engaging, natural, as if a knowledgeable friend is narrating

## Critical Format Rules (MUST FOLLOW)
1. **Preserve `[N]` prefix on every line** — number and brackets must be identical to source
2. **One-to-one line mapping**: [1] → [1], [2] → [2], ..., [160] → [160]. Do NOT merge or split any lines.
3. **Preserve `>>` prefix** for interview quotes
4. **Preserve `#` chapter headings** — translate the heading text
5. **Preserve blank lines** between sections
6. **Keep "Brilliant"** in English (sponsor brand name)
7. **Keep `[snorts]`** as-is or translate to `[笑声]`

## Glossary (apply consistently)
| English | Chinese |
|---------|---------|
| NFL (National Football League) | NFL（美国国家橄榄球联盟）— annotate on first use only |
| Buffalo Bills | 布法罗比尔队 |
| New Highark / New Hark / New Highmark / New High Mark | 新海马克体育场 |
| Bill's Mafia | Bills Mafia球迷团 |
| Super Bowl | 超级碗 |
| hydronic system | 水暖系统 |
| snow melt system | 融雪系统 |
| canopy | 顶篷 |
| pre-cast concrete stands | 预制混凝土看台 |
| standing only section | 纯站立区 |
| game day | 比赛日 |
| form follows function | 形式服从功能 |
| SoFi Stadium | SoFi体育场 |
| Mercedes-Benz Stadium | 梅赛德斯-奔驰体育场 |
| Allegiant/Allegent Stadium | Allegiant体育场 |
| US Bank Stadium | 美国银行体育场 |
| Dallas Cowboys | 达拉斯牛仔队 |
| Real Madrid | 皇家马德里 |
| Josh Allen | 乔什·艾伦 |
| 49ers | 旧金山49人队 |
| Wrestlemania | 摔角狂热大赛 |

## Translation Principles
- Rewrite into natural, engaging Chinese — not word-for-word translation
- Break overly long Chinese sentences for readability, but keep within the `[N]` line boundary
- Use idiomatic Chinese expressions; avoid Europeanized sentence structures
- "Eyewashering" → 令人咋舌的 (likely "eyewatering" mispronounced)
- "[snorts]" → [笑] or keep
- "Across the pond" → 大西洋对岸
- "Kitted out" → 配备了
- "Rolling in money" → 财源滚滚
- "Gigs" (concerts context) → 演唱会
- "Hearkens back to" → 让人想起/回归
- Technical engineering terms: use precise Chinese equivalents
