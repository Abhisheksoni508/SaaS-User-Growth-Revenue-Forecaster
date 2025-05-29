import streamlit as st
import pandas as pd
from forecast import run_forecast

st.title("📈 Revenue Forecaster Lite")

# Inputs
months = st.slider("Months to Forecast", 12, 36, 24)
start_users = st.number_input("Starting Users", 0, 100000, 100)
growth_rate = st.number_input("Monthly Growth Rate (%)", 0.0, 100.0, 10.0) / 100
churn_rate = st.number_input("Monthly Churn Rate (%)", 0.0, 100.0, 5.0) / 100
revenue_per_user = st.number_input("Revenue per User (£)", 0.0, 1000.0, 10.0)
cost_per_user = st.number_input("Cost per User (£)", 0.0, 1000.0, 3.0)
fixed_cost = st.number_input("Fixed Monthly Overhead (£)", 0.0, 100000.0, 1000.0)

# Toggles
boost_rev = st.checkbox("💸 +10% Revenue per User after Month 6")
cut_growth = st.checkbox("📉 -50% Growth Rate after Month 12")

# Run forecast
df, totals = run_forecast(
    months, start_users, growth_rate, churn_rate,
    revenue_per_user, cost_per_user, fixed_cost,
    boost_rev, cut_growth
)

# Output
st.line_chart(df.set_index("Month")[["Revenue (£)", "Costs (£)", "Profit (£)"]])
st.dataframe(df)

st.subheader("📊 Totals")
st.write(f"**Cumulative Revenue**: £{totals['revenue']:,.2f}")
st.write(f"**Cumulative Costs**: £{totals['cost']:,.2f}")
st.write(f"**Cumulative Profit**: £{totals['profit']:,.2f}")
st.subheader("📊 Forecast Summary")

col1, col2, col3 = st.columns(3)

col1.metric("Total Revenue (£)", f"{totals['revenue']:,.2f}")
col2.metric("Total Cost (£)", f"{totals['cost']:,.2f}")
col3.metric("Total Profit (£)", f"{totals['profit']:,.2f}")


# Export buttons
st.download_button("Download CSV", df.to_csv(index=False), "forecast.csv", "text/csv")
st.download_button("Download JSON", df.to_json(orient="records"), "forecast.json", "application/json")


