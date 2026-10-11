class AnomalyEngine:
    """
    Detects utility consumption spikes and estimates OPEX reduction targets.
    """

    @staticmethod
    def detect_anomaly(historical_readings: list[float], current_reading: float, threshold_multiplier: float = 1.25) -> dict:
        """
        Compares current utility reading against rolling historical baseline 
        to catch energy spikes and compute financial savings potential.
        """
        if not historical_readings:
            return {
                "is_anomaly": False,
                "baseline_average": 0.0,
                "potential_opex_savings_usd": 0.0
            }
        
        baseline_avg = sum(historical_readings) / len(historical_readings)
        threshold = baseline_avg * threshold_multiplier
        is_anomaly = current_reading > threshold
        
        # Estimate OPEX savings target (targeting 12.5% reduction on excess utility costs)
        excess_consumption = max(0.0, current_reading - baseline_avg)
        estimated_savings = excess_consumption * 0.125 * 0.15  # assuming $0.15 per unit cost

        return {
            "is_anomaly": is_anomaly,
            "current_reading": current_reading,
            "baseline_average": round(baseline_avg, 2),
            "threshold": round(threshold, 2),
            "potential_opex_savings_usd": round(estimated_savings, 2)
        }
