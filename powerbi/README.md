# Power BI Build Specification

Import `data/raw/*.csv` or connect the equivalent BigQuery marts.

## Model
- `customers` 1:* `loans`
- `loans` 1:1 demo `repayments`
- `customers` 1:* `transactions`
- `customers` 1:1 demo `insurance_policies`

Create a proper Date table and keep it disconnected from text date columns until model dates are standardized.

## Core DAX measures
```DAX
AUM = SUM(loans[outstanding_principal])
Disbursal = SUM(loans[original_amount])
Loans = DISTINCTCOUNT(loans[loan_id])
Customers = DISTINCTCOUNT(customers[customer_id])
Delinquency Rate = DIVIDE(CALCULATE([Loans], loans[dpd] > 0), [Loans])
NPL Proxy Rate = DIVIDE(CALCULATE([Loans], loans[dpd] >= 90), [Loans])
Avg Interest Rate = AVERAGE(loans[interest_rate])
Collection Efficiency = DIVIDE(SUM(repayments[amount_paid]), SUM(repayments[amount_due]))
Cross Sell Rate = DIVIDE(CALCULATE(DISTINCTCOUNT(insurance_policies[customer_id]), insurance_policies[policy_active] = TRUE()), [Customers])
```

## UX rules
- Dark executive header + white content cards.
- Put 6 KPI cards above the fold.
- Use one accent color for positive/neutral and a single warning color for risk.
- Avoid pie charts for product mix; use ranked bars.
- Every risk visual must have a clearly labeled denominator.
- Add a “Decision” text box under every page: “What should management do next?”
