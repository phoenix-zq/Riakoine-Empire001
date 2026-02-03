FROM gcc:latest
WORKDIR /app
COPY . .
RUN mkdir -p build && cd build && cmake .. && make
CMD ["./build/riakoine_engine"]
