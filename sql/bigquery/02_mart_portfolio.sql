CREATE OR REPLACE TABLE `finsight_bfsi.mart_portfolio` AS
SELECT l.loan_id, l.customer_id, c.state, c.segment, l.product,
       l.original_amount, l.outstanding_principal, l.dpd,
       CASE
         WHEN l.dpd=0 THEN 'Current'
         WHEN l.dpd<=30 THEN '1-30 DPD'
         WHEN l.dpd<90 THEN '31-90 DPD'
         ELSE '90+ DPD'
       END AS risk_band
FROM `finsight_bfsi.stg_loans` l
LEFT JOIN `finsight_bfsi.stg_customers` c
ON l.customer_id=c.customer_id;
