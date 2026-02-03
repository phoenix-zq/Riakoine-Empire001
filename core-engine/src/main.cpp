#include <iostream>
#include <thread>
#include <vector>
#include "../include/connectors/MarketConnector.h"
#include "connectors/BinanceDriver.cpp"
#include "connectors/ForexDriver.cpp"

int main() {
    std::cout << "Starting Riakoine Empire [Institutional Engine]..." << std::endl;

    BinanceDriver crypto_feed;
    ForexDriver forex_feed;

    // Connect in parallel threads
    std::thread t1([&](){ crypto_feed.connect(); });
    std::thread t2([&](){ forex_feed.connect(); });

    crypto_feed.subscribe("BTCUSDT");
    forex_feed.subscribe("XAUUSD"); 

    std::cout << "[SYSTEM] Dual-Feed Active. Aggregating Liquidity..." << std::endl;

    t1.join();
    t2.join();
    return 0;
}
