#pragma once
#include <string>
#include <iostream>

struct RiakoineTick {
    std::string symbol;
    double price;
    double volume;
    long timestamp;
    bool is_bid;
};

class MarketConnector {
public:
    virtual void connect() = 0;
    virtual void subscribe(const std::string& symbol) = 0;
    virtual ~MarketConnector() {}
};
