🏦 FinSight AI — BFSI Lending, Risk & Customer Intelligence

End-to-End Data Analyst Portfolio Project | BFSI | 2026

FinSight AI is a synthetic BFSI decision-intelligence platform built to simulate how a retail bank / NBFC can combine lending, credit-risk, collections, customer, transaction and insurance data into one analytics workflow.

The project demonstrates the complete analyst journey:

Business Problem → Data → SQL → Python/R/SAS → KPI Layer → BI → Dashboard → AI Insights → Business Action

🚀 Project Snapshot

Area

Coverage

Domain

Banking, Financial Services & Insurance (BFSI)

Focus

Lending • Credit Risk • Collections • Customer Intelligence • Cross-sell

Data

Synthetic BFSI datasets

Analytics

SQL • Python • R • SAS

BI / Visualization

Power BI • Tableau • Streamlit • Plotly

Cloud-ready

BigQuery-ready SQL architecture

AI

Deterministic Insight Engine + Optional OpenAI layer

Testing

Pytest

Spreadsheet

Advanced Excel

Status

✅ Portfolio / Interview Ready

🎯 Business Problem

BFSI leadership needs a trusted analytical view to answer questions such as:

How large is the active loan portfolio?

Which products and customer segments drive portfolio concentration?

Where is delinquency and 90+ DPD exposure concentrated?

Which accounts should collections prioritize?

Which customer groups show product or insurance whitespace?

How can KPI analysis be converted into clear management actions?

FinSight AI brings these questions into a single analytical workflow.

💡 What This Project Demonstrates

Portfolio Management

AUM and disbursal analysis

Product concentration

Portfolio mix

Business KPI monitoring

Credit Risk

DPD bucket analysis

Delinquency monitoring

90+ DPD / NPL proxy

Product-level risk comparison

Collections

Collection efficiency

Collection gap

Priority account logic

Recovery-focused recommendations

Customer Intelligence

Customer segmentation

Product penetration

Transaction activity

Customer value signals

Insurance Cross-sell

Insurance penetration

Product whitespace

Eligible customer opportunity analysis

AI-assisted Analytics

KPI interpretation

Risk alerts

Concentration insights

Collection recommendations

Cross-sell suggestions

🧩 Solution Architecture

                 ┌──────────────────────────────┐
                 │     Synthetic BFSI Data      │
                 │ Customers / Loans /          │
                 │ Repayments / Transactions /  │
                 │ Insurance Policies           │
                 └──────────────┬───────────────┘
                                │
                                ▼
                 ┌──────────────────────────────┐
                 │ Data Validation & Profiling   │
                 │ Schema • Duplicates • Range  │
                 │ Missing / Quality Checks      │
                 └──────────────┬───────────────┘
                                │
                                ▼
                 ┌──────────────────────────────┐
                 │ BigQuery Analytics Layer     │
                 │ Raw → Staging → Data Marts   │
                 └──────────────┬───────────────┘
                                │
                ┌───────────────┼────────────────┐
                ▼               ▼                ▼
          Python / R          SAS           SQL / BigQuery
          EDA + KPI        Risk Analysis     KPI + Risk
                │               │                │
                └───────────────┼────────────────┘
                                ▼
                 ┌──────────────────────────────┐
                 │ BI / Semantic KPI Layer     │
                 │ Power BI + Tableau           │
                 └──────────────┬───────────────┘
                                │
                                ▼
                 ┌──────────────────────────────┐
                 │ FinSight AI Executive App   │
                 │ Streamlit + Plotly           │
                 └──────────────┬───────────────┘
                                │
                                ▼
                 ┌──────────────────────────────┐
                 │ AI Insight Copilot           │
                 │ Deterministic + Optional LLM │
                 └──────────────┬───────────────┘
                                │
                                ▼
                    Business Decisions & Actions

🛠️ Technology Stack

Layer

Tools

Programming

Python, Pandas, NumPy, R

Querying

SQL, Google BigQuery SQL

Visualization

Plotly, Streamlit

BI

Power BI, Tableau

Statistical Analysis

SAS

Spreadsheet Analytics

Advanced Excel

AI

Optional OpenAI API + deterministic fallback

Testing

Pytest

Version Control

Git / GitHub

📁 Project Structure

BFSI-Lending-Risk-Intelligence-Platform/
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

📊 Data Model

customers.csv

Customer-level information used for:

geography

segmentation

demographic analysis

customer intelligence

loans.csv

Loan-level information used for:

product analysis

AUM

disbursals

outstanding exposure

DPD / risk analysis

repayments.csv

Repayment behavior used for:

amount due

amount paid

collection efficiency

collection gap

transactions.csv

Customer activity signals used for:

engagement analysis

transaction behavior

segmentation support

insurance_policies.csv

Insurance data used for:

penetration analysis

product whitespace

cross-sell opportunity

Data note: All datasets are synthetic and intended only for portfolio / learning purposes.

📈 Core KPI Framework

AUM

Assets Under Management

AUM = Σ Outstanding Principal

Disbursals

Disbursals = Σ Original Principal

Delinquency Rate

Delinquency Rate =
Overdue Active Loans / Active Loans

NPL Proxy

NPL Proxy =
Loans with DPD >= 90 / Active Loans

Analytical proxy only — not a regulatory NPA/NPL calculation.

Collection Efficiency

Collection Efficiency =
Amount Collected / Amount Due

Insurance Cross-sell Rate

Cross-sell Rate =
Customers with Active Insurance / Eligible Active-loan Customers

Yield

Yield =
Interest Income Proxy / Average Outstanding

Use only when the underlying interest / income fields are available.

🖥️ Executive Dashboard

The Streamlit application is designed as a BFSI executive command center.

Executive Overview

AUM

Disbursals

Loans

Delinquency

NPL Proxy

Collection Efficiency

Portfolio Health

Product Concentration

Business Snapshot

Credit Risk

DPD Distribution

Risk Buckets

90+ DPD Exposure

Product Risk Matrix

Risk Concentration

Collections

Collection Efficiency

Collection Gap

Recovery Analysis

Priority Accounts

Action-oriented Insights

Customer & Insurance

Customer Segments

Insurance Penetration

Product Whitespace

Cross-sell Opportunities

AI Insight Copilot

Risk Alerts

Concentration Insights

Collection Recommendations

Cross-sell Opportunities

🤖 AI Insight Copilot

FinSight AI uses a two-layer approach:

Filtered KPI / Analytical Data
             │
             ▼
   Deterministic Insight Engine
             │
       Always Available
             │
             ▼
       Optional OpenAI Layer
             │
             ▼
Management-ready narrative

Deterministic Layer

The dashboard remains functional without an API key.

Optional LLM Layer

When OPENAI_API_KEY is configured, the application can generate management-ready narrative from the filtered analytical context.

AI Guardrails

Do not send customer PII.

Ground outputs in available KPI data.

Keep source values visible.

Separate facts from recommendations.

Never present synthetic results as real banking performance.

🔍 Example Management Insights

🔴 Credit Risk

Prioritize 90+ DPD exposure and identify the products or segments contributing the largest outstanding risk.

🟦 Portfolio Concentration

Review concentration in the highest-AUM product alongside its delinquency and NPL profile before increasing origination.

🟢 Collections

Prioritize high-gap and high-DPD accounts before they migrate into more severe delinquency buckets.

🟣 Cross-sell

Identify eligible higher-value customers with limited insurance penetration and prioritize relevant cross-sell campaigns.

🧪 Data Quality & Testing

Automated validation includes:

Required input files

Required columns

Loan ID uniqueness

Non-negative DPD

Monetary value validation

Insurance flag validation

Repayment field validation

Run tests:

python -m pytest -q

Compile-check Python:

python -m compileall app python tests

🚀 Quick Start

1. Clone

git clone https://github.com/mihirr00051/BFSI-Lending-Risk-Intelligence-Platform.git
cd BFSI-Lending-Risk-Intelligence-Platform

2. Create environment

python -m venv .venv

3. Activate environment

.\.venv\Scripts\Activate.ps1

4. Install dependencies

pip install -r requirements.txt

5. Run the dashboard

python -m streamlit run .pppp.py

6. Run analytics

python .\pythonnalysis.py

7. Run tests

python -m pytest -q

🧠 SQL / BigQuery Layer

The SQL layer follows a simple analytics flow:

Raw Data
   ↓
Staging
   ↓
Analytics Mart
   ↓
KPI Queries
   ↓
Risk / Collections / Customer Analysis

Scripts:

01_staging.sql
02_mart_portfolio.sql
03_kpi_queries.sql
04_credit_risk.sql
05_collections.sql
06_customer_insurance.sql

📊 Power BI

Suggested report pages:

Executive Overview

Credit Risk

Collections

Customer & Insurance

Growth / Cross-sell

Recommended visuals:

KPI Cards

Portfolio by Product

DPD Distribution

Risk Matrix

State / Region Analysis

Collection Gap

Customer Segment Analysis

Screenshots:

powerbi/screenshots/

📈 Tableau

Suggested views:

Portfolio Overview

Product Risk Matrix

DPD Distribution

Collections Gap

Insurance Penetration

Geography / Branch Analysis where supported by the dataset

Screenshots:

tableau/screenshots/

📗 Advanced Excel

Supporting analyst workflows:

KPI reconciliation

Pivot analysis

Lookups / aggregation

Exception tracking

Management summaries

Workbook:

excel/FinSight_BFSI_Analytics.xlsx

📉 R & SAS

R

Exploratory data analysis and statistical visualization:

r/eda.R

SAS

Structured credit-risk and portfolio analysis:

sas/risk_analysis.sas

✅ Project Validation Checklist

Before sharing with recruiters:

[x] Streamlit dashboard runs
[x] Python code compiles
[x] Unit/data-quality tests included
[x] Synthetic data clearly labelled
[x] Secrets excluded from Git
[x] SQL layer documented
[x] BI folders prepared
[x] Interview documentation included
[ ] Add final Power BI screenshots
[ ] Add final Tableau screenshots

💼 Interview Pitch

30-second version

“FinSight AI is an end-to-end BFSI analytics platform I built to simulate a retail lending and customer-intelligence environment. I connected customer, loan, repayment, transaction and insurance data, built SQL and Python analytics layers, added credit-risk and collections analysis, and exposed the final KPIs through an executive Streamlit dashboard with optional AI-assisted insights.”

What I would discuss in an interview

Why AUM matters for portfolio concentration

How DPD acts as a credit-risk signal

Why 90+ DPD is used as an analytical NPL proxy

How collection efficiency is calculated

How collection priority can be ranked

How customer-product whitespace can support cross-sell

How the prototype could move from CSV → BigQuery → semantic BI layer

⚠️ Important Limitations

This is a portfolio simulation, not a live banking platform.

Do not present it as:

real customer performance

production underwriting

regulatory NPA reporting

real profitability

real-time banking data

production-grade model-risk approval

unless those capabilities are actually implemented and validated.

🔮 Production Roadmap

A future production architecture could evolve toward:

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
ML Risk Models
     ↓
LLM Insight Service
     ↓
Monitoring / Governance

👤 About the Project

FinSight AI — BFSI Lending, Risk & Customer Intelligence

Focus Areas

Data Analytics · BFSI · Credit Risk · Collections · Customer Intelligence · BI · SQL · Python · AI

⭐ Why this project matters

The goal is not to demonstrate a long list of tools.

The goal is to demonstrate an analyst's ability to convert:

Business Problem → Data → Analysis → KPI → Visualization → Insight → Action
