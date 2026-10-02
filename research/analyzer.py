import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Load Data
sns.set_theme(style="whitegrid")
df = pd.read_csv("../data/final_backtest_results.csv")
df['period'] = df.index

#Perfect Smoothing Symmetry
WINDOW = 100
df['smoothed_panic'] = df['market_panic'].rolling(window=WINDOW).mean()
df['smoothed_leverage'] = df['leverage_cap'].rolling(window=WINDOW).mean()

#Create Stacked Subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8), sharex=True)

#Top Graph: Market Panic Index
ax1.plot(df['period'], df['smoothed_panic'], color='darkred', linewidth=2.5)
ax1.fill_between(df['period'], df['smoothed_panic'], df['smoothed_panic'].min(), color='red', alpha=0.15)
ax1.set_ylabel('Market Panic Index\n(100-Period MA)', fontsize=11, fontweight='bold', color='darkred')
ax1.set_title('Macro System Dynamics\nTop: Market Volatility Threat | Bottom: Biological Circuit Breaker Defense', fontsize=14, fontweight='bold', pad=15)

#Bottom Graph: Executed Leverage Cap
ax2.plot(df['period'], df['smoothed_leverage'], color='darkgreen', linewidth=2.5)
ax2.fill_between(df['period'], df['smoothed_leverage'], df['smoothed_leverage'].min(), color='lightgreen', alpha=0.15)
ax2.set_ylabel('Executed Leverage Cap\n(100-Period MA)', fontsize=11, fontweight='bold', color='darkgreen')
ax2.set_xlabel('Timeline (Simulated 4,150 Periods)', fontsize=12, fontweight='bold')

# 4. Formatting
plt.tight_layout()

# Save the Graph
output_filename = "../outcomes/final_analysis.png"
plt.savefig(output_filename, dpi=300, bbox_inches='tight')
print(f"Saved graph as: {output_filename}")


plt.close()
