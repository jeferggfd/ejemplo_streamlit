import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

# Configuración inicial de la página web
st.set_page_config(page_title="Venta de Transformers", page_icon="🤖")
st.title("VENTA DE TRANSFORMERS 🤖")

# Carga de datos optimizada con caché
@st.cache_data
def cargar_datos() -> pd.DataFrame:
    return pd.read_csv("ventas.csv", sep=";", parse_dates=["fecha"])

df = cargar_datos()

# --- Filtros en la barra lateral (Sidebar) ---
st.sidebar.title("pagina de pasita")
st.sidebar.header("Filtros")
st.sidebar.image("boca.jpg")  # Imagen institucional en el sidebar

colores = st.sidebar.multiselect(
    "Colores", 
    sorted(df["color"].unique()), 
    default=sorted(df["color"].unique())
)

anios = st.sidebar.multiselect(
    "Años", 
    sorted(df["fecha"].dt.year.unique()), 
    default=sorted(df["fecha"].dt.year.unique())
)

# Filtrado dinámico del DataFrame usando operadores booleanos
filtrado = df[df["color"].isin(colores) & df["fecha"].dt.year.isin(anios)]

# Validación de seguridad si el filtro queda vacío
if filtrado.empty:
    st.warning("Selecciona al menos un color y un año en los filtros laterales.")
    st.stop()

# --- Sección de Métricas (KPIs) ---
col1, col2 = st.columns(2)
col1.metric("Total de unidades vendidas", f"{filtrado['unidades'].sum():,}")
col2.metric("Color más vendido", filtrado.groupby("color")["unidades"].sum().idxmax())

# --- Gráfico 1: Ventas por color (Barras) ---
st.subheader("Ventas totales por color")
por_color = filtrado.groupby("color")["unidades"].sum().sort_values(ascending=False)

fig1, ax1 = plt.subplots(figsize=(8, 4))
ax1.bar(por_color.index, por_color.values, color="#1f77b4", edgecolor="black")
ax1.set_ylabel("Unidades")
ax1.set_xlabel("Color")
ax1.grid(axis="y", linestyle="--", alpha=0.7)
st.pyplot(fig1)

# --- Gráfico 2: Evolución mensual (Líneas) ---
st.subheader("Evolución mensual")
pivot = filtrado.pivot_table(index="fecha", columns="color", values="unidades", aggfunc="sum")

fig2, ax2 = plt.subplots(figsize=(10, 5))
pivot.plot(ax=ax2, marker="o")
ax2.set_ylabel("Unidades")
ax2.set_xlabel("Fecha")
ax2.grid(True, linestyle="--", alpha=0.6)
st.pyplot(fig2)

# --- Funcionalidad Extra: Botón de Descarga ---
st.markdown("---")
csv_data = filtrado.to_csv(index=False).encode('utf-8')
st.download_button(
    label="📥 Descargar datos filtrados en CSV",
    data=csv_data,
    file_name="reporte_filtrado.csv",
    mime="text/csv"
)

# --- Expansor para ver la tabla de datos subyacente ---
with st.expander("Ver tabla de datos detallada"):
    st.dataframe(filtrado)
