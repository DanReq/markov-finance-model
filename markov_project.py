#%%
import pandas as pd
import numpy as np
#bibliotecas para visuzalizar 
import seaborn as sns
import matplotlib.pyplot as plt
from collections import Counter
#%%
#debido a que es un archivo grande de datos, seleccionaré las columnas que necesito
df = pd.read_csv('./data1.csv', usecols=[' ROA(C) before interest and depreciation before interest', ' Current Ratio', ' Quick Ratio'])

#verificar los tipos de datos
#%%
print(df.dtypes) # Son datos numéricos en su mayoría

#Cambio de nombre a más sencillos
#%%
df = df.rename(columns={
    ' ROA(C) before interest and depreciation before interest': 'ROA_C_before_interest',
    ' Current Ratio': 'Current_Ratio',
    ' Quick Ratio': 'Quick_Ratio'
})

# %%
print(df)

# %%
print(df.isnull().values.any()) #Para comprobar si existe algún valor nulo en los datos
#Si no existen valores nulos, entonces no es necesario imputar o eliminar datos

# %%
print(df.describe())
#Escalar los datos para su visualización
df_scaled = df * 10

# %%
# Histograma prueba de un indicador
sns.histplot(df['ROA_C_before_interest'], kde=True)
plt.show()

#Visualización general de distribución datos
#%%
# Gráfico de densidad de kernel
sns.kdeplot(data=df_scaled[['ROA_C_before_interest', 'Current_Ratio', 'Quick_Ratio']])
plt.title("Distribución de Indicadores Financieros (Escalados)")
plt.xlim(0, 10)  # Ajustando los límites del eje x
plt.show()


# Función para clasificar empresas con base en múltiples indicadores y en percentiles
#%%
def clasifica_empresa_percentiles(row):
    if (row['ROA_C_before_interest'] > 0.535563 and
        row['Current_Ratio'] > 0.01626953 and
        row['Quick_Ratio'] > 0.01224911):
        return 'Estable' #Considero el percentil 75%
    elif (0.476527 <= row['ROA_C_before_interest'] <= 0.535563 and 0.007555047 <= row['Current_Ratio'] <= 0.01626953 and 0.004725903 <= row['Quick_Ratio'] <= 0.01224911):
        return 'Riesgo' #Considero los percentiles 25% y 75%
    else:
        return 'Quiebra'

# Aplicar la nueva función al DataFrame
df['estado_empresa'] = df.apply(clasifica_empresa_percentiles, axis=1)

#%%
# Verificar la distribución de categorías
print(df['estado_empresa'].value_counts())


#Aplicare las cadenas de Markov
#%%
# Paso 1: Verificar la columna de estados
print(df['estado_empresa'].unique())  # Solo tiene que haber 'Estable', 'Riesgo', 'Quiebra'

# Paso 2: Crear una matriz de transición
# Crear una tabla de frecuencia para transiciones entre estados consecutivos
#%%
df['estado_anterior'] = df['estado_empresa'].shift(1)
frecuencia = pd.crosstab(df['estado_anterior'], df['estado_empresa'])

# Convertir a probabilidades dividiendo entre la suma por filas
#%%
matriz_transicion = frecuencia.div(frecuencia.sum(axis=1), axis=0).fillna(0)
print("Matriz de transición:")
print(matriz_transicion)

#Visualización matriz utilizando mapa de calor
#%%
sns.heatmap(matriz_transicion, annot=True, fmt=".2f", cmap="coolwarm")
plt.title("Matriz de Transición de Estados")
plt.ylabel("Estado Inicial")
plt.xlabel("Estado Siguiente")
plt.show()

# Paso 3: Simulación con la matriz de transición
#%%
def simulacion_markov(matriz_transicion, estado_inicial, pasos):
    
    # Crear un DataFrame con una columna para los estados y llenarla con el estado inicial
    df = pd.DataFrame({'estado': [estado_inicial] * pasos})

    # Iterar sobre los pasos y actualizar el estado actual utilizando .loc
    for i in range(1, pasos):
        df.loc[i, 'estado'] = np.random.choice(
            matriz_transicion.columns, 
            p=matriz_transicion.loc[df.loc[i-1, 'estado']].values
        )

    return df['estado'].tolist()

# Simular una cadena de Markov por 10 pasos, comenzando en "Estable"
simulacion = simulacion_markov(matriz_transicion, 'Estable', 10)
print("Simulación de la cadena de Markov:")
print(simulacion)

frecuencia_estados = Counter(simulacion)
moda = frecuencia_estados.most_common(1)
print("Utilizando la moda, la mayor probabilidad es:", moda[0][0])
# %%
