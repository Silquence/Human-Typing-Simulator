<div align="center">
  <img src="icon.png" width="88" alt="Human Typing Simulator icon">

  <h1>Human Typing Simulator v1.0.0 Founder's Edition</h1>

  <p>
    <img alt="Product of EZhouWorks" src="https://img.shields.io/badge/Product_of-Silquence-black">
    <img alt="Windows Ready" src="https://img.shields.io/badge/Windows-Ready-blue">
    <img alt="MacOS Ready" src="https://img.shields.io/badge/MacOS-Ready-blue">
    <img alt="NaturalType 2.0" src="https://img.shields.io/badge/NaturalType-2.0-yellow">
    <img alt="NaturalType 3.0" src="https://img.shields.io/badge/NaturalType-3.0-green">
  </p>

  <p>
    A precision-driven human typing simulation tool powered by NaturalType.
  </p>
</div>

---

## 版本摘要：

Human Typing Simulator Founder's Edition 是 Human Typing Simulator 的最新正式版本，发行版号为 v1.0.0.

相较于公测（Beta）版本，Founder's Edition 以 NaturalType 3.0 为核心，重构了文本处理、错误生成、精准纠错和运行状态反馈，使自动输入过程更接近真实的人类键入行为。

## Release Note:

Human Typing Simulator Founder's Edition is the latest official release of Human Typing Simulator, published as version v1.0.0.

Compared with the Beta release, Founder's Edition is centered around NaturalType 3.0 and upgrades text processing, error generation, precise correction, and runtime status feedback to deliver a more realistic human-like typing flow.

---

## 核心能力

- **NaturalType 3.0 精准纠错模型**：在单词级输入中生成错字，并通过光标移动、退格和重写完成更自然的修正过程。
- **Hybrid Mode 混合模式**：支持在 NaturalType 3.0 与 NT2.0G 错误生成逻辑之间混合调用，降低长文本输入中的模式重复感。
- **动态错误率与动态速度**：可根据输入进程调整错误频率和节奏变化，模拟疲劳、停顿和速度波动。
- **真实键盘事件模拟**：通过按键级输入处理大小写、标点、空格、换行与特殊字符，使输出行为更接近真实键盘操作。
- **运行状态反馈**：界面提供 Ready、Model、Paused 等状态提示，便于观察当前输入模型与运行状态。
- **鼠标移动暂停机制**：运行中移动鼠标可触发暂停确认；在精准纠错过程中会等待当前单词修正完成后再进入暂停流程。
- **输入安全检查**：在开始输入前检测非 ASCII 字符，并在发现异常字符时提示用户确认与重置。
- **现代化 GUI**：基于 customtkinter 构建的风格化界面，提供错误率、输入速度、动态选项和文本输入区域。

## Key Features

- **NaturalType 3.0 precise correction model**: Generates typos at word level, then performs cursor movement, deletion, and rewriting for a more natural correction process.
- **Hybrid Mode**: Supports mixed invocation between NaturalType 3.0 and NT2.0G error generation to reduce repetitive patterns in long-form typing.
- **Dynamic error rate and dynamic speed**: Adjusts typo frequency and rhythm variation during typing to simulate fatigue, pauses, and speed fluctuation.
- **Real keyboard-event simulation**: Handles uppercase letters, punctuation, spaces, line breaks, and special characters through key-level input behavior.
- **Runtime status feedback**: Displays Ready, Model, and Paused states in the interface for clearer visibility into the active typing process.
- **Mouse-movement pause control**: Moving the mouse during active typing can trigger pause confirmation; during precise correction, the simulator waits until the current word is completed.
- **Input validation**: Detects non-ASCII characters before typing starts and prompts the user when unexpected characters are found.
- **Modern GUI**: Built with customtkinter, featuring a modern interface with controls for error rate, typing speed, dynamic options, and text input.

---

## 最新版本相较 Beta 的主要更新

| 模块 | Beta | Founder's Edition               |
| --- | --- |---------------------------------|
| 默认模型 | NaturalType 2.0 风格的随机错字与退格修正 | NaturalType 3.0 单词级精准纠错以及混合调用模式 |
| 混合模式 | 不支持 | 支持 Hybrid Mode，可混合调用 NT2.0G     |
| 文本处理 | 按字符读取缓存文本 | 按换行、空白、单词和标点分词处理                |
| 错误率范围 | 最高 20 | 最高 100                          |
| 状态显示 | 基础界面控制 | Ready / Model / Paused 状态指示     |
| 输入校验 | 无显式字符校验 | 启动前检测非 ASCII 字符                 |

## Major Updates from Beta

| Module | Beta | Founder's Edition                                                  |
| --- | --- |--------------------------------------------------------------------|
| Default model | NaturalType 2.0-style random typo and backspace correction | NaturalType 3.0 word-level precise correction and hybrid mode      |
| Hybrid mode | Not supported | Supported, with mixed NT2.0G invocation                            |
| Text processing | Character-by-character cache reading | Tokenized handling of line breaks, spaces, words, and punctuation  |
| Error-rate range | Up to 20 | Up to 100                                                          |
| Status display | Basic interface controls | Ready / Model / Paused status indicators                           |
| Input validation | No explicit character validation | Non-ASCII character detection before typing                        |

---

## 简介

Human Typing Simulator 是一款基于 Python 的自动化输入工具。它通过智能错误生成、动态速率调整和人性化节奏控制，使自动输入的文本看起来完全由真人敲出，而非机械的复制粘贴。

最新版本将核心输入逻辑升级为 NaturalType 3.0：程序会以单词为单位模拟输入、制造错误、移动光标并精准修正，使打字过程呈现更完整的“输入-出错-回看-修正”链路。对于长文本演示、自动化测试、教学录制和需要自然输入节奏的场景，Founder's Edition 提供了比 Beta 版本更稳定、更细腻的模拟体验。

## Introduction:

Human Typing Simulator is a Python-based automated input tool. Through intelligent error generation, dynamic rate adjustment, and human-like rhythm control, it makes automatically typed text appear as if it were typed by a real person, rather than mechanically copied and pasted.

The latest version upgrades the core typing logic to NaturalType 3.0. It simulates typing at word level, creates typos, moves the cursor, and corrects mistakes precisely, producing a more complete "type - mistype - review - correct" flow. For long-form demonstrations, automation testing, teaching recordings, and scenarios that require natural typing rhythm, Founder's Edition offers a more stable and detailed simulation experience than the Beta release.

---

## 版本文件

- `HumanTypingSimulatorFE.py`：最新稳定版本，Human Typing Simulator Founder's Edition。
- `HumanTypingSimulatorBeta.py`：公测版本，保留 NaturalType 2.0 阶段的基础输入逻辑。
- `ToBeImplemented.md`：后续功能规划。

## Version Files

- `HumanTypingSimulatorFE.py`: Latest version, Human Typing Simulator Founder's Edition.
- `HumanTypingSimulatorBeta.py`: Beta release, preserving the NaturalType 2.0-stage baseline typing logic.
- `ToBeImplemented.md`: Planned future features.
