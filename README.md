🚀 FinSight AI – BFSI Lending, Risk & Customer Intelligence Platform

<p align="center">














</p>

📌 Project Overview

FinSight AI is an end-to-end BFSI decision-intelligence and analytics platform designed to simulate how a retail bank or NBFC can combine lending, credit-risk, collections, customer, transaction, and insurance data into a unified analytical workflow.

The project demonstrates the complete analyst journey:

Business Problem
      ↓
Data
      ↓
Validation
      ↓
SQL
      ↓
Python / R / SAS
      ↓
KPI Layer
      ↓
Power BI / Tableau
      ↓
Streamlit Executive Dashboard
      ↓
AI-assisted Insights
      ↓
Business Action

The objective is to demonstrate how raw business data can be transformed into KPIs, risk signals, management insights, and action-oriented recommendations.

⚠️ Data Disclaimer: All datasets used in this project are synthetic and intended only for portfolio and learning purposes.

🎯 Key Features

End-to-End BFSI Analytics Workflow

Lending Portfolio Analysis

AUM & Disbursal Analysis

Credit Risk & DPD Analysis

90+ DPD / NPL Analytical Proxy

Collections & Recovery Analysis

Customer Segmentation

Transaction Behavior Analysis

Insurance Penetration & Cross-sell Analysis

SQL / BigQuery-ready Analytics Layer

Python EDA & KPI Analysis

R Exploratory Data Analysis

SAS Risk Analysis

Power BI Executive Reporting

Tableau Analytical Views

Streamlit Executive Dashboard

Plotly Interactive Visualizations

Deterministic AI Insight Engine

Optional OpenAI Insight Layer

Data Quality Validation

Pytest-based Testing

Git / GitHub Portfolio Structure

🏦 BFSI Business Use Cases

FinSight AI is designed around practical business questions faced by lending and financial-services teams.

Portfolio Management

How large is the active loan portfolio?

Which products contribute the highest AUM?

Where is portfolio concentration increasing?

Which products or customer segments drive portfolio mix?

Credit Risk

Where is delinquency concentrated?

What percentage of active loans has 90+ DPD?

Which products carry higher outstanding risk?

Which segments require additional risk attention?

Collections

How efficient are collections?

Where is the highest collection gap?

Which accounts should collections prioritize?

Which accounts show recovery potential?

Customer Intelligence

Which customer segments are most valuable?

How active are customers across transactions?

Which customers show higher engagement?

Where are product opportunities concentrated?

Insurance Cross-sell

What is insurance penetration among eligible customers?

Which customers have product whitespace?

Which customer groups represent potential cross-sell opportunities?

🏗️ System Architecture

                       Synthetic BFSI Data
                              │
        ┌─────────────────────┼─────────────────────┐
        │                     │                     │
   Customers               Loans              Repayments
        │                     │                     │
        └─────────────────────┼─────────────────────┘
                              │
                    Transactions / Insurance
                              │
                              ▼
                ┌─────────────────────────┐
                │ Data Validation &       │
                │ Profiling               │
                │ Schema / Duplicates /   │
                │ Range / Missing Checks  │
                └────────────┬────────────┘
                             │
                             ▼
                ┌─────────────────────────┐
                │ BigQuery Analytics      │
                │ Raw → Staging → Marts  │
                └────────────┬────────────┘
                             │
             ┌───────────────┼────────────────┐
             ▼               ▼                ▼
        Python / R         SAS           SQL / BigQuery
        EDA + KPI      Risk Analysis       KPI + Risk
             │               │                │
             └───────────────┼────────────────┘
                             ▼
                ┌─────────────────────────┐
                │ BI / Semantic KPI Layer │
                │ Power BI + Tableau      │
                └────────────┬────────────┘
                             │
                             ▼
                ┌─────────────────────────┐
                │ FinSight AI Executive   │
                │ Streamlit + Plotly      │
                └────────────┬────────────┘
                             │
                             ▼
                ┌─────────────────────────┐
                │ AI Insight Copilot      │
                │ Deterministic + Optional│
                │ OpenAI Layer             │
                └────────────┬────────────┘
                             │
                             ▼
                  Business Decisions
                       & Actions

⚙️ Technology Stack

Category

Technologies

Programming

Python, Pandas, NumPy

Querying

SQL, Google BigQuery SQL

Visualization

Plotly, Streamlit

Business Intelligence

Power BI, Tableau

Statistical Analysis

R, SAS

Spreadsheet Analytics

Advanced Excel

AI

Deterministic Insight Engine, Optional OpenAI API

Testing

Pytest

Version Control

Git, GitHub

Data

Synthetic BFSI datasets

📂 Project Structure

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

🚀 Installation

1️⃣ Clone Repository

git clone https://github.com/mihirr00051/BFSI-Lending-Risk-Intelligence-Platform.git

cd BFSI-Lending-Risk-Intelligence-Platform

2️⃣ Create Virtual Environment

python -m venv .venv

3️⃣ Activate Environment

Windows PowerShell

.\.venv\Scripts\Activate.ps1

4️⃣ Install Dependencies

pip install -r requirements.txt

📊 Dataset

The project uses synthetic BFSI datasets representing multiple business entities.

data/raw/

├── customers.csv
├── loans.csv
├── repayments.csv
├── transactions.csv
└── insurance_policies.csv

Dataset Coverage

Dataset

Purpose

customers.csv

Geography, segmentation, demographics, customer intelligence

loans.csv

Products, AUM, disbursals, exposure, DPD

repayments.csv

Amount due, amount paid, collections

transactions.csv

Customer activity and engagement

insurance_policies.csv

Insurance penetration and cross-sell

▶️ Running the Analytics Application

Run Streamlit Dashboard

python -m streamlit run .\app\app.py

The application provides an executive command center for:

Portfolio Overview

Credit Risk

Collections

Customer Intelligence

Insurance Cross-sell

AI-assisted Insights

Run Python Analytics

python .\python\analysis.py

📈 Core KPI Framework

Assets Under Management — AUM

AUM = Σ Outstanding Principal

Measures the outstanding principal represented by the active loan portfolio.

Disbursals

Disbursals = Σ Original Principal

Measures total original loan principal disbursed.

Delinquency Rate

Delinquency Rate =
Overdue Active Loans / Active Loans

Used to monitor overdue exposure across the active portfolio.

NPL Proxy

NPL Proxy =
Loans with DPD >= 90 / Active Loans

⚠️ This is an analytical proxy only and is not a regulatory NPA/NPL calculation.

Collection Efficiency

Collection Efficiency =
Amount Collected / Amount Due

Measures the percentage of due amounts successfully collected.

Insurance Cross-sell Rate

Cross-sell Rate =
Customers with Active Insurance /
Eligible Active-loan Customers

Measures insurance penetration among eligible active-loan customers.

Yield

Yield =
Interest Income Proxy / Average Outstanding

Use this metric only when the underlying interest/income fields are available.

🖥️ Executive Dashboard

The Streamlit application is designed as a BFSI Executive Command Center.

📌 Executive Overview

Dashboard includes:

AUM

Disbursals

Total Loans

Delinquency

NPL Proxy

Collection Efficiency

Portfolio Health

Product Concentration

Business Snapshot

🔴 Credit Risk

Dashboard includes:

DPD Distribution

Risk Buckets

90+ DPD Exposure

Product Risk Matrix

Risk Concentration

🟢 Collections

Dashboard includes:

Collection Efficiency

Collection Gap

Recovery Analysis

Priority Accounts

Action-oriented Insights

🟣 Customer & Insurance

Dashboard includes:

Customer Segments

Insurance Penetration

Product Whitespace

Cross-sell Opportunities

🤖 AI Insight Copilot

Dashboard includes:

Risk Alerts

Concentration Insights

Collection Recommendations

Cross-sell Opportunities

🤖 AI Insight Copilot

FinSight AI follows a two-layer insight architecture.

Filtered KPI / Analytical Context
                │
                ▼
      Deterministic Insight Engine
                │
                ▼
          Always Available
                │
                ▼
        Optional OpenAI Layer
                │
                ▼
      Management-ready Narrative

Deterministic Insight Layer

The dashboard remains functional without an API key.

Business rules convert filtered KPI signals into structured management insights.

Optional OpenAI Layer

When OPENAI_API_KEY is configured, the application can generate a management-ready narrative using the filtered analytical context.

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

🧠 SQL / BigQuery Analytics Layer

The SQL layer follows a structured analytics flow:

Raw Data
   ↓
Staging
   ↓
Analytics Mart
   ↓
KPI Queries
   ↓
Risk / Collections / Customer Analysis

SQL Modules

File

Purpose

01_staging.sql

Staging layer

02_mart_portfolio.sql

Portfolio analytics mart

03_kpi_queries.sql

Core KPI calculations

04_credit_risk.sql

Credit-risk analysis

05_collections.sql

Collections analysis

06_customer_insurance.sql

Customer and insurance analysis

📊 Power BI

Suggested Report Pages

Executive Overview

Credit Risk

Collections

Customer & Insurance

Growth / Cross-sell

Recommended Visuals

KPI Cards

Portfolio by Product

DPD Distribution

Risk Matrix

State / Region Analysis

Collection Gap

Customer Segment Analysis

Screenshots

powerbi/screenshots/

📈 Tableau

Suggested Views

Portfolio Overview

Product Risk Matrix

DPD Distribution

Collections Gap

Insurance Penetration

Geography / Branch Analysis where supported by the dataset

Screenshots

tableau/screenshots/

📗 Advanced Excel

Supporting analyst workflows include:

KPI reconciliation

Pivot analysis

Lookups / aggregation

Exception tracking

Management summaries

Workbook

excel/FinSight_BFSI_Analytics.xlsx

📉 R & SAS

R

Exploratory data analysis and statistical visualization:

r/eda.R

SAS

Structured credit-risk and portfolio analysis:

sas/risk_analysis.sas

🧪 Data Quality & Testing

Automated validation includes:

Required input files

Required columns

Loan ID uniqueness

Non-negative DPD

Monetary value validation

Insurance flag validation

Repayment field validation

Run Tests

python -m pytest -q

Compile-check Python

python -m compileall app python tests

✅ Project Validation Checklist

Before sharing the project with recruiters:

✅ Streamlit dashboard runs

✅ Python code compiles

✅ Unit/data-quality tests included

✅ Synthetic data clearly labelled

✅ Secrets excluded from Git

✅ SQL layer documented

✅ BI folders prepared

✅ Interview documentation included

⬜ Add final Power BI screenshots

⬜ Add final Tableau screenshots

📷 Project Screenshots

Add your actual screenshots to the corresponding folder before publishing this section.

Executive Dashboard



Power BI Dashboard



Tableau Dashboard



SQL / Analytics



AI Insight Copilot



💼 Interview Pitch

30-Second Version

“FinSight AI is an end-to-end BFSI analytics platform I built to simulate a retail lending and customer-intelligence environment. I connected customer, loan, repayment, transaction, and insurance data; built SQL and Python analytics layers; added credit-risk and collections analysis; and exposed the final KPIs through an executive Streamlit dashboard with optional AI-assisted insights.”

🎤 Key Interview Discussion Areas

Be prepared to explain:

Why AUM matters for portfolio concentration

How DPD acts as a credit-risk signal

Why 90+ DPD is used as an analytical NPL proxy

How collection efficiency is calculated

How collection priority can be ranked

How customer-product whitespace supports cross-sell

How the prototype could evolve from CSV → BigQuery → Semantic BI Layer

Why synthetic data is used for portfolio demonstration

How AI insights should remain grounded in KPI data

⚠️ Important Limitations

FinSight AI is a portfolio simulation, not a live banking platform.

Do not present it as:

Real customer performance

Production underwriting

Regulatory NPA reporting

Real profitability

Real-time banking data

Production-grade model-risk approval

unless those capabilities are actually implemented and validated.

🔮 Production Roadmap

A future production-oriented architecture could evolve toward:

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

Future Enhancements

Cloud-native data ingestion

Incremental data pipelines

dbt transformation layer

Enterprise semantic layer

ML-based credit-risk models

Advanced collection prioritization

Customer lifetime-value modelling

Production monitoring and governance

Role-based access and security

Automated insight distribution

⭐ Why This Project Matters

The goal is not to demonstrate a long list of tools.

The goal is to demonstrate the ability to convert:

Business Problem
      ↓
Data
      ↓
Validation
      ↓
Analysis
      ↓
KPI
      ↓
Visualization
      ↓
Insight
      ↓
Business Action

This project therefore demonstrates a complete analyst-to-decision workflow across BFSI lending, risk, collections, customer intelligence, BI, and AI-assisted analytics.

👨‍💻 Author

Mihirr Dobariya

Data Analyst | AI/ML Engineer | GenAI & Analytics Enthusiast

GitHub:

https://github.com/mihirr00051

LinkedIn:

https://www.linkedin.com/in/mihirr51

🙏 Acknowledgements

This project uses and demonstrates:

Python

Pandas

NumPy

SQL

Google BigQuery SQL

Power BI

Tableau

Streamlit

Plotly

R

SAS

Advanced Excel

Pytest

Git

GitHub

Optional OpenAI API

⭐ Support

If you found this project useful,

please consider giving it a ⭐ on GitHub.

📄 License

This project is released under the MIT License.

<p align="center">

Made with ❤️ by Mihirr Dobariya

</p>
