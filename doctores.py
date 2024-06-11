import streamlit as st
import comments
from estudio import Estudio
from utils import Utils

st.set_page_config(
    page_title="RH Doctores",
    page_icon="👨‍⚕️",
)

st.title("Doctores")

clientes = []

col1,col2 = st.columns(2)
client = col1.text_input("Ingresar numero de cliente", value="0")
clave = col2.text_input("Ingresar clave de acceso", value="*")

exists = False;
exists = Utils.pair_exists(int(client), str(clave))
if(exists):
    st.write("Bienvenido")
    paciente, path = Utils.get_paciente_and_path(int(client), str(clave))
    db = Utils.readCSVtoBiomarcador("biomarcadores.csv")
    resultados = Utils.readCSVtoEstudio(path)
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
    com = st.text_input("Comentarios")
    if st.button("Enviar"):
        comments.comment1 = com
        st.write("Comentario enviado")

else:
    st.write("Incorrecto, intente de nuevo")