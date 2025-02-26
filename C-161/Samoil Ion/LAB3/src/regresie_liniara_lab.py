#!/usr/bin/env python
# coding: utf-8

# # Laborator 3. Regresia Liniara in Python utilizand Pandas si Scikit-Learn
# #

# ## Cuprins
# 
# 1. Selectarea setului de date.
# 2. Importarea bibliotecilor si setului de date.
# 3. Studierea setului de date.
# 4. Setarea problemei si Pregatirea setului de date pentru antrenare.<br>
#    a. Divizare in set de date pentru antrenare si set de date pentru testare. <br>
#    b. Utilizarea k-folds cross validation pentru testare.
# 5. Initializarea modelului de regresie liniara si aplicarea acestuia pe datele noastre.
# 6. Concluzii.

# ## Selectarea setului de date
# 1. Setul de date il veti alege de sine stator din urmatoarele repositorii (important este ca setul de date sa fie compatibil cu rezolvarea problemei de regresie liniara):<br>
#    a. https://archive.ics.uci.edu/ml/datasets.php?format=&task=&att=&area=&numAtt=&numIns=&type=&sort=taskDown&view=table <br>
#    b. https://www.kaggle.com/rtatman/datasets-for-regression-analysis <br>
#    c. https://data.world/datasets/regression <br>
#    d. https://www.kdnuggets.com/datasets/index.html
# 2. Creati un fisier de tip jupyter notebook in aceeasi mapa.
# 
# ### Cei care nu-si gasesc nimic potrivit pot folosi acelasi dataset folosit anterior (lab. 2).
# ### Exemplul va fi pe datasetul utilizat in lab. 2.
#    

# ## Importarea bibliotecilor si setului de date

# In[2]:


import pandas as pd
import numpy as np
from scipy import stats
from sklearn import preprocessing
from sklearn.model_selection import KFold
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# incarcam fisierul .csv intr-un dataframe |
# daca la voi nu e csv, incercati mai intai sa-l transformati in csv
# 

# In[3]:


data = pd.read_csv('imbd_superhero.csv', header=None)
# nu avem setate numele de coloane | 
# in lab 2 le-am setat direct in fctia read_csv utilizand atributul names='' | 
# insa le putem seta si dupa incarcarea fisierului
data.columns = ['An', 'Titlu','Organizatia', 'IMBD', 'AltRating', 'DataX', 'UnkColumn', 'PretMediulaBilet', 'NrDeSpectatori', 'TopPentruAncutare']


# ## Studierea setului de date prin manipularea acestuia

# Hai sa vizualizam datele, grafic

# In[4]:


data.plot(figsize=(18, 5)) # figsize este marimea dreptunghiului unde este afisat graficul (latimea si lungimea)


# Daca privim mai atent datele putem observa niste lucruri stranii in grafic
# 1. Se pare ca anumite date lipsesc (acolo unde este sters graficul)
# 2. Se pare ca avem anomalii in date. (anumite date nu coincid cu valorile de min sau max care le poate lua o coloana)

# Pentru a verifica daca nu lipsesc unele valori in setul nostru de date folosim fctia isnull()
# 

# In[5]:


data.isnull().values.any()


# Functia a returnat <b> True </b> ceea ce inseamna ca trebuie sa analiam si sa vedem ce date lipsesc

# In[6]:


# afisarea tabelara primelor date din tabel
data.head()


# Observam anumite date cu valoarea <b>NaN</b> (Not a Number) in coloanele <i>UnkColumn</i> si <i>NrDeSpectatori</i> care, probabil, ne pun piedica. <br>
# O metoda ar fi sa scapam de aceste valori prin a sterge randurile unde ele apar.<br>
# Putem aceste randuri utilizand functia dropna(). <br>
# Functia dropna() sterge randul unde cel putin un element lipseste sau este diferit de valoare coloanei.<br>
# Functia folosita pe coloane, ex. dropna(axis='column'), sterge coloana unde cel putin un element lispste.

# In[4]:


## data fara randuri cu erori
data_fara_lipse = data.dropna()
data_fara_lipse.tail()


# ## Anomalii in anumite coloane (Muntii din grafic)

# Anomaliile din date sunt niste valori extreme ale unor caracteristici. <br>
# Valorile extreme, de obicei, apar in rezulatatul unui experiment eronat, sau chiar poate fi o valoare corecta.
# Cel mai bine este sa le stergem.

# In[5]:


data.hist(figsize = (15,20))


# ## Definirea problemei de regresie
# 

# Presupunem ca vrem la anul sa mergem la un film de la DC si vrem sa cunoastem care va fi pretul mediu la bilet.

# Drept urmare, din datele noastre putem lua ca si o caracteristica din observarile anterioare pentru variabila independenta x - coloana "An", iar drept raspuns variabila dependenta y - coloana "PretMediulaBilet"

# In[6]:


dc = data[data['Organizatia'] == 'DC']
XY = dc[['An', 'PretMediulaBilet']]
# caracteristica an - variabila independenta x
X = dc['An']
# raspunsul Pretul mediu la bilet - variabila dependenda y
Y = dc['PretMediulaBilet']
X.count() == Y.count() ## daca true, avem acelasi numar de observatii
print("Numarul de observatii este ")
n = X.count()
print(n) ## 20 de observatii
print("Incepand cu ")
print(X.iloc[0]) ## iloc - indexul
print("pana in")
print(X.iloc[n-1])


# functia .iloc [] este bazata in principal pe pozitia intreaga (de la 0 la lungimea-1 a coloanei).
# 

# In[7]:


XY.plot.scatter(y = 'PretMediulaBilet', x = 'An')


# In[8]:


XY.corr()
# XY.descibe()


# In[9]:



model = LinearRegression()


# In[10]:


scores = []
kfold = KFold(n_splits = 3, shuffle = True, random_state=42)


# In[12]:


X = dc.as_matrix(['An'])
Y = dc.as_matrix(['PretMediulaBilet'])


# In[212]:





# In[15]:


pretMediuBilet_model = model.fit(X,Y)
pretMediuBilet_model.predict(np.array([[1978]]))


# In[20]:


Y[:4]


# In[221]:


for i, (train, test) in enumerate(kfold.split(X, Y)):
     scores.append(model.score(X, Y))
print(scores)

