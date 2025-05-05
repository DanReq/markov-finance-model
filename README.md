# 📊 Predicción de Rentabilidad con Cadenas de Markov

Este proyecto aplica **cadenas de Markov** para modelar y predecir la rentabilidad futura de una empresa a partir de sus características financieras históricas. Utiliza técnicas estadísticas para estimar la probabilidad de transición entre distintos estados financieros y proporciona visualizaciones que apoyan el análisis.

## 📌 Objetivo

El objetivo es desarrollar un sistema que permita:
- Clasificar empresas en distintos estados financieros (por ejemplo: solvente, en riesgo, en quiebra)
- Calcular la matriz de transición entre estos estados
- Estimar la probabilidad de que una empresa se mantenga o cambie de estado en el futuro
- Aplicar este modelo a datos reales financieros

## 🧠 Fundamento Teórico

Este análisis se basa en la teoría de **cadenas de Markov discretas**, un modelo probabilístico que permite estudiar sistemas que cambian de estado de forma secuencial y aleatoria. La evolución depende únicamente del estado actual, lo que se conoce como la **propiedad de Markov**.

## 🛠️ Tecnologías Utilizadas

- Python 3.13
- Pandas, NumPy
- Matplotlib, Seaborn
- fpdf (para generar PDF)
- Git

## 📈 Dataset

El dataset utilizado proviene de [Kaggle - Company Bankruptcy Prediction](https://www.kaggle.com/datasets/). Incluye variables financieras como:
- ROA (Return on Assets)
- Total Debt / Total Net Worth
- Operating Profit Rate
- Interest Coverage Ratio
- Liquidez y capital contable

## 📘 Generación de Informe

El informe final del análisis es generado automáticamente como un archivo PDF que resume:
- Preprocesamiento de datos
- Matriz de transición
- Análisis de estados
- Conclusiones gráficas y teóricas

## ✍️ Autor

Este proyecto fue desarrollado por **Daniel Reséndiz Quiroz** como parte de un trabajo para certificación de análisis de datos y usando matemáticas aplicadas.


