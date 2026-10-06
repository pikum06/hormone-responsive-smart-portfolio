import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Load and Align Data
df_results = pd.read_csv("../outcomes/csv/final_backtest_results.csv")
df_bio = pd.read_csv("../outcomes/csv/processed_bio_signals.csv")

# Create a combined dataframe for the matrix
df_matrix = df_results[['BTC_Rolling_Vol_30d', 'leverage_cap', 'executed_leverage']].copy()
df_matrix['Bio_Stress_Index'] = df_bio['RMSSD'].iloc[:len(df_results)].values

#The Correlation Heatmap
plt.figure(figsize=(10, 8))
corr_matrix = df_matrix.corr()

sns.heatmap(corr_matrix, annot=True, cmap='RdYlGn', center=0, fmt=".2f", linewidths=0.5)
plt.title("System Interdependency Matrix\n(Bio-Signals vs. Market Stress vs. Risk Exposure)", fontsize=14)
plt.savefig("../outcomes/graphs/correlation_heatmap.png", dpi=300)
plt.close()
print("Saved: correlation_heatmap.png")
