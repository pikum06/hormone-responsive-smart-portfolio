import pandas as pd
import os
from solana.rpc.api import Client
from solders.pubkey import Pubkey

PROGRAM_ID = Pubkey.from_string("69pk4SPGUu2obf39o6Rm755ZQhbqfeNRdhFtR1rQe2tz")
def sync_bio_to_blockchain():
    # Direct path since we are in the research folder
    csv_filename = "final_backtest_results.csv"
    
    # Connecting to Local Validator 
    
    client = Client("http://127.0.0.1:8899") 
    
    try:
        if client.is_connected():
            print("Successfully connected to Solana Local Validator.")
    except Exception:
        print("Error: Solana Validator is not running. Run 'solana-test-validator' in another tab.")
        return

    if not os.path.exists(csv_filename):
        print(f"Error: Could not find {csv_filename} in the current folder.")
        return

    # Loading the data
    df = pd.read_csv(csv_filename)
    print(f"Synchronizing Biometric State to Ledger")

    for i, row in df.iterrows():
        
        # Using the columns we validated for Professor Malmendier
        lev_cap = int(row['executed_leverage'] * 10) 
        stress_flag = True if row['leverage_cap'] < 1.0 else False
        
        
        # This simulates the 'Anchor Instruction' call
        print(f"Propagating Index {i}: Enforcing {lev_cap/10}x Leverage | Stress Mode: {stress_flag}")
        
        
        # Stop after a few rows for the initial test
        if i >= 4: break

if __name__ == "__main__":
    sync_bio_to_blockchain()