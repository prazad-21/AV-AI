# 🤖 AI-Driven System Health Monitor (Python + Gemini API)

A lightweight Linux-based monitoring tool that captures real-time hardware telemetry and uses Generative AI to provide actionable system optimization and troubleshooting advice.

## 🌟 Overview
Most system monitors only show graphs and numbers. This project goes a step further by feeding raw hardware data (CPU, RAM, Disk, Temperature) into the **Gemini AI** engine to interpret the system's "health" in plain English.

## 🛠️ Technical Features
- **Data Extraction:** Uses `psutil` to fetch granular system stats (CPU Load per core, Memory paging, Disk I/O).
- **AI Analysis:** Sends periodic hardware snapshots to Gemini API for heuristic performance analysis.
    ** Telegrame ** Message send via Telegrame 
- **Root Cause Detection:** AI identifies resource-hungry processes and suggests optimization steps (e.g., "Thermal throttling detected, consider closing browser tabs").
- **Minimal Overhead:** Designed for low-resource systems (4GB RAM) with optimized polling intervals to prevent CPU spikes.

## 🧰 Tech Stack
- **Python
- **psutil: Cross-platform hardware data retrieval.
- **Google Generative AI:** For intelligent log interpretation.
    **Telegrame : Hardware message send to telegrame
- **OS: Linux (Tested on Parrot Security OS).

## 🚀 Getting Started

### installation guide
gitclone https://github.com/prazad-21/AI-monitor.git
cd AI-monitor
python3 AI-monitor
    
