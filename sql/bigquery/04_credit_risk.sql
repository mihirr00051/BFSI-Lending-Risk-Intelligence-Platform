SELECT
  product,
  COUNT(*) AS loans,
  SUM(outstanding_principal) AS AUM,
  AVG(IF(dpd>0,1,0)) AS delinquency_rate,
  AVG(IF(dpd>=90,1,0)) AS npl_proxy,
  AVG(dpd) AS avg_dpd
FROM `finsight_bfsi.mart_portfolio`
GROUP BY product
ORDER BY npl_proxy DESC, AUM DESC;
