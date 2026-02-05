import asyncio
import os
import pandas as pd
from datetime import datetime, timedelta
from deriv_api import DerivAPI
from telegram import Bot
from dotenv import load_dotenv

load_dotenv(dotenv_path="/root/.env")

# --- SURVIVAL CONFIG ---
MARKETS = ["R_10", "R_25", "R_50", "R_75", "R_100"]
STAKE = 0.35 # Mandatory minimum to avoid lockout
VAULT_ID = "CRW827152"
TRADE_ID = os.getenv("TRADE_ACCOUNT")
TG_TOKEN = os.getenv("TELEGRAM_TOKEN")
TG_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
COOL_DOWN_MINUTES = 30

bot = Bot(token=TG_TOKEN) if TG_TOKEN else None
rest_until = {}

async def send_tg(msg):
    if bot and TG_CHAT_ID:
        try: await bot.send_message(chat_id=TG_CHAT_ID, text=f"🛡️ ZACK1 SURVIVAL:\n{msg}")
        except: print("TG Error")

async def get_apn_intel(api, symbol):
    d_data = await api.ticks_history({'ticks_history': symbol, 'count': 50, 'style': 'candles', 'granularity': 86400})
    df_d = pd.DataFrame(d_data['candles'])
    price = float(df_d['close'].iloc[-1])
    
    # 7. Weekly/Daily Alignment (APN Core)
    w_open, d_open = float(d_data['candles'][0]['open']), float(d_data['candles'][-1]['open'])
    pdh, pdl = float(df_d['high'].iloc[-2]), float(df_d['low'].iloc[-2])
    
    # Directional Check
    bias = "BULL" if (price > w_open and price > d_open) else "BEAR" if (price < w_open and price < d_open) else "WAIT"
    
    return {"symbol": symbol, "bias": bias, "pdh": pdh, "pdl": pdl, "price": price}

async def execute_trade(api, symbol, direction):
    if symbol in rest_until and datetime.now() < rest_until[symbol]: return False
    try:
        contract_type = "CALL" if direction == "BULL" else "PUT"
        proposal = await api.proposal({"proposal": 1, "amount": STAKE, "basis": "stake", "contract_type": contract_type, "currency": "USD", "symbol": symbol, "duration": 5, "duration_unit": "t"})
        if 'proposal' in proposal:
            buy = await api.buy({"buy": proposal['proposal']['id'], "price": STAKE})
            contract_id = buy['buy']['contract_id']
            await send_tg(f"🎯 SURVIVAL STRIKE: {direction} on {symbol}")
            
            await asyncio.sleep(15) 
            result = await api.proposal_open_contract({"proposal_open_contract": 1, "contract_id": contract_id})
            profit = float(result['proposal_open_contract'].get('profit', 0))

            if profit < 0:
                rest_until[symbol] = datetime.now() + timedelta(minutes=COOL_DOWN_MINUTES)
                await send_tg(f"⚠️ LOSS. Restoring discipline. 30min pause for {symbol}.")
            else:
                await send_tg(f"✅ WIN. Recovery in progress.")
    except Exception as e:
        await send_tg(f"⚠️ System Error: {e}")
    return False

async def main():
    api = DerivAPI(app_id=1089)
    await api.authorize({'authorize': os.getenv("TRADE_TOKEN")})
    await send_tg("🦅 Zack1 Survival Mode: $0.35 Min-Stake Engaged.")

    while True:
        try:
            for symbol in MARKETS:
                if symbol in rest_until and datetime.now() < rest_until[symbol]: continue
                intel = await get_apn_intel(api, symbol)
                # 8:54 Benson Trap logic with 1.0005/0.9995 depth
                if intel['bias'] == "BULL" and intel['price'] <= intel['pdl'] * 1.0005:
                    await execute_trade(api, symbol, "BULL")
                elif intel['bias'] == "BEAR" and intel['price'] >= intel['pdh'] * 0.9995:
                    await execute_trade(api, symbol, "BEAR")
            await asyncio.sleep(30)
        except: await asyncio.sleep(10)

if __name__ == "__main__":
    asyncio.run(main())
