import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(page_title="Video Games Analytics Dashboard", layout="wide")

st.title("🎮 Video Games Sales & Performance Dashboard")
st.markdown("Explore global market trends and predictive insights.")

@st.cache_data
def load_data():
    try:
        # Intenta cargar el archivo si existe
        return pd.read_csv("data/processed/games_clean.csv")
    except Exception:
        # Si no existe, genera un dataset sintético para demostración
        np.random.seed(42)
        platforms = ["PS4", "PS5", "XOne", "Series X", "Switch", "PC"]
        genres = ["Action", "Shooter", "Role-Playing", "Sports", "Misc", "Racing"]
        publishers = ["Nintendo", "Electronic Arts", "Activision", "Sony Interactive", "Ubisoft"]
        
        data = {
            "Name": [f"Game Title {i}" for i in range(1, 201)],
            "Platform": np.random.choice(platforms, 200),
            "Year_of_Release": np.random.randint(2015, 2024, 200),
            "Genre": np.random.choice(genres, 200),
            "Publisher": np.random.choice(publishers, 200),
            "Global_Sales": np.round(np.random.exponential(scale=2.5, size=200) + 0.1, 2),
            "Critic_Score": np.random.randint(50, 99, 200),
            "User_Score": np.round(np.random.uniform(5.0, 9.8, 200), 1)
        }
        return pd.DataFrame(data)

df = load_data()

# Filtros laterales
st.sidebar.header("Filter Options")
selected_genres = st.sidebar.multiselect(
    "Select Genre:", 
    options=df["Genre"].unique(), 
    default=list(df["Genre"].unique()[:3])
)

df_filtered = df[df["Genre"].isin(selected_genres)] if selected_genres else df

# Métricas principales
col1, col2, col3 = st.columns(3)
col1.metric("Total Titles Analyzed", len(df_filtered))
col2.metric("Total Global Sales (M)", f"${df_filtered['Global_Sales'].sum():.2f}M")
col3.metric("Avg Critic Score", f"{df_filtered['Critic_Score'].mean():.1f}/100")

st.markdown("---")

# Visualizaciones
col_chart1, col_chart2 = st.columns(2)

with col_chart1:
    fig_bar = px.bar(
        df_filtered.groupby("Platform")["Global_Sales"].sum().reset_index(),
        x="Platform", y="Global_Sales",
        title="Global Sales by Platform",
        color="Platform",
        color_discrete_sequence=px.colors.qualitative.Bold
    )
    st.plotly_chart(fig_bar, use_container_width=True)

with col_chart2:
    fig_scatter = px.scatter(
        df_filtered,
        x="Critic_Score", y="Global_Sales",
        color="Genre",
        size="Global_Sales",
        hover_name="Name",
        title="Critic Score vs. Global Sales"
    )
    st.plotly_chart(fig_scatter, use_container_width=True)
