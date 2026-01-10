# proyectoFinal_Analitica

Autores 
- Gómez Molina Isaac Emiliano
- Zhang Tan Rubi
Grupo 5AM1

## Descripción

Este repositorio contiene el proyecto final de la asignatura Analítica y Visualización de Datos de la Licenciatura en Ciencia de Datos en la Escuela Superior de Cómputo (ESCOM) del Instituto Politécnico Nacional (IPN).

El proyecto analiza la relación entre el consumo de alcohol y el rendimiento académico en estudiantes de secundaria portuguesa.

Se aplicaron técnicas de:
- Preprocesamiento de datos
- Análisis exploratorio (correlación de Pearson, PCA, MDS)
- Visualización interactiva mediante un dashboard en Streamlit

**Objetivo General:**  
Examinar la relación entre el rendimiento académico de los alumnos y el consumo de alcohol a través de variables personales, académicas y sociales, utilizando técnicas de análisis y visualización interactiva de datos.

**Enlaces importantes:**
- [Dashboard Interactivo (Streamlit)](https://proyectofinaljln8g.streamlit.app/)
- [Notebook (Google Colab)](https://colab.research.google.com/drive/1kBp3VRgBAc_0qWOkHq71MGOAWMm34gm3?usp=sharing)
- [Dataset Original (Kaggle)](https://www.kaggle.com/datasets/uciml/student-alcohol-consumption/data)

## Requisitos e Instalación

Se requiere **Python 3.12 o superior**.

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/rubi-zh/proyectoFinal_Analitica.git
   cd proyectoFinal_Analitica
2. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
3. Ejecutar el Notebook:
   ```bash
   # Instalar Jupyter (si no lo tienes)
   pip install jupyter
   # Abrir Jupyter Notebook
   jupyter notebook ProyectoFinal_Analitica.ipynb
4. Ejecutar el dashboard:
   ```bash
   streamlit run app.py
Se abrirá automáticamente en tu navegador. Asegúrate de tener los archivos student_por.csv y student_por_preprocesado.csv en la carpeta raíz. El dashboard utiliza el archivo preprocesado.

## Uso

1. Notebook (ProyectoFinal_Analitica.ipynb)
   
   Ejecuta las celdas en orden para ver:
    - Carga y exploración inicial del dataset
    - Preprocesamiento (creación de variables: alcohol_promedio, tendencia_desempeño, rendimiento)
    - Detección de outliers
    - Correlación de Pearson
    - Reducción de dimensionalidad: PCA y MDS
    - Visualizaciones exploratorias

   El notebook genera y guarda el archivo student_por_preprocesado.csv.

2. Dashboard interactivo (app.py)
   - Filtros: Escuela (GP/MS), Sexo (F/M), Nivel de rendimiento (Bajo/Medio/Alto)
   - Indicadores clave:
      - Promedio de calificación final (G3)
      - Tasa de aprobación (G3 ≥ 10)
      - Consumo promedio de alcohol (1-5)

   - Secciones principales:
      - Rendimiento académico (histogramas, evolución G1-G2-G3, por sexo)
      - Características demográficas (distribución por edad, consumo por edad)
      - Factores de riesgo (alcohol vs rendimiento, entre semana vs fin de semana)
      - Comparación por sexo (Dalc y Walc)

## Estructura del Repositorio
```text
proyectoFinal_Analitica/
├── app.py                          # Dashboard Streamlit
├── requirements.txt                # Dependencias
├── student_por.csv                 # Dataset original (649 registros, 33 variables)
├── student_por_preprocesado.csv    # Dataset procesado con variables derivadas
├── ProyectoFinal_Analitica.ipynb   # Notebook completo con todo el análisis
└── ProyectoFinal.pdf               # Documento formal del proyecto (31 páginas)
