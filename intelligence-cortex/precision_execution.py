import sys
import time

class EmpirePrecision:
    def __init__(self):
        self.regime = "TREND" # Options: TREND or RANGE
        self.entry = 65475.0
        self.stop_loss = 65300.0

    def manage_risk(self, current_price):
        print(f"\n--- [PRECISION MANAGER] ---")
        # 1. First move: Protect the Capital
        if current_price >= self.entry + 150 and self.stop_loss < self.entry:
            self.stop_loss = self.entry + 10.0
            print(">> STATUS: Target 1 Hit. Stop moved to BREAK-EVEN.")

        # 2. Strategy Choice: Trail vs. Hold
        if self.regime == "TREND":
            new_trail = current_price - 200.0
            if new_trail > self.stop_loss:
                self.stop_loss = new_trail
                print(f">> MODE: Trending. Trailing Stop active at {self.stop_loss}")
        else:
            print(">> MODE: Ranging. Holding fixed Break-Even to avoid chop.")
            
        sys.stdout.flush()

if __name__ == "__main__":
    p = EmpirePrecision()
    while True:
        p.manage_risk(65800.0) # Simulation
        time.sleep(15)
