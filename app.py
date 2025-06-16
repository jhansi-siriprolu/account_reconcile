import streamlit as st
import pandas as pd
from src.reconcile import match_transactions

st.title("🧾 Grocers Account Reconciliation Tool")

st.sidebar.header("Upload Files")
bank_file = st.sidebar.file_uploader("Upload Bank Statement CSV", type=["csv"])
ledger_file = st.sidebar.file_uploader("Upload Ledger CSV", type=["csv"])

if bank_file and ledger_file:
    bank_df = pd.read_csv(bank_file)
    ledger_df = pd.read_csv(ledger_file)
    st.write("### Preview: Bank Data", bank_df.head())
    st.write("### Preview: Ledger Data", ledger_df.head())

    with st.spinner("Reconciling..."):
        matches, _ = match_transactions(bank_df, ledger_df)
        recon_output = []
        grouped = matches.to_frame().reset_index().groupby('level_0')['level_1'].apply(list)
        for i, (bank_idx, ledger_ids) in enumerate(grouped.items(), start=1):
            recon_output.append({
                'reconid': i,
                'bankid': str(bank_idx),
                'ledgerids': ','.join(map(str, ledger_ids))
            })
        recon_df = pd.DataFrame(recon_output)
        st.success("✅ Reconciliation Complete!")
        st.dataframe(recon_df)
        csv = recon_df.to_csv(index=False).encode('utf-8')
        st.download_button("Download Reconciliation Report", csv, "reconciliation_report.csv", "text/csv")
else:
    st.info("Upload both CSV files to start reconciliation.")