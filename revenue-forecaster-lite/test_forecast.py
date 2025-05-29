from forecast import run_forecast

def test_forecast_basic():
    df, totals = run_forecast(2, 100, 0.1, 0.05, 10, 3, 1000, False, False)
    assert df.iloc[0]["Active Users"] > 0
    assert totals["revenue"] > 0
