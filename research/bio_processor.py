import pandas as pd
import numpy as np

#Load the SWELL HRV dataset

path = "../data/hrv/hrv dataset/data/final/train.csv" 
df = pd.read_csv(path)

print("Dataset Loaded")
print(df['condition'].value_counts())

#Define the 'Biological Circuit Breaker' Logic
#mapping physiological conditions to a Leverage Multiplier (0.0 to 1.0)
def map_stress_to_leverage(condition):
    if condition == 'no stress':
        return 1.0  # 100% of allowed leverage
    elif condition == 'interruption':
        return 0.5  # Reduce leverage by 50%
    elif condition == 'time pressure':
        return 0.1  # Emergency de-risking: 10% limit
    else:
        return 1.0

# Apply the mapping
df['leverage_cap'] = df['condition'].apply(map_stress_to_leverage)

#Save a new data file with the leverage caps for merging with market data
processed_path = "../outcomes/csv/processed_bio_signals.csv"
df[['MEAN_RR', 'RMSSD', 'condition', 'leverage_cap']].to_csv(processed_path, index=False)

print(f"\nProcessed data saved to {processed_path}")
print(df[['condition', 'leverage_cap']].head(10))