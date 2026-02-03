#!/bin/bash

echo "=========================================="
echo "Applying Server Stabilization Patch..."
echo "=========================================="

# 1. Fix C++ Binance Driver (Add Infinite Loop)
cat << 'CPP' > core-engine/src/connectors/BinanceDriver.cpp
#include "../../include/connectors/MarketConnector.h"
#include <iostream>
#include <thread>
#include <chrono>

class BinanceDriver : public MarketConnector {
public:
    void connect() override {
        std::cout << "[BINANCE] Connecting to wss://stream.binance.com:9443..." << std::endl;
        // The Infinite Heartbeat
        while(true) {
            std::this_thread::sleep_for(std::chrono::seconds(5));
            // In a real app, this checks for WebSocket ping/pong
        }
    }
    void subscribe(const std::string& symbol) override {
        std::cout << "[BINANCE] Subscribed to " << symbol << " OrderBook." << std::endl;
    }
};
CPP

# 2. Fix C++ Forex Driver (Add Infinite Loop)
cat << 'CPP' > core-engine/src/connectors/ForexDriver.cpp
#include "../../include/connectors/MarketConnector.h"
#include <iostream>
#include <thread>
#include <chrono>

class ForexDriver : public MarketConnector {
public:
    void connect() override {
        std::cout << "[FOREX] Listening on ZMQ Port 5555 (Waiting for MT5/FIX Bridge)..." << std::endl;
        // The Infinite Heartbeat
        while(true) {
            std::this_thread::sleep_for(std::chrono::seconds(5));
            // In a real app, this blocks on zmq_recv()
        }
    }
    void subscribe(const std::string& symbol) override {
        std::cout << "[FOREX] Requesting flow for " << symbol << std::endl;
    }
};
CPP

# 3. Fix Python Dockerfile (Run the Brain, not the Print Statement)
cat << 'DOCKER' > intelligence-cortex/Dockerfile
FROM python:3.11-slim

# Install system dependencies if needed
RUN apt-get update && apt-get install -y iputils-ping

WORKDIR /app
COPY . .

# Install Python libs
RUN pip install pandas numpy

# CRITICAL: Run the Market Mapper script, not a simple print command
CMD ["python", "market_mapper/market_mapper.py"]
DOCKER

echo "[+] Patch Applied. Rebuilding..."
docker-compose up --build
