# Polymarket Trading Bot

**What is your native language?**
[🇨🇳 中文](README.zh.md) · [🇷🇺 Русский](README.ru.md)

---
<img width="1991" height="793" alt="thumbnail" src="https://github.com/user-attachments/assets/74c48148-0002-496e-9f42-efa4d6408029" />
<br><br>

<p align="center">
  <strong>⭐ Want more profitable trading bots?</strong><br><br>
  Built by <a href="https://github.com/zsc-dao"><strong>ZSC DAO</strong></a> — high-performance automated trading systems for Polymarket.<br><br>
  <a href="https://github.com/zsc-dao"><img alt="GitHub" src="https://img.shields.io/badge/GitHub-gamma--trade--lab-181717?logo=github&logoColor=white"></a>&nbsp;
  <a href="https://t.me/RetroValix"><img alt="Telegram" src="https://img.shields.io/badge/Telegram-@leshuuuk-26A5E4?logo=telegram&logoColor=white"></a>
</p>

---
## How do this bot work on polymarket?

https://github.com/user-attachments/assets/a978bc2e-ed85-4b9b-821c-17f5f33b276b

---

## Proof of work

<img width="1919" height="1035" alt="1" src="https://github.com/user-attachments/assets/27f00a58-db8d-4992-a1ed-1b5ee741bede" />

<img width="1919" height="1032" alt="2" src="https://github.com/user-attachments/assets/447c9671-3f47-4bde-a4be-744af27bdbb1" />

<img width="1916" height="1008" alt="4" src="https://github.com/user-attachments/assets/8b88610b-c54b-4e3d-b7a6-2ccef7b72ca4" />

<img width="1823" height="942" alt="3" src="https://github.com/user-attachments/assets/f7052333-8107-40d8-9703-d1bbd2b77bc7" />

---

## Core Idea

Prediction markets for short-horizon BTC moves are noisy and fast. This project treats them like a **systematic trading problem**: pull in market and context data, normalize it through a single ingestion path, fuse multiple detectors into a decision, then execute through a broker adapter with **hard risk limits** (small size per trade, take profit parameters). The goal is not "one magic signal" but a **testable stack** you can run in simulation, observe in Grafana, and only then point at live capital.

---