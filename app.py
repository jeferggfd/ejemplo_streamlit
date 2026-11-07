import streamlit as st

st.title("Mi primera aplicación de Streamlit")
st.header("¡Hola, Streamlit!")
st.text("Esta es una aplicación simple")

texto_usuario = st.text_input("Escribe algo:")
if texto_usuario:
  st.write(f"Escribiste: {texto_usuario}")
    
if st.button("Haz clic"):
  st.success("¡Botón principal presionado con éxito!")

st.sidebar.title("Mi primera barra lateral de Streamlit")
st.sidebar.header("¡Hola, Barra Lateral!")
st.sidebar.text("Esto es una barra lateral")

texto_sidebar = st.sidebar.text_input("Escribe algo en la barra:")
if texto_sidebar:
  st.sidebar.write(f"Escribiste en la barra: {texto_sidebar}")

if st.sidebar.button("Haz clic pero en la barra lateral"):
  st.sidebar.success("¡Botón lateral presionado!")
