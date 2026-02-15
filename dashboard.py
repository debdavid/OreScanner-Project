import streamlit as st
import pandas as pd
import time
import os

# DASHBOARD CONFIG
st.set_page_config(page_title="OreScanner HQ", layout="wide")
DATA_FILE = "ore_log.csv"

st.title("⛏️ OreScanner HQ - Live Monitor")

# DASHBOARD LAYOUT
col1, col2 = st.columns(2)
with col1:
    kpi_count = st.empty() # Placeholder for the big number
with col2:
    st.write("### Latest Alerts")
    log_feed = st.empty() # Placeholder for the table

st.write("### 📈 Production Velocity")
chart_spot = st.empty() # Placeholder for the chart

# REAL-TIME LOOP
while True:
    if os.path.exists(DATA_FILE):
        try:
            # Read the CSV
            df = pd.read_csv(DATA_FILE)
            
            if not df.empty:
                # 1. UPDATE METRICS
                total_ore = df["Count"].max() if not df.empty else 0
                kpi_count.metric(label="Total Ore Processed", value=f"{total_ore} tons")
                
                # 2. UPDATE TABLE (Show last 5 rows)
                log_feed.dataframe(df.tail(5), hide_index=True)
                
                # 3. UPDATE CHART
                # Create a simple bar chart of events
                chart_spot.bar_chart(df, x="Timestamp", y="Count")
        except Exception as e:
            st.error(f"Error reading data: {e}")
    else:
        st.warning("Waiting for Backend to start...")

    # Refresh every 1 second
    time.sleep(1)
    
