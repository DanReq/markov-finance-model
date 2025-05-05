from fpdf import FPDF
import matplotlib.pyplot as plt
import seaborn as sns

# Clase personalizada para el PDF
class PDF(FPDF):
    def footer(self):
        self.set_y(-15)
        self.set_font('Times', 'I', 8)
        self.cell(0, 10, f'Página {self.page_no()}', 0, 0, 'C')

    def add_title(self, title):
        self.set_font('Times', 'B', 14)
        self.cell(0, 10, title, ln=True)
        self.ln(2)

    def add_paragraph(self, text):
        self.set_font('Times', '', 12)
        self.multi_cell(0, 6, text)
        self.ln(2)

# Crear PDF
pdf = PDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()

# Portada formal
pdf.set_font('Times', 'B', 24)
pdf.set_text_color(0, 0, 0)
pdf.multi_cell(0, 10, 'Análisis de Indicadores Financieros para la Predicción de Estados con Cadenas de Markov', align='C')
pdf.ln(20)

pdf.set_font('Times', '', 14)
pdf.cell(0, 10, 'Autor: Daniel Reséndiz Quiroz', ln=True, align='C')
pdf.cell(0, 10, 'Fecha: 08 de enero de 2025', ln=True, align='C')
pdf.ln(30)

pdf.add_page()

# Introducción
pdf.add_title('Introducción')
pdf.add_paragraph(
    "La estabilidad financiera es un tema de vital importancia para empresas, inversionistas y organismos reguladores. "
    "Este proyecto busca analizar el riesgo de quiebra de empresas mediante el uso de cadenas de Markov, un modelo "
    "matemático que permite estudiar procesos estocásticos donde el estado futuro depende únicamente del actual."
)

# Objetivo
pdf.add_title('Objetivo')
pdf.add_paragraph(
    "Predecir la estabilidad financiera de las empresas a través de modelos estocásticos. Se pretende:\n"
    "- Identificar patrones en indicadores clave como ROA o Current Ratio.\n"
    "- Clasificar empresas en estados financieros probables.\n"
    "- Modelar probabilidades de transición y simular escenarios futuros."
)

# Metodología
pdf.add_title('Metodología Utilizada')
pdf.add_paragraph(
    "1. Obtención y limpieza de datos financieros clave.\n"
    "2. Construcción de una matriz de transición.\n"
    "3. Aplicación de cadenas de Markov para simular cambios de estado.\n"
    "4. Interpretación de resultados y visualización."
)

# Preprocesamiento de Datos
pdf.add_title('Preprocesamiento de Datos')
pdf.add_paragraph(
    "Se cargaron los datos desde 'data1.csv' obtenido de Kaggle (Company Bankruptcy Prediction). Se seleccionaron columnas como:\n"
    "- ROA(C) before interest and depreciation before interest\n"
    "- Current Ratio\n"
    "- Quick Ratio\n"
    "Las columnas fueron renombradas y se eliminaron valores nulos."
)

# Clasificación
pdf.add_title('Clasificación de Empresas')
pdf.add_paragraph(
    "Las empresas se clasificaron en:\n"
    "- Estable: Percentil > 75%\n"
    "- Riesgo: Percentil entre 25% y 75%\n"
    "- Quiebra: Percentil < 25%"
)

# Matriz de Transición
pdf.add_title('Matriz de Transición')
pdf.add_paragraph("La matriz presenta las probabilidades de transición entre los estados financieros:")
pdf.set_font('Courier', '', 11)
pdf.multi_cell(0, 6,
    "            Estable   Quiebra   Riesgo\n"
    "Estable       0.20      0.63      0.17\n"
    "Quiebra       0.08      0.71      0.21\n"
    "Riesgo        0.06      0.66      0.28\n")
pdf.ln(2)

# Interpretación
pdf.add_title('Interpretación de Resultados')
pdf.add_paragraph(
    "- Empresas en 'Estable' tienen mayor probabilidad de caer en 'Quiebra'.\n"
    "- Las empresas en 'Quiebra' tienen alta probabilidad de permanecer ahí.\n"
    "- Riesgo es un estado inestable con alta probabilidad de caer en Quiebra."
)

# Visualización
pdf.add_title('Visualización de la Matriz de Transición')
fig, ax = plt.subplots()
sns.heatmap(
    [[0.2, 0.63, 0.17], [0.08, 0.71, 0.21], [0.06, 0.66, 0.28]],
    annot=True, cmap="coolwarm", xticklabels=['Estable', 'Quiebra', 'Riesgo'],
    yticklabels=['Estable', 'Quiebra', 'Riesgo'], ax=ax
)
plt.title("Matriz de Transición")
plt.savefig("matriz_transicion.png")
plt.close()
pdf.image("matriz_transicion.png", x=15, w=180)
pdf.ln(2)

# Simulación
pdf.add_title('Simulación de la Cadena de Markov')
pdf.add_paragraph(
    "Se simularon 10 pasos iniciando desde 'Estable'. Se observó que las empresas tienden a caer en 'Quiebra' conforme avanzan los pasos, confirmando la alta inestabilidad del estado 'Estable' en el modelo."
)

# Conclusiones
pdf.add_title('Conclusiones')
pdf.add_paragraph(
    "Este análisis demuestra cómo las cadenas de Markov permiten modelar y predecir transiciones financieras. La alta persistencia del estado 'Quiebra' sugiere la necesidad de monitoreo constante y estrategias de prevención más sólidas."
)

# Referencias
pdf.add_title('Referencias')
pdf.set_font('Times', '', 11)
pdf.multi_cell(0, 6,
    "1. Kaggle Dataset: 'Company Bankruptcy Prediction'\n"
    "2. Pindyck, R. S., & Rubinfeld, D. L. (2009). Microeconomía. Pearson.\n"
    "3. Anton, H., & Rorres, C. (2005). Álgebra lineal con aplicaciones. Limusa Wiley.\n"
    "4. Grossman, S. (1988). Aplicaciones de álgebra lineal. Grupo Editorial Iberoamérica.\n"
    "5. https://github.com/pamelacab/Simulador-Cadenas-de-Markov")
pdf.ln(2)

# Guardar PDF
pdf.output("data_analysis_markov.pdf")

print("PDF generado correctamente como 'data_analysis_markov.pdf'")

