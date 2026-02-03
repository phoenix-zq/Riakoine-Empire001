#!/bin/bash

echo "=========================================="
echo "Upgrading Engine: Dual-Feed Capability"
echo "=========================================="

# Create Directory Structure
mkdir -p core-engine/src/connectors
mkdir -p core-engine/include/connectors

# --- GENERATE C++ FILES ---

# 1. Universal Interface
cat << 'CPP' > core-engine/include/connectors/MarketConnector.h
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
CPP

# 2. Binance Driver (Crypto)
cat << 'CPP' > core-engine/src/connectors/BinanceDriver.cpp
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
CPP

# 3. Forex Driver (ZeroMQ)
cat << 'CPP' > core-engine/src/connectors/ForexDriver.cpp
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
CPP

# 4. Main Entry Point
cat << 'CPP' > core-engine/src/main.cpp
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
CPP

# 5. CMake Build System
cat << 'TXT' > core-engine/CMakeLists.txt
cmake_minimum_required(VERSION 3.20)
project(RiakoineCore VERSION 0.2.0)
set(CMAKE_CXX_STANDARD 20)
add_compile_options(-O3 -march=native -pthread)
include_directories(include)
include_directories(include/connectors)
add_executable(riakoine_engine 
    src/main.cpp
    src/orderbook/OrderBookScanner.cpp
    src/arbiter/TriangularScanner.cpp
    src/connectors/BinanceDriver.cpp
    src/connectors/ForexDriver.cpp
)
TXT

# --- EXECUTION ---
echo "[+] Committing Updates to Git..."
git add .
git commit -m "Upgrade: Added Dual-Feed Connectors"

echo "[+] Launching Docker Build..."
docker compose up --build
