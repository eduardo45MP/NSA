# 🛰 NSA — Network Security Assistant

**NSA (Network Security Assistant)** is a project focused on **the study, analysis, and diagnosis of Wi-Fi network security**, developed to identify weaknesses, evaluate configurations, and **transform technical data into actionable information**.

The project emphasises **defensive security, practical learning, and awareness**, enabling users to understand the real level of protection of their wireless networks.

---

## 🎯 Project Objective

NSA exists to answer a simple and critical question:

> **“Is my Wi-Fi network really secure?”**

To achieve this, the project provides tools that:
- detect available Wi-Fi networks,
- analyse security protocols and mechanisms,
- identify risks and misconfigurations,
- generate clear reports with recommendations.

All of this is done with a strong focus on **education and ethical responsibility**.

---

## 🔒 Features

- 📡 **Wi-Fi network scanning**
  - Detection of available networks and their technical parameters.
  - Script: `scan_wifi_networks.py`

- 🔍 **Security analysis**
  - Evaluation of encryption, protocols, and common exposures.
  - Script: `sec_analysis.py`

- 📑 **Security reports**
  - Generation of structured reports with diagnosis and recommendations.
  - Script: `sec_report.py`

- 📂 **Wi-Fi profile management**
  - Saving and reusing analysed network configurations.
  - Script: `wifi_profile.py`

---

## 🧱 Project Structure

Current state of the repository:

```

NSA/
├── docs/               # Project documentation
├── README.md           # Main documentation (EN)
└── README.pt.md        # Portuguese documentation

````

The structure is intentionally kept simple to support **study, readability, and incremental evolution**.

---

## ⚙️ Technologies

- **Python 3.10+**
- Suggested libraries and tools:
  - `scapy` — packet and traffic analysis
  - `socket` / `subprocess` — interaction with network interfaces
  - `pandas` — data organisation and analysis
  - `reportlab` — report generation

🖥 **Compatibility**
- Linux (some features require administrator privileges).

---

## 🚀 How to Use

1. Clone the repository:
```bash
git clone https://github.com/your-username/NSA.git
cd NSA
````

2. Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the network scan:

```bash
sudo python scan_wifi_networks.py
```

5. Perform the security analysis:

```bash
python sec_analysis.py
```

6. Generate the report:

```bash
python sec_report.py
```

---

## 🧠 Project Approach

NSA **does not automate attacks** and does not perform indiscriminate exploitation.

Core principles:

* knowledge before exploitation;
* diagnosis before action;
* technical clarity without hiding risks;
* continuous learning.

The project is designed to **teach real-world security**, not to enable abuse.

---

## ⚠️ Legal Disclaimer

This project is intended for **educational, experimental, and cybersecurity research purposes**.

⚡ **Use only on networks you own or have explicit authorisation to analyse.**
Misuse is the sole responsibility of the user.

---

## 🛣 Evolution Vision

NSA is designed to grow incrementally and may evolve towards:

* deeper analysis of Wi-Fi protocols,
* comparative and historical reports,
* advanced modularisation of analysers,
* richer CLI interfaces or future dashboards.

Project evolution prioritises:
**clarity, control, and responsibility**.

---

## 📜 Licence

MIT — free to use, study, and modify.

---

✨ Created by **Eduardo45MP.dev**
Open project for studies in **Wi-Fi network security**