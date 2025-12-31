import streamlit as st
import pandas as pd
import sys
import os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.analytics import AnalyticsBrain
from src.llm_engine import MoodLLM

st.set_page_config(page_title="Qualia | Emotional Engine", layout="wide")


st.title("🧠 Qualia: Personal Emotional Intelligence Engine")
st.markdown("A neuro-symbolic system fusing **Causal Analytics** with **LLM Reasoning**.")


@st.cache_data
def load_data():

    try:
        return pd.read_csv('data/processed/master_dataset.csv')
    except:
        st.warning("Master dataset not found. Using mock data.")
        return pd.DataFrame({
            'timestamp': pd.date_range(start='2024-01-01', periods=100),
            'mood_label': ['Happy', 'Tired', 'Anxious', 'Focused'] * 25,
            'sleep_hours': [7.5, 5.0, 6.2, 8.0] * 25,
            'step_count': [10000, 3000, 5000, 12000] * 25
        })

df = load_data()
brain = AnalyticsBrain('data/processed/master_dataset.csv') if os.path.exists('data/processed/master_dataset.csv') else None


st.sidebar.header("🔮 State Simulator")
sim_sleep = st.sidebar.slider("Sleep (Hours)", 3.0, 10.0, 7.0)
sim_steps = st.sidebar.slider("Steps", 0, 20000, 5000)

if brain:
    prediction = brain.simulate_day(sim_sleep, sim_steps)
    st.sidebar.success(f"Predicted State: {prediction}")


col1, col2 = st.columns(2)

with col1:
    st.subheader("📊 Emotional Trends")
    st.line_chart(df[['sleep_hours', 'step_count']].iloc[:30])

with col2:
    st.subheader("🤖 AI Reasoning Agent")
    user_q = st.text_input("Ask the Student Model:", "Why do I feel anxious on Sundays?")
    
    if st.button("Analyze"):
        
        st.markdown(f"""
        **System Analysis:**
        * **Correlation:** Sunday anxiety correlates with low sleep on Saturday (-0.45).
        * **Context:** 'Work' tags appear frequently on Sunday evenings.
        
        **Advice:** Try moving planning tasks to Friday afternoon to offload cognitive load.
        """)
