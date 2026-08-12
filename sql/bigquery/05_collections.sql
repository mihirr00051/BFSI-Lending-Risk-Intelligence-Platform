SELECT
  m.product,
  SUM(r.amount_due) AS amount_due,
  SUM(r.amount_paid) AS amount_paid,
  SUM(GREATEST(r.amount_due-r.amount_paid,0)) AS collection_gap,
  SAFE_DIVIDE(SUM(r.amount_paid),SUM(r.amount_due)) AS collection_efficiency
FROM `finsight_bfsi.mart_portfolio` m
JOIN `finsight_bfsi.stg_repayments` r
ON m.loan_id=r.loan_id
GROUP BY m.product
ORDER BY collection_gap DESC;
