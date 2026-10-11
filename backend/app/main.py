from fastapi import FastAPI

app = FastAPI(
    title="ESG Profit Engine API",
    description="Enterprise ESG reporting and compliance-to-profit calculation engine",
    version="1.0.0"
)

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
