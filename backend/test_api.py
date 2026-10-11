from fastapi.testclient import TestClient
import sys
import os

# Ensure app module can be imported correctly
sys.path.append(os.path.join(os.path.dirname(__file__), "app"))
from main import app

client = TestClient(app)

def test_api_endpoints():
    print("🚀 Running ESG Profit Engine API Verification Suite...\n")

    # 1. Test Root Endpoint
    response = client.get("/")
    assert response.status_code == 200
    print("✓ Root Endpoint Passed:", response.json())

    # 2. Test Health Check
    response = client.get("/health")
    assert response.status_code == 200
    print("✓ Health Check Passed:", response.json())

    # 3. Test GHG Calculation Engine
    calc_payload = {
        "activity_type": "electricity",
        "quantity": 2500.0
    }
    response = client.post("/api/v1/calculations/emissions", json=calc_payload)
    assert response.status_code == 200
    calc_data = response.json()["data"]
    assert calc_data["scope"] == "Scope 2"
    assert "calculation_hash" in calc_data
    print("✓ GHG Emissions Calculation Passed (SHA-256 Hash Generated):", calc_data["calculation_hash"][:16] + "...")

    # 4. Test Energy Anomaly Detection
    anomaly_payload = {
        "historical_readings": [1200.0, 1250.0, 1180.0, 1220.0],
        "current_reading": 1650.0
    }
    response = client.post("/api/v1/profit/anomaly-check", json=anomaly_payload)
    assert response.status_code == 200
    anomaly_data = response.json()["data"]
    assert anomaly_data["is_anomaly"] is True
    print("✓ Energy Anomaly Detection Passed (Potential OPEX Savings: $" + str(anomaly_data["potential_opex_savings_usd"]) + ")")

    # 5. Test RFP RAG Pipeline Query
    rfp_payload = {
        "query": "What is the average utility OPEX reduction?"
    }
    response = client.post("/api/v1/profit/rfp-query", json=rfp_payload)
    assert response.status_code == 200
    rfp_data = response.json()["data"]
    assert rfp_data["matched_evidence_count"] > 0
    print("✓ RFP RAG Pipeline Query Passed:", rfp_data["suggested_rfp_response"])

    print("\n✨ All platform backend tests passed successfully!")

if __name__ == "__main__":
    test_api_endpoints()
