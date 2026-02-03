#include <iostream>
#include <vector>

struct Level { double price; double vol; };

class InstitutionalOBI {
public:
    double get_imbalance(const std::vector<Level>& bids, const std::vector<Level>& asks) {
        double b_vol = 0, a_vol = 0;
        // Focus only on the 'inner' market (top 5 levels) where the real fight happens
        for(int i=0; i<5 && i<bids.size(); ++i) b_vol += bids[i].vol;
        for(int i=0; i<5 && i<asks.size(); ++i) a_vol += asks[i].vol;
        return (b_vol - a_vol) / (b_vol + a_vol);
    }
};

int main() {
    std::cout << "[ENGINE] High-Frequency OBI Logic Online." << std::endl;
    InstitutionalOBI scanner;
    // Mock Data: Heavy Buy Side Presence
    std::vector<Level> bids = {{65000, 45.5}, {64995, 30.0}};
    std::vector<Level> asks = {{65005, 5.2}, {65010, 4.8}};
    
    double imbalance = scanner.get_imbalance(bids, asks);
    std::cout << "[OBI] Ratio: " << imbalance << (imbalance > 0.7 ? " (STRONG LONG BIAS)" : "") << std::endl;
    return 0;
}
