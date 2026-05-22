from fastapi import FastAPI
from datetime import datetime
import random

app = FastAPI()

@app.get("/")
def root():
    return {"status": "live", "message": "World Cup Arbitrage Agent"}

@app.get("/v1/predict")
def predict():
    return {
        "timestamp": datetime.now().isoformat(),
        "matches_today": random.randint(1, 4),
        "fx_flows_usd": {
            "USD": 5850000,
            "MXN": 2340000,
            "CAD": 1755000
        },
        "arbitrage_opportunity": "Buy USD, sell MXN",
        "spread_bps": 320
    }
