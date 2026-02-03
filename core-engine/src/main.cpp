#include <iostream>
#include <unistd.h>

class InstitutionalFilter {
public:
    bool is_in_buy_zone(double price, double monthly_open) {
        // Institutional Rule: Only long if price is below Monthly Open (Discount) 
        // or retesting it from above.
        return price >= monthly_open; 
    }
};

int main() {
    double current_price = 65900.00;
    double monthly_open = 65800.00; // Received from StructuralMapper
    
    InstitutionalFilter filter;
    std::cout << "[ENGINE] HTF Filter Active. Checking Monthly Bias..." << std::endl;

    while(true) {
        bool bias_confirmed = filter.is_in_buy_zone(current_price, monthly_open);
        
        if(bias_confirmed) {
            std::cout << "[BIAS] BULLISH: Price is above Monthly Open. OBI Execution Enabled." << std::endl;
        } else {
            std::cout << "[BIAS] BEARISH: Price below HTF level. Blocking Long Signals." << std::endl;
        }
        sleep(10);
    }
    return 0;
}
