import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Setup and Load Data
sns.set_theme(style="whitegrid")
df = pd.read_csv("../data/final_backtest_results.csv")
df['period'] = df.index

# Calculate Stress Level
STANDARD_LEVERAGE = 10.0
df['stress_level'] = STANDARD_LEVERAGE - df['leverage_cap']

# Scaling to 250 filters out high-frequency noise and reveals the macro trend
WINDOW = 250
rolling_corr = df['stress_level'].rolling(window=WINDOW).corr(df['market_panic'])

# 3. Build the Plot
plt.figure(figsize=(12, 6))

plt.plot(df['period'], rolling_corr, color='teal', linewidth=2)

plt.axhline(y=0, color='black', linestyle='-', linewidth=1.5, alpha=0.8)

plt.axhspan(-0.2, 0.2, color='gray', alpha=0.15)

# Plotting the graphs
plt.title(f'Cortisol-Beta Correlation\n(Biological Stress vs. Market Volatility)', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Timeline (Simulated 4,150 Periods)', fontsize=12, fontweight='bold')
plt.ylabel('Coupling Coefficient (Pearson)', fontsize=12, fontweight='bold')
plt.ylim(-1, 1)

plt.tight_layout()

# 4. Save the Graph
output_filename = "../outcomes/Cortisol.png"
plt.savefig(output_filename, dpi=300, bbox_inches='tight')
print(f"Saved graph as: {output_filename}")
plt.close()