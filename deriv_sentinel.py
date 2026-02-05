import asyncio
import os
import json
from deriv_api import DerivAPI
from dotenv import load_dotenv

# Load credentials
load_dotenv()
API_TOKEN = os.getenv("DERIV_API_TOKEN")
APP_ID = 1089  # Official Deriv API ID

async def run_sentinel():
    if not API_TOKEN:
        print("❌ Error: DERIV_API_TOKEN not found in .env")
        return

    print("🌐 Connecting to Deriv Synthetic Network...")
    
    # Initialize connection
    api = DerivAPI(app_id=APP_ID)

    try:
        # 1. Authorize (Login)
        authorize = await api.authorize({'authorize': API_TOKEN})
        print(f"✅ Login Successful! User: {authorize['authorize']['email']}")
        
        # 2. Check Balance
        balance = await api.balance()
        currency = balance['balance']['currency']
        amount = balance['balance']['balance']
        print(f"💰 Wallet Balance: {amount} {currency}")

        if float(amount) == 0:
            print("⚠️ Warning: Balance is 0. Ensure you transferred funds to the correct account.")

        # 3. Scan Market (Volatility 100 Index)
        symbol = "R_100" 
        print(f"\n📡 Scanning {symbol} (Volatility 100 Index)...")
        
        # Get current tick
        tick = await api.ticks({'ticks': symbol})
        current_price = tick['tick']['quote']
        print(f"📊 Current Price: {current_price}")
        
        print("\n✅ SYSTEM READY. The Sentinel is online and watching.")

    except Exception as e:
        print(f"❌ Critical Error: {e}")
    
    finally:
        # Close connection nicely
        await api.disconnect()

if __name__ == "__main__":
    asyncio.run(run_sentinel())
