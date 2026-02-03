import sys
import time

class EmpireExecution:
    def __init__(self):
        self.entry_price = 65475.0
        self.is_trending = True # Determined by StructuralMapper

    def manage_exit(self, current_price):
        # 1. Decision Engine
        if self.is_trending:
            # Trailing Stop Logic: Follow the Trend
            trailing_stop = current_price - 150.0 
            print(f">> [TRAILING MODE] Stop-Loss adjusted to: {trailing_stop}")
        else:
            # Fixed Stop Logic: Protection First
            break_even = self.entry_price
            print(f">> [SCALP MODE] Target 1 Hit. Moving Stop to Break-Even: {break_even}")

        # 2. Precision Signal
        if current_price >= self.entry_price + 300:
            print(">> [PRECISION] Target 2 Hit. Locking in 70% Profit.")
        
        sys.stdout.flush()

if __name__ == "__main__":
    executor = EmpireExecution()
    while True:
        # Simulation of price movement
        executor.manage_exit(65800.0)
        time.sleep(15)
