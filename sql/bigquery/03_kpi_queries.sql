SELECT
  SUM(outstanding_principal) AS AUM,
  SUM(original_amount) AS Disbursals,
  COUNT(DISTINCT loan_id) AS Loans,
  AVG(IF(dpd>0,1,0)) AS Delinquency,
  AVG(IF(dpd>=90,1,0)) AS NPL_Proxy
FROM `finsight_bfsi.mart_portfolio`;

SELECT product, SUM(outstanding_principal) AUM, COUNT(*) Loans
FROM `finsight_bfsi.mart_portfolio`
GROUP BY product
ORDER BY AUM DESC;
