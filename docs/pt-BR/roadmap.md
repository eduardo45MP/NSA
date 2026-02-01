# 🛣 Roadmap — NSA (Network Security Assistant)

Este roadmap define a evolução planejada do **NSA – Network Security Assistant** de forma **incremental, responsável e orientada ao aprendizado prático**.

O objetivo não é correr para funcionalidades chamativas, mas construir um sistema **confiável, compreensível e tecnicamente sólido**, onde cada etapa entrega valor real e mensurável.

---

## Princípios que guiam o roadmap

- **Segurança defensiva em primeiro lugar**
- **Conhecimento antes de exploração**
- **Evolução incremental**
- **Clareza técnica acima de complexidade desnecessária**
- **Uso ético e responsável**

---

## Fase 1 — Fundação (estado atual)

🎯 **Objetivo:** estabelecer um núcleo funcional mínimo e confiável.

Entregas principais:
- Varredura básica de redes Wi-Fi disponíveis
- Coleta de informações essenciais:
  - SSID
  - BSSID
  - canal
  - tipo de criptografia
- Estrutura inicial de scripts independentes
- Execução local via CLI
- Documentação inicial do projeto

Resultado esperado:
- Capacidade de **identificar e listar redes**
- Base sólida para análises futuras
- Projeto utilizável para estudo e testes controlados

---

## Fase 2 — Análise de segurança estruturada

🎯 **Objetivo:** transformar dados brutos em diagnóstico técnico.

Entregas planejadas:
- Classificação de segurança por rede:
  - aberta
  - WEP
  - WPA / WPA2
  - WPA3
- Identificação de configurações fracas ou obsoletas
- Regras básicas de avaliação de risco
- Normalização dos dados coletados
- Separação clara entre coleta e análise

Resultado esperado:
- Diagnóstico compreensível do nível de segurança
- Primeira camada real de **inteligência defensiva**

---

## Fase 3 — Relatórios e recomendações

🎯 **Objetivo:** tornar os resultados acionáveis e educativos.

Entregas planejadas:
- Geração de relatórios estruturados (PDF ou similar)
- Sumário executivo por rede analisada
- Recomendações práticas de mitigação
- Linguagem acessível sem perder precisão técnica
- Possibilidade de exportação de resultados

Resultado esperado:
- Usuário entende **o que está errado e por quê**
- Ponte clara entre análise técnica e ação corretiva

---

## Fase 4 — Modularização e arquitetura interna

🎯 **Objetivo:** preparar o projeto para crescimento sustentável.

Entregas planejadas:
- Organização modular dos componentes:
  - scanner
  - analisador
  - gerador de relatórios
  - perfis
- Interfaces claras entre módulos
- Redução de acoplamento entre scripts
- Base para testes automatizados
- Padronização de entradas e saídas

Resultado esperado:
- Código mais legível, testável e extensível
- Facilidade para adicionar novas análises

---

## Fase 5 — Perfis, histórico e comparações

🎯 **Objetivo:** adicionar contexto temporal às análises.

Entregas planejadas:
- Armazenamento de perfis de redes analisadas
- Histórico de varreduras
- Comparação de segurança ao longo do tempo
- Detecção de mudanças relevantes em configurações
- Base local simples (ex.: JSON ou SQLite)

Resultado esperado:
- Visão evolutiva da segurança da rede
- Uso do NSA como ferramenta de acompanhamento contínuo

---

## Fase 6 — Interface CLI avançada

🎯 **Objetivo:** melhorar experiência sem perder simplicidade.

Entregas planejadas:
- CLI unificada para execução de módulos
- Flags e parâmetros claros
- Modos:
  - scan
  - analyze
  - report
- Feedback visual básico (cores, status)
- Mensagens de erro mais explicativas

Resultado esperado:
- Uso mais fluido e profissional
- Menor fricção para usuários recorrentes

---

## Fase 7 — Expansões controladas (opcional)

🎯 **Objetivo:** explorar novas capacidades sem romper princípios.

Possíveis explorações:
- Análise passiva de tráfego (sem injeção)
- Suporte a novos padrões e cenários Wi-Fi
- Relatórios comparativos entre ambientes
- Integração com outras ferramentas defensivas

⚠️ Esta fase depende de maturidade técnica, ética e documental.

---

## Fora de escopo (decisão explícita)

O NSA **não pretende**:
- automatizar ataques ou exploração ativa
- realizar quebra de senhas
- substituir auditorias profissionais formais
- operar sem autorização explícita

Esses limites são **deliberados** e fazem parte da identidade do projeto.

---

## Visão final

O NSA evolui como um **projeto vivo de aprendizado aplicado**, onde:
- cada fase entrega valor real,
- a complexidade cresce de forma consciente,
- a ética acompanha o avanço técnico.

> **Segurança não é força bruta.  
É entendimento, visibilidade e decisão informada.**