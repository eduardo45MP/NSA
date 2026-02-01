# 🛰 NSA — Network Security Assistant

O **NSA (Network Security Assistant)** é um projeto de **estudo, análise e diagnóstico de segurança em redes Wi-Fi**, desenvolvido para identificar fragilidades, avaliar configurações e **transformar dados técnicos em informação acionável**.

O foco do projeto é **segurança defensiva, aprendizado prático e conscientização**, permitindo que usuários entendam o real nível de proteção de suas redes sem fio.

---

## 🎯 Objetivo do Projeto

O NSA existe para responder a uma pergunta simples e crítica:

> **“Minha rede Wi-Fi é realmente segura?”**

Para isso, o projeto fornece ferramentas que:
- detectam redes Wi-Fi disponíveis,
- analisam protocolos e mecanismos de segurança,
- identificam riscos e más configurações,
- geram relatórios claros com recomendações.

Tudo isso com **ênfase educacional e responsabilidade ética**.

---

## 🔒 Funcionalidades

- 📡 **Varredura de redes Wi-Fi**
  - Detecção de redes disponíveis e seus parâmetros técnicos.
  - Script: `scan_wifi_networks.py`

- 🔍 **Análise de segurança**
  - Avaliação de criptografia, protocolos e exposições comuns.
  - Script: `sec_analysis.py`

- 📑 **Relatórios de segurança**
  - Geração de relatórios estruturados com diagnóstico e recomendações.
  - Script: `sec_report.py`

- 📂 **Gestão de perfis Wi-Fi**
  - Salvamento e reutilização de configurações analisadas.
  - Script: `wifi_profile.py`

---

## 🧱 Estrutura do Projeto

Estado atual do repositório:

```

NSA/
├── docs/               # Documentação do projeto
├── README.md           # Documentação principal (EN)
└── README.pt.md        # Documentação em português

````

A estrutura foi mantida simples para facilitar **estudo, leitura e evolução incremental**.

---

## ⚙️ Tecnologias

- **Python 3.10+**
- Bibliotecas e ferramentas sugeridas:
  - `scapy` — análise de pacotes e tráfego
  - `socket` / `subprocess` — interação com interfaces de rede
  - `pandas` — organização e análise de dados
  - `reportlab` — geração de relatórios

🖥 **Compatibilidade**
- Linux (algumas funcionalidades exigem privilégios de administrador).

---

## 🚀 Como Utilizar

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/NSA.git
cd NSA
````

2. Crie e ative um ambiente virtual:

```bash
python3 -m venv venv
source venv/bin/activate
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Execute a varredura de redes:

```bash
sudo python scan_wifi_networks.py
```

5. Realize a análise de segurança:

```bash
python sec_analysis.py
```

6. Gere o relatório:

```bash
python sec_report.py
```

---

## 🧠 Abordagem do Projeto

O NSA **não automatiza ataques** nem executa exploração indiscriminada.

Princípios centrais:

* conhecimento antes de exploração;
* diagnóstico antes de ação;
* clareza técnica sem ocultar riscos;
* aprendizado contínuo.

O projeto foi pensado para **ensinar segurança real**, não para facilitar abuso.

---

## ⚠️ Aviso Legal

Este projeto possui finalidade **educacional, experimental e de pesquisa em segurança cibernética**.

⚡ **Utilize apenas em redes próprias ou com autorização explícita.**
O uso indevido é de responsabilidade exclusiva do usuário.

---

## 🛣 Visão de Evolução

O NSA foi concebido para crescer de forma incremental, podendo evoluir para:

* análises mais profundas de protocolos Wi-Fi,
* relatórios comparativos e históricos,
* modularização avançada dos analisadores,
* interfaces CLI mais ricas ou dashboards futuros.

A evolução do projeto prioriza:
**clareza, controle e responsabilidade**.

---

## 📜 Licença

MIT — livre para uso, estudo e modificação.

---

✨ Criado por **Eduardo45MP.dev**
Projeto aberto de estudos em **segurança de redes Wi-Fi**