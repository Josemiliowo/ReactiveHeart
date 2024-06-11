import streamlit as st
import datetime
from estudio import Estudio
from utils import Utils
import comments

st.set_page_config(
    page_title="RH Pacientes",
    page_icon="😷",
)

st.set_option('deprecation.showPyplotGlobalUse', False)
st.title("Pacientes")

st.markdown("🟢   Conectado actualmente a:      _Marker-0123_")

st.write("N. de cliente: ", 12491)
if st.checkbox("Mostrar clave de acceso"):
    st.write("Clave de cliente: ", "0124QfrR9")
else:
    st.write("Clave de cliente: ", "**********")

t = datetime.datetime.now()

st.subheader("Análisis")

st.write('Ejecutrar análisis con datos de ', t.strftime("%H:%M:%S"), " al dia de ", t.strftime("%D"))

if st.button("Ejecutar"):
    db = Utils.readCSVtoBiomarcador("biomarcadores.csv")
    resultados = Utils.readCSVtoEstudio("resultados1.csv")
    estudio = Estudio("Juan", "2021-01-01", resultados, db, comments.comment1)

    col1, col2 = st.columns(2)
    col1.pyplot(Utils.create_pie_chart(estudio.runStudyProp()))
    col2.pyplot(Utils.create_pie_chart(estudio.runStudyNonProp()))
    col1.write("Gráfico teniendo en cuenta distancia de parámetros")
    col2.write("Gráfico sin tener en cuenta distancia de parámetros")

    col3 = st.columns(1)
    pd = Utils.csv_to_dataframe("resultados1.csv")
    st.table(pd)

    col4 = st.columns(1)
    st.subheader("Comentarios de medico:")
    st.write(estudio.getComment())