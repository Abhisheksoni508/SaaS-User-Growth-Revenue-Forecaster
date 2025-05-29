import pandas as pd

def run_forecast(months, start_users, growth, churn, rpu, cpu, fixed, boost_rev, cut_growth):
    data = []
    users = start_users
    current_growth = growth
    current_rpu = rpu

    for month in range(1, months + 1):
        if boost_rev and month == 7:
            current_rpu *= 1.10
        if cut_growth and month == 13:
            current_growth *= 0.5

        users += users * current_growth
        users -= users * churn

        revenue = users * current_rpu
        cost = users * cpu + fixed
        profit = revenue - cost

        data.append({
            "Month": month,
            "Active Users": round(users),
            "Revenue (£)": round(revenue, 2),
            "Costs (£)": round(cost, 2),
            "Profit (£)": round(profit, 2),
        })

    df = pd.DataFrame(data)
    totals = {
        "revenue": df["Revenue (£)"].sum(),
        "cost": df["Costs (£)"].sum(),
        "profit": df["Profit (£)"].sum()
    }

    return df, totals
