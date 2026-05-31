# Dashboard Interativo de Recrutamento – Transporte & RH

🚀 Este projeto foi desenvolvido para demonstrar como transformar dados brutos em **insights acionáveis** usando Python e Power BI.  
Ele simula um cenário real de recrutamento para uma empresa de transporte/logística e constrói um dashboard interativo que pode ser utilizado por equipes de RH e gestores para **monitorar a eficiência do processo seletivo**.

<img width="1055" height="623" alt="image" src="https://github.com/user-attachments/assets/8e3e13ff-0e6b-4d8c-8250-a2385a6001af" />


## 🔍 O Que Este Projeto Entrega

📊 **Dashboard interativo no Power BI** com:
- Visualizações modernas e informativas (donut charts, barras, KPIs, slicers)  
- Análises estratégicas por **Departamento** e **Fonte de Recrutamento**  
- Indicadores chave (KPIs):
  - % de aprovação na triagem  
  - % de aprovação na entrevista  
  - % de contratação final  
  - Tempo médio gasto em cada etapa

🧠 O dashboard permite filtros dinâmicos com *Slicers*, possibilitando:
- Filtrar por departamento
- Filtrar por fonte de recrutamento
- Navegar entre aprovações e contratações  
- Obter insights instantâneos sobre performance de recrutamento

---

## 🧱 Tecnologias Utilizadas

| Ferramenta | Uso |
|------------|-----|
| **Python** | Geração de dados, cálculo de KPIs e exportação para CSV |
| **Pandas & Numpy** | Manipulação e processamento de dados |
| **Matplotlib & Seaborn** | Visualizações preliminares em Python |
| **Power BI Desktop** | Construção do dashboard interativo |
| **CSV** | Integração entre Python e Power BI |

---

## 🛠️ Estrutura do Projeto

1️⃣ **Código Python**  
- Gera 100 candidatos fictícios  
- Cria colunas de datas, aprovação e contratação  
- Calcula métricas médias e exporta `recrutamento_transporte.csv`  

2️⃣ **Arquivo CSV**  
- Importado no Power BI para modelagem e visualização  

3️⃣ **Dashboard no Power BI**  
- Visualmente atrativo e funcional  
- Interatividade com filtros e rótulos que facilitam a tomada de decisão

---

## 🧪 Como Reproduzir

### 🔹 1. Executar o script Python
Execute o código Python para gerar os dados fictícios:

```bash
python gerar_recrutamento.py
