from pathlib import Path
import pandas as pd

ROOT=Path(__file__).resolve().parents[1]

def test_raw_files_exist():
    for name in ['customers.csv','loans.csv','repayments.csv','transactions.csv','insurance_policies.csv']:
        assert (ROOT/'data/raw'/name).exists()

def test_loan_keys_and_ranges():
    loans=pd.read_csv(ROOT/'data/raw/loans.csv')
    assert loans.loan_id.is_unique
    assert (loans.outstanding_principal >= 0).all()
    assert (loans.original_amount > 0).all()
    assert ((loans.dpd >= 0) & (loans.dpd <= 3650)).all()
