cmake_minimum_required(VERSION 3.20)
project(RiakoineCore VERSION 0.1.0)
set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED True)
add_compile_options(-O3 -march=native -funroll-loops -Wall)
include_directories(include)
# Compile both the OrderBook Scanner and Arbiter
add_executable(riakoine_engine 
    src/orderbook/OrderBookScanner.cpp
    src/arbiter/TriangularScanner.cpp
)
