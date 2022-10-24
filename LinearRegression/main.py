import math
from sklearn import linear_model
from sklearn.metrics import r2_score
import pandas as pd
import numpy as np

#nomeando e selecionando colunas 
columns = ['carat', 'depth', 'price']
df = pd.read_csv("csv/diamonds.csv", header = 0, usecols= columns, index_col=False)

#dividindo a amostra

amostra = df.sample(frac=1)
treino = amostra[:math.floor(len(amostra)*0.80)]
teste = amostra[:math.floor(len(amostra)*0.20)]

#modelando a reta
reta = linear_model.LinearRegression()
reta.fit(treino[["carat", "depth"]], treino[["price"]])

#r2 do modelo
predict = reta.predict(teste[["carat", "depth"]]);
r2= r2_score(predict, teste["price"])

print(r2)type -p curl >/dev/null || sudo apt install curl -y
curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg \
&& sudo chmod go+r /usr/share/keyrings/githubcli-archive-keyring.gpg \
&& echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null \
&& sudo apt update \
&& sudo apt install gh -y