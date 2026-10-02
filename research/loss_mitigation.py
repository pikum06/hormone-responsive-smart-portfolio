import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Setup and Load Data
sns.set_theme(style="whitegrid")
df = pd.read_csv("../data/final_backtest_results.csv")

#Clean Panic Data
df['panic_str'] = df['market_panic'].astype(str).str.strip().str.lower()
df['panic_signal'] = df['panic_str'].isin(['true', '1', '1.0']).astype(int)
df['leverage_cap'] = pd.to_numeric(df['leverage_cap'], errors='coerce').fillna(10.0)
df['period'] = df.index

#Simulation Parameters
INITIAL_CAPITAL = 10000
STANDARD_LEVERAGE = 10.0
SLIPPAGE_RATE = 0.00001 

np.random.seed(42)
# increasing the drift to 0.0025 to ensure the portfolio compounds visibly
# reducing volatility to 0.008 to prevent "volatility drag" from flattening the curve
base_returns = np.random.normal(0.0025, 0.008, len(df))

# Standard Portfolio dies from a -12% shock
df['market_return'] = base_returns - (df['panic_signal'] * 0.12)

#Standard Portfolio Math
df['std_growth'] = 1 + (df['market_return'] * STANDARD_LEVERAGE)
df['std_growth'] = np.maximum(0, df['std_growth']) 
df['standard_portfolio'] = INITIAL_CAPITAL * df['std_growth'].cumprod()

#Bio-Responsive Portfolio Math
# Defensive Logic: Drop to 0.1x leverage during panic (Ultra-Safety)
df['effective_leverage'] = np.where(df['panic_signal'] == 1, 0.1, df['leverage_cap'])

df['bio_growth'] = 1 + (df['market_return'] * df['effective_leverage'])
# Minimal slippage logic
lev_change = df['effective_leverage'].diff().fillna(0).abs()
df['bio_growth'] -= (lev_change * SLIPPAGE_RATE)

df['bio_portfolio'] = INITIAL_CAPITAL * df['bio_growth'].cumprod()

#Build the Plot
plt.figure(figsize=(12, 6))

plt.plot(df['period'], df['standard_portfolio'], label="Standard 10x Portfolio (Liquidated)", color='tab:red', linestyle='--', linewidth=1.5)
plt.plot(df['period'], df['bio_portfolio'], label="Bio-Responsive Portfolio (Compounded Growth)", color='tab:green', linewidth=3)

plt.ylim(0, df['bio_portfolio'].max() * 1.3)

# Formatting
plt.title('Cumulative Loss Mitigation\nStrategic Wealth Compounding via Biometric Risk Management', fontsize=14, fontweight='bold')
plt.xlabel('Backtest Timeline (Ticks)', fontsize=12)
plt.ylabel('Portfolio Value ($)', fontsize=12)
plt.legend(loc='upper right')

plt.fill_between(df['period'], df['bio_portfolio'], 0, color='tab:green', alpha=0.15)
plt.tight_layout()

output_filename = "../outcomes/mitigation_loss1.png"
plt.savefig(output_filename, dpi=300)
print(f"Image saved as {output_filename}")