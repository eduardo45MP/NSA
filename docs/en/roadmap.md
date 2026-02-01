# 🛣 Roadmap — NSA (Network Security Assistant)

This roadmap defines the planned evolution of the **NSA – Network Security Assistant** in an **incremental, responsible, and learning-driven** manner.

The goal is not to rush into flashy features, but to build a **reliable, understandable, and technically solid system**, where each phase delivers real and measurable value.

---

## Guiding principles

- **Defensive security first**
- **Knowledge before exploitation**
- **Incremental evolution**
- **Technical clarity over unnecessary complexity**
- **Ethical and responsible use**

---

## Phase 1 — Foundation (current state)

🎯 **Objective:** establish a minimal, functional, and reliable core.

Main deliveries:
- Basic scanning of available Wi-Fi networks
- Collection of essential information:
  - SSID
  - BSSID
  - channel
  - encryption type
- Initial structure of independent scripts
- Local execution via CLI
- Initial project documentation

Expected outcome:
- Ability to **identify and list networks**
- Solid foundation for future analysis
- A usable project for study and controlled testing

---

## Phase 2 — Structured security analysis

🎯 **Objective:** transform raw data into technical diagnosis.

Planned deliveries:
- Security classification per network:
  - open
  - WEP
  - WPA / WPA2
  - WPA3
- Identification of weak or obsolete configurations
- Basic risk evaluation rules
- Normalisation of collected data
- Clear separation between data collection and analysis

Expected outcome:
- Understandable security diagnosis
- First real layer of **defensive intelligence**

---

## Phase 3 — Reports and recommendations

🎯 **Objective:** make results actionable and educational.

Planned deliveries:
- Generation of structured reports (PDF or similar)
- Executive summary per analysed network
- Practical mitigation recommendations
- Accessible language without losing technical accuracy
- Ability to export results

Expected outcome:
- Users understand **what is wrong and why**
- Clear bridge between technical analysis and corrective action

---

## Phase 4 — Modularisation and internal architecture

🎯 **Objective:** prepare the project for sustainable growth.

Planned deliveries:
- Modular organisation of components:
  - scanner
  - analyser
  - report generator
  - profiles
- Clear interfaces between modules
- Reduced coupling between scripts
- Foundation for automated testing
- Standardised inputs and outputs

Expected outcome:
- More readable, testable, and extensible code
- Easier addition of new analysis capabilities

---

## Phase 5 — Profiles, history, and comparisons

🎯 **Objective:** add temporal context to security analysis.

Planned deliveries:
- Storage of analysed network profiles
- Scan history
- Security comparison over time
- Detection of relevant configuration changes
- Simple local storage layer (e.g. JSON or SQLite)

Expected outcome:
- Evolutionary view of network security
- NSA usable as a continuous monitoring tool

---

## Phase 6 — Advanced CLI interface

🎯 **Objective:** improve usability without sacrificing simplicity.

Planned deliveries:
- Unified CLI for all modules
- Clear flags and parameters
- Modes such as:
  - scan
  - analyse
  - report
- Basic visual feedback (colours, status)
- More explicit and helpful error messages

Expected outcome:
- Smoother and more professional user experience
- Reduced friction for recurring users

---

## Phase 7 — Controlled expansions (optional)

🎯 **Objective:** explore new capabilities without breaking core principles.

Possible explorations:
- Passive traffic analysis (no injection)
- Support for additional Wi-Fi standards and scenarios
- Comparative reports across environments
- Integration with other defensive tools

⚠️ This phase depends on technical, ethical, and documentation maturity.

---

## Explicitly out of scope

The NSA **does not aim to**:
- automate attacks or active exploitation
- perform password cracking
- replace professional security audits
- operate without explicit authorisation

These limits are **intentional** and part of the project’s identity.

---

## Final vision

NSA evolves as a **living project of applied learning**, where:
- each phase delivers real value,
- complexity grows consciously,
- ethics evolve alongside technical capability.

> **Security is not brute force.  
It is understanding, visibility, and informed decision-making.**