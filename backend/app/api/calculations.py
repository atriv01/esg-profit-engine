from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from services.ghg_engine import GHGEngine

router = APIRouter(prefix="/api/v1/calculations", tags=["GHG Calculations"])

class CalculationRequest(BaseModel):
    activity_type: str  # e.g., 'electricity', 'natural_gas', 'diesel'
    quantity: float     # e.g., 1500.0
    custom_factor: float | None = None

@router.post("/emissions")
def calculate_facility_emissions(payload: CalculationRequest):
    """
    API endpoint to compute Scope 1 or Scope 2 emissions 
    and return audit-ready SHA-256 calculation hashes.
    """
    try:
        result = GHGEngine.calculate_emissions(
            activity_type=payload.activity_type,
            quantity=payload.quantity,
            custom_factor=payload.custom_factor
        )
        return {
            "status": "success",
            "data": result
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
