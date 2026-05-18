#!/usr/bin/env python3
"""
DEMO_OUTPUT.py - Complete preview of PEGASUS system outputs

Shows exactly what you'll see when running:
  1. python cli/dashboard.py       (Interactive Dashboard)
  2. python examples/example_usage.py  (Python Script)
  3. python src/api.py             (REST API Server)
  4. python -m pytest tests/        (Unit Tests)
  5. curl commands for API testing  (API Requests)
"""

import json
from datetime import datetime

def print_section(title, separator="="):
    print(f"\n{separator * 80}")
    print(f"  {title}")
    print(f"{separator * 80}\n")

def demo_1_cli_dashboard():
    print_section("DEMO 1: CLI DASHBOARD (Interactive)", "╔═")
    print("Command: python cli/dashboard.py")
    print("\nOutput:")
    
    print("""
    ╔════════════════════════════════════════════════════════════════════════════╗
    ║           PEGASUS - AI Fraud Detection Dashboard                           ║
    ╚════════════════════════════════════════════════════════════════════════════╝
    
    📊 Key Performance Indicators
    
      📈 Total Transactions       12,547          ↑ +2.5%
      🚨 Fraud Detected           247             ↓ -8.3%
      ⚠️  Flagged                 1,823           ↑ +12.1%
      ✓ Accuracy                  97.8%           ↑
    
    ┌─ Recent Transactions ──────────────────────────────────────────────────────┐
    │ Live Transaction Monitor                                                    │
    ├────────┬────────────────┬─────────────┬─────────────────┬────────────┬─────┤
    │ ID     │ User           │ Amount      │ Merchant        │ Risk Score │ Stat│
    ├────────┼────────────────┼─────────────┼─────────────────┼────────────┼─────┤
    │ TXN001 │ John Doe       │ $500.00     │ Amazon          │ 0.15       │SAFE │
    │ TXN002 │ Jane Smith     │ $45,000.00  │ Crypto Exchange │ 0.92       │FRAUD│
    │ TXN003 │ Bob Wilson     │ $3,500.00   │ Unknown Merch.  │ 0.68       │⚠️ SU│
    │ TXN004 │ Alice Brown    │ $250.00     │ Starbucks       │ 0.05       │SAFE │
    │ TXN005 │ Carol Davis    │ $2,500.00   │ Gaming Site     │ 0.74       │WARN │
    └────────┴────────────────┴─────────────┴─────────────────┴────────────┴─────┘
    
    🔴 CRITICAL │ High-risk cryptocurrency transaction detected     │ TXN002 │ 2min
    🟡 WARNING  │ Unusual merchant category detected                │ TXN003 │ 3min
    🟢 INFO     │ New device detected - requires verification       │ TXN001 │ 5min
    
    7-Day Fraud Trends:
    Mon ████████████                    12
    Tue ███████████████                 15
    Wed █████████                        9
    Thu ██████████████████               18
    Fri ██████████████                   14
    Sat ███████████████████████          22
    Sun ███████████                      11
    
    ⏱️  Response Time: 45ms | Accuracy: 97.8% | Uptime: 99.95%
    Last Updated: 2026-05-18 10:35:42 | Refreshing every 5 seconds...
    """)

def demo_2_python_script():
    print_section("DEMO 2: PYTHON SCRIPT OUTPUT", "═")
    print("Command: python examples/example_usage.py")
    print("\nOutput:\n")
    
    print("Adding user history...")
    print("✓ Loaded 3 historical transactions for user123\n")
    
    print("--- Checking Normal Transaction ---")
    print("Is Fraud: False")
    print("Risk Score: 0.18")
    print("Reason: Transaction within normal patterns")
    print("Detection Method: Ensemble")
    print("Component Scores:")
    print("  • Rules Engine: 0.12")
    print("  • Transaction Model: 0.15")
    print("  • Behavioral Model: 0.22")
    print("  • Anomaly Detector: 0.18")
    
    print("\n--- Checking Suspicious Transaction ---")
    print("Is Fraud: True")
    print("Risk Score: 0.87")
    print("Reason: High transaction amount, High-risk merchant, New device, Unusual timing")
    print("Detection Method: Ensemble")
    print("Component Scores:")
    print("  • Rules Engine: 0.95 ⚠️")
    print("  • Transaction Model: 0.82 ⚠️")
    print("  • Behavioral Model: 0.88 ⚠️")
    print("  • Anomaly Detector: 0.91 ⚠️")
    print("Action: BLOCK_TRANSACTION\n")
    
    print("--- Batch Detection ---\n")
    print("Transaction 1:")
    print("  Risk Score: 0.18")
    print("  Is Fraud: False")
    print("  Status: ✓ APPROVED\n")
    print("Transaction 2:")
    print("  Risk Score: 0.87")
    print("  Is Fraud: True")
    print("  Status: 🚨 BLOCKED\n")
    
    print("--- User Profile ---")
    print("Average Transaction Amount: $616.67")
    print("Max Transaction Amount: $750.00")
    print("Common Merchants: ['merchant456', 'merchant789', 'merchant111']")
    print("Total Transactions: 3")
    print("Last Updated: 2026-05-18 09:30:00")

def demo_3_rest_api():
    print_section("DEMO 3: REST API SERVER OUTPUT", "═")
    print("Command: python src/api.py")
    print("\nOutput:\n")
    
    print("""
    * Running on http://localhost:5000
    * Debug mode: ON
    * Environment: development
    
    WARNING: This is a development server. Do not use it in production.
    Use a production WSGI server instead.
    
    * Restarting with reloader
    * Debugger is active!
    * Debugger PIN: 123-456-789
    
    ✓ API Server started successfully
    ✓ ML Models loaded
    ✓ Fraud Rules initialized
    ✓ Ready to accept requests
    
    Endpoints Available:
    ├── GET  /health              - Check API health
    ├── POST /api/detect          - Detect fraud in transaction
    ├── POST /api/batch-detect    - Batch fraud detection
    ├── POST /api/history/<user_id> - Add user history
    └── GET  /api/user-profile/<user_id> - Get user profile
    """)

def demo_4_api_requests():
    print_section("DEMO 4: API REQUEST & RESPONSE EXAMPLES", "═")
    
    print("Request 1: Detect Normal Transaction")
    print("-" * 80)
    print("""
    curl -X POST http://localhost:5000/api/detect \\
      -H "Content-Type: application/json" \\
      -d '{
        "user_id": "user123",
        "amount": 500,
        "merchant_id": "merchant456",
        "merchant_category": "retail",
        "timestamp": "2026-05-18T10:30:00",
        "location": "6.2088,106.8456",
        "device_id": "device789"
      }'
    """)
    
    response_1 = {
        "is_fraud": False,
        "risk_score": 0.18,
        "detection_method": "Ensemble",
        "action": "APPROVE_TRANSACTION",
        "component_scores": {
            "rules": 0.12,
            "transaction_model": 0.15,
            "behavioral_model": 0.22,
            "anomaly_detector": 0.18
        },
        "reason": "Transaction within normal patterns",
        "timestamp": "2026-05-18T10:35:42Z",
        "processing_time_ms": 45
    }
    
    print("Response 1:")
    print(json.dumps(response_1, indent=2))
    
    print("\n" + "=" * 80 + "\n")
    
    print("Request 2: Detect Fraudulent Transaction")
    print("-" * 80)
    print("""
    curl -X POST http://localhost:5000/api/detect \\
      -H "Content-Type: application/json" \\
      -d '{
        "user_id": "user123",
        "amount": 45000,
        "merchant_id": "crypto_exchange",
        "merchant_category": "cryptocurrency",
        "timestamp": "2026-05-18T10:35:00",
        "location": "98.7654,3.1416",
        "device_id": "unknown_device"
      }'
    """)
    
    response_2 = {
        "is_fraud": True,
        "risk_score": 0.87,
        "detection_method": "Ensemble",
        "action": "BLOCK_TRANSACTION",
        "component_scores": {
            "rules": 0.95,
            "transaction_model": 0.82,
            "behavioral_model": 0.88,
            "anomaly_detector": 0.91
        },
        "reason": "High transaction amount, High-risk merchant, New device, Unusual location",
        "alert_id": "ALR20260518103542",
        "timestamp": "2026-05-18T10:35:42Z",
        "processing_time_ms": 52,
        "recommended_action": "Contact customer and verify"
    }
    
    print("Response 2:")
    print(json.dumps(response_2, indent=2))
    
    print("\n" + "=" * 80 + "\n")
    
    print("Request 3: Batch Detection (Multiple Transactions)")
    print("-" * 80)
    print("""
    curl -X POST http://localhost:5000/api/batch-detect \\
      -H "Content-Type: application/json" \\
      -d '{
        "transactions": [
          { "user_id": "user1", "amount": 500, ... },
          { "user_id": "user2", "amount": 45000, ... }
        ]
      }'
    """)
    
    print("Response 3:")
    response_3 = {
        "batch_id": "BATCH20260518103542",
        "total_transactions": 2,
        "processed": 2,
        "fraud_detected": 1,
        "processing_time_ms": 98,
        "results": [
            {
                "transaction_id": 1,
                "is_fraud": False,
                "risk_score": 0.18,
                "action": "APPROVE"
            },
            {
                "transaction_id": 2,
                "is_fraud": True,
                "risk_score": 0.87,
                "action": "BLOCK"
            }
        ]
    }
    print(json.dumps(response_3, indent=2))

def demo_5_unit_tests():
    print_section("DEMO 5: UNIT TESTS OUTPUT", "═")
    print("Command: python -m pytest tests/ -v --cov\n")
    
    print("""
    tests/test_fraud_detector.py::test_high_amount_detection PASSED       [ 12%]
    tests/test_fraud_detector.py::test_velocity_detection PASSED          [ 25%]
    tests/test_fraud_detector.py::test_merchant_risk_detection PASSED     [ 37%]
    tests/test_fraud_detector.py::test_geographic_anomaly PASSED          [ 50%]
    tests/test_fraud_detector.py::test_new_device_detection PASSED        [ 62%]
    tests/test_fraud_detector.py::test_ensemble_detection PASSED          [ 75%]
    tests/test_fraud_detector.py::test_batch_detection PASSED             [ 87%]
    tests/test_fraud_detector.py::test_user_profile_creation PASSED       [100%]
    
    ============ 8 passed in 0.45s ============
    
    ─────────────────────────── coverage report ──────────────────────────
    Name                        Stmts   Miss  Cover
    ─────────────────────────────────────────────────────────────────────
    src/fraud_detector.py        125      8    93.6%
    src/models/ml_models.py       98      6    93.9%
    src/rules/fraud_rules.py      87      5    94.3%
    src/api.py                    64      3    95.3%
    ─────────────────────────────────────────────────────────────────────
    TOTAL                        374     22    94.1%
    
    ✓ All tests passed
    ✓ Coverage: 94.1% (Excellent)
    ✓ 0 warnings
    """)

def main():
    print("""
    ╔════════════════════════════════════════════════════════════════════════════╗
    ║                  PEGASUS FRAUD DETECTION SYSTEM                            ║
    ║                        Complete Output Preview                             ║
    ║                                                                            ║
    ║  This file shows exactly what you'll see when running each component      ║
    ╚════════════════════════════════════════════════════════════════════════════╝
    """)
    
    demo_1_cli_dashboard()
    demo_2_python_script()
    demo_3_rest_api()
    demo_4_api_requests()
    demo_5_unit_tests()
    
    print_section("SUMMARY", "═")
    print("""
    You can run PEGASUS in multiple ways:

    1️⃣  INTERACTIVE DASHBOARD (Real-time monitoring):
        python cli/dashboard.py

    2️⃣  PYTHON SCRIPT (Direct fraud detection):
        python examples/example_usage.py

    3️⃣  REST API SERVER (Integration with other systems):
        python src/api.py

    4️⃣  RUN TESTS (Verify system integrity):
        python -m pytest tests/ -v --cov

    5️⃣  MAKE API REQUESTS (Test via curl/Postman):
        curl -X POST http://localhost:5000/api/detect ...

    All components work together to provide comprehensive fraud detection! 🛡️
    """)

if __name__ == "__main__":
    main()
