CREATE OR REPLACE TABLE `finsight_bfsi.stg_customers` AS
SELECT CAST(customer_id AS STRING) customer_id,
       CAST(state AS STRING) state,
       CAST(segment AS STRING) segment
FROM `finsight_bfsi.raw_customers`;

CREATE OR REPLACE TABLE `finsight_bfsi.stg_loans` AS
SELECT CAST(loan_id AS STRING) loan_id,
       CAST(customer_id AS STRING) customer_id,
       CAST(product AS STRING) product,
       CAST(original_amount AS FLOAT64) original_amount,
       CAST(outstanding_principal AS FLOAT64) outstanding_principal,
       CAST(dpd AS INT64) dpd
FROM `finsight_bfsi.raw_loans`;
