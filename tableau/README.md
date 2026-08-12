# Tableau Build Specification

Recommended Tableau pages:
1. Executive Command Center
2. Credit Risk Explorer
3. Collections Command Center
4. Customer 360
5. Growth & Cross-sell
6. AI Insight Feed

Use parameters for `State`, `Product`, `Segment`, `Channel`, and `As Of Date`.

Suggested calculated fields:
- `NPL Proxy = SUM(IIF([dpd] >= 90, 1, 0)) / COUNT([loan_id])`
- `Delinquency Rate = SUM(IIF([dpd] > 0, 1, 0)) / COUNT([loan_id])`
- `Collection Efficiency = SUM([amount_paid]) / SUM([amount_due])`
- `AUM = SUM([outstanding_principal])`

For Tableau Cloud, Tableau Pulse can be used as the AI-driven metric insight layer.
