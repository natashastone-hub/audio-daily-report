# -*- coding: utf-8 -*-
"""Build data/2026-11-09.json from the cached arXiv XML + curated Chinese summaries."""
import json, os, xml.etree.ElementTree as ET

NS = {'a': 'http://www.w3.org/2005/Atom'}
BASE = os.path.join(os.path.dirname(__file__), '..')

CURATED = {
    "2611.08092": {
        "zh": "提出 E-Gaborformer：严格因果（不看未来音频）的流式语音识别编码器，用门控 DeltaNet-2 循环层与滑窗注意力按 3:1 混合，所有时域卷积都由固定的因果 Gabor 原子字典构建。流式状态恒定（生产规模下约 19MB/通话，同尺寸因果注意力编码器十分钟后超 1GB）。LibriSpeech 受控实验中最快提前 18% 达到目标精度；生产环境 0.6B 希伯来语+英语流式 transducer 相比同尺寸 NVIDIA Nemotron 3.5 ASR Streaming 在英语语音智能体流量上 WER 低 28-31%，希伯来语 WER 相对旧生产系统低至多 20%，同一套权重可同时服务严格因果与 480ms 前瞻解码。",
        "tags": ["ASR", "Streaming", "Causal Encoder", "Gated DeltaNet", "Production"],
        "highlight": True,
        "links": [{"label": "arXiv", "url": "https://arxiv.org/abs/2611.08092"},
                  {"label": "PDF", "url": "https://arxiv.org/pdf/2611.08092"}],
    },
    "2611.08972": {
        "zh": "提出 AccentCanvas：一个共享的离散扩散模型，同时做「口音归一化」和「L1→L2 口音转换」，用于配音场景（要改发音但保留内容、音色与原始时间对齐）。训练数据为跨配对同 prompt 录音与合成配对；用帧级语音活动与保重复单元在合成过程中引导局部时长。两项任务上口音转换效果（Accent Arrival）与听感口音相似度均为最优，语音边界误差比最强基线低 73% 以上；代价是 L1→L2 的 WER 高于 TokAN / Vevo-Style，揭示了「口音相似度」与「可识别度」之间的取舍。",
        "tags": ["Accent Conversion", "Discrete Diffusion", "Dubbing", "Speech Editing"],
        "highlight": True,
        "links": [{"label": "arXiv", "url": "https://arxiv.org/abs/2611.08972"},
                  {"label": "PDF", "url": "https://arxiv.org/pdf/2611.08972"},
                  {"label": "Demo", "url": "https://smokedindia.github.io/accentcanvas/"}],
    },
    "2611.08695": {
        "zh": "提出 FoleyForge：面向音效（sound effects）的指令驱动编辑生成模型——给一段音频和一句自由文本指令，在保持原音频身份的前提下完成语义、风格或类 DSP 的修改，单一模型覆盖全部编辑类型。由于公开音频编辑数据缺失，作者用音频语言模型自动构造「DSP 声学编辑 + 相似性保持语义编辑」数据，再用其微调 rectified-flow 音频生成模型，并把响度变化、编辑强度、输入派生的轮廓包络做成可经 CFG 调节的属性控制。指令遵循度达 SOTA，音质与源保真度有竞争力。",
        "tags": ["Audio Editing", "Sound Effects", "Rectified Flow", "Instruction Following"],
        "highlight": True,
        "links": [{"label": "arXiv", "url": "https://arxiv.org/abs/2611.08695"},
                  {"label": "PDF", "url": "https://arxiv.org/pdf/2611.08695"}],
    },
    "2611.08758": {
        "zh": "针对基于大自监督前端语音伪造检测器在域偏移（未见合成器、传输编解码、陌声声学环境）下退化的问题，提出冲突感知元学习框架 CAML：base-DGS 用非对称投影把 meta-train 梯度作为主锚点；EMA-DGS 用指数滑动平均的稳定锚点减少域偏移引发的梯度冲突；LW-DGS 把干预细化到逐层参数张量。在多个跨数据集基准与架构上多数设置 EER 优于基线，最大相对改善 45.2%。",
        "tags": ["Deepfake Detection", "Domain Generalization", "Meta-Learning", "Speech Security"],
        "highlight": False,
        "links": [{"label": "arXiv", "url": "https://arxiv.org/abs/2611.08758"},
                  {"label": "PDF", "url": "https://arxiv.org/pdf/2611.08758"}],
    },
    "2611.08791": {
        "zh": "研究「头顶飞过的飞机能否定位录音地点」：螺旋桨/旋翼在音频中留下多普勒曲线，公开 ADS-B 档案记录装有设备的飞机。作者做了预注册、带时间戳盲测：24 个新地点、录音端自带时钟、300 秒容差、20km 见方区域内，三个定位器中最好的一个在 4 个地点把清晰掠过片段定位到 1km 内（随机猜期望 0.57，校正后 p=0.0065），时间错位或音频互换则全部失败。另在 1600 段随机公开录音上，定位器最多作答 20 次、最多命中 2 次。发布 AircraftWitness 基准与 1170 万条录音的通行标签，附带代码。",
        "tags": ["Audio Forensics", "Geo-localization", "Benchmark", "Privacy"],
        "highlight": False,
        "links": [{"label": "arXiv", "url": "https://arxiv.org/abs/2611.08791"},
                  {"label": "PDF", "url": "https://arxiv.org/pdf/2611.08791"},
                  {"label": "GitHub", "url": "https://github.com/nyu-kr/aircraftwitness"}],
    },
    "2611.08966": {
        "zh": "指出连续音乐情绪识别（MER）常用指标「逐帧相关性池化」被曲间差异主导，无法区分「跟着情绪走」与「只会按歌曲平均排序」的模型。作者把标注方差分解为曲间/曲内两部分，用滑窗 Lin 一致性相关系数（CCC）对准曲内动态，并用单一权重 λ 控制取舍（DEAM 1764 首上 λ 从 0→1：池化 Arousal r 0.843→0.810，曲内平均 r 0.204→0.368）。据此提出开源模型 MMAS：冻结 MERT-v1-95M 嵌入 + 自动转谱得到的十维符号特征，双分支时序卷积 + 跨模态注意力，每 0.5s 预测 Arousal/Valence，支持 DEAM 与 PMEmo 联合训练，并给出 split-conformal 置信区间（93.7% / 90.0% 覆盖率）。",
        "tags": ["Music Emotion Recognition", "Evaluation Metric", "Conformal Prediction", "Open Source"],
        "highlight": False,
        "links": [{"label": "arXiv", "url": "https://arxiv.org/abs/2611.08966"},
                  {"label": "PDF", "url": "https://arxiv.org/pdf/2611.08966"}],
    },
}

NEWS = [
    {
        "title": "Shizuku AI 发布 Shizuku-Duplex：80ms 心跳的日文全双工语音模型，支持后台工具调用",
        "url": "https://shizuku.ai/en/blog/1/",
        "summary": "日本初创 Shizuku AI 于 11 月 8 日发布 Shizuku-Duplex，称其为除 OpenAI GPT-Live 之外首个具备智能对话能力的日文全双工模型。核心设计：80ms 一个 tick，每个 tick 同时听与说（用 TensorRT/Triton 优化保证单 tick <80ms 实时预算）；先以文本形式生成「内心独白」再合成语音，从而自行决定何时开口/何时沉默；交互模型 + 后台模型双脑结构，遇到搜索或重推理时输出 DELEGATE token 交给后台工具模型，前台继续对话（示例中 web 搜索耗时 7.1s 而对话未中断）；每约 5 分钟自动压缩上下文（auto-compaction），切换在单 tick 内完成。自建日文全双工评测集（内容打分由 Claude Opus 5.5 担任裁判）显示：六模型中对话自然度最高，六项轮次转换指标中五项为全双工模型最优，响应内容仅次于 GPT-Live；语音结束到回复中位延迟 0.57s（GPT-Live 0.53s、Gemini Live 1.27s、GPT-Realtime 1.61s）。注意均为厂商自评，权重未开源。"
    }
]

NOTE = "本报告窗口覆盖 2026-11-08 09:30 → 2026-11-09 10:50（Asia/Shanghai）。arXiv eess.AS / cs.SD 在 11-07 至 11-09 无新提交（周末无公告），故论文部分以「补录 11-05/11-06 批次中此前早报/午报未覆盖的 audio 相关工作」为主；新闻侧周末发布量极低，仅 Shizuku-Duplex 落在 24 小时窗口内。"


def main():
    tree = ET.parse(os.path.join(BASE, '_arxiv_today.xml'))
    entries = {}
    for e in tree.getroot().findall('a:entry', NS):
        aid = e.find('a:id', NS).text.split('/abs/')[-1]
        aid = aid.split('v')[0]
        entries[aid] = e

    papers = []
    for aid, c in CURATED.items():
        e = entries.get(aid)
        if e is None:
            raise SystemExit('missing ' + aid)
        title = ' '.join(e.find('a:title', NS).text.split())
        pub = e.find('a:published', NS).text[:10]
        authors = [a.find('a:name', NS).text for a in e.findall('a:author', NS)]
        authors_str = ', '.join(authors) if len(authors) <= 4 else ', '.join(authors[:3]) + ', et al.'
        papers.append({
            "title": title,
            "url": "https://arxiv.org/abs/" + aid,
            "date": pub,
            "authors": authors_str,
            "abstract": c["zh"],
            "tags": c["tags"],
            "highlight": c["highlight"],
            "links": c["links"],
        })

    # highlight first, then by date desc
    papers.sort(key=lambda p: (not p["highlight"], p["date"]), reverse=False)
    data = {"papers": papers, "news": NEWS, "note": NOTE}
    out = os.path.join(BASE, 'data', '2026-11-09.json')
    with open(out, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print('wrote', out, 'papers', len(papers), 'news', len(NEWS))


if __name__ == '__main__':
    main()
