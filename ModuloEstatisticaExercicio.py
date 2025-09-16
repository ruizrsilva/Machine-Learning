import pandas as pd
import matplotlib.pyplot as plt

# Dicionário de faturamento
dict_faturamento = {
    'data_ref': [
        '2023-01-01', 
        '2020-02-01', 
        '2021-03-01', 
        '2022-04-01', 
        '2023-05-01',
        '2023-06-01', 
        '2020-07-01', 
        '2021-08-01', 
        '2022-09-01', 
        '2023-10-01',
        '2022-11-01', 
        '2023-12-01',
        ],
    'valor': [
        400000, 
        890000, 
        760000, 
        430000, 
        920000,
        340000, 
        800000, 
        500000, 
        200000, 
        900000,
        570000, 
        995000,
        ]
}

#criando dicionario
df_faturamento = pd.DataFrame.from_dict(dict_faturamento)
df_faturamento

#Verificando tipo
df_faturamento.info()

#Convertendo e verificando novamente
df_faturamento['data_ref'] =  pd.to_datetime(df_faturamento['data_ref'])
df_faturamento.info()

#Média
Media = df_faturamento["valor"].mean()
print("Resultado:", (Media))

#Grafico de linhas
df_faturamento['data_ref'] = df_faturamento['data_ref'].dt.month
df_faturamento.plot.line(x='data_ref', y='valor')

#Grafico de barras
df_faturamento.plot.bar(x="data_ref", y="valor")
