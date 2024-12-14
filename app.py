import streamlit as st
st.sidebar.title("MENU")
app_mode = st.sidebar.selectbox('Selecciona Página',['Portada','Controles'])
# st.sidebar.image("logocasagrande.jpg") #two pages
if app_mode=='Portada':   
	st.balloons()
	st.title('Mi Primera Aplicación en Streamlit')
	st.header('Maestria en Inteligencia Artificial y Ciencia de Datos')
	st.header('Autor: Patricio Navarrete')
	st.caption('Paradigmas de Programación para Inteligencia Artificial y Análisis de Datos C2024 P1')
if app_mode=='Controles': 
	st.title("Ingreso de Datos")
	st.number_input('Ingrese su edad', 0,100)
	st.text_input('Nombres y Apellidos')
	st.slider('Seleccione un mes del año', 1,12)
	st.checkbox('Acepto los términos y condiciones')
	st.radio('Seleccione su género',['Masculino','Femenino'])
	st.selectbox('Seleccione pais de origen',['Argentina','Brasil','Colombia','Ecuador','México'])
	st.file_uploader('Cargar archivo')
	st.date_input('Selecciona una fecha')
	st.time_input('Selecciona una hora')
	st.button('Enviar')

