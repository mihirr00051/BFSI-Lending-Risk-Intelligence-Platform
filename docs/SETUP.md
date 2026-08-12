# Setup

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
pip install -r requirements.txt
python python/generate_data.py
python python/analysis.py
streamlit run app/app.py
```

## BigQuery
1. Create project and dataset `finsight_bfsi`.
2. Upload raw CSVs to Cloud Storage or BigQuery tables.
3. Run SQL in `sql/bigquery/01_staging.sql`, then `02_mart_portfolio.sql`, then `03_kpi_queries.sql`.

## Tableau / Power BI
Use the generated CSVs for local development first. Re-point the semantic model to BigQuery marts when a cloud environment is available.
