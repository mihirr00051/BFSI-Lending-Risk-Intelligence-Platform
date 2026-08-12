SELECT
  c.state,
  COUNT(DISTINCT c.customer_id) AS customers,
  AVG(IF(i.policy_active=1,1,0)) AS insurance_penetration
FROM `finsight_bfsi.stg_customers` c
LEFT JOIN `finsight_bfsi.raw_insurance_policies` i
ON c.customer_id=i.customer_id
GROUP BY c.state
ORDER BY insurance_penetration DESC;
