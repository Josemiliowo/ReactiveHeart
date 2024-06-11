# With love from Josemiliowo

import streamlit as st

st.set_page_config(
    page_title="CVD Imaging",
    page_icon="❤️",
)

st.title(":green[Bienvenido al portal de CVD Imaging]")
st.write("Hoy en día, el proceso para detectar enfermedades cardiovasculares es muy tardado por lo que aumenta el riesgo. Igualmente, mucha gente evita hacerse dichos estudios por los costos que tienen o por la falta de accesibilidad a un especialista que mande a hacer los estudios necesarios.")

col1,col2 = st.columns(2)
col1.header("Reactive Heart")
col1.write("Por eso creamos un kit de estudio para la detección de biomarcadores que estan asociados enfermedades cardiacas para determinar el riesgo de estas de manera")
col1.write("- Fácil")
col1.write("- Rápida")
col1.write("- Accesible")
col2.write("Imagen")
col1.write("Si estas interesado en adquirir nuestro producto, haz click [aqui](%s) para encontrar un distribuidor cerca de ti." % "https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwj_k5HDptSGAxU9KkQIHZHqAUAQi6AMegQIChAB&url=https%3A%2F%2Fmaps.google.com%2Fmaps%3Fclient%3Dopera-gx%26hs%3Df9q%26sca_esv%3D1994aae6371246d6%26output%3Dsearch%26q%3Dgoogle%2Bmaps%2Bfarmacias%2Bsimilares%26source%3Dlnms%26entry%3Dmc%26ved%3D1t%3A200715%26ictx%3D111&usg=AOvVaw13iITTm4qRN2Rgv0mT505r&opi=89978449")

col1.write()
st.write("Para mas información acerca de que son los biomarcadores y como es que nuestro producto puede ayudarte, visita nuestra página de [información](%s)" % "informacion")

st.divider()

col3 = st.columns(1)
st.header("¿A quien le sirve Reactive Heart?")

col4, col5 = st.columns(2)
col4.subheader("Para pacientes")
col4.write("Tras comprar el producto, puedes acceder al portal de usuarios de nuestro producto, tras conectar el dispositivo utilizando Bluetooth, puedes ver los resultados de tus estudios y recibir una interpretación llevada a cabo por nuestros algoritmos.")
col4.write("Igualmente, esta información puede guardarse en la nube y compartirse con tu médico de confianza para un análisis adicional.")
col4.write("[Pagina de pacientes](%s)" % "pacientes")

col5.image("imagenes\pacientes.jpg")

col6,col7 = st.columns(2)
col7.subheader("Para doctores")
col7.write("Como médco, resulta extremadamente cómodo el solicitar y revisar estudios a través de nosotros. No solo garantizamos un medio periódico de chequeo a sus pacientes, si no que comartimos el tiempo real sus resultados para que pueda llevar a cabo revisiones periódicas de forma remota.")
col7.write("Para empezar a operar como doctor con nosotros regístrese, y solicite el número de usuario y código de referencia de sus pacientes para verlos en su portal.")
col7.write("[Pagina de doctores](%s)" % "doctores")

col6.image("imagenes\doctores.jpg")

st.divider()

col8 = st.columns(1)
