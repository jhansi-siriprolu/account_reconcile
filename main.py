import pandas as pd
from src.reconcile import match_transactions, evaluate_model

bank = pd.read_csv('data/bank_statements.csv')
ledger = pd.read_csv('data/store_ledger.csv')

matches, features = match_transactions(bank, ledger)
output = []
grouped = matches.to_frame().reset_index().groupby('level_0')['level_1'].apply(list)
for i, (bank_idx, ledger_ids) in enumerate(grouped.items(), start=1):
    output.append({
        'reconid': i,
        'bankid': str(bank_idx),
        'ledgerids': ','.join(map(str, ledger_ids))
    })
recon_df = pd.DataFrame(output)
recon_df.to_csv('output/reconciliation_report.csv', index=False)
print("✅ Reconciliation completed. Output saved to 'output/reconciliation_report.csv'.")