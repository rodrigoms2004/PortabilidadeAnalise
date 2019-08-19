
# coding: utf-8

# # Portabilidade e carteirização de clientes

# In[1]:


# bibliotecas úteis
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt


# ## Carteira Massivo

# In[2]:


carteira = pd.read_csv('./carteira_massivo.csv', ';', low_memory=False)


# In[3]:


print('Carteira possui', carteira.shape[0], 'registros')


# In[4]:


# Colunas disponíveis na carteira
list(carteira.columns)


# In[5]:


# Cria dataframe auxiliar para visualizar parte dos dados
carteira_auxiliar = carteira[['DOCUMENTO', 'SEGMENTO_VALOR']].copy()

print('Carteira possui', carteira_auxiliar.shape[0], 'registros')


# In[6]:


# preenche os registros sem segmentação com NA, para entrar na contagem abaixo
carteira_auxiliar = carteira_auxiliar.fillna('NA')

# Mostra a quantidade de segmentações disponiveis
list(carteira_auxiliar.drop_duplicates(subset='SEGMENTO_VALOR', keep='first')['SEGMENTO_VALOR'])


# In[7]:


# quantidade de clientes por segmentação
carteira_auxiliar.groupby(['SEGMENTO_VALOR']).count()


# ## Carteira sem massivo

# In[8]:


carteiraTOP = pd.read_csv('./Carteira_sem_Massivo.csv', ';', low_memory=False)


# In[9]:


print('Carteira sem massivo possui', carteiraTOP.shape[0], 'registros')


# In[10]:


list(carteiraTOP.columns)


# In[11]:


carteiraTOP_auxiliar = carteiraTOP[['DOCUMENTO', 'SEGMENTO_VALOR']].copy()


# In[12]:


# preenche os registros sem segmentação com NA, para entrar na contagem abaixo
carteiraTOP_auxiliar = carteiraTOP_auxiliar.fillna('NA')

# Mostra a quantidade de segmentações disponiveis
list(carteiraTOP_auxiliar.drop_duplicates(subset='SEGMENTO_VALOR', keep='first')['SEGMENTO_VALOR'])


# In[13]:


# quantidade de clientes por segmentação
carteiraTOP_auxiliar.groupby(['SEGMENTO_VALOR']).count()


# In[14]:


# REMOVE OS ZEROS A ESQUERDA DO DOCUMENTO (CNPJ)
carteiraTOP_auxiliar['DOCUMENTO'] = carteiraTOP_auxiliar['DOCUMENTO'].str.replace(r'^[0]{1,}', '', 1)


# ## SUPERCARTEIRA

# In[15]:


print("Carteira TOP sem massivo:", carteiraTOP_auxiliar.shape)
print("Carteira com massivo:    ", carteira_auxiliar.shape)
print("TOTAL:", carteiraTOP_auxiliar.shape[0] + carteira_auxiliar.shape[0])


# In[16]:


# Funde as duas carteiras
superCarteira = carteira_auxiliar.append(carteiraTOP_auxiliar)
superCarteira.shape


# In[17]:


# remoção de duplicados
superCarteira = superCarteira.drop_duplicates(subset='DOCUMENTO', keep='first')


# In[18]:


# superCarteira[superCarteira['DOCUMENTO'] == 'COLOQUE O CNPJ AQUI']


# ## COTAÇÕES

# In[19]:


# cotações outubro de 2018
outubro2018 = pd.read_excel('./2018/EVOL_COTAÇOES_TOP_31.10.2018.xlsx', sheet_name=0,                           converters={'CPF/CNPJ': str}                          )[['COD_GRUPO', 'GRUPO_ECONOMICO', 'CPF/CNPJ']]


# cotações novembro de 2018
novembro2018 = pd.read_excel('./2018/EVOL_COTAÇOES_TOP_30.11.2018.xlsx', sheet_name=0,                           converters={'CPF/CNPJ': str}                          )[['COD_GRUPO', 'GRUPO_ECONOMICO', 'CPF/CNPJ']]


# cotações dezembro de 2018
dezembro2018 = pd.read_excel('./2018/EVOL_COTAÇOES_TOP_17.12.2018.xlsx', sheet_name=0,                           converters={'CPF/CNPJ': str}                          )[['COD_GRUPO', 'GRUPO_ECONOMICO', 'CPF/CNPJ']]


# In[20]:


# cotações janeiro de 2019
janeiro2019 = pd.read_excel('./2019/EVOL_COTAÇOES_TOP_29.01.2019.xlsx', sheet_name=0,                           converters={'CPF/CNPJ': str}                          )[['COD_GRUPO', 'GRUPO_ECONOMICO', 'CPF/CNPJ']]


# cotações fevereiro de 2019
fevereiro2019 = pd.read_excel('./2019/EVOL_COTAÇOES_TOP_28.02.2019.xlsx', sheet_name=0,                           converters={'CPF/CNPJ': str}                          )[['COD_GRUPO', 'GRUPO_ECONOMICO', 'CPF/CNPJ']]

# cotações março de 2019
marco2019 = pd.read_excel('./2019/EVOL_COTAÇOES_TOP_29.03.2019.xlsx', sheet_name=0,                           converters={'CPF/CNPJ': str}                          )[['COD_GRUPO', 'GRUPO_ECONOMICO', 'CPF/CNPJ']]

    
# cotações abril de 2019
abril2019 = pd.read_excel('./2019/EVOL_COTAÇOES_TOP_26.04.2019.xlsx', sheet_name=0,                             converters={'CPF/CNPJ': str}                          )[['COD_GRUPO', 'GRUPO_ECONOMICO', 'CPF/CNPJ']]
    
# cotações maio de 2019
maio2019 = pd.read_excel('./2019/EVOL_COTAÇOES_TOP_31.05.2019.xlsx', sheet_name=0,                             converters={'CPF/CNPJ': str}                         )[['COD_GRUPO', 'GRUPO_ECONOMICO', 'CPF/CNPJ']]
    
# cotações junho de 2019
junho2019 = pd.read_excel('./2019/EVOL_COTAÇOES_TOP_ 28.06.2019.xlsx', sheet_name=0,                             converters={'CPF/CNPJ': str}                          )[['COD_CLI', 'Cliente', 'CPF/CNPJ']]
    
# cotações julho de 2019
julho2019 = pd.read_excel('./2019/EVOL_COTAÇOES_TOP_31.07.2019.xlsx', sheet_name=0,                             converters={'CPF/CNPJ': str}                          )[['COD_CLI', 'Cliente', 'CPF/CNPJ']]

    


# In[21]:


# padronizando as colunas de CPF/CNPJ para DOCUMENTO

# 2018
outubro2018 = outubro2018.rename(columns={"CPF/CNPJ": "DOCUMENTO"})
novembro2018 = novembro2018.rename(columns={"CPF/CNPJ": "DOCUMENTO"})
dezembro2018 = dezembro2018.rename(columns={"CPF/CNPJ": "DOCUMENTO"})

# 2019
janeiro2019 = janeiro2019.rename(columns={"CPF/CNPJ": "DOCUMENTO"})
fevereiro2019 = fevereiro2019.rename(columns={"CPF/CNPJ": "DOCUMENTO"})
marco2019 = marco2019.rename(columns={"CPF/CNPJ": "DOCUMENTO"})
abril2019 = abril2019.rename(columns={"CPF/CNPJ": "DOCUMENTO"})
maio2019 = maio2019.rename(columns={"CPF/CNPJ": "DOCUMENTO"})

junho2019 = junho2019.rename(columns={"CPF/CNPJ": "DOCUMENTO", "COD_CLI": "COD_GRUPO", "Cliente": "GRUPO_ECONOMICO"})
julho2019 = julho2019.rename(columns={"CPF/CNPJ": "DOCUMENTO", "COD_CLI": "COD_GRUPO", "Cliente": "GRUPO_ECONOMICO"})
    


# # COTAÇÕES 2018/2019

# In[22]:


# faz o join entre as carteiras e os meses

# 2018
carteiraOutubro2018 = pd.merge(outubro2018, superCarteira, how='left', on='DOCUMENTO')
carteiraNovembro2018 = pd.merge(novembro2018, superCarteira, how='left', on='DOCUMENTO')
carteiraDezembro2018 = pd.merge(dezembro2018, superCarteira, how='left', on='DOCUMENTO')

# 2019
carteiraJaneiro2019 = pd.merge(janeiro2019, superCarteira, how='left', on='DOCUMENTO')
carteiraFevereiro2019 = pd.merge(fevereiro2019, superCarteira, how='left', on='DOCUMENTO')
carteiraMarco2019 = pd.merge(marco2019, superCarteira, how='left', on='DOCUMENTO')
carteiraAbril2019 = pd.merge(abril2019, superCarteira, how='left', on='DOCUMENTO')
carteiraMaio2019 = pd.merge(maio2019, superCarteira, how='left', on='DOCUMENTO')
carteiraJunho2019 = pd.merge(junho2019, superCarteira, how='left', on='DOCUMENTO')
carteiraJulho2019 = pd.merge(julho2019, superCarteira, how='left', on='DOCUMENTO')


# In[23]:


# preenche os registros sem segmentação com NA, para entrar na contagem abaixo

# 2018
carteiraOutubro2018 = carteiraOutubro2018.fillna('NA')
carteiraNovembro2018 = carteiraNovembro2018.fillna('NA')
carteiraDezembro2018 = carteiraDezembro2018.fillna('NA')

# 2019
carteiraJaneiro2019 = carteiraJaneiro2019.fillna('NA')
carteiraFevereiro2019 = carteiraFevereiro2019.fillna('NA')
carteiraMarco2019 = carteiraMarco2019.fillna('NA')
carteiraAbril2019 = carteiraAbril2019.fillna('NA')
carteiraMaio2019 = carteiraMaio2019.fillna('NA')
carteiraJunho2019 = carteiraJunho2019.fillna('NA')
carteiraJulho2019 = carteiraJulho2019.fillna('NA')

carteiraDezembro2018.shape


# In[24]:


# carteira_auxiliar[carteira_auxiliar['DOCUMENTO'] == 'COLOQUE O CNPJ AQUI']


# ## Remoção dos clientes duplicados

# In[25]:


# 2018
carteiraOutubro2018 = carteiraOutubro2018.drop_duplicates(subset='DOCUMENTO', keep='first')
carteiraNovembro2018 = carteiraNovembro2018.drop_duplicates(subset='DOCUMENTO', keep='first')
carteiraDezembro2018 = carteiraDezembro2018.drop_duplicates(subset='DOCUMENTO', keep='first')


# 2019
carteiraJaneiro2019 = carteiraJaneiro2019.drop_duplicates(subset='DOCUMENTO', keep='first')
carteiraFevereiro2019 = carteiraFevereiro2019.drop_duplicates(subset='DOCUMENTO', keep='first')
carteiraMarco2019 = carteiraMarco2019.drop_duplicates(subset='DOCUMENTO', keep='first')
carteiraAbril2019 = carteiraAbril2019.drop_duplicates(subset='DOCUMENTO', keep='first')
carteiraMaio2019 = carteiraMaio2019.drop_duplicates(subset='DOCUMENTO', keep='first')
carteiraJunho2019 = carteiraJunho2019.drop_duplicates(subset='DOCUMENTO', keep='first')
carteiraJulho2019 = carteiraJulho2019.drop_duplicates(subset='DOCUMENTO', keep='first')

carteiraDezembro2018.shape


# In[26]:


# carteiraJunho2019[carteiraJunho2019['SEGMENTO_VALOR'] == 'NA']


# # SEGMENTAÇÃO 2018

# In[27]:


# quantidade de clientes por segmentação em outubro 2018
segOut2018 = carteiraOutubro2018[['SEGMENTO_VALOR', 'DOCUMENTO']].groupby(['SEGMENTO_VALOR']).count() #.plot(kind='bar')
# segOut2018.plot(kind='bar', title='Outubro 2018')
segOut2018 = segOut2018.rename(columns={"DOCUMENTO": "OUT2018"})
segOut2018
# data = data[['DOCUMENTO']]
# data = (100. * data / data.sum()).round(2).plot(kind='bar', title='Outubro 2018')


# In[28]:


# quantidade de clientes por segmentação em novembro 2018
segNov2018 = carteiraNovembro2018[['SEGMENTO_VALOR', 'DOCUMENTO']].groupby(['SEGMENTO_VALOR']).count()
segNov2018 = segNov2018.rename(columns={"DOCUMENTO": "NOV2018"})
segNov2018


# In[29]:


# quantidade de clientes por segmentação em dezembro 2018
segDez2018 = carteiraDezembro2018[['SEGMENTO_VALOR', 'DOCUMENTO']].groupby(['SEGMENTO_VALOR']).count()
segDez2018 = segDez2018.rename(columns={"DOCUMENTO": "DEZ2018"})
segDez2018


# ## Consolidado 2018

# In[30]:


seg2018 = pd.concat([segOut2018, segNov2018, segDez2018], axis=1).reindex(segOut2018.index).fillna(0)
# seg2018 = (100. * seg2018 / seg2018.sum()).round(2)
seg2018


# # SEGMENTAÇÃO 2019

# ## SEGMENTAÇÃO DE CLIENTES JANEIRO 2019

# In[31]:


# quantidade de clientes por segmentação em Janeiro 2019
segJan2019 = carteiraJaneiro2019[['SEGMENTO_VALOR', 'DOCUMENTO']].groupby(['SEGMENTO_VALOR']).count()
segJan2019 = segJan2019.rename(columns={"DOCUMENTO": "JAN2019"})
segJan2019


# ## SEGMENTAÇÃO DE CLIENTES FEVEREIRO 2019

# In[32]:


# quantidade de clientes por segmentação em Fevereiro 2019
segFev2019 = carteiraFevereiro2019[['SEGMENTO_VALOR', 'DOCUMENTO']].groupby(['SEGMENTO_VALOR']).count()
segFev2019 = segFev2019.rename(columns={"DOCUMENTO": "FEV2019"})
segFev2019


# ## SEGMENTAÇÃO DE CLIENTES MARÇO 2019

# In[33]:


# quantidade de clientes por segmentação em Março 2019
segMar2019 = carteiraMarco2019[['SEGMENTO_VALOR', 'DOCUMENTO']].groupby(['SEGMENTO_VALOR']).count()
segMar2019 = segMar2019.rename(columns={"DOCUMENTO": "MAR2018"})
segMar2019


# ## SEGMENTAÇÃO DE CLIENTES ABRIL 2019

# In[34]:


segAbr2019 = carteiraAbril2019[['SEGMENTO_VALOR', 'DOCUMENTO']].groupby(['SEGMENTO_VALOR']).count()
segAbr2019 = segAbr2019.rename(columns={"DOCUMENTO": "ABR2019"})
segAbr2019


# ## SEGMENTAÇÃO DE CLIENTES MAIO 2019

# In[35]:


segMai2019 = carteiraMaio2019[['SEGMENTO_VALOR', 'DOCUMENTO']].groupby(['SEGMENTO_VALOR']).count()
segMai2019 = segMai2019.rename(columns={"DOCUMENTO": "MAI2019"})
segMai2019


# ## SEGMENTAÇÃO DE CLIENTES JUNHO 2019
# 

# In[36]:


segJun2019 = carteiraJunho2019[['SEGMENTO_VALOR', 'DOCUMENTO']].groupby(['SEGMENTO_VALOR']).count()
segJun2019 = segJun2019.rename(columns={"DOCUMENTO": "JUN2019"})
segJun2019


# ## SEGMENTAÇÃO DE CLIENTES JULHO 2019
# 

# In[37]:


segJul2019 = carteiraJulho2019[['SEGMENTO_VALOR', 'DOCUMENTO']].groupby(['SEGMENTO_VALOR']).count()
segJul2019 = segJul2019.rename(columns={"DOCUMENTO": "JUL2019"})
segJul2019


# ## Consolidado 2019

# In[38]:


seg2019 = pd.concat([segJan2019,                      segFev2019,                      segMar2019,                      segAbr2019,                      segMai2019,                      segJun2019,                      segJul2019                     ], axis=1).reindex(segJan2019.index).fillna(0)

# seg2019 = (100. * seg2019 / seg2019.sum()).round(2)
seg2019


# # GERANDO OS RESULTADOS

# In[39]:


seg2018 = (seg2018 / seg2018.sum())
seg2018


# In[40]:


seg2019 = (seg2019 / seg2019.sum())
seg2019


# In[41]:


with pd.ExcelWriter('resultPortabilidade.xlsx') as writer:
    seg2018.to_excel(writer, sheet_name='2018')
    seg2019.to_excel(writer, sheet_name='2019')
    


# # Empresas não encontradas

# ## 2018

# In[42]:


naOut2018 = carteiraOutubro2018[carteiraOutubro2018['SEGMENTO_VALOR'] == 'NA']
# naOut2018


# In[43]:


naNov2018 = carteiraNovembro2018[carteiraNovembro2018['SEGMENTO_VALOR'] == 'NA']
# naNov2018


# In[44]:


naDez2018 = carteiraDezembro2018[carteiraDezembro2018['SEGMENTO_VALOR'] == 'NA']
# naDez2018


# In[45]:


df2018 = [naOut2018, naNov2018, naDez2018]


# In[46]:


na2018 = pd.concat(df2018, axis=0, join='outer', ignore_index=False, keys=None,
                          levels=None, names=None, verify_integrity=False, copy=True)


# In[47]:


na2018 = na2018.drop_duplicates(subset='DOCUMENTO', keep='first')
print('Em 2018 foram ', na2018.shape[0], ' empresas não encontradas')


# ## 2019

# In[48]:


naJan2019 = carteiraJaneiro2019[carteiraJaneiro2019['SEGMENTO_VALOR'] == 'NA']
# naJan2019


# In[49]:


naMai2019 = carteiraMaio2019[carteiraMaio2019['SEGMENTO_VALOR'] == 'NA']
# naMai2019


# In[50]:


naJun2019 = carteiraJunho2019[carteiraJunho2019['SEGMENTO_VALOR'] == 'NA']
# naJun2019


# In[51]:


naJul2019 = carteiraJulho2019[carteiraJulho2019['SEGMENTO_VALOR'] == 'NA']
# naJul2019


# In[52]:


df2019 = [naJan2019, naMai2019, naJun2019, naJul2019]


# In[53]:


na2019 = pd.concat(df2019, axis=0, join='outer', ignore_index=False, keys=None,
                          levels=None, names=None, verify_integrity=False, copy=True)


# In[54]:


na2019 = na2019.drop_duplicates(subset='DOCUMENTO', keep='first')
print('Em 2019 foram ', na2019.shape[0], ' empresas não encontradas')


# ## Consolidado não encontradas

# In[55]:


dfGeral = [pd.concat(df2018), pd.concat(df2019)]


# In[56]:


naGeral = pd.concat(dfGeral, axis=0, join='outer', ignore_index=False, keys=None,
                          levels=None, names=None, verify_integrity=False, copy=True)
# naGeral


# In[57]:


naGeral = naGeral.drop_duplicates(subset='DOCUMENTO', keep='first')
print('Geral de ', naGeral.shape[0], ' empresas não encontradas')


# In[58]:


with pd.ExcelWriter('semSegmentacao.xlsx') as writer:
    naGeral.to_excel(writer, sheet_name='clientes')

    

