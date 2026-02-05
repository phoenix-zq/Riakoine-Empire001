import asyncio
import os
from datetime import datetime, timedelta
from deriv_api import DerivAPI
from dotenv import load_dotenv

# Load environment only if run directly or explicitly requested
def load_config():
    load_dotenv(dotenv_path="/root/Riakoine-Empire001/.env")
    return os.getenv("TRADE_TOKEN")

class MarketScanner:
    def __init__(self, token=None):
        self.token = token if token else load_config()
        self.api = DerivAPI(app_id=1089)

    async def fetch_structure(self, symbol="R_100"):
        """
        Returns a dictionary with raw market data.
        Does NOT print anything. Pure logic.
        """
        try:
            await self.api.authorize({'authorize': self.token})
            
            # Fetch Daily Candles (Last 14 days)
            daily_candles = await self.api.ticks_history({
                'ticks_history': symbol,
                'adjust_start_time': 1,
                'count': 14,
                'end': 'latest',
                'style': 'candles',
                'granularity': 86400 
            })

            if 'candles' not in daily_candles:
                return None

            candles = daily_candles['candles']
            
            # 1. Weekly Bias Logic
            today = datetime.utcnow()
            days_since_monday = today.weekday()
            week_start_index = -(days_since_monday + 1)
            
            # Handle edge case if data is short
            if abs(week_start_index) <= len(candles):
                week_open_price = float(candles[week_start_index]['open'])
            else:
                week_open_price = float(candles[0]['open'])

            current_price = float(candles[-1]['close'])
            daily_open_price = float(candles[-1]['open'])

            # 2. Market Structure (Swing Points)
            # Look at previous 10 days (excluding today)
            past_10_days = candles[-11:-1]
            swing_high = max([float(c['high']) for c in past_10_days])
            swing_low = min([float(c['low']) for c in past_10_days])

            # 3. Determine Bias
            weekly_bias = "BULLISH" if current_price > week_open_price else "BEARISH"
            daily_bias = "BULLISH" if current_price > daily_open_price else "BEARISH"
            
            # 4. Determine Structure Phase
            if current_price > swing_high:
                phase = "BREAKOUT_UP"
            elif current_price < swing_low:
                phase = "BREAKDOWN_DOWN"
            else:
                phase = "RANGING"

            return {
                "symbol": symbol,
                "current_price": current_price,
                "weekly_bias": weekly_bias,
                "week_open": week_open_price,
                "daily_bias": daily_bias,
                "daily_open": daily_open_price,
                "structure_phase": phase,
                "resistance": swing_high,
                "support": swing_low
            }

        except Exception as e:
            print(f"Scanner Error: {e}")
            return None
        finally:
            await self.api.disconnect()

async def main():
    """
    The Visual Reporter. Runs only when executed directly.
    """
    scanner = MarketScanner()
    print("\n🗺️  CONNECTING TO SATELLITE... (Scanning R_100)")
    data = await scanner.fetch_structure()

    if data:
        print("="*50)
        print(f"📡 ASSET: {data['symbol']} | PRICE: {data['current_price']}")
        print("="*50)
        
        # Color coding for visual clarity
        wb_icon = "🟢" if data['weekly_bias'] == "BULLISH" else "🔴"
        db_icon = "🟢" if data['daily_bias'] == "BULLISH" else "🔴"
        
        print(f"🗓️  WEEKLY BIAS:  {data['weekly_bias']} {wb_icon}")
        print(f"   (Week Open: {data['week_open']})")
        print("-" * 30)
        print(f"☀️  DAILY BIAS:   {data['daily_bias']} {db_icon}")
        print(f"   (Day Open: {data['daily_open']})")
        print("-" * 30)
        print(f"🏰 STRUCTURE MAP:")
        print(f"   🛑 Resistance: {data['resistance']}")
        print(f"   🛡️ Support:    {data['support']}")
        print(f"   🚩 Phase:      {data['structure_phase']}")
        print("="*50 + "\n")
        
        # Strategic Advice
        if data['weekly_bias'] == data['daily_bias']:
            print(f"✅ CONFLUENCE DETECTED: {data['weekly_bias']}")
            print(f"👉 RECOMMENDATION: Look for {data['weekly_bias']} entries only.")
        else:
            print(f"⚠️ CONFLICT DETECTED")
            print(f"👉 RECOMMENDATION: Stand Down. Market is choppy.")
    else:
        print("❌ Failed to retrieve structure data.")

if __name__ == "__main__":
    asyncio.run(main())
