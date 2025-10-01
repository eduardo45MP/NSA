# 🛰 NSA – Network Security Assistant

**NSA (Network Security Assistant)** é um sistema inovador desenvolvido para **testar, analisar e aumentar a segurança de redes Wi-Fi**.
O objetivo é fornecer uma ferramenta **versátil, intuitiva e personalizável** que permita ao usuário avaliar a robustez de suas conexões sem fio.

---

## 🔒 Funcionalidades
- 📡 **Varredura de redes Wi-Fi disponíveis** (`scan_wifi_networks.py`).
- 🔍 **Análise de segurança** de redes detectadas (`sec_analysis.py`).
- 📑 **Geração de relatórios detalhados** com recomendações (`sec_report.py`).
- 📂 **Gestão de perfis Wi-Fi** para salvar e reusar configurações (`wifi_profile.py`).

---

## 📂 Estrutura do Projeto
```

NSA/
├── scan_wifi_networks.py   # Scanner de redes Wi-Fi
├── sec_analysis.py         # Módulo de análise de segurança
├── sec_report.py           # Gerador de relatórios
└── wifi_profile.py         # Manipulação de perfis Wi-Fi

````

---

## ⚙️ Tecnologias
- **Python 3.10+**
- Bibliotecas sugeridas:
  - `scapy` (análise de pacotes)
  - `socket` / `subprocess` (interfaces de rede)
  - `pandas` / `reportlab` (relatórios)
- Compatibilidade: Linux (requer privilégios de administrador para certas operações).

---

## 🚀 Como Usar
1. Clone este repositório:
```bash
git clone https://github.com/seu-usuario/NSA.git
cd NSA
````

2. Crie um ambiente virtual e instale dependências:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

3. Execute o scanner:

```bash
sudo python scan_wifi_networks.py
```

4. Rode a análise de segurança:

```bash
python sec_analysis.py
```

5. Gere relatório:

```bash
python sec_report.py
```

---

## ⚠️ Aviso Legal

Este projeto tem finalidade **educacional e de pesquisa em segurança cibernética**.
O uso é de responsabilidade do usuário.
⚡ **Nunca utilize em redes que não sejam suas ou sem permissão explícita.**

---

## 📜 Licença

MIT – livre para uso e modificação.

---

✨ Criado por **Eduardo45MP.dev** como repositório aberto de estudos em **segurança de redes Wi-Fi**.
