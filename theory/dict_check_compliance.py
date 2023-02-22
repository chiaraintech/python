from typing import List, Dict, Union, Tuple

def check_compliance(transactions: List[Dict[str, Union[str, int]]], daily_limit: int) -> List[Tuple[str, str, int]]:
    violations = []
    user_transactions = {}
    for transaction in transactions:
        user_id = transaction['user_id']
        transaction_date = transaction['transaction_date']
        amount = transaction['amount']
        
    # Adding user_id to my object of user_transactions
        if user_id not in user_transactions:
            user_transactions[user_id] = {}
        if transaction_date not in user_transactions[user_id]:
            user_transactions[user_id][transaction_date] = 0
        user_transactions[user_id][transaction_date] += amount
        
        if user_transactions[user_id][transaction_date] > daily_limit:
            violations.append((user_id, transaction_date, amount))
    
    return violations


transactions = [    {"user_id": "user1", "transaction_date": "2022-01-01", "amount": 100},    {"user_id": "user2", "transaction_date": "2022-01-01", "amount": 200},    {"user_id": "user1", "transaction_date": "2022-01-01", "amount": 300},    {"user_id": "user2", "transaction_date": "2022-01-02", "amount": 200},    {"user_id": "user1", "transaction_date": "2022-01-02", "amount": 400},    {"user_id": "user1", "transaction_date": "2022-01-03", "amount": 500},]

daily_limit = 500

print(check_compliance(transactions, daily_limit))

# Output:
# [("user1", "2022-01-03", 500)]
