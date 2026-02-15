
import os
import threading
import time
import json
import random
from datetime import datetime

def gatekeeper():
    print("\033[1;33m🔒 RIAKOINE EMPIRE ACCESS CONTROL 🔒\033[0m")
    key = "700"
    attempt = input("Enter Access Key: ")
    if attempt == key:
        print("\033[1;32m✅ Access Granted. Welcome Rafiki.\033[0m")
        return True
    else:
        print("\033[1;31m❌ Access Denied.\033[0m")
        return False

def elint_scanner():
    while True:
        signal = random.randint(-115, -60)
        timestamp = datetime.now().strftime("%H:%M:%S")
        with open("ngong_hills_log.csv", "a") as log:
            log.write(f"{timestamp},{signal}dBm,Scanning...\n")
        time.sleep(300)

if __name__ == "__main__":
    if gatekeeper():
        # Start ELINT
        t = threading.Thread(target=elint_scanner)
        t.daemon = True
        t.start()
        print("📡 ELINT Scanner Active (Background)...")
        
        # Try to launch main app if it exists, else just log
        try:
            import main
            print("🚀 Launching Riakoine Forge...")
            main.RiakoineApp().run()
        except:
            print("⚠️ Main App UI not found, running in Console Mode.")
            while True:
                time.sleep(1)
