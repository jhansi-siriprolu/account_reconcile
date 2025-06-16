import pandas as pd
from src.reconcile import match_transactions

def test_multi_card_transaction():
    bank_df = pd.DataFrame([
        {'bank_id': 601, 'date': '2024-06-04', 'description': 'POS Counter 5 Card1', 'amount': 300, 'transaction_type': 'debit'},
        {'bank_id': 602, 'date': '2024-06-04', 'description': 'POS Counter 5 Card2', 'amount': 200, 'transaction_type': 'debit'},
    ])
    ledger_df = pd.DataFrame([
        {'ledger_id': 701, 'date': '2024-06-04', 'description': 'Counter 5', 'amount': 500, 'transaction_type': 'debit'},
    ])
    matches, _ = match_transactions(bank_df, ledger_df)
    matched_df = matches.to_frame().reset_index()
    bank_to_ledger = matched_df.groupby('level_0')['level_1'].apply(list).to_dict()
    ledger_target = 701
    for bank_id in [601, 602]:
        assert bank_id in bank_to_ledger
        assert ledger_target in bank_to_ledger[bank_id]