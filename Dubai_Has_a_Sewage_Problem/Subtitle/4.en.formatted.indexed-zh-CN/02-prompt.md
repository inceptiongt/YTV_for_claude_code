# Translation Prompt

## Task
Translate a YouTube video subtitle file from English to Simplified Chinese (zh-CN).

## Style
Conversational — casual, friendly, spoken-like. As if a witty Chinese presenter is narrating this to a general audience. Preserve humor, sarcasm, and the host's personality.

## Audience
General Chinese-speaking viewers interested in construction/engineering/urban topics.

## Critical Format Rules (NON-NEGOTIABLE)
1. Every `[N]` numbered line must appear exactly once in the output — same line count, same order
2. `[N]` prefix must be preserved at the start of each line
3. Chapter headings (`# Title`) must be translated (keep `#`)
4. Do NOT merge two numbered lines into one, do NOT split one line into two
5. Verify: use `grep -c '^\[' output` — must match input count

## Glossary
| English | Chinese |
|---------|---------|
| Dubai Strategic Sewage Tunnels | 迪拜战略污水隧道 |
| Burj Khalifa | 哈利法塔 |
| Palm Jumeirah | 朱美拉棕榈岛 |
| poop snake | 粪便蛇 |
| Thames Tideway Tunnel | 泰晤士潮道隧道 |
| Jebel Ali | 杰贝阿里 |
| Deira | 德伊勒 |
| Al Warsan | 瓦尔桑 |
| Joseph Bazalgette | 约瑟夫·巴扎尔盖特 |
| Sheikh Mohammed bin Rashid Al Maktoum | 穆罕默德·本·拉希德·阿勒马克图姆酋长 |
| Great Stink | 大恶臭 |
| Brilliant | Brilliant |
| B1M | B1M |
| Megabuilds | Megabuilds |
| Penguin Random House | 企鹅兰登书屋 |
| Dubai 2040 | 迪拜2040 |
| Southern Growth Corridor | 南部增长走廊 |
| Bur Dubai | 布尔迪拜 |
| Monte Carlo | 蒙特卡洛 |

## Idiom Handling
- "up a creek without a paddle" → 束手无策/陷入困境
- "plan is a foot" → 计划已在推进（note: "a foot" is a pun on "afoot"）
- "naughties" → 千禧年初/零零年代
- "blingiest" → 最浮华的/最土豪的
- "pong" (smell) → 臭味/异味
- "mahoosive" (massive) → 超级庞大的/巨无霸
- "baubles" → 奢靡之物
- "love-it-or-hate-it" → 让人又爱又恨的
- "dunk on" → 嘲讽/贬低
- "caught short" → 措手不及

## Special Handling
- Filler "uh" → 呃（keep natural)
- ">>" → keep as ">>" (indicates interview/cut)
- "[clears throat]" → 【清清嗓子】
- Rolls-Royce running gag: maintain the absurdist humor across [52]→[63]→[67]
- Financial jargon in [54]: translate literally but keep the deliberately overcomplicated feel
- Sponsor segments [55]–[67] and [138]–[141]: keep specific details (30 days, 20%, QR code, brilliant.org/theB1M)
