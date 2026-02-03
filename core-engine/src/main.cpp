#include <iostream>
#include <string>

void execute_hybrid_logic(std::string regime, double price) {
    std::cout << "[ENGINE] Current Regime: " << regime << std::endl;
    if (regime == "TREND") {
        std::cout << "[EXECUTION] Strategy: Institutional Trailing Active." << std::endl;
    } else {
        std::cout << "[EXECUTION] Strategy: Scalp Mode (Fixed BE) Active." << std::endl;
    }
}

int main() {
    // Integration: The Engine reads the 'FINAL BIAS' from the Mapper
    std::string current_regime = "TREND"; // Mocked from Mapper
    execute_hybrid_logic(current_regime, 65800.0);
    return 0;
}
