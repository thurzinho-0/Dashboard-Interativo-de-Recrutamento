# Dashboard Interativo de Recrutamento

Este projeto combina **Python** e **Power BI** para criar um dashboard interativo que analisa todo o processo de recrutamento e contratação para o setor de transporte/logística. Ele é ideal para **RH, gestores de equipe ou analistas de dados**, fornecendo insights estratégicos sobre candidatos, aprovações e performance do processo seletivo.

---

## Sobre o Projeto

O objetivo é simular um cenário real de recrutamento e demonstrar como dados podem ser transformados em decisões inteligentes:

- **Analisar candidatos por departamento e fonte de recrutamento**
- **Medir performance do processo seletivo** (triagem, entrevista e contratação)
- **Identificar gargalos e oportunidades de melhoria**
- **Visualizar KPIs e estatísticas de forma clara e interativa**

A primeira parte do projeto usa Python para gerar **100 candidatos fictícios**, com datas de inscrição, triagem, entrevista, decisão e status de contratação. Os dados são exportados para CSV e importados no Power BI para visualização.

---

## Tecnologias Utilizadas

- **Python 3.x**: geração e tratamento de dados (`pandas`, `numpy`)  
- **Matplotlib e Seaborn**: gráficos exploratórios e verificação de dados  
- **Power BI Desktop**: visualizações interativas e dashboards  
- **CSV**: integração entre Python e Power BI  

---

## Estrutura do Dashboard

O dashboard contém:

- **Donut Chart Duplo**: aprovação por departamento e status de contratação (Sim/Não)
- **Gráficos de Barras**: taxa de contratação por departamento e por fonte
- **Cartões KPI**:  
  - % de aprovação na triagem  
  - % de aprovação na entrevista  
  - % de contratação final  
- **Slicers Interativos**: filtro por departamento ou fonte de recrutamento
- **Rótulos e tooltips** para fácil interpretação dos dados  

O layout foi pensado para **visualização rápida**, permitindo que qualquer gestor de RH identifique rapidamente performance e gargalos.

---

## Como Reproduzir

1. **Gerar dados fictícios com Python**:  
   Execute o script `recrutamento_transporte.py` para criar o CSV.

2. **Importar CSV no Power BI**:  
   - `Obter dados → CSV → recrutamento_transporte.csv`  
   - Carregue os dados e configure os gráficos.

3. **Configurar visualizações**:  
   - Crie donut charts, gráficos de barras e KPIs  
   - Adicione Slicers para interatividade

---

## Resultado Esperado

O dashboard fornece **informações estratégicas de forma clara**:

- Qual departamento tem maior aprovação ou taxa de contratação
- Quais fontes de recrutamento são mais eficientes
- Tempo médio gasto em cada etapa do processo seletivo

É uma demonstração prática de como **dados podem guiar decisões de RH**, transformando informações em insights acionáveis.

---

## Imagem do Dashboard
<img width="1070" height="538" alt="image" src="https://github.com/user-attachments/assets/5d159c04-8642-4f9f-9940-6cb9f2444fe9" />


---

## Licença
MIT License – livre para estudo, portfólio e projetos pessoais.****
