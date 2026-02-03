#include <iostream>

struct Trade {
    double entry;
    double stop_loss;
    bool trend_mode;
};

void update_exit_strategy(Trade& t, double current_price) {
    if (t.trend_mode) {
        // Institutional Trailing: Move SL to the last 4H Swing Low
        t.stop_loss = current_price - 100.0; 
        std::cout << "[ENGINE] Trailing SL Updated: " << t.stop_loss << std::endl;
    } else {
        // Scalp Mode: Protect Capital
        t.stop_loss = t.entry; // Move to Break-Even
        std::cout << "[ENGINE] Scalp Mode: Stop moved to Break-Even." << std::endl;
    }
}

int main() {
    Trade myTrade = {65475.0, 65300.0, true}; // Starting in Trend Mode
    std::cout << "[ENGINE] Precision Execution Active." << std::endl;
    
    // Simulate price move
    update_exit_strategy(myTrade, 65850.0);
    return 0;
}
