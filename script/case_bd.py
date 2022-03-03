import basedosdados as bd
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix
from scipy.stats import norm
import numpy as np
import seaborn as sns
import itertools
import cartopy.crs as ccrs
import cartopy.feature as cf
import cartopy.io.shapereader as shpreader
from cartopy.feature import ShapelyFeature

res_part_mun = bd.read_table(dataset_id='br_tse_eleicoes', 
table_id='resultados_partido_municipio',
billing_project_id="projetoapp-340617")

res_part_mun.info()

df1 = res_part_mun[res_part_mun["turno"] == 2]
df1 = df1[df1["ano"] == 2018]
df1 = df1[df1["cargo"] == "presidente"]
df1 = df1.reset_index()
df1["total_votos"] = df1["votos_nominais"] + df1["votos_nao_nominais"]
df1 = df1.drop(['index', 'votos_nominais', 'votos_nao_nominais', 'tipo_eleicao'], axis=1)
df1

pt = df1[df1['sigla_partido']=='PT']
pt = pt.rename(columns={'total_votos':'votos_PT'})
pt = pt.reset_index()
pt = pt.drop(['index','sigla_partido'], axis=1)
pt

psl = df1[df1['sigla_partido']=='PSL']
psl = psl[['id_municipio','total_votos']]
psl = psl.rename(columns={'total_votos':'votos_PSL'})
psl = psl.reset_index()
psl = psl.drop(['index','id_municipio'],axis=1)
psl

df2 = pd.concat([pt,psl],axis=1)
df2

df2.groupby("sigla_uf").agg({"votos_PT":"sum","votos_PSL":"sum"}).plot(kind="barh",
                                                                       color=["r","b"],
                                                                       figsize = (10,10),
                                                                       edgecolor = "k",
                                                                       linewidth =1
                                                                                )

plt.title("Votos no 2º turno da eleição de 2018 por UF")
plt.legend(loc = "best" , prop = {"size" : 14})
plt.xlabel("Total de Votos")
plt.show()

plt.figure(figsize=(20,20))
plt.subplot(211)
agg = df2.groupby(["sigla_uf"]).agg({"votos_PT":"sum","votos_PSL":"sum"})

agg["votos_PT"].plot.pie(colors=sns.color_palette("Reds_r",10),
                             autopct="%1.0f%%",
                             wedgeprops={"linewidth":10,"edgecolor":"white"})

plt.ylabel("")
my_circ = plt.Circle((0,0),.7,color ="white")
plt.gca().add_artist(my_circ)
plt.title("Proporção de votos no PT por UF")
plt.subplot(212)
agg["votos_PSL"].plot.pie(colors=sns.color_palette("Blues_r",10),
                           autopct="%1.0f%%",
                           wedgeprops={"linewidth":10,"edgecolor":"white"})

plt.ylabel("")
my_circ = plt.Circle((0,0),.7,color ="white")
plt.gca().add_artist(my_circ)
plt.title("Proporção de votos no PSL por UF")
plt.show()
