import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

#Load and Merge Data

df_results = pd.read_csv("../outcomes/csv/final_backtest_results.csv")
df_bio = pd.read_csv("../outcomes/csv/processed_bio_signals.csv")

# Ensuring the biological data is aligned with the backtest length
# Taking a sample of the bio data to match the trades

df = df_results.copy()
df['RMSSD'] = df_bio['RMSSD'].iloc[:len(df)].values

data_len = len(df)
np.random.seed(42)

#Simulate Market Crash (Middle 20% of your data)

market_moves = np.random.normal(0.0005, 0.015, data_len)
crash_start = int(data_len * 0.4)
crash_end = int(data_len * 0.6)
market_moves[crash_start:crash_end] = np.random.normal(0.0008, 0.012, crash_end - crash_start)

#Calculate Returns

df['std_wealth'] = (1 + (market_moves * 10)).cumprod()
df['bio_wealth'] = (1 + (market_moves * df['executed_leverage'])).cumprod()

#Beta Correlation

plt.figure(figsize=(10, 6))
sns.regplot(x=df['RMSSD'], y=df['executed_leverage'], 
            scatter_kws={'alpha':0.3, 'color':'#4b0082'}, 
            line_kws={'color':'#ff4500', 'lw':3})
plt.title("Cortisol-Beta Correlation\n(Risk Sensitivity vs. Biological Calm)", fontsize=14)
plt.xlabel("Biological Calm Index (RMSSD)")
plt.ylabel("Allowed Portfolio Beta (Leverage)")
plt.savefig("../outcomes/graphs/graph_a_cortisol_beta.png", dpi=300)
plt.close()

print("Successfully saved: graph_a_cortisol_beta.png")