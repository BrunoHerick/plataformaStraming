#coding: utf-8
import pandas as pd
import matplotlib.pyplot as grafico

arquivo = pd.read_csv("/home/brunohelghast/PROFISSIONAL/PYTHON/SCIKIT_LEARN/streaming/MoviesOnStreamingPlatforms.csv")
arquivo = arquivo.iloc[:,1:10]
arquivo["Age"].fillna("none",inplace=True)
#arquivo.dropna(inplace=True)

livre = arquivo[arquivo["Age"] == 18]
print(len(livre))

netflix = arquivo.iloc[:,1:6]
hulu = arquivo.iloc[:,[0,1,2,3,4,6]]
primeVideo = arquivo.iloc[:,[0,1,2,3,4,7]]
disney = arquivo.iloc[:,[0,1,2,3,4,8]]

netflix = netflix[netflix["Netflix"] == 1]
hulu = hulu[hulu["Hulu"] == 1]
primeVideo = primeVideo[primeVideo["Prime Video"] == 1]
disney = disney[disney["Disney"] == 1]

#print(arquivo.corr()["Rotten Tomatoes"].sort_values(ascending=True))

#print(arquivo["Rotten Tomatoes"].describe())

""" print(netflix["Age"].value_counts())
print(hulu["Age"].value_counts())
print(primeVideo["Age"].value_counts())
print(disney["Age"].value_counts()) """

""" grafico.subplot(2,2,1)
grafico.title("Netflix")
grafico.ylabel("Qtd de filmes lancados por decada")
grafico.hist(netflix["Year"], bins=6, range=(1960,2020))
grafico.grid()
grafico.subplot(2,2,2)
grafico.title("Hulu")
grafico.hist(hulu["Year"], bins=6, range=(1960,2020))
grafico.grid()
grafico.subplot(2,2,3)
grafico.title("Disney")
grafico.xlabel("Ano")
grafico.ylabel("Qtd de filmes lancados por decada")
grafico.hist(disney["Year"], bins=6, range=(1960,2020))
grafico.grid()
grafico.subplot(2,2,4)
grafico.title("Prime Video")
grafico.xlabel("Ano")
grafico.hist(primeVideo["Year"], bins=6, range=(1960,2020))
grafico.grid()
grafico.show() """

""" disney2000 = disney[disney["Year"] >= 2005]
print(len(disney2000["Year"])/(len(disney)*1.0))
print(disney2000["Year"].value_counts())
#disneyLivreParaTodos = disney[disney["Age"] == 0]
#print(len(disneyLivreParaTodos)/(len(disney)*1.0))
#print(disney["Age"].value_counts())
#print(len(disney))
grafico.hist(disney["Year"], bins=12, range=(1960,2020))
#grafico.boxplot(disney["Age"])
grafico.title("Disney (ano de lancamento dos filme catalogados)",size=18)
#grafico.title("Disney (classificacao indicativa)")
grafico.grid()
grafico.xlabel("Ano",size=18)
#grafico.ylabel("Faixa etaria")
grafico.ylabel("Quantidade",size=18)
grafico.show() """ 

""" #primeVideo2000 = primeVideo[primeVideo["Year"] >= 2000]
#print(len(primeVideo2000["Year"])/(len(primeVideo)*1.0))
#print(primeVideo2000["Year"].value_counts())
#primeVideoMaiores = primeVideo[primeVideo["Age"] >= 18]
#print(len(primeVideoMaiores)/(len(primeVideo)*1.0))
#print(primeVideo["Age"].value_counts())
#print(len(primeVideo))
grafico.hist(primeVideo["Year"], bins=6, range=(1960,2020))
#grafico.boxplot(primeVideo["Age"])
grafico.title("Prime Video (ano de lancamento dos filme catalogados)")
#grafico.title("Prime Video (classificacao indicativa)")
grafico.grid()
grafico.xlabel("Ano")
#grafico.ylabel("Faixa etaria")
grafico.ylabel("Quantidade")
grafico.show() """

""" hulu2010 = hulu[hulu["Year"] >= 2010]
#print(len(hulu2010["Year"])/(len(hulu)*1.0))
huluAcimaDe13 = hulu[hulu["Age"] >= 13]
print(len(huluAcimaDe13)/(len(hulu)*1.0))
#print(hulu["Age"].value_counts())
grafico.hist(hulu["Year"], bins=12, range=(1960,2020))
#grafico.boxplot(hulu["Age"])
grafico.title("Hulu (ano de lancamento dos filme catalogados)")
#grafico.title("Hulu (classificacao indicativa)")
grafico.grid()
#grafico.xlabel("Ano")
#grafico.ylabel("Faixa etaria")
grafico.ylabel("Quantidade")
grafico.show() """

""" netflixApartirDe2015 = netflix[netflix["Year"] >= 2015]
#print(len(netflixApartirDe2015["Year"])/(len(netflix)*1.0))
netflixAcimaDe13 = netflix[netflix["Age"] >= 13]
#print(len(netflixAcimaDe13)/(len(netflix)*1.0))
#grafico.hist(netflix["Year"], bins=12, range=(1960,2020))
grafico.boxplot(netflix["Age"])
grafico.title("Netflix (ano de lancamento dos filme catalogados)")
grafico.title("Netflix (classificacao indicativa)")
grafico.grid()
#grafico.xlabel("Ano")
grafico.ylabel("Faixa etaria")
#grafico.ylabel("Quantidade")
grafico.show() """

""" 
Content
    The dataset contains data that was scraped, which comprised a comprehensive list of movies available on various streaming platforms
Inspiration
    Which streaming platform(s) can I find this movie on?
    Target age group movies vs the streaming application they can be found on
"""

""" Análises
-Cerca de 53% dos filmes catálogados na plataforma Disney foram lançados depois de 2005.
-Cerca de 51% dos filmes catálogados na Disney são livres para todas as idades.

-A metade dos filmes catálogados na plataforma Prime Video são para maiores de 18 anos.
-Cerca de 74% dos filmes catálogados na plataforma Prime Video foram lançados depois dos anos 2000.

-Cerca de 81% dos filmes catálogados na plataforma Hulu são para maiores de 13 anos
-Cerca de 75% dos filmes catálogados na plataforma Hulu foram lançados depois de 2010.

-Cerca de 73% dos filmes catálogados na Netflix foram lançados depois de 2015.
-Cerca de 75% dos filmes catálogados na Netflix são para maiores de 13 anos
"""

""" def verificarFilme(titulo):
    arquivo = pd.read_csv("SCIKIT_LEARN/netflix/MoviesOnStreamingPlatforms.csv")
    arquivo = arquivo.iloc[:,1:10]
    netflix = arquivo.iloc[:,1:6]
    hulu = arquivo.iloc[:,[0,1,2,3,4,6]]
    primeVideo = arquivo.iloc[:,[0,1,2,3,4,7]]
    disney = arquivo.iloc[:,[0,1,2,3,4,8]]
    netflix = netflix[netflix["Netflix"] == 1]
    hulu = hulu[hulu["Hulu"] == 1]
    primeVideo = primeVideo[primeVideo["Prime Video"] == 1]
    disney = disney[disney["Disney"] == 1]
    plataformas = list()
    if titulo in list(disney["Title"]):
        plataformas.append("Disney")
    if titulo in list(netflix["Title"]):
        plataformas.append("Netflix")
    if titulo in list(hulu["Title"]):
        plataformas.append("Hulu")
    if titulo in list(primeVideo["Title"]):
        plataformas.append("Prime Video")
    if len(plataformas) == 0: 
        return "Nenhuma plataforma tem esse filme"
    else:
        plataformas
print(verificarFilme("Wild Prairie Rose")) """