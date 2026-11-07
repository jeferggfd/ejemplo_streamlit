import streamlit as st

st.title("Mi primera aplicación de Streamlit")
st.header("¡HOLAAAAAAAAAA!")
st.text("Esta sera mi primer intento de mi pagina")

texto_usuario = st.text_input("Dime algo:")
if texto_usuario:
  st.write(f"Escribiste: {texto_usuario}")
    
if st.button("presiona aqui"):
  st.success("¡elb boton fue seleccionado con exito!")

st.sidebar.title("mi primera barra fue selecionado con exito")
st.sidebar.header("¡increible una Barra Lateral!")
st.sidebar.text("aquie les muestro mi primera barra")

texto_sidebar = st.sidebar.text_input("Di algo en la barra:")
if texto_sidebar:
  st.sidebar.write(f"Escribiste en la barra: {texto_sidebar}")

if st.sidebar.button("Haz clic pero en la barra lateral"):
  st.sidebar.success("¡Botón lateral presionado!")
