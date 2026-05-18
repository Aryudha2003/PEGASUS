"""
Example usage of PEGASUS Fraud Detection System
"""

from datetime import datetime
from src.fraud_detector import FraudDetector

# Initialize the detector
detector = FraudDetector(model_type='ensemble')

# Example: Add historical transactions for a user to build their profile
historical_transactions = [
    {
        'user_id': 'user123',
        'amount': 500,
        'merchant_id': 'merchant456',
        'merchant_category': 'retail',
        'timestamp': '2026-05-10T10:30:00',
        'location': '6.2088,106.8456',
        'device_id': 'device789'
    },
    {
        'user_id': 'user123',
        'amount': 750,
        'merchant_id': 'merchant789',
        'merchant_category': 'restaurant',
        'timestamp': '2026-05-11T19:00:00',
        'location': '6.2088,106.8456',
        'device_id': 'device789'
    },
    # Add more transactions...
]

print("Adding user history...")
detector.add_user_history('user123', historical_transactions)

# Example: Check a normal transaction
print("\n--- Checking Normal Transaction ---")
normal_transaction = {
    'user_id': 'user123',
    'amount': 600,
    'merchant_id': 'merchant111',
    'merchant_category': 'retail',
    'timestamp': datetime.now().isoformat(),
    'location': '6.2088,106.8456',
    'device_id': 'device789'
}

result = detector.detect(normal_transaction)
print(f"Is Fraud: {result['is_fraud']}")
print(f"Risk Score: {result['risk_score']:.2f}")
print(f"Reason: {result['reason']}")
print(f"Detection Method: {result['detection_method']}")

# Example: Check a suspicious transaction
print("\n--- Checking Suspicious Transaction ---")
suspicious_transaction = {
    'user_id': 'user123',
    'amount': 50000,
    'merchant_id': 'merchant_crypto',
    'merchant_category': 'cryptocurrency',
    'timestamp': datetime.now().isoformat(),
    'location': '6.2088,106.8456',
    'device_id': 'device999'  # Unknown device
}

result = detector.detect(suspicious_transaction)
print(f"Is Fraud: {result['is_fraud']}")
print(f"Risk Score: {result['risk_score']:.2f}")
print(f"Reason: {result['reason']}")
print(f"Component Scores: {result['component_scores']}")

# Example: Batch detection
print("\n--- Batch Detection ---")
transactions = [normal_transaction, suspicious_transaction]
batch_results = detector.batch_detect(transactions)

for i, result in enumerate(batch_results, 1):
    print(f"\nTransaction {i}:")
    print(f"  Risk Score: {result['risk_score']:.2f}")
    print(f"  Is Fraud: {result['is_fraud']}")

# Example: Get user profile
print("\n--- User Profile ---")
profile = detector.get_user_profile('user123')
if profile:
    print(f"Average Transaction Amount: ${profile['avg_amount']:.2f}")
    print(f"Max Transaction Amount: ${profile['max_amount']:.2f}")
    print(f"Common Merchants: {profile['common_merchants']}")
    print(f"Total Transactions: {profile['transaction_count']}")
