PAYMENT_TRANSACTIONS = {}


def save_transaction(txn_id, order_id):
    PAYMENT_TRANSACTIONS[txn_id] = order_id


def get_transaction(txn_id):
    return PAYMENT_TRANSACTIONS.get(txn_id)


def transaction_used(txn_id):
    return txn_id in PAYMENT_TRANSACTIONS


def all_transactions():
    return PAYMENT_TRANSACTIONS.items()
