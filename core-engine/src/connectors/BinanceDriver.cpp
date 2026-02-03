#include "../../include/connectors/MarketConnector.h"
#include <iostream>

class BinanceDriver : public MarketConnector {
public:
    void connect() override {
        std::cout << "[BINANCE] Connecting to wss://stream.binance.com:9443..." << std::endl;
    }
    void subscribe(const std::string& symbol) override {
        std::cout << "[BINANCE] Subscribed to " << symbol << " OrderBook." << std::endl;
    }
};
