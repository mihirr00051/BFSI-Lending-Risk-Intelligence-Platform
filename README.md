🏦 FinSight AI — BFSI Lending, Risk & Customer Intelligence

Portfolio-ready End-to-End Data Analyst Project | 2026A modern synthetic BFSI analytics platform designed to simulate a retail bank / NBFC decision-intelligence environment across lending, credit risk, collections, customer intelligence, insurance cross-sell, BI and AI-assisted insights.

📌 Executive Summary

FinSight AI is an end-to-end BFSI analytics solution that connects customer, loan, repayment, transaction and insurance data into a single analytical workflow.

The project is designed around the kinds of questions a banking / NBFC analytics team would typically answer:

How large is the active lending portfolio?

Which products, branches and customer segments drive portfolio growth?

Where is delinquency concentrated?

Which customers have strong value but low product penetration?

Where should collections teams prioritize intervention?

Which customer segments are suitable for insurance cross-sell?

How can management convert portfolio KPIs into actionable decisions?

The solution combines Python, SQL/BigQuery, R, SAS, Power BI, Tableau, Advanced Excel and Streamlit, with an optional AI insight layer.

⚠️ Important: All data is synthetic and created exclusively for portfolio / learning purposes. The dashboard should not be presented as actual bank performance or as a production credit-decisioning system.

🎯 Business Objective

FinSight AI creates a unified analytics layer for five major BFSI decision areas:

Decision Area

Business Question

Portfolio Management

Where is capital deployed and how is AUM distributed?

Credit Risk

Which products / regions / cohorts have higher delinquency or NPL exposure?

Collections

Where is the collection gap concentrated and which accounts should be prioritized?

Customer Intelligence

Which customers / segments have higher value or engagement?

Cross-sell

Which eligible customers have insurance / product whitespace?

🧩 Solution Architecture

                    ┌─────────────────────────────┐
                    │   Synthetic BFSI Sources    │
                    │ Customers / Loans /         │
                    │ Repayments / Transactions / │
                    │ Insurance Policies           │
                    └──────────────┬──────────────┘
                                   │
                                   ▼
                    ┌─────────────────────────────┐
                    │ Data Validation & Profiling  │
                    │ Missing values / Duplicates  │
                    │ Schema / Range checks        │
                    └──────────────┬──────────────┘
                                   │
                                   ▼
                    ┌─────────────────────────────┐
                    │ BigQuery Analytics Layer     │
                    │ Raw → Staging → Data Marts   │
                    └──────────────┬──────────────┘
                                   │
                  ┌────────────────┼────────────────┐
                  ▼                ▼                ▼
             Python / R           SAS          SQL Analysis
             EDA / KPI        Credit Risk       KPI / Risk
                  │                │                │
                  └────────────────┼────────────────┘
                                   ▼
                    ┌─────────────────────────────┐
                    │   BI / Semantic KPI Layer   │
                    │   Power BI + Tableau        │
                    └──────────────┬──────────────┘
                                   │
                                   ▼
                    ┌─────────────────────────────┐
                    │   FinSight AI Dashboard     │
                    │   Streamlit Executive UI    │
                    └──────────────┬──────────────┘
                                   │
                                   ▼
                    ┌─────────────────────────────┐
                    │ AI Insight Copilot           │
                    │ Deterministic fallback       │
                    │ Optional OpenAI layer        │
                    └──────────────┬──────────────┘
                                   │
                                   ▼
                    ┌─────────────────────────────┐
                    │ Management Actions          │
                    │ Risk / Collections / Growth │
                    │ Cross-sell / Monitoring      │
                    └─────────────────────────────┘

🛠️ Technology Stack

Layer

Technologies

Data

Synthetic CSV, BigQuery-ready schema

Querying

SQL, Google BigQuery SQL

Programming

Python, Pandas, NumPy, R

BI / Visualization

Power BI, Tableau, Streamlit, Plotly

Statistical / Risk Analysis

SAS

Spreadsheet Analytics

Advanced Excel

AI

Optional OpenAI-powered insight layer + deterministic fallback

Testing

Pytest

Documentation

Markdown

Version Control

Git / GitHub

📁 Project Structure

FinSight-AI-BFSI-Analytics-2026/
│
├── app/
│   └── app.py
│
├── data/
│   ├── raw/
│   │   ├── customers.csv
│   │   ├── loans.csv
│   │   ├── repayments.csv
│   │   ├── transactions.csv
│   │   └── insurance_policies.csv
│   │
│   └── processed/
│       ├── customer_priority.csv
│       └── portfolio_by_state_product.csv
│
├── docs/
│   ├── INTERVIEW_STORY.md
│   └── SETUP.md
│
├── excel/
│   └── FinSight_BFSI_Analytics.xlsx
│
├── powerbi/
│   ├── README.md
│   └── screenshots/
│
├── python/
│   ├── analysis.py
│   └── generate_data.py
│
├── r/
│   └── eda.R
│
├── sas/
│   └── risk_analysis.sas
│
├── sql/
│   └── bigquery/
│       ├── 01_staging.sql
│       ├── 02_mart_portfolio.sql
│       ├── 03_kpi_queries.sql
│       ├── 04_credit_risk.sql
│       ├── 05_collections.sql
│       └── 06_customer_insurance.sql
│
├── tableau/
│   ├── README.md
│   └── screenshots/
│
├── tests/
│   └── test_project.py
│
├── .gitignore
├── README.md
└── requirements.txt

📊 Core Dataset

customers.csv

Customer-level attributes such as:

customer ID

geography / state

customer segment

demographic attributes

income-related signals

loans.csv

Loan / portfolio attributes such as:

loan ID

customer ID

product

original amount

outstanding principal

DPD

loan status / lifecycle attributes where available

repayments.csv

Repayment behavior including:

loan ID

amount due

amount paid

collection / payment behavior signals

transactions.csv

Customer activity and transaction-level signals that can support:

engagement analysis

monthly activity

transaction behavior

customer segmentation

insurance_policies.csv

Insurance ownership / policy information for:

penetration analysis

customer-product whitespace

cross-sell opportunity identification

📈 KPI Framework

AUM

Assets Under Management

AUM = Σ Outstanding Principal

Measures the active loan exposure being managed.

Disbursals

Disbursals = Σ Original Principal

Used to monitor lending deployment / origination scale for the selected scope.

Delinquency Rate

Delinquency Rate =
Overdue Active Loans / Active Loans

NPL Proxy

NPL Proxy =
Loans with DPD >= 90 / Active Loans

This is a portfolio proxy for analytical use, not a regulatory NPA/NPL calculation.

Collection Efficiency

Collection Efficiency =
Amount Collected / Amount Due

Insurance Cross-sell Rate

Cross-sell Rate =
Customers with Active Insurance / Eligible Active-loan Customers

Yield

Yield =
Interest Income Proxy / Average Outstanding

Use this metric only when the required interest / income fields exist in the selected analytical dataset.

🖥️ Streamlit Dashboard

The Streamlit application is designed as an executive BFSI command center.

Dashboard Modules

1. Executive Overview

AUM

Disbursals

Loan count

Delinquency

NPL proxy

Collection efficiency

Portfolio health

Product concentration

Business snapshot

2. Credit Risk

DPD distribution

Current vs overdue accounts

90+ DPD exposure

Product risk matrix

Risk concentration

3. Collections

Collection efficiency

Collection gap

Product-level recovery

Priority accounts

Collection management insights

4. Customer & Insurance Intelligence

State-level insurance penetration

Customer segments

Product penetration

Cross-sell opportunities

5. AI Insight Copilot

Portfolio risk alerts

Concentration insights

Collection recommendations

Insurance cross-sell opportunities

🤖 AI Insight Copilot

FinSight AI follows a two-layer design:

Filtered KPI / Analytical Data
            │
            ▼
   Deterministic Insight Engine
            │
            ├── Always available
            └── No API key required
            │
            ▼
     Optional OpenAI Layer
            │
            ▼
Management-ready narrative

Default behavior

The application remains functional without an API key using deterministic business rules.

Optional LLM layer

When OPENAI_API_KEY is configured, the application can add a narrative layer over the filtered KPI context.

Recommended guardrails:

Do not send customer PII.

Ground the response in filtered KPI rows.

Keep source values visible.

Distinguish facts from recommendations.

Never present synthetic outputs as real banking data.

🔍 Example Business Insights

Typical management-oriented outputs include:

Risk

NPL proxy is elevated. Prioritize 90+ DPD accounts and isolate the products or regions contributing the largest outstanding exposure.

Concentration

A single loan product contributes the largest AUM share. Review concentration against product-level delinquency before increasing origination.

Collections

Collection efficiency is below target. Prioritize partial and missed payments before accounts migrate into higher DPD buckets.

Cross-sell

Insurance penetration is below potential in selected customer groups. Explore cross-sell opportunities among eligible, higher-value customers.

🧪 Data Quality & Testing

The project includes automated tests covering:

required raw files

expected columns

unique loan IDs

non-negative DPD

non-negative monetary values

insurance flag quality

repayment field validation

Run:

python -m pytest -q

Python compilation check:

python -m compileall app python tests

🚀 Setup

1. Create virtual environment

python -m venv .venv

2. Activate

Windows PowerShell

.\.venv\Scripts\Activate.ps1

3. Install dependencies

pip install -r requirements.txt

4. Run the dashboard

python -m streamlit run .\app\app.py

🔎 Python Analysis

Run:

python .\python\analysis.py

This can generate processed analytics outputs such as:

data/processed/
├── customer_priority.csv
└── portfolio_by_state_product.csv

🧠 SQL / BigQuery Layer

The SQL layer is organized into:

01_staging.sql
02_mart_portfolio.sql
03_kpi_queries.sql
04_credit_risk.sql
05_collections.sql
06_customer_insurance.sql

This reflects a typical progression:

Raw Sources
   ↓
Staging
   ↓
Analytics Mart
   ↓
KPI Queries
   ↓
Business Analysis

📊 Power BI

Suggested report pages:

Executive Overview

Credit Risk

Collections

Customer & Insurance

Growth / Cross-sell

Recommended visuals:

KPI cards

product portfolio bars

DPD bucket analysis

state heatmap

risk matrix

collection gap

customer segment analysis

Add final exported report screenshots to:

powerbi/screenshots/

📈 Tableau

Suggested Tableau views:

Portfolio Overview

Product Risk Matrix

DPD Distribution

Collections Gap

Insurance Penetration

Branch / Geography Analysis where supported by the available dataset

Add final Tableau screenshots to:

tableau/screenshots/

📗 Advanced Excel

Excel can be used as a supporting analyst layer for:

KPI reconciliation

pivot analysis

lookup / aggregation workflows

exception tracking

management-ready summaries

Workbook:

excel/FinSight_BFSI_Analytics.xlsx

📉 R & SAS

R

Used for exploratory analysis and statistical visualization.

r/eda.R

SAS

Used for structured risk analysis and portfolio summaries.

sas/risk_analysis.sas

✅ Project Validation Checklist

Before publishing to GitHub:

[ ] Streamlit dashboard runs
[ ] No deprecated Streamlit warnings
[ ] pytest passes
[ ] Python compilation passes
[ ] Raw datasets are synthetic
[ ] No secrets / API keys committed
[ ] README screenshots added
[ ] Power BI screenshots added
[ ] Tableau screenshots added
[ ] SQL scripts documented
[ ] Interview story reviewed

💼 Interview Positioning

30-second explanation

“FinSight AI is an end-to-end BFSI analytics project I built to simulate a lending and customer-intelligence environment. I connected customer, loan, repayment, transaction and insurance data, built SQL and Python analytics layers, added credit-risk and collections analysis, and exposed the final KPIs through an executive Streamlit dashboard with optional AI-assisted business insights.”

Strong interview areas

Be ready to explain:

Why AUM is more useful than raw loan count for portfolio concentration.

Why DPD is a leading operational risk signal.

How 90+ DPD is used as an NPL proxy in a portfolio simulation.

How collection efficiency is calculated.

How the collection gap is prioritized.

Why synthetic data must be clearly labeled.

Why deterministic rules are useful as a fallback for LLM applications.

How you would move the prototype from CSV → BigQuery → semantic BI layer in production.

⚠️ Important Limitations

This is a portfolio simulation, not a real bank platform.

Do not claim:

real customer performance

production credit underwriting

regulatory NPA reporting

real profitability

real-time banking data

production-grade model risk approval

unless those capabilities are actually implemented and validated.

📌 Future Production Roadmap

A production version could add:

Kafka / CDC
     ↓
Cloud Storage
     ↓
BigQuery
     ↓
dbt / Data Quality
     ↓
Semantic Layer
     ↓
Power BI / Tableau
     ↓
Feature Store / ML Risk Models
     ↓
LLM Insight Service
     ↓
Monitoring / Governance

👤 Author

FinSight AI — BFSI Analytics Portfolio Project

Focus Areas:Data Analytics • BFSI • Credit Risk • Collections • Customer Intelligence • BI • SQL • Python • AI

⭐ Portfolio Note

This project is intentionally designed to demonstrate end-to-end analytical thinking:

Business Problem → Data → SQL → Analysis → KPI → Visualization → Insight → Action

The goal is not to show as many tools as possible. The goal is to show how an analyst converts messy business data into decisions.