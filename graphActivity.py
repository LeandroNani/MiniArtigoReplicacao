import pandas as pd
from ineq.indexes import gini

# Carregar os dados do arquivo activity.data
df = pd.read_csv("activity.data")

# Converter a coluna "Frequency" para uma lista
frequency_list = df["Frequency"].tolist()

# Calcular o Coeficiente de Gini
gini_coefficient = gini(frequency_list)

# Criar a tabela
data = {"Repositório": ["VSCode"], "Coeficiente de Gini (Contribuições)": [gini_coefficient]}
tabela = pd.DataFrame(data)

# Imprimir a tabela
print(tabela.to_string(index=False))