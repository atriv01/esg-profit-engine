from fastapi import FastAPI
from api.calculations import router as calculations_router
from api.profit_engine import router as profit_router

app = FastAPI(
    title="ESG Profit Engine API",
    description="Enterprise ESG reporting and compliance-to-profit calculation engine",
    version="1.0.0"
)

# Include API routers
app.include_router(calculations_router)
app.include_router(profit_router)

@app.get("/")
def read_root():
    return {
        "status": "online",
        "platform": "ESG Profit Engine",
        "version": "1.0.0",
        "compliance": "CSRD / ISSB Ready"
    }

@app.get("/health")
def health_check():
    return {"database": "connected", "cache": "connected"}
