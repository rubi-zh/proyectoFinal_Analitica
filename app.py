import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Proyecto Final", layout="wide")
st.title("Consumo de Alcohol en Estudiantes")

@st.cache_data
def load_data():
    return pd.read_csv("student_por_preprocesado.csv")

df = load_data()

#Filtros
st.sidebar.header("Filtros")

escuela_filtro = st.sidebar.multiselect(
    "Escuela", df['school'].unique(), df['school'].unique()
)

sexo_filtro = st.sidebar.multiselect(
    "Sexo", df['sex'].unique(), df['sex'].unique()
)

rendimiento_opciones = df['rendimiento'].dropna().unique().tolist()
rendimiento_filtro = st.sidebar.multiselect(
    "Nivel de Rendimiento", rendimiento_opciones, rendimiento_opciones
)

df_filtrado = df[
    (df['school'].isin(escuela_filtro)) &
    (df['sex'].isin(sexo_filtro)) &
    (df['rendimiento'].isin(rendimiento_filtro))
]

st.sidebar.markdown(f"**Total de estudiantes:** {len(df_filtrado)}")

if len(df_filtrado) == 0:
    st.warning("No hay datos para los filtros seleccionados.")
    st.stop()

#Indicadores
col1, col2, col3, col4 = st.columns(4)

with col1:
    promedio_g3 = df_filtrado['G3'].mean()
    promedio_total = df['G3'].mean()
    st.metric(
        "Calificación Promedio Final",
        f"{promedio_g3:.1f}",
    )

with col2:
    tasa_aprob = (df_filtrado['G3'] >= 10).sum() / len(df_filtrado) * 100
    st.metric(
        "Tasa de Aprobación",
        f"{tasa_aprob:.1f}%"
    )

with col3:
    st.metric(
        "Ausencias Promedio",
        f"{df_filtrado['absences'].mean():.1f}"
    )

with col4:
    st.metric(
        "Consumo Alcohol Promedio (1–5)",
        f"{df_filtrado['alcohol_promedio'].mean():.2f}"
    )

st.markdown("---")

#Gráficas
st.subheader("Rendimiento Académico")
st.caption("Análisis del desempeño y su evolución durante el curso.")

col1, col2 = st.columns(2)

with col1:
    fig_g3 = px.histogram(
        df_filtrado,
        x='G3',
        color='rendimiento',
        nbins=20,
        title="Distribución de Calificaciones Finales",
        labels={'G3': 'Calificación Final', 'count': 'Número de Estudiantes'},
        color_discrete_map={'Bajo': 'red', 'Medio': 'yellow', 'Alto': 'green'}
    )
    st.plotly_chart(fig_g3, use_container_width=True)

with col2:
    periodos = pd.DataFrame({
        'Periodo': ['G1', 'G2', 'G3'],
        'Promedio': [
            df_filtrado['G1'].mean(),
            df_filtrado['G2'].mean(),
            df_filtrado['G3'].mean()
        ]
    })

    fig_evol = px.line(
        periodos,
        x='Periodo',
        y='Promedio',
        markers=True,
        title="Evolución Promedio de Calificaciones"
    )
    st.plotly_chart(fig_evol, use_container_width=True)

col1, col2 = st.columns(2)

with col1:
    count = df_filtrado.groupby(['sex', 'rendimiento']).size().reset_index(name='count')
    fig_sex = px.bar(
        count,
        x='rendimiento',
        y='count',
        color='sex',
        barmode='group',
        title="Rendimiento por Sexo",
        labels={'count': 'Número de Estudiantes'}
    )
    st.plotly_chart(fig_sex, use_container_width=True)

with col2:
    edu_etiquetas = {0: 'Ninguna', 1: 'Primaria', 2: '5°–9°', 3: 'Secundaria', 4: 'Superior'}
    df_plot = df_filtrado.copy()
    df_plot['edu_prom_padres'] = df_plot['edu_prom_padres'].map(edu_etiquetas)

    fig_edu = px.box(
        df_plot,
        x='edu_prom_padres_label',
        y='G3',
        title="Educación de los Padres vs Calificación Final",
        labels={'G3': 'Calificación Final'}
    )
    fig_edu.update_xaxes(
        categoryorder='array',
        categoryarray=['Ninguna', 'Primaria', '5°–9°', 'Secundaria', 'Superior']
    )
    st.plotly_chart(fig_edu, use_container_width=True)

st.markdown("---")

st.subheader("Características Demográficas")
st.caption("Distribución de edad y patrones generales de consumo.")

col1, col2 = st.columns(2)

with col1:
    fig_edad = px.histogram(
        df_filtrado,
        x='age',
        nbins=len(df_filtrado['age'].unique()),
        title="Distribución de Estudiantes por Edad",
        labels={'age': 'Edad'}
    )
    st.plotly_chart(fig_edad, use_container_width=True)

with col2:
    alc_edad = df_filtrado.groupby('age')['alcohol_promedio'].mean().reset_index()
    fig_alc_edad = px.line(
        alc_edad,
        x='age',
        y='alcohol_promedio',
        markers=True,
        title="Consumo de Alcohol Promedio por Edad",
        labels={'alcohol_promedio': 'Consumo Promedio (1–5)'}
    )
    st.plotly_chart(fig_alc_edad, use_container_width=True)

st.markdown("---")

st.subheader("Factores de Riesgo")
st.caption("Relación entre hábitos, salud y desempeño académico.")

col1, col2 = st.columns(2)

with col1:
    fig_alc = px.box(
        df_filtrado,
        x='rendimiento',
        y='alcohol_promedio',
        color='rendimiento',
        title="Consumo de Alcohol vs Rendimiento Académico"
    )
    st.plotly_chart(fig_alc, use_container_width=True)

with col2:
    fig_health = px.box(
        df_filtrado,
        x='health',
        y='absences',
        title="Estado de Salud vs Ausencias Escolares",
        labels={'health': 'Salud (1=muy mala, 5=muy buena)'}
    )
    st.plotly_chart(fig_health, use_container_width=True)

alc_promedio = pd.DataFrame({
    'Tipo': ['Entre semana', 'Fin de semana'],
    'Promedio': [
        df_filtrado['Dalc'].mean(),
        df_filtrado['Walc'].mean()
    ]
})
fig_dalc_walc = px.bar(
    alc_promedio,
    x='Tipo',
    y='Promedio',
    text='Promedio',
    title="Consumo de Alcohol: Entre Semana vs Fin de Semana"
)
st.plotly_chart(fig_dalc_walc, use_container_width=True)

st.markdown("---")
st.subheader("Análisis de Consumo por Sexo")
st.caption("Comparativa de niveles de consumo entre hombres y mujeres.")

col1, col2 = st.columns(2)

with col1:
    fig_walc_sexo = px.histogram(
        df_filtrado,
        x='Walc',
        color='sex',
        barmode='group', 
        nbins=5,
        title="Consumo: Fin de Semana (Walc)",
        labels={
            'Walc': 'Nivel de Consumo (1-5)',
            'sex': 'Sexo',
            'count': 'Número de Estudiantes'
        },
        color_discrete_map={'F': '#f472b6', 'M': '#3b82f6'}
    )
    st.plotly_chart(fig_walc_sexo, use_container_width=True)

with col2:
    fig_dalc_sexo = px.histogram(
        df_filtrado,
        x='Dalc',
        color='sex',
        barmode='group', 
        nbins=5,
        title="Consumo: Entre Semana (Dalc)",
        labels={
            'Dalc': 'Nivel de Consumo (1-5)',
            'sex': 'Sexo',
            'count': 'Número de Estudiantes'
        },
        color_discrete_map={'F': '#f472b6', 'M': '#3b82f6'}
    )
    st.plotly_chart(fig_dalc_sexo, use_container_width=True)

st.markdown(
    """
    <div style="text-align:center; color:gray">
    Proyecto Final - Analítica y Visualización de Datos | Grupo 5AM1<br>
    Isaac Emiliano Gómez Molina • Rubi Zhang Tan
    </div>
    """,
    unsafe_allow_html=True
)
