from pathlib import Path
import numpy as np
import pandas as pd

OUT = Path(__file__).resolve().parents[1] / 'data' / 'raw'
OUT.mkdir(parents=True, exist_ok=True)
rng = np.random.default_rng(42)
N = 5000

states = ['Karnataka','Maharashtra','Gujarat','Tamil Nadu','Telangana','Delhi NCR','West Bengal','Rajasthan']
products = ['Personal Loan','Home Loan','Auto Loan','Business Loan','Education Loan']
segments = ['Mass','Mass Affluent','Affluent','Emerging']
channels = ['Branch','Digital','DSA','Partner']

customer_id = np.array([f'C{100001+i}' for i in range(N)])
age = rng.integers(22, 61, N)
income = np.clip(rng.lognormal(mean=11.1, sigma=0.55, size=N), 180000, 5000000).round(-3)
segment = pd.cut(income, bins=[0,500000,1000000,2000000,np.inf], labels=['Mass','Emerging','Mass Affluent','Affluent']).astype(str)
credit_score = np.clip(rng.normal(720, 65, N), 520, 850).round().astype(int)
state = rng.choice(states, N, p=[.22,.17,.12,.12,.10,.10,.08,.09])
city = rng.choice(['Bengaluru','Mumbai','Ahmedabad','Chennai','Hyderabad','Delhi','Kolkata','Jaipur'], N)
customer_since = pd.to_datetime('2019-01-01') + pd.to_timedelta(rng.integers(0,2600,N), unit='D')
customers = pd.DataFrame({
    'customer_id':customer_id,'age':age,'annual_income':income,'segment':segment,'credit_score':credit_score,
    'state':state,'city':city,'customer_since':customer_since.date.astype(str)
})

loan_n = 7200
loan_id = np.array([f'L{200001+i}' for i in range(loan_n)])
loan_customer = rng.choice(customer_id, loan_n)
product = rng.choice(products, loan_n, p=[.38,.16,.20,.18,.08])
channel = rng.choice(channels, loan_n, p=[.35,.32,.18,.15])
disbursement_date = pd.to_datetime('2023-01-01') + pd.to_timedelta(rng.integers(0,1200,loan_n), unit='D')
amount = np.select([
    product=='Home Loan', product=='Business Loan', product=='Auto Loan', product=='Education Loan'],
    [rng.uniform(1200000,6000000,loan_n),rng.uniform(300000,3000000,loan_n),rng.uniform(150000,1800000,loan_n),rng.uniform(100000,1200000,loan_n)],
    default=rng.uniform(50000,900000,loan_n)
).round(-3)
tenure = rng.choice([12,24,36,48,60,84,120], loan_n)
rate = np.select([product=='Home Loan',product=='Business Loan',product=='Auto Loan',product=='Education Loan'],[rng.uniform(8.1,11.5,loan_n),rng.uniform(10.5,18,loan_n),rng.uniform(9,15,loan_n),rng.uniform(8.5,13,loan_n)],default=rng.uniform(11,22,loan_n)).round(2)
base_risk = 760 - np.searchsorted([500000,1000000,2000000], rng.uniform(0,2500000,loan_n))*30
credit_lookup = customers.set_index('customer_id')['credit_score']
cs = pd.Series(loan_customer).map(credit_lookup).to_numpy()
raw_risk = np.clip((720-cs)/60 + rng.normal(0,0.65,loan_n), -2, 3)
dpd = np.where(raw_risk > 1.4, rng.integers(45,181,loan_n), np.where(raw_risk>0.5,rng.integers(1,60,loan_n),rng.integers(0,16,loan_n)))
status = np.where(dpd>=90,'NPL',np.where(dpd>0,'Delinquent','Current'))
term_factor = np.maximum(0.15, 1 - (pd.Timestamp('2026-08-01')-disbursement_date).days/(tenure*30))
outstanding = (amount*np.clip(term_factor + rng.normal(0,.05,loan_n),.08,1)).round(0)
loans = pd.DataFrame({
    'loan_id':loan_id,'customer_id':loan_customer,'product':product,'channel':channel,'disbursement_date':disbursement_date.date.astype(str),
    'original_amount':amount,'tenure_months':tenure,'interest_rate':rate,'dpd':dpd,'loan_status':status,'outstanding_principal':outstanding
})

# Repayment records — one observation per loan for a portfolio-level demo
monthly_due = (amount/tenure).round(0)
collection_ratio = np.where(dpd>=90,rng.uniform(.05,.55,loan_n),np.where(dpd>0,rng.uniform(.60,.95,loan_n),rng.uniform(.93,1.03,loan_n)))
amount_paid = (monthly_due*collection_ratio).round(0)
repayments = pd.DataFrame({
    'repayment_id':[f'R{300001+i}' for i in range(loan_n)], 'loan_id':loan_id,
    'due_date':(disbursement_date+pd.to_timedelta(tenure//3*30,unit='D')).date.astype(str),
    'amount_due':monthly_due,'amount_paid':amount_paid,
    'payment_status':np.where(amount_paid>=monthly_due,'Paid',np.where(amount_paid>0,'Partial','Missed'))
})

# Transaction activity: 30k account-level monthly snapshots
T=30000
cust_tx=rng.choice(customer_id,T)
txn_date=pd.to_datetime('2025-01-01')+pd.to_timedelta(rng.integers(0,580,T),unit='D')
transactions=pd.DataFrame({
    'transaction_id':[f'T{400001+i}' for i in range(T)],'customer_id':cust_tx,'transaction_date':txn_date.date.astype(str),
    'transaction_type':rng.choice(['UPI','NEFT','IMPS','ATM','POS','SALARY'],T,p=[.28,.12,.12,.12,.24,.12]),
    'amount':rng.lognormal(8.2,1.0,T).round(2)
})

# Insurance cross-sell
eligible = pd.DataFrame({'customer_id':customer_id})
has_policy=rng.random(N)<0.29
insurance=pd.DataFrame({
    'policy_id':[f'P{500001+i}' for i in range(N)],'customer_id':customer_id,
    'policy_type':rng.choice(['Health','Life','Motor','Personal Accident'],N),
    'annual_premium':np.where(has_policy,rng.uniform(4000,45000,N).round(0),0),
    'policy_active':has_policy
})

customers.to_csv(OUT/'customers.csv',index=False)
loans.to_csv(OUT/'loans.csv',index=False)
repayments.to_csv(OUT/'repayments.csv',index=False)
transactions.to_csv(OUT/'transactions.csv',index=False)
insurance.to_csv(OUT/'insurance_policies.csv',index=False)
print('Generated:', OUT)
for f in OUT.glob('*.csv'):
    print(f.name, pd.read_csv(f).shape)
