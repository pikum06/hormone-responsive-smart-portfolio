import pandas as pd
import os

base_dir = os.path.dirname(os.path.abspath(__file__))

market_path = os.path.join(base_dir, "../data/macro_stress/Global_Market_Stress_and_Liquidity_Regimes.csv") 

try:
    m_df = pd.read_csv(market_path)
    print("Market Data Loaded")
    
    # used BTC Volatility as our Market Stress indicator
    vol_col = 'BTC_Rolling_Vol_30d'
    
    if vol_col in m_df.columns:
        threshold = m_df[vol_col].mean()
        m_df['market_panic'] = m_df[vol_col] > threshold
        
        # Save a processed version for merging with bio data and backtest results
        m_df[['Date', vol_col, 'market_panic']].to_csv("../data/processed_market_signals.csv", index=False)
        print(f"Using {vol_col} to detect panic.")
        print(m_df[['Date', 'market_panic']].head())
    else:
        print(f"Error: Could not find {vol_col}. Check column names!")

except Exception as e:
    print(f"Error: {e}")