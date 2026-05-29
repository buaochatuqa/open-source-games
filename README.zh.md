<div align="center">

# Polymarket 量化交易机器人

**面向 Polymarket 预测市场的高性能自动化交易系统。**

[🇬🇧 English](README.md) · [🇨🇳 中文](README.zh.md) · [🇷🇺 Русский](README.ru.md)

<img width="1776" height="576" alt="Polymarket Trading Bots" src="https://github.com/user-attachments/assets/eb7920c1-03ab-47f0-8da2-daa07891c227" />

<br>

由 **[ZSC DAO](https://github.com/zsc-dao)** 出品 —— 一套生产级交易机器人,将预测市场转化为系统化、风控严格的量化策略。

[![GitHub](https://img.shields.io/badge/GitHub-ZSC--Dao-181717?logo=github&logoColor=white)](https://github.com/zsc-dao)
[![Telegram](https://img.shields.io/badge/Telegram-@leshuuuk-26A5E4?logo=telegram&logoColor=white)](https://t.me/leshuuuk)

</div>

---

## 目录

- [项目概览](#项目概览)
- [Crypto Bot —— 5/15 分钟 BTC 短线交易](#crypto-bot--515-分钟-btc-短线交易)
- [Weather Bot —— Polymarket 天气市场套利](#weather-bot--polymarket-天气市场套利)
- [Sports Bot —— 世界杯与大型赛事](#sports-bot--世界杯与大型赛事)
- [联系方式](#联系方式)
- [免责声明](#免责声明)

---

## 项目概览

本仓库汇集了一系列面向 **Polymarket** 及相关预测市场的自动化交易机器人。每个机器人都将市场视为一个系统化的量化交易问题 —— 通过多信号聚合、仿真优先测试、可观测性建设以及严格的风控来实现稳定收益。

| 机器人 | 市场 | 策略 | 亮点 |
| --- | --- | --- | --- |
| **Crypto Bot** | BTC 短期预测 | 多信号聚合 + 风控执行 | 生产级架构,Grafana 全链路可观测 |
| **Weather Bot** | 天气事件市场 | 低价 "No" 仓位凸性收益 | 利润 ~$13.8K · ROI 431% |
| **Sports Bot** | 世界杯与电竞赛事 | 早期建仓 + 波动率交易 | 累计六位数美元利润 |

---

## Crypto Bot —— 5/15 分钟 BTC 短线交易

<p align="center">
  <img width="338" height="360" alt="Crypto Bot 看板" src="https://github.com/user-attachments/assets/52998028-92c3-4a64-83da-3d5a736dca22" />
  <img width="338" height="360" alt="Crypto Bot 业绩" src="https://github.com/user-attachments/assets/ce0185c2-78c0-422f-b130-dcee469eb7b5" />
</p>

一套系统化的 BTC 短线交易机器人,将预测市场当作量化问题来处理,而不是单纯的投机。

### 工作原理

机器人持续接入行情和上下文数据,通过统一管线进行信号归一化,再由决策引擎融合多个检测模型,最终通过 Broker 适配器在严格的风控规则下执行交易。

### 核心理念

- **多信号聚合** —— 将多个弱信号融合为稳健决策,而不是依赖单一的"圣杯指标"
- **仿真优先** —— 所有策略上线前必须经过严格的回测与仿真验证
- **可观测性** —— 完整的 Grafana 监控盘,实时跟踪盈亏、延迟与信号健康度
- **纪律执行** —— 预先设定仓位规模、止盈、止损规则,严格执行

### 设计目标

构建可扩展、可测试、可生产部署的交易基础设施 —— **风控与系统可靠性的重要性不低于预测准确率**。

---

## Weather Bot —— Polymarket 天气市场套利

<p align="center">
  <img width="338" height="360" alt="Weather Bot 业绩" src="https://github.com/user-attachments/assets/fb6ffcd4-28be-4de0-bcbf-eb55b5e21178" />
</p>

https://github.com/user-attachments/assets/7b76663f-ac4c-4c92-9eea-be8b73005092

一种凸性收益策略 —— 在天气事件市场上,以极低的价格(约 1¢ 赔率)大量买入 "No" 仓位。

### 策略思路

接受大量小额、上限可控的亏损,以换取偶发的巨额回报。**一次中标即可覆盖数百次失败下注**,从而把不利的胜率转化为整体盈利系统。

### 业绩表现

| 指标 | 数值 |
| --- | --- |
| 胜率 | ~27% |
| 净利润 | ~$13.8K |
| 投资回报率 (ROI) | **431%** |

### 策略有效的原因

- **风险/收益不对称** —— 单笔亏损有界,潜在盈利无上限
- **严谨的资金管理** —— 仓位规模设计可承受长连败
- **大数定律** —— 高交易频次平滑凸性收益分布

> 一句话总结:**持续小亏 + 偶发大赚 = 长期盈利**。

---

## Sports Bot —— 世界杯与大型赛事

https://github.com/user-attachments/assets/b024d9cd-7cbf-4b1b-9618-ff45e4f9bdbd

一套面向 **FIFA 世界杯**及大型电竞赛事的波动率交易策略。

### 策略思路

不去预测谁会夺冠 —— 而是**交易价格波动**。在赛事早期、概率仍然很低、价格便宜时,在多支队伍上建立小仓位,然后在公众情绪、比赛结果和流动性推动赔率变化时获利。

### 工作流程

1. **早期建仓** —— 在概率较低、价格便宜时,在多支队伍上分散建立小仓位
2. **捕捉波动** —— 持有仓位,穿越炒作周期、舆论变化和赛果驱动的价格重定价
3. **择机离场** —— 在情绪推动赔率明显高于建仓价时择机止盈

### 策略有效的原因

这套策略本质上更像 **波动率交易**,而非传统体育博彩。通过捕捉价格波动与流动性失衡(而不是预测比赛结果),策略已在体育与电竞市场累计实现 **六位数美元利润**。

> **多队早期小仓 + 炒作周期精选止盈 = 长期盈利**。

---

## 联系方式

想要定制机器人、合作,或获取更多盈利策略?

- **GitHub:** [ZSC DAO](https://github.com/zsc-dao)
- **Telegram:** [@leshuuuk](https://t.me/leshuuuk)

---

## 免责声明

本项目中的机器人仅用于**学习与研究目的**。预测市场与量化交易存在重大资金风险,且在部分国家或地区可能不合法。历史表现不代表未来收益。使用本项目代表你已自行承担相应风险,并须遵守当地法律法规与平台服务条款。
