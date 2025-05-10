
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Billionaire Tracker", layout="wide")

st.title("🚀 Billionaire Progress Tracker")

uploaded_file = st.file_uploader("Upload Your Tracker (Excel)", type=["xlsx"])

if uploaded_file:
    df = pd.read_excel(uploaded_file)

    # Clean up columns
    df.columns = [col.strip() for col in df.columns]
    st.subheader("📅 Monthly Tracking Table")
    st.dataframe(df, use_container_width=True)

    # Plot Expected vs Actual
    st.subheader("📈 Expected vs Actual Balance")
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(df['Month #'], df['Expected Balance'], label='Expected Balance', linestyle='--', marker='o')

    if 'Actual Balance' in df.columns and df['Actual Balance'].notna().any():
        ax.plot(df['Month #'], df['Actual Balance'], label='Actual Balance', marker='o')

    ax.set_xlabel("Month")
    ax.set_ylabel("Balance ($)")
    ax.set_title("Balance Growth")
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)

    # Progress to 1 Billion
    latest_actual = df['Actual Balance'].dropna().iloc[-1] if df['Actual Balance'].notna().any() else 0
    progress_pct = min(latest_actual / 1_000_000_000, 1.0)
    st.subheader("🏁 Progress to $1 Billion")
    st.progress(progress_pct, text=f"{progress_pct*100:.2f}% to $1B")

    # Growth Percentage Table
    if 'Growth % (Actual)' in df.columns:
        st.subheader("📊 Monthly Growth (%)")
        growth_df = df[['Month #', 'Date', 'Growth % (Actual)']].dropna()
        st.dataframe(growth_df, use_container_width=True)

    st.markdown("---")
    st.markdown("Built for the grind. Billionaire status loading... 💸")
else:
    st.info("👆 Upload your Excel tracker to get started.")
