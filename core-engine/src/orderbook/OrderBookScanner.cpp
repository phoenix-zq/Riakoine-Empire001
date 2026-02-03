#include <iostream>
#include <vector>

struct PriceLevel { double price; double volume; };

class OrderBookScanner {
public:
    void update_level(double price, double volume) {
        std::cout << "[SCANNER] Update: " << price << std::endl;
    }
};
