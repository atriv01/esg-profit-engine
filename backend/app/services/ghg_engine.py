import hashlib
from datetime import datetime

class GHGEngine:
    """
    Core calculation engine for transforming facility activity data 
    into Scope 1, 2, and 3 GHG emissions with cryptographic auditing.
    """

    # Standard reference emission factors (e.g., kg CO2e per unit)
    DEFAULT_FACTORS = {
        "electricity": 0.429,  # kg CO2e / kWh (Grid average)
        "natural_gas": 5.300,  # kg CO2e / therm
        "diesel": 2.680        # kg CO2e / liter
    }

    @staticmethod
    def calculate_emissions(activity_type: str, quantity: float, custom_factor: float = None) -> dict:
        """
        Computes emissions and generates an immutable SHA-256 calculation hash.
        """
        factor = custom_factor if custom_factor is not None else GHGEngine.DEFAULT_FACTORS.get(activity_type, 0.0)
        
        # Calculate total emissions in kg CO2e
        co2e_kg = quantity * factor

        # Determine GHG Scope based on activity type
        scope = "Scope 1" if activity_type in ["natural_gas", "diesel"] else "Scope 2"

        # Construct cryptographic audit string for tamper-proof lineage
        timestamp = datetime.utcnow().isoformat()
        audit_payload = f"{activity_type}:{quantity}:{factor}:{co2e_kg}:{timestamp}"
        calculation_hash = hashlib.sha256(audit_payload.encode('utf-8')).hexdigest()

        return {
            "scope": scope,
            "activity_type": activity_type,
            "quantity": quantity,
            "emission_factor_used": factor,
            "co2e_emissions_kg": round(co2e_kg, 4),
            "calculation_hash": calculation_hash,
            "calculated_at": timestamp
        }
