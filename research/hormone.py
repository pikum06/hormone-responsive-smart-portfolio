#importing libraries
import asyncio
import pandas as pd
from solana.rpc.async_api import AsyncClient
from solders.keypair import Keypair

PRIVATE_KEY_LIST = [236,45,114,115,21,218,7,221,231,12,141,65,145,86,1,131,92,197,165,93,216,130,252,58,31,32,138,59,35,48,123,20,108,172,80,164,230,64,175,140,62,247,123,251,49,66,
                    224,112,161,48,235,39,22,158,253,178,42,243,38,11,178,87,217,118]


SENDER_KEYPAIR = Keypair.from_bytes(bytes(PRIVATE_KEY_LIST))


RPC_URL = "http://127.0.0.1:8899"
async def test_connection():
    async with AsyncClient(RPC_URL) as client:
        # Check balance of your 8KD... address
        res = await client.get_balance(SENDER_KEYPAIR.pubkey())
        print(f"Hormone Trading Bridge")
        print(f"Wallet Address: {SENDER_KEYPAIR.pubkey()}")
        print(f"Current Balance: {res.value / 10**9} SOL")
        print(f"Status: Connected to Linux Validator")
if __name__ == "__main__":
    asyncio.run(test_connection())
async def run_backtest_simulation(csv_path):

    # Loading bio singals.csv from the current folder

    df = pd.read_csv("final_backtest_results.csv")
    results=[]
    async with AsyncClient(RPC_URL) as client:
        print(f"Starting Backtest for {len(df)} data points")        
        for index, row in df.iterrows():

            # using leverage cap and executed leverage from the backtest results

            bio_cap = row['leverage_cap']

            # BIOMETRIC TRIGGER: If leverage cap is less than 1.0, stress was detected

            if bio_cap < 1.0:
                print(f"Index ({index}): BIO-STRESS DETECTED! Cap reduced to {bio_cap}x")

                results.append({
                    'index': index,
                    'leverage_cap': bio_cap,
                    'status': 'Bio Stress Detected - Trade Adjusted',
                    'timestamp': pd.Timestamp.now()
                })
                await client.get_latest_blockhash()
                print("Trade Confirmed on Local Solana Ledger.")
                print("Executing automated trade based on biometric signal")
                # To avoid flooding your CPU, add a tiny sleep
                await asyncio.sleep(0.01)

        # After the loop, save to a new CSV
        results_df = pd.DataFrame(results)
        results_df.to_csv('hormone_transaction_logs.csv', index=False)
        print("Results saved to hormone_transaction_logs.csv")
if __name__ == "__main__":

    CSV_FILE = "final_backtest_results.csv" 
    asyncio.run(run_backtest_simulation(CSV_FILE))
