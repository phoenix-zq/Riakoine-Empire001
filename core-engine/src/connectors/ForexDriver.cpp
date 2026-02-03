#include "../../include/connectors/MarketConnector.h"
#include <iostream>
#include <thread>
#include <chrono>

class ForexDriver : public MarketConnector {
public:
    void connect() override {
        std::cout << "[FOREX] Listening on ZMQ Port 5555 (Waiting for MT5/FIX Bridge)..." << std::endl;
        // Infinite Heartbeat to keep thread alive
        while(true) {
            std::this_thread::sleep_for(std::chrono::seconds(5));
        }
    }
    void subscribe(const std::string& symbol) override {
        std::cout << "[FOREX] Requesting flow for " << symbol << std::endl;
    }
};
