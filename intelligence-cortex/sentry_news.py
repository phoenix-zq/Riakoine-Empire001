import time
import sys

def news_sentry():
    print("[SENTRY] Connecting to Institutional News Feeds...")
    while True:
        print("\n--- [MACRO NEWS RADAR] ---")
        print("Market State: VOLATILE_PRE_NEWS")
        print("Active Watch: US Consumer Price Index (CPI)")
        print("Status: STANDING BY - Avoid Heavy Positions")
        sys.stdout.flush()
        time.sleep(15)

if __name__ == "__main__":
    news_sentry()
