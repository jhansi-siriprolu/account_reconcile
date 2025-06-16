# Grocers Reconciliation

Automated account reconciliation using RecordLinkage with classification, evaluation, and Streamlit support.

# 🧾 Grocers Reconciliation System

A smart Python-based tool to **reconcile daily bank statements and ledger entries** from a grocery outlet. Detects mismatches, missing transactions, and potential fraud using rule-based logic and fuzzy matching.

---

## 🚀 Features

### 🔍 Smart Transaction Reconciliation
- Reconciles **bank transactions** and **ledger entries** using `transaction_id` extracted from ledger descriptions.
- Groups and matches **multi-card payments** and **multi-item purchases** into a single logical transaction using smart grouping and amount aggregation.

### ✅ Fraud and Error Detection
- Reports:
  - ✅ **Matched Transactions**
  - ⚠️ **Missing Transaction IDs** in ledger entries
  - ❌ **Amount Mismatches** between ledger and bank
  - 🕵️ **Unmatched Ledger Entries** (potential fraud/store theft)
- Ignores:
  - Legitimate **refunds** (negative amount without transaction ID)
  - **Store expenses** (positive entries without transaction ID)

### 🤖 Fallback Matching with Record Linkage
- Uses fuzzy record matching for transactions without `transaction_id` using:
  - Date similarity
  - Amount similarity
  - Counter/store keywords

### 📊 Streamlit Dashboard
- Interactive UI for:
  - Uploading `bank.csv` and `ledger.csv`
  - Viewing reconciliation results
  - Downloading matched and unmatched reports


### 🧹 Clean Project Structure
- Modular architecture:
  - `src/preprocess.py` – preprocessing functions
  - `src/reconcile.py` – matching logic
  - `app.py` – Streamlit interface
- Configured `.gitignore` to exclude:
  - `venv/`
  - `reconcile/`
  - output files (`*.csv`)

---

## 🧰 Installation

```bash
# Clone the repo
git clone https://github.com/your-username/grocers-reconciliation.git
cd grocers-reconciliation

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

## 📦 How to Run

streamlit run app.py
