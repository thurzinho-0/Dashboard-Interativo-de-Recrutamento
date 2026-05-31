import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------
# Configurações iniciais
np.random.seed(42)
sns.set(style="whitegrid")

# -----------------------------
# Definir transportadoras (efictício) e departamentos
fontes_recrutamento = ['LinkedIn','Indeed','Indicação','Site da Empresa']
departamentos = ['Operações', 'TI', 'Logística', 'Financeiro']

num_candidatos = 100
candidatos = []

# -----------------------------
# Gerar candidatos fictícios
for i in range(num_candidatos):
    data_inscricao = datetime.today() - timedelta(days=np.random.randint(1,60))
    data_triagem = data_inscricao + timedelta(days=np.random.randint(1,7))
    data_entrevista = data_triagem + timedelta(days=np.random.randint(1,7))
    data_decisao = data_entrevista + timedelta(days=np.random.randint(1,5))
    
    aprovado_triagem = np.random.choice(['Sim','Não'], p=[0.8,0.2])
    aprovado_entrevista = 'Sim' if aprovado_triagem=='Sim' else 'Não'
    contratado = 'Sim' if aprovado_entrevista=='Sim' and np.random.rand()>0.3 else 'Não'
    
    candidatos.append({
        'CandidatoID': i+1,
        'Fonte': np.random.choice(fontes_recrutamento),
        'Departamento': np.random.choice(departamentos),
        'Data_Inscricao': data_inscricao,
        'Data_Triagem': data_triagem,
        'Data_Entrevista': data_entrevista,
        'Data_Decisao': data_decisao,
        'Aprovado_Triagem': aprovado_triagem,
        'Aprovado_Entrevista': aprovado_entrevista,
        'Contratado': contratado
    })

# -----------------------------
# Criar DataFrame
df = pd.DataFrame(candidatos)

# -----------------------------
# Criar coluna numérica para Contratado
df['Contratado_Num'] = df['Contratado'].map({'Sim':1,'Não':0})

# -----------------------------
# Calcular tempos de cada etapa
df['Data_Inscricao'] = pd.to_datetime(df['Data_Inscricao'])
df['Data_Triagem'] = pd.to_datetime(df['Data_Triagem'])
df['Data_Entrevista'] = pd.to_datetime(df['Data_Entrevista'])
df['Data_Decisao'] = pd.to_datetime(df['Data_Decisao'])

df['Tempo_Triagem'] = (df['Data_Triagem'] - df['Data_Inscricao']).dt.days
df['Tempo_Entrevista'] = (df['Data_Entrevista'] - df['Data_Triagem']).dt.days
df['Tempo_Decisao'] = (df['Data_Decisao'] - df['Data_Entrevista']).dt.days

# -----------------------------
# KPIs Gerais
print("=== KPIs Gerais ===")
print(f"Taxa aprovação triagem: {(df['Aprovado_Triagem']=='Sim').mean()*100:.2f}%")
print(f"Taxa aprovação entrevista: {(df['Aprovado_Entrevista']=='Sim').mean()*100:.2f}%")
print(f"Taxa contratação final: {(df['Contratado']=='Sim').mean()*100:.2f}%")
print(f"Tempo médio Triagem (dias): {df['Tempo_Triagem'].mean():.2f}")
print(f"Tempo médio Entrevista (dias): {df['Tempo_Entrevista'].mean():.2f}")
print(f"Tempo médio Decisão (dias): {df['Tempo_Decisao'].mean():.2f}")

# -----------------------------
# Análise por Fonte
fonte_summary = df.groupby('Fonte')['Contratado_Num'].mean()*100
print("\nContratações por Fonte (%):")
print(fonte_summary)

plt.figure(figsize=(8,5))
sns.barplot(x=fonte_summary.index, y=fonte_summary.values, palette='viridis')
plt.title("Contratações por Fonte - Transporte", fontsize=14,fontweight='bold')
plt.ylabel("Taxa de Contratação (%)")
plt.ylim(0,100)
for i,v in enumerate(fonte_summary.values):
    plt.text(i,v+1,f"{v:.1f}%",ha='center',fontweight='bold')
plt.show()

# -----------------------------
# Análise por Departamento
dept_summary = df.groupby('Departamento')['Contratado_Num'].mean()*100
print("\nContratações por Departamento (%):")
print(dept_summary)

plt.figure(figsize=(8,5))
sns.barplot(x=dept_summary.index, y=dept_summary.values, palette='magma')
plt.title("Contratações por Departamento - Transporte", fontsize=14,fontweight='bold')
plt.ylabel("Taxa de Contratação (%)")
plt.ylim(0,100)
for i,v in enumerate(dept_summary.values):
    plt.text(i,v+1,f"{v:.1f}%",ha='center',fontweight='bold')
plt.show()

# -----------------------------
# Salvar CSV
df.to_csv("recrutamento_transporte.csv",index=False)
print("\nArquivo 'recrutamento_transporte.csv' salvo com sucesso!")

# -----------------------------
# Mostrar exemplos
print("\nExemplo de registros:")
print(df.head())
