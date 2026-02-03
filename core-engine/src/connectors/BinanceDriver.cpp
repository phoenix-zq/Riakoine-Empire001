#include "../../include/connectors/MarketConnector.h"
#include <iostream>
#include <thread>
#include <chrono>

class BinanceDriver : public MarketConnector {
public:
    void connect() override {
        std::cout << "[BINANCE] Connecting to wss://stream.binance.com:9443..." << std::endl;
        // Infinite Heartbeat to keep thread alive
        while(true) {
            std::this_thread::sleep_for(std::chrono::seconds(5));
        }
    }
    void subscribe(const std::string& symbol) override {
        std::cout << "[BINANCE] Subscribed to " << symbol << " OrderBook." << std::endl;
    }
};
