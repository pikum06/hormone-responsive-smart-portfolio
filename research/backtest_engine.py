import pandas as pd

# Loading two processed files
bio = pd.read_csv("../data/processed_bio_signals.csv")
mkt = pd.read_csv("../data/processed_market_signals.csv")

#simulating a trading day
#maximum length in market signals is 4150, so we will sample 4150 from the bio signals to match
sim_length = 4150
sample_mkt = mkt.head(sim_length).copy()
sample_bio = bio.sample(sim_length).reset_index(drop=True)

# Merge the cortisol data with the market
results = pd.concat([sample_mkt, sample_bio['leverage_cap']], axis=1)

# The Circuit Breaker Logic:
# Actual Leverage = 10 * Bio Leverage Cap
def simulate_trade(row):
    intended_leverage = 10
    return intended_leverage * row['leverage_cap']

results['executed_leverage'] = results.apply(simulate_trade, axis=1)

print("BACKTEST RESULTS")
print(results[['Date', 'BTC_Rolling_Vol_30d', 'market_panic', 'leverage_cap', 'executed_leverage']].head(20))

results.to_csv("../data/final_backtest_results.csv", index=False)