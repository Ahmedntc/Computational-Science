import pandas as pd
import numpy as np

# 1. importar os dados de CSV do dataset de seeds:
# https://raw.githubusercontent.com/celsocrivelaro/simple-datasets/main/seeds.csv
# 2. colocar as linhas de cabeçalho: 
  # 1. Área A,
  # 2. Perímetro P,
  # 3. Extensão do núcleo,
  # 4. Largura,
  # 5. Coeficiente de Assimetria
  # 6. Extensão do sulgo do núcleo.
# 3. remover colunas extras no final
# 4. remover as linhas com valores nulos
# 5. Adicionar um campo Compactação cujo o cálculo é C = 4*pi*A/P^2
# 6. Exportar para CSV o valor final

