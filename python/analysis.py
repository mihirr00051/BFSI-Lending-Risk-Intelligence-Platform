from pathlib import Path
import pandas as pd

ROOT=Path(__file__).resolve().parents[1]
RAW=ROOT/'data/raw'
OUT=ROOT/'data/processed'; OUT.mkdir(exist_ok=True)
customers=pd.read_csv(RAW/'customers.csv')
loans=pd.read_csv(RAW/'loans.csv',parse_dates=['disbursement_date'])
rep=pd.read_csv(RAW/'repayments.csv')
ins=pd.read_csv(RAW/'insurance_policies.csv')

df=loans.merge(customers,on='customer_id',how='left').merge(rep[['loan_id','amount_due','amount_paid']],on='loan_id',how='left')
df['delinquent_flag']=(df['dpd']>0).astype(int)
df['npl_flag']=(df['dpd']>=90).astype(int)
df['collection_efficiency']=df['amount_paid']/df['amount_due'].replace(0,pd.NA)

portfolio=(df.groupby(['state','product'],as_index=False).agg(
    loans=('loan_id','count'), aum=('outstanding_principal','sum'), original_amount=('original_amount','sum'),
    delinquency_rate=('delinquent_flag','mean'), npl_rate=('npl_flag','mean'), avg_rate=('interest_rate','mean'),
    collection_efficiency=('collection_efficiency','mean')))
portfolio.to_csv(OUT/'portfolio_by_state_product.csv',index=False)

customer_value=df.groupby('customer_id',as_index=False).agg(
    active_loans=('loan_id','count'),aum=('outstanding_principal','sum'),avg_rate=('interest_rate','mean'),max_dpd=('dpd','max'))
cx=customer_value.merge(ins[['customer_id','policy_active','annual_premium']],on='customer_id',how='left')
cx['cross_sell_eligible']=(cx['policy_active'].fillna(False)==False).astype(int)
cx['priority_score']=(cx['aum']/cx['aum'].max()*50 + (cx['max_dpd'].clip(0,120)/120)*35 + cx['avg_rate']/25*15).round(2)
cx.sort_values('priority_score',ascending=False).to_csv(OUT/'customer_priority.csv',index=False)
print('Processed analytics written to', OUT)
