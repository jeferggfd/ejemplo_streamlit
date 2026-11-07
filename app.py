import streamlit as st

# 1. TÍTULOS Y TEXTOS EN EL ÁREA PRINCIPAL
st.title("Mi primera aplicación de Streamlit")
st.header("¡HOLA")
st.text("Esta sera mi primer intento de mi pagina")

# 2. CAPTURA Y CONDICIONAL DE TEXTO (Área Principal)
# st.text_input crea una caja de texto y guarda lo que escribas en una variable (texto_usuario)
texto_usuario = st.text_input("Dime algo:")

# El 'if' evalúa: "Si la variable 'texto_usuario' tiene contenido (no está vacía)..."
if texto_usuario:
  # ...entonces muestra en pantalla el texto formateado con lo que el usuario escribió
  st.write(f"Escribiste: {texto_usuario}")

# 3. BOTÓN PRINCIPAL
# st.button crea un botón interactivo. Si haces clic en él, devuelve True (verdadero) por un instante.
if st.button("presiona aqui"):
  # Si se presionó, muestra un mensaje de éxito verde
  st.success("¡Botón principal presionado!")


# 4. ELEMENTOS EN LA BARRA LATERAL (Usando st.sidebar)
# Todo lo que tenga '.sidebar.' antes se desplaza automáticamente a la columna izquierda.
st.sidebar.title("mi primera barra...")
st.sidebar.header("¡increible una Barra Lateral!")
st.sidebar.text("aqui les muestro mi primera barra")

# 5. CAPTURA Y CONDICIONAL DE TEXTO (En la Barra Lateral)
# Funciona igual que el anterior, pero el input vive exclusivamente en el panel lateral.
texto_sidebar = st.sidebar.text_input("Di algo en la barra:")

if texto_sidebar:
  # Muestra el resultado dentro de la barra lateral
  st.sidebar.write(f"Escribiste en la barra: {texto_sidebar}")

# 6. BOTÓN EN LA BARRA LATERAL
if st.sidebar.button("Haz clic pero en la barra lateral"):
  # Muestra un mensaje de éxito flotante en la barra lateral
  st.sidebar.success("¡Botón lateral presionado!")
