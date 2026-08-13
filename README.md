<div align="center">

🚀 FinSight AI

BFSI Lending • Credit Risk • Collections • Customer Intelligence

Enterprise-style Decision Intelligence & Analytics Platform

<br/>










<br/>

Portfolio Project • BFSI • Data Analytics • Business Intelligence • AI-assisted Insights

</div>

✨ What is FinSight AI?

FinSight AI is a synthetic BFSI decision-intelligence platform that simulates how a retail bank or NBFC can combine:

Customers • Loans • Repayments • Transactions • Insurance

into one analytical workflow for portfolio management, credit risk, collections, customer intelligence, and cross-sell decisions.

🎯 Core objective

Turn:

Business Problem → Data → Analysis → KPI → Visualization → Insight → Action

into a single, interview-ready analytics solution.

⚠️ Data Disclaimer: All datasets are synthetic and intended only for portfolio and learning purposes.

🧭 Quick Navigation

Section

Section

Section

Business Problem

Architecture

Tech Stack

Data Model

KPI Framework

Executive Dashboard

AI Copilot

SQL / BigQuery

Power BI

Tableau

Testing

Quick Start

Interview Pitch

Roadmap

Author

💼 Business Problem

BFSI leadership needs a trusted analytical layer to answer questions such as:

Business Question

Analytical Area

How large is the active portfolio?

Portfolio Management

Which products drive AUM concentration?

Portfolio Mix

Where is delinquency concentrated?

Credit Risk

Which accounts need collection priority?

Collections

Which customers show product whitespace?

Customer Intelligence

Where are insurance cross-sell opportunities?

Cross-sell

How can KPIs become management actions?

Decision Intelligence

FinSight AI connects these questions through one reusable analytical workflow.

🎯 What the Project Demonstrates

🏦 Portfolio Management

AUM and disbursal analysis

Product concentration

Portfolio mix

Business KPI monitoring

🔴 Credit Risk

DPD bucket analysis

Delinquency monitoring

90+ DPD / NPL analytical proxy

Product-level risk comparison

🟢 Collections

Collection efficiency

Collection gap

Priority account logic

Recovery-focused recommendations

🟣 Customer Intelligence

Customer segmentation

Product penetration

Transaction activity

Customer value signals

🟠 Insurance Cross-sell

Insurance penetration

Product whitespace

Eligible customer opportunity analysis

🤖 AI-assisted Analytics

KPI interpretation

Risk alerts

Concentration insights

Collection recommendations

Cross-sell suggestions

🏗️ Solution Architecture

┌──────────────────────────────────────────────────────────┐
│                  SYNTHETIC BFSI DATA                    │
│ Customers │ Loans │ Repayments │ Transactions │ Insurance│
└────────────────────────────┬─────────────────────────────┘
                             │
                             ▼
┌──────────────────────────────────────────────────────────┐
│              DATA VALIDATION & PROFILING                 │
│ Schema • Duplicates • Missing • Range • Quality Checks  │
└────────────────────────────┬─────────────────────────────┘
                             │
                             ▼
┌──────────────────────────────────────────────────────────┐
│              ANALYTICS DATA LAYER                        │
│                 Raw → Staging → Marts                   │
│                   BigQuery-ready SQL                    │
└────────────────────────────┬─────────────────────────────┘
                             │
              ┌──────────────┼──────────────┐
              ▼              ▼              ▼
        ┌──────────┐   ┌──────────┐   ┌────────────┐
        │ Python/R │   │   SAS    │   │ SQL / BQ   │
        │ EDA + KPI│   │ Risk     │   │ KPI + Risk │
        └────┬─────┘   └────┬─────┘   └─────┬──────┘
             └──────────────┼───────────────┘
                            ▼
┌──────────────────────────────────────────────────────────┐
│                 BI / KPI LAYER                          │
│                 Power BI • Tableau                      │
└────────────────────────────┬─────────────────────────────┘
                             │
                             ▼
┌──────────────────────────────────────────────────────────┐
│              FINSIGHT AI EXECUTIVE APP                  │
│                  Streamlit • Plotly                     │
└────────────────────────────┬─────────────────────────────┘
                             │
                             ▼
┌──────────────────────────────────────────────────────────┐
│                 AI INSIGHT COPILOT                      │
│        Deterministic Rules + Optional OpenAI            │
└────────────────────────────┬─────────────────────────────┘
                             │
                             ▼
                  ┌──────────────────────┐
                  │ Business Decisions   │
                  │      & Actions       │
                  └──────────────────────┘

🧰 Technology Stack

<table>
<tr>
<th>Layer</th>
<th>Technology</th>
<th>Purpose</th>
</tr>

<tr>
<td>Programming</td>
<td>Python, Pandas, NumPy</td>
<td>Data preparation & analytics</td>
</tr>

<tr>
<td>Querying</td>
<td>SQL, BigQuery SQL</td>
<td>KPI, portfolio & risk analysis</td>
</tr>

<tr>
<td>BI</td>
<td>Power BI, Tableau</td>
<td>Business reporting & dashboards</td>
</tr>

<tr>
<td>Application</td>
<td>Streamlit, Plotly</td>
<td>Interactive executive analytics</td>
</tr>

<tr>
<td>Statistics</td>
<td>R, SAS</td>
<td>EDA & structured risk analysis</td>
</tr>

<tr>
<td>Spreadsheet</td>
<td>Advanced Excel</td>
<td>Reconciliation & analyst workflows</td>
</tr>

<tr>
<td>AI</td>
<td>Deterministic Engine, Optional OpenAI</td>
<td>Management-ready insights</td>
</tr>

<tr>
<td>Testing</td>
<td>Pytest</td>
<td>Project & data-quality validation</td>
</tr>

<tr>
<td>Version Control</td>
<td>Git, GitHub</td>
<td>Source-code management</td>
</tr>
</table>

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

🗃️ Data Model

<details>
<summary><b>customers.csv</b> — Customer intelligence</summary>

Used for:

Geography

Segmentation

Demographic analysis

Customer intelligence

</details>

<details>
<summary><b>loans.csv</b> — Lending & risk</summary>

Used for:

Product analysis

AUM

Disbursals

Outstanding exposure

DPD / risk analysis

</details>

<details>
<summary><b>repayments.csv</b> — Collections</summary>

Used for:

Amount due

Amount paid

Collection efficiency

Collection gap

</details>

<details>
<summary><b>transactions.csv</b> — Customer activity</summary>

Used for:

Engagement analysis

Transaction behavior

Segmentation support

</details>

<details>
<summary><b>insurance_policies.csv</b> — Cross-sell</summary>

Used for:

Insurance penetration

Product whitespace

Cross-sell opportunity

</details>

📈 Core KPI Framework

KPI

Formula

Business Purpose

AUM

Σ Outstanding Principal

Portfolio size

Disbursals

Σ Original Principal

Originations / lending volume

Delinquency Rate

Overdue Active Loans / Active Loans

Delinquency monitoring

NPL Proxy

Loans with DPD >= 90 / Active Loans

Analytical risk signal

Collection Efficiency

Amount Collected / Amount Due

Collections performance

Cross-sell Rate

Customers with Active Insurance / Eligible Active-loan Customers

Insurance penetration

Yield

Interest Income Proxy / Average Outstanding

Yield analysis where fields exist

⚠️ NPL Proxy is analytical only and is not a regulatory NPA/NPL calculation.

🖥️ Executive Dashboard

FinSight AI is designed as a BFSI Executive Command Center.

📊 Executive Overview

AUM

Disbursals

Loan count

Delinquency

NPL Proxy

Collection Efficiency

Portfolio Health

Product Concentration

🔴 Credit Risk

DPD Distribution

Risk Buckets

90+ DPD Exposure

Product Risk Matrix

Risk Concentration

🟢 Collections

Collection Efficiency

Collection Gap

Recovery Analysis

Priority Accounts

🟣 Customer & Insurance

Customer Segments

Insurance Penetration

Product Whitespace

Cross-sell Opportunities

🤖 AI Insights

Risk Alerts

Concentration Insights

Collection Recommendations

Cross-sell Opportunities

🤖 AI Insight Copilot

FinSight AI uses a two-layer insight architecture:

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

Deterministic Layer

The dashboard remains functional without an API key.

Optional OpenAI Layer

When OPENAI_API_KEY is configured, the application can generate a management-ready narrative using the filtered analytical context.

🛡️ AI Guardrails

Do not send customer PII

Ground insights in available KPI data

Keep source values visible

Separate facts from recommendations

Never present synthetic results as real banking performance

🔍 Example Management Insights

Signal

Management Action

🔴 90+ DPD exposure

Prioritize high-risk products / segments

🟦 High product concentration

Review concentration alongside delinquency

🟢 High collection gap

Prioritize recovery-focused accounts

🟣 Low insurance penetration

Target eligible high-value customers

🧠 SQL / BigQuery Layer

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

KPI calculations

04_credit_risk.sql

Credit-risk analysis

05_collections.sql

Collections analysis

06_customer_insurance.sql

Customer + insurance analysis

📊 Power BI

Recommended Report Pages

Executive Overview → Credit Risk → Collections → Customer & Insurance → Growth / Cross-sell

Recommended Visuals

KPI Cards

Portfolio by Product

DPD Distribution

Risk Matrix

State / Region Analysis

Collection Gap

Customer Segment Analysis

📁 Screenshots:

powerbi/screenshots/

📈 Tableau

Suggested Views

Portfolio Overview

Product Risk Matrix

DPD Distribution

Collections Gap

Insurance Penetration

Geography / Branch Analysis where supported by the dataset

📁 Screenshots:

tableau/screenshots/

📗 Advanced Excel

Supporting workflows:

KPI reconciliation

Pivot analysis

Lookups / aggregation

Exception tracking

Management summaries

📄 Workbook:

excel/FinSight_BFSI_Analytics.xlsx

📉 R & SAS

R

r/eda.R

Exploratory data analysis and statistical visualization.

SAS

sas/risk_analysis.sas

Structured credit-risk and portfolio analysis.

🧪 Data Quality & Testing

Automated validation covers:

Required input files

Required columns

Loan ID uniqueness

Non-negative DPD

Monetary values

Insurance flags

Repayment fields

Run tests

python -m pytest -q

Python compile check

python -m compileall app python tests

🚀 Quick Start

1. Clone

git clone https://github.com/mihirr00051/BFSI-Lending-Risk-Intelligence-Platform.git
cd BFSI-Lending-Risk-Intelligence-Platform

2. Create environment

python -m venv .venv

3. Activate — Windows PowerShell

.\.venv\Scripts\Activate.ps1

4. Install

pip install -r requirements.txt

5. Run dashboard

python -m streamlit run .\app\app.py

6. Run analytics

python .\python\analysis.py

7. Run tests

python -m pytest -q

✅ Project Validation

Check

Status

Streamlit dashboard

✅

Python compile check

✅

Data-quality / unit tests

✅

Synthetic data labelled

✅

Secrets excluded from Git

✅

SQL layer documented

✅

BI structure prepared

✅

Interview documentation

✅

Final Power BI screenshots

⬜

Final Tableau screenshots

⬜

🖼️ Project Screenshots

Replace the following files with your actual screenshots before publishing.

Executive Dashboard

screenshots/streamlit-dashboard.png

Power BI

screenshots/powerbi-dashboard.png

Tableau

screenshots/tableau-dashboard.png

AI Insight Copilot

screenshots/ai-insights.png

💼 Interview Pitch

🎤 30-Second Version

“FinSight AI is an end-to-end BFSI analytics platform I built to simulate a retail lending and customer-intelligence environment. I connected customer, loan, repayment, transaction, and insurance data; built SQL and Python analytics layers; added credit-risk and collections analysis; and exposed the final KPIs through an executive Streamlit dashboard with optional AI-assisted insights.”

Key discussion areas

Why AUM matters for portfolio concentration

How DPD acts as a credit-risk signal

Why 90+ DPD is used as an analytical proxy

How collection efficiency is calculated

How collection priority can be ranked

How product whitespace supports cross-sell

How CSV analytics could evolve toward BigQuery and a semantic BI layer

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

Cloud-native ingestion

Incremental data pipelines

dbt transformation layer

Semantic data model

ML-based credit-risk scoring

Advanced collections prioritization

Customer lifetime-value analytics

Role-based access and security

Production monitoring & governance

⭐ Why This Project Matters

The value of this project is not the number of tools used.

It is the ability to convert a business problem into measurable decisions:

<div align="center">

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

</div>

That is the core analyst-to-decision workflow demonstrated by FinSight AI.

👨‍💻 Author

<div align="center">

Mihirr Dobariya

Data Analyst • AI/ML Engineer • GenAI & Analytics





</div>

📄 License

This project is released under the MIT License.

<div align="center">

⭐ If this project is useful, consider starring the repository.

Built with Python • SQL • BI • Analytics • AI

</div>
