# 🎙️ Audio Daily Report

Audio 领域前沿论文与新闻日报，由 AI 每日自动抓取、总结、推送。

🔗 [在线浏览 →](https://natashastone-hub.github.io/audio-daily-report/)

## 📋 覆盖方向

- 🗣️ **TTS / 语音合成** — 零样本、流式、多语言、情感合成
- 🎵 **音频生成** — 音乐、音效、通用音频生成
- 👂 **语音识别 (ASR)** — 端到端、多语言、噪声鲁棒
- 🌐 **语音翻译 / 同声传译** — Speech-to-Speech Translation
- 🧠 **音频理解** — 音频事件检测、声场景分析、音频问答
- 🎤 **声音克隆** — 零样本跨语言声音克隆
- 🔧 **音频编码与处理** — 神经编解码、质量评估、增强

## 📅 日报归档

每日早上 9:30 自动生成，报告存放在 `reports/` 目录下，按 `YYYY-MM-DD.html` 命名。

## 🛠️ 项目结构

```
├── index.html          # 首页（自动跳转最新日报）
├── dates.json          # 日期列表（用于下拉选择）
├── reports/            # 生成的日报 HTML
├── data/               # 日报源数据 JSON
├── templates/          # HTML 模板
└── scripts/            # 生成脚本
    ├── generate_report.py      # JSON → HTML
    └── update-dates-json.ps1   # 更新日期索引
```

## 🤖 自动化

由 OpenClaw AI Agent 每天早上 9:30 (Asia/Shanghai) 自动：
1. 搜索 arXiv / HuggingFace / Web 前沿动态
2. 筛选与总结论文和新闻
3. 生成 HTML 日报并推送到 GitHub Pages
4. 通过企业微信推送摘要
