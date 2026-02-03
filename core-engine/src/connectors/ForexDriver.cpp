#include "../../include/connectors/MarketConnector.h"
#include <iostream>

class ForexDriver : public MarketConnector {
public:
    void connect() override {
        std::cout << "[FOREX] Listening on ZMQ Port 5555 (Waiting for MT5/FIX Bridge)..." << std::endl;
    }
    void subscribe(const std::string& symbol) override {
        std::cout << "[FOREX] Requesting flow for " << symbol << std::endl;
    }
};
