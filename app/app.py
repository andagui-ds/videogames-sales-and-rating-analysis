import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Video Games Analytics Dashboard", layout="wide")

st.title("🎮 Video Games Sales & Performance Dashboard")
st.markdown("Explore global market trends and predictive insights.")

@st.cache_data
def load_data():
    return pd.read_csv("data/processed/games_clean.csv")

try:
    df = load_data()

    # Filtros laterales
    genre = st.sidebar.multiselect("Select Genre:", df["Genre"].unique(), default=df["Genre"].unique()[:3])
    df_filtered = df[df["Genre"].isin(genre)]

    # Visualización principal
    fig = px.bar(
        df_filtered.groupby("Platform")["Global_Sales"].sum().reset_index(),
        x="Platform", y="Global_Sales", title="Global Sales by Platform"
    )
    st.plotly_chart(fig, use_container_width=True)
except Exception as e:
    st.info("Añade el archivo 'games_clean.csv' en 'data/processed/' para visualizar las gráficas.")
