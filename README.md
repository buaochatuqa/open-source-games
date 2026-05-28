<div align="center">

# Polymarket Trading Bots

**High-performance automated trading systems for Polymarket prediction markets.**

[🇬🇧 English](README.md) · [🇨🇳 中文](README.zh.md) · [🇷🇺 Русский](README.ru.md)

<img width="1776" height="576" alt="Polymarket Trading Bots" src="https://github.com/user-attachments/assets/eb7920c1-03ab-47f0-8da2-daa07891c227" />

<br>

Built by **[ZSC DAO](https://github.com/zsc-dao)** — a collection of production-grade bots that turn prediction markets into systematic, risk-managed trading strategies.

[![GitHub](https://img.shields.io/badge/GitHub-ZSC--Dao-181717?logo=github&logoColor=white)](https://github.com/zsc-dao)
[![Telegram](https://img.shields.io/badge/Telegram-@leshuuuk-26A5E4?logo=telegram&logoColor=white)](https://t.me/leshuuuk)

</div>

---

## Table of Contents

- [Overview](#overview)
- [Crypto Bot — 5/15 min BTC Trading](#crypto-bot--515-min-btc-trading)
- [Weather Bot — Polymarket Weather Arbitrage](#weather-bot--polymarket-weather-arbitrage)
- [Sports Bot — FIFA World Cup & Tournaments](#sports-bot--fifa-world-cup--tournaments)
- [Contact](#contact)
- [Disclaimer](#disclaimer)

---

## Overview

This repository hosts a family of automated trading bots designed for **Polymarket** and related prediction markets. Each bot treats markets as a systematic trading problem — combining signal aggregation, simulation-first testing, observability, and disciplined risk management.

| Bot | Market | Strategy | Highlight |
| --- | --- | --- | --- |
| **Crypto Bot** | BTC short-term prediction | Multi-signal aggregation + risk-managed execution | Production-grade infra with Grafana observability |
| **Weather Bot** | Weather event markets | Convex payoff on low-priced "No" positions | ~$13.8K profit · 431% ROI |
| **Sports Bot** | FIFA World Cup & esports | Early-entry volatility trading | Six-figure profits across tournaments |

---

## Crypto Bot — 5/15 min BTC Trading

<p align="center">
  <img width="338" height="360" alt="Crypto Bot dashboard" src="https://github.com/user-attachments/assets/52998028-92c3-4a64-83da-3d5a736dca22" />
  <img width="338" height="360" alt="Crypto Bot performance" src="https://github.com/user-attachments/assets/ce0185c2-78c0-422f-b130-dcee469eb7b5" />
</p>

A systematic short-term BTC trading bot that approaches prediction markets as a quantitative problem — not speculation.

### How it works

The bot continuously ingests market and contextual data, normalizes signals through a unified pipeline, combines multiple detection models into a decision engine, and executes trades through a broker adapter under strict risk management rules.

### Core principles

- **Signal aggregation** — multiple weak signals combined into a robust decision rather than relying on a single "magic indicator"
- **Simulation-first testing** — every strategy is backtested and validated before live deployment
- **Observability** — full Grafana dashboards for live monitoring of P&L, latency, and signal health
- **Disciplined execution** — predefined position sizing, take-profit, and stop-loss logic

### Design goal

Build scalable, testable, production-grade trading infrastructure where **risk control and system reliability matter as much as prediction accuracy**.

---

## Weather Bot — Polymarket Weather Arbitrage

<p align="center">
  <video width="338" height="360" src="https://github.com/user-attachments/assets/7b76663f-ac4c-4c92-9eea-be8b73005092"></video>
  <img width="338" height="360" alt="Weather Bot performance" src="https://github.com/user-attachments/assets/fb6ffcd4-28be-4de0-bcbf-eb55b5e21178" />
</p>

A convex-payoff strategy that buys large volumes of extremely low-priced "No" positions (~1¢ odds) across weather-event markets.

### The thesis

Accept many small, capped losses in exchange for rare, outsized payouts. A single win can offset hundreds of losing positions — turning an unfavorable hit rate into a profitable system.

### Performance

| Metric | Value |
| --- | --- |
| Win rate | ~27% |
| Profit | ~$13.8K |
| ROI | **431%** |

### Why it works

- **Asymmetric risk/reward** — bounded downside per trade, unbounded relative upside
- **Disciplined bankroll management** — position sizing keeps the strategy solvent through long losing streaks
- **High trade volume** — law-of-large-numbers smoothing of the convex payoff distribution

> In short: **small consistent losses + rare outsized wins = long-term profitability.**

---

## Sports Bot — FIFA World Cup & Tournaments

<p align="center">
  <video src="https://github.com/user-attachments/assets/b024d9cd-7cbf-4b1b-9618-ff45e4f9bdbd"></video>
</p>

A volatility-trading strategy for major tournaments such as the **FIFA World Cup** and large esports events.

### The thesis

Don't predict the winner — **trade the price movement**. Enter low-cost positions across many teams early in a tournament, then profit as odds shift with public sentiment, match results, and liquidity flows.

### How it works

1. **Early entry** — open small positions across all teams while probabilities are still low and cheap
2. **Volatility capture** — hold through hype cycles, narrative shifts, and result-driven repricing
3. **Selective exit** — take profit when sentiment momentum lifts odds well above entry

### Why it works

This behaves more like **volatility trading** than traditional sports betting. By exploiting price movement and liquidity inefficiencies rather than match outcomes, the strategy has previously produced **six-figure profits** across both sports and esports markets.

> **Small early entries across many outcomes + selective profit-taking during hype cycles = long-term profitability.**

---

## Contact

Interested in custom bots, partnerships, or access to more profitable strategies?

- **GitHub:** [ZSC DAO](https://github.com/zsc-dao)
- **Telegram:** [@leshuuuk](https://t.me/leshuuuk)

---

## Disclaimer

These bots are provided for **educational and research purposes**. Trading and prediction markets carry significant financial risk and may not be legal in your jurisdiction. Past performance does not guarantee future results. Use at your own risk and ensure compliance with all applicable laws and platform terms of service.
