import pandas as pd
import sys
import os

def get_structural_markings():
    print("[MAPPER] Scanning Institutional HTF Levels (Yearly -> 1H)...")
    
    # Priority: NMOG (Month) > NWOG (Week) > NDOG (Day)
    markings = {
        "Yearly_Open": 64200.00,  # Example: Jan 1st Open
        "Monthly_Open": 65800.00, # Current Month Open
        "Weekly_Gap_CE": 65350.50, # 50% of the NWOG
        "Swing_High_4H": 66100.00,
        "Swing_Low_4H": 64800.00
    }

    print("\n--- [INSTITUTIONAL MAP] ---")
    for level, price in markings.items():
        print(f"LEVEL: {level:<15} | PRICE: {price:.2f}")
    
    # Check for 'Opening Gaps'
    nwog_present = True # Simulated check
    if not nwog_present:
        print("[!] NWOG absent. Pivoting to NDOG (Daily Gap) as primary anchor.")
    
    sys.stdout.flush()

if __name__ == "__main__":
    get_structural_markings()
