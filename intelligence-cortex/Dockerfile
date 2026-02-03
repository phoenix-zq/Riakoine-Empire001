FROM python:3.11-slim
RUN pip install pandas numpy
WORKDIR /app
COPY . .
CMD ["python", "market_mapper/market_mapper.py"]
