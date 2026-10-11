from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from services.anomaly_engine import AnomalyEngine
from services.rfp_rag import RFPRagPipeline

router = APIRouter(prefix="/api/v1/profit", tags=["Profit Engine"])

class AnomalyRequest(BaseModel):
    historical_readings: list[float]
    current_reading: float
    threshold_multiplier: float | None = 1.25

class RFPRequest(BaseModel):
    query: str

@router.post("/anomaly-check")
def check_energy_anomaly(payload: AnomalyRequest):
    """
    Checks utility consumption for spikes and calculates OPEX savings opportunities.
    """
    try:
        result = AnomalyEngine.detect_anomaly(
            historical_readings=payload.historical_readings,
            current_reading=payload.current_reading,
            threshold_multiplier=payload.threshold_multiplier
        )
        return {"status": "success", "data": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/rfp-query")
def query_rfp_metrics(payload: RFPRequest):
    """
    Queries verified ESG metrics to generate high-win-rate procurement responses.
    """
    try:
        pipeline = RFPRagPipeline()
        result = pipeline.query_knowledge_base(query=payload.query)
        return {"status": "success", "data": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
