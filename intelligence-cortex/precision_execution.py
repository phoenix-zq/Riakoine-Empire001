import sys
import time

class EmpirePrecision:
    def __init__(self):
        self.entry_price = 0
        self.stop_loss = 0
        self.regime = "RANGE" # Default

    def manage_trade(self, current_price, entry, mode):
        # 1. First Target: Move to Break-Even (BE)
        # Institutional Rule: If +10 pips, move to BE+1 to cover commissions
        if current_price >= entry + 100 and self.stop_loss < entry:
            self.stop_loss = entry + 10
            print(f">> [SAFETY] Target 1 Hit. Stop moved to BREAK-EVEN.")

        # 2. Hybrid Decision: Trail or Hold
        if mode == "TREND":
            # Trailing: Follow the 50% (CE) of the most recent FVG
            new_stop = current_price - 150.0 
            if new_stop > self.stop_loss:
                self.stop_loss = new_stop
                print(f">> [HYBRID] Trending detected. Trailing SL to: {self.stop_loss}")
        else:
            print(f">> [HYBRID] Ranging detected. Holding Fixed BE to protect capital.")
        
        sys.stdout.flush()

if __name__ == "__main__":
    manager = EmpirePrecision()
    # Simulated Trade
    manager.manage_trade(65600, 65475, "TREND")
