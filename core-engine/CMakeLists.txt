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
