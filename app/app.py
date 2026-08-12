import os
from pathlib import Path

import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st


# ============================================================
# PAGE + GLOBAL STYLING
# ============================================================

st.set_page_config(
    page_title="FinSight AI | BFSI Intelligence",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown(
    """
    <style>
        /* ---------- App background ---------- */
        .stApp {
            background:
                radial-gradient(circle at 15% 0%, rgba(37,99,235,.10), transparent 28%),
                radial-gradient(circle at 85% 5%, rgba(16,185,129,.08), transparent 25%),
                linear-gradient(135deg, #f8fbff 0%, #f4f7fb 52%, #eef3f9 100%);
        }

        /* ---------- Main container ---------- */
        .block-container {
            max-width: 1650px;
            padding-top: 0.9rem;
            padding-bottom: 2rem;
        }


        /* ============================================================
           PREMIUM 3D / FINTECH UI SYSTEM
           ============================================================ */

        :root {
            --navy: #08111f;
            --navy-2: #101c32;
            --blue: #2563eb;
            --blue-2: #60a5fa;
            --green: #10b981;
            --purple: #8b5cf6;
            --red: #ef4444;
            --amber: #f59e0b;
            --surface: rgba(255,255,255,.86);
            --surface-strong: rgba(255,255,255,.96);
            --border: rgba(148,163,184,.24);
            --shadow: 0 18px 45px rgba(15,23,42,.10);
        }

        [data-testid="stAppViewContainer"] {
            background:
                radial-gradient(circle at 7% 3%, rgba(59,130,246,.12), transparent 24%),
                radial-gradient(circle at 90% 10%, rgba(139,92,246,.10), transparent 22%),
                linear-gradient(140deg, #eef5ff 0%, #f8fbff 48%, #edf4fb 100%);
        }

        .block-container {
            max-width: 1540px !important;
            padding-top: 1.15rem !important;
            padding-bottom: 2rem !important;
        }

        /* ---------- Premium hero ---------- */
        .hero {
            position: relative;
            overflow: hidden;
            background:
                radial-gradient(circle at 88% 18%, rgba(96,165,250,.25), transparent 22%),
                radial-gradient(circle at 15% 110%, rgba(139,92,246,.18), transparent 28%),
                linear-gradient(145deg, #08111f 0%, #121f36 58%, #16253f 100%);
            border-radius: 28px;
            padding: 28px 30px 25px 30px;
            margin-bottom: 15px;
            border: 1px solid rgba(255,255,255,.08);
            box-shadow: 0 22px 55px rgba(15,23,42,.22);
        }

        .hero::before {
            content: "";
            position: absolute;
            width: 190px;
            height: 190px;
            right: -65px;
            top: -85px;
            border-radius: 50%;
            border: 1px solid rgba(255,255,255,.10);
            box-shadow:
                0 0 0 18px rgba(255,255,255,.018),
                0 0 0 36px rgba(255,255,255,.014);
        }

        .hero-title {
            position: relative;
            z-index: 2;
            color: #ffffff;
            font-size: clamp(34px, 4vw, 46px);
            font-weight: 900;
            letter-spacing: -1.4px;
            text-shadow: 0 2px 15px rgba(0,0,0,.22);
        }

        .hero-subtitle {
            position: relative;
            z-index: 2;
            color: #dbeafe !important;
            font-size: 14px;
            font-weight: 650;
        }

        /* ---------- LIVE status ---------- */
        .live-status-card,
        .hero-pill {
            position: relative;
            overflow: hidden;
            border-radius: 999px !important;
            background: rgba(16,185,129,.12) !important;
            border: 1px solid rgba(16,185,129,.40) !important;
            color: #86efac !important;
            box-shadow:
                inset 0 1px 0 rgba(255,255,255,.10),
                0 0 18px rgba(16,185,129,.10);
            backdrop-filter: blur(10px);
        }

        .live-dot,
        .live-status-dot {
            width: 10px !important;
            height: 10px !important;
            min-width: 10px !important;
            border-radius: 50% !important;
            background: #22c55e !important;
            box-shadow:
                0 0 0 4px rgba(34,197,94,.12),
                0 0 15px rgba(34,197,94,.78);
        }

        @keyframes premiumLive {
            0%, 100% { transform: scale(1); box-shadow: 0 0 0 4px rgba(34,197,94,.10), 0 0 15px rgba(34,197,94,.65); }
            50% { transform: scale(1.18); box-shadow: 0 0 0 7px rgba(34,197,94,.06), 0 0 20px rgba(34,197,94,.90); }
        }

        .live-dot,
        .live-status-dot {
            animation: premiumLive 1.7s infinite ease-in-out;
        }

        /* ---------- 3D KPI cards ---------- */
        .kpi-card {
            position: relative;
            overflow: hidden;
            min-height: 136px;
            padding: 18px 17px 16px 17px !important;
            background:
                linear-gradient(145deg, rgba(255,255,255,.98), rgba(245,249,255,.88));
            border: 1px solid rgba(148,163,184,.24) !important;
            border-radius: 20px !important;
            box-shadow:
                0 12px 24px rgba(15,23,42,.08),
                inset 0 1px 0 rgba(255,255,255,.85);
            transition: transform .18s ease, box-shadow .18s ease;
        }

        .kpi-card:hover {
            transform: translateY(-5px);
            box-shadow:
                0 19px 36px rgba(15,23,42,.12),
                inset 0 1px 0 rgba(255,255,255,.90);
        }

        .kpi-card::before {
            content: "";
            position: absolute;
            inset: 0;
            pointer-events: none;
            background:
                linear-gradient(120deg, rgba(255,255,255,.38), transparent 28%),
                radial-gradient(circle at 105% 105%, var(--kpi-glow, rgba(37,99,235,.10)), transparent 40%);
        }

        .kpi-icon {
            position: relative;
            width: 46px !important;
            height: 46px !important;
            min-width: 46px !important;
            border-radius: 15px !important;
            font-size: 22px !important;
            border: 1px solid rgba(255,255,255,.72) !important;
            box-shadow:
                0 10px 16px rgba(15,23,42,.15),
                inset 0 1px 2px rgba(255,255,255,.85),
                inset 0 -5px 10px rgba(15,23,42,.05);
            transform: perspective(500px) rotateX(7deg) rotateY(-5deg);
        }

        .kpi-icon::after {
            content: "";
            position: absolute;
            inset: 2px;
            border-radius: 13px;
            border-top: 1px solid rgba(255,255,255,.65);
            pointer-events: none;
        }

        .kpi-label {
            color: #475569 !important;
            font-size: 11px !important;
            font-weight: 900 !important;
            letter-spacing: 1.05px !important;
        }

        .kpi-value {
            color: #0b1324 !important;
            font-size: clamp(24px, 2vw, 31px) !important;
            font-weight: 900 !important;
            text-shadow: 0 1px 0 #fff;
        }

        .kpi-caption {
            color: #7c8aa0 !important;
            font-size: 10.5px !important;
        }

        /* ---------- Department cards ---------- */
        .dept-heading-title {
            color: #0b1324 !important;
            font-size: 22px !important;
            font-weight: 950 !important;
        }

        .dept-heading-sub {
            color: #64748b !important;
            font-size: 12px !important;
        }

        .native-dept-icon {
            position: relative;
            width: 54px !important;
            height: 54px !important;
            border-radius: 17px !important;
            font-size: 27px !important;
            background:
                linear-gradient(145deg, #ffffff, #dbeafe) !important;
            border: 1px solid rgba(255,255,255,.85) !important;
            box-shadow:
                0 12px 22px rgba(37,99,235,.16),
                inset 0 2px 3px rgba(255,255,255,.95),
                inset 0 -7px 12px rgba(37,99,235,.06);
            transform: perspective(600px) rotateX(7deg) rotateY(-7deg);
        }


        .native-dept-icon.blue {
            background: linear-gradient(145deg,#eff6ff,#60a5fa) !important;
            box-shadow: 0 12px 24px rgba(37,99,235,.24), inset 0 2px 3px rgba(255,255,255,.92), inset 0 -8px 12px rgba(37,99,235,.08);
        }

        .native-dept-icon.red {
            background: linear-gradient(145deg,#fff1f2,#fb7185) !important;
            box-shadow: 0 12px 24px rgba(239,68,68,.20), inset 0 2px 3px rgba(255,255,255,.92), inset 0 -8px 12px rgba(239,68,68,.08);
        }

        .native-dept-icon.green {
            background: linear-gradient(145deg,#ecfdf5,#34d399) !important;
            box-shadow: 0 12px 24px rgba(16,185,129,.20), inset 0 2px 3px rgba(255,255,255,.92), inset 0 -8px 12px rgba(16,185,129,.08);
        }

        .native-dept-icon.purple {
            background: linear-gradient(145deg,#f5f3ff,#a78bfa) !important;
            box-shadow: 0 12px 24px rgba(139,92,246,.20), inset 0 2px 3px rgba(255,255,255,.92), inset 0 -8px 12px rgba(139,92,246,.08);
        }

        .native-dept-icon.amber {
            background: linear-gradient(145deg,#fffbeb,#fbbf24) !important;
            box-shadow: 0 12px 24px rgba(245,158,11,.20), inset 0 2px 3px rgba(255,255,255,.92), inset 0 -8px 12px rgba(245,158,11,.08);
        }

        .native-dept-icon::after {
            content: "";
            position: absolute;
            left: 9px;
            right: 9px;
            top: 6px;
            height: 10px;
            border-radius: 50%;
            background: rgba(255,255,255,.62);
            filter: blur(1px);
        }

        /* ---------- Native card polish ---------- */
        div[data-testid="stVerticalBlockBorderWrapper"] {
            border-radius: 18px !important;
            border: 1px solid rgba(148,163,184,.22) !important;
            background: linear-gradient(145deg, rgba(255,255,255,.97), rgba(248,250,252,.90)) !important;
            box-shadow:
                0 11px 24px rgba(15,23,42,.07),
                inset 0 1px 0 rgba(255,255,255,.90);
        }

        /* ---------- Section headers ---------- */
        .section-head {
            display: flex;
            align-items: center;
            gap: 12px;
            margin: 16px 0 5px 0;
        }

        .section-icon {
            width: 42px !important;
            height: 42px !important;
            min-width: 42px !important;
            border-radius: 13px !important;
            font-size: 20px !important;
            background: linear-gradient(145deg, #ffffff, #dbeafe) !important;
            border: 1px solid #c8dbf6 !important;
            box-shadow:
                0 9px 20px rgba(37,99,235,.13),
                inset 0 1px 2px rgba(255,255,255,.95);
        }

        .section-title {
            color: #0b1324 !important;
            font-size: 20px !important;
            font-weight: 900 !important;
        }

        .section-subtitle {
            color: #64748b !important;
            font-size: 12px !important;
        }

        /* ---------- AI insight cards ---------- */
        .insight-card {
            background:
                linear-gradient(145deg, rgba(255,255,255,.98), rgba(247,249,252,.90));
            border-radius: 18px !important;
            border: 1px solid rgba(148,163,184,.22) !important;
            box-shadow:
                0 11px 24px rgba(15,23,42,.07),
                inset 0 1px 0 rgba(255,255,255,.90);
        }

        .insight-title {
            color: #0b1324 !important;
            font-weight: 900 !important;
        }

        .insight-text {
            color: #334155 !important;
            font-size: 13px !important;
            line-height: 1.55 !important;
        }

        /* ---------- Plotly panel shell ---------- */
        div[data-testid="stPlotlyChart"] {
            border-radius: 18px;
            border: 1px solid rgba(148,163,184,.18);
            background: rgba(255,255,255,.70);
            box-shadow:
                0 10px 25px rgba(15,23,42,.06),
                inset 0 1px 0 rgba(255,255,255,.85);
            padding: 4px;
        }

        /* ---------- Tables ---------- */
        div[data-testid="stDataFrame"] {
            border-radius: 16px;
            overflow: hidden;
            border: 1px solid rgba(148,163,184,.20);
            box-shadow: 0 8px 18px rgba(15,23,42,.05);
        }

        /* ---------- Hide Streamlit chrome ---------- */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}

        /* ---------- Main content readability ---------- */
        [data-testid="stAppViewContainer"] .stMarkdown,
        [data-testid="stAppViewContainer"] .stCaption,
        [data-testid="stAppViewContainer"] p,
        [data-testid="stAppViewContainer"] label {
            color: #0f172a;
        }

        [data-testid="stAppViewContainer"] [data-testid="stCaptionContainer"] * {
            color: #64748b !important;
        }

        /* Keep important dashboard content stable after mouse selection */
        .hero, .kpi-card, .dept-heading, .dept-card,
        .section-head, .section-subtitle, .health-card,
        .insight-card, .live-status-card {
            user-select: none;
            -webkit-user-select: none;
        }

        ::selection {
            background: #bfdbfe;
            color: #0f172a;
        }


        /* ---------- Premium Sidebar ---------- */
        section[data-testid="stSidebar"] {
            background:
                radial-gradient(circle at 15% 0%, rgba(37,99,235,.16), transparent 28%),
                linear-gradient(180deg, #07101d 0%, #0c1727 58%, #0a1423 100%);
            border-right: 1px solid rgba(148,163,184,.12);
            box-shadow: 14px 0 40px rgba(2,6,23,.13);
        }

        section[data-testid="stSidebar"] > div:first-child {
            padding-top: 1.35rem;
        }

        section[data-testid="stSidebar"] h2,
        section[data-testid="stSidebar"] h3 {
            color: #f8fafc !important;
            letter-spacing: -.2px;
        }

        section[data-testid="stSidebar"] .stCaption {
            color: #94a3b8 !important;
        }

        /* Selectbox containers */
        section[data-testid="stSidebar"] div[data-baseweb="select"] > div {
            background: rgba(255,255,255,.045) !important;
            border: 1px solid rgba(148,163,184,.18) !important;
            border-radius: 13px !important;
            min-height: 46px !important;
            box-shadow:
                inset 0 1px 0 rgba(255,255,255,.05),
                0 7px 18px rgba(2,6,23,.12);
        }

        section[data-testid="stSidebar"] div[data-baseweb="select"] > div:hover {
            border-color: rgba(96,165,250,.58) !important;
            background: rgba(255,255,255,.065) !important;
        }

        section[data-testid="stSidebar"] [role="option"] {
            background: #0d1726 !important;
            color: #f8fafc !important;
        }

        section[data-testid="stSidebar"] [role="option"][aria-selected="true"] {
            background: #17263d !important;
            color: #bfdbfe !important;
        }

        /* Sidebar reset button */
        section[data-testid="stSidebar"] div.stButton > button {
            min-height: 44px;
            border-radius: 13px;
            background: linear-gradient(145deg, rgba(255,255,255,.10), rgba(255,255,255,.04));
            color: #f8fafc;
            border: 1px solid rgba(148,163,184,.22);
            box-shadow:
                0 10px 18px rgba(2,6,23,.16),
                inset 0 1px 0 rgba(255,255,255,.08);
        }

        section[data-testid="stSidebar"] div.stButton > button:hover {
            border-color: rgba(96,165,250,.55);
            background: linear-gradient(145deg, rgba(59,130,246,.18), rgba(255,255,255,.06));
        }

        .sidebar-brand {
            display:flex;
            align-items:center;
            gap:12px;
            padding:13px 12px;
            border-radius:16px;
            background:linear-gradient(145deg,rgba(255,255,255,.08),rgba(255,255,255,.03));
            border:1px solid rgba(148,163,184,.12);
            box-shadow:0 12px 25px rgba(2,6,23,.14);
            margin-bottom:8px;
        }

        .sidebar-brand-icon {
            width:42px;
            height:42px;
            border-radius:13px;
            display:flex;
            align-items:center;
            justify-content:center;
            font-size:21px;
            background:linear-gradient(145deg,#dbeafe,#60a5fa);
            box-shadow:0 8px 18px rgba(37,99,235,.24), inset 0 1px 2px rgba(255,255,255,.85);
        }

        .sidebar-brand-title {
            color:#ffffff;
            font-size:17px;
            font-weight:900;
            letter-spacing:-.4px;
        }

        .sidebar-brand-sub {
            color:#94a3b8;
            font-size:10px;
            margin-top:2px;
        }

        /* ---------- Sidebar ---------- */
        section[data-testid="stSidebar"] {
            background: linear-gradient(180deg, #0b1220 0%, #111827 100%);
            border-right: 1px solid rgba(255,255,255,.08);
        }

        section[data-testid="stSidebar"] * {
            color: #f8fafc !important;
        }

        section[data-testid="stSidebar"] label {
            color: #cbd5e1 !important;
            font-weight: 600;
        }

        /* ---------- Hero ---------- */
        .hero {
            background:
                linear-gradient(135deg, rgba(15,23,42,.98), rgba(17,24,39,.97)),
                radial-gradient(circle at 80% 10%, rgba(59,130,246,.35), transparent 25%);
            border-radius: 24px;
            padding: 28px 30px;
            margin-bottom: 20px;
            box-shadow: 0 20px 45px rgba(15,23,42,.16);
            border: 1px solid rgba(255,255,255,.08);
        }

        .hero-title {
            color: #ffffff;
            font-size: 38px;
            font-weight: 850;
            letter-spacing: -1px;
            margin: 0;
        }

        .hero-subtitle {
            color: #dbeafe;
            font-size: 15px;
            font-weight: 600;
            margin-top: 8px;
        }

        .hero-pill {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            margin-top: 14px;
            background: rgba(16,185,129,.14);
            color: #bbf7d0;
            border: 1px solid rgba(52,211,153,.35);
            border-radius: 999px;
            padding: 7px 13px;
            font-size: 12px;
            font-weight: 800;
            animation: liveGlow 2s infinite;
        }

        .live-dot {
            width: 9px;
            height: 9px;
            border-radius: 50%;
            background: #22c55e;
            display: inline-block;
            box-shadow: 0 0 0 0 rgba(34,197,94,.55);
            animation: livePulse 1.6s infinite;
        }

        @keyframes livePulse {
            0% { box-shadow: 0 0 0 0 rgba(34,197,94,.55); }
            70% { box-shadow: 0 0 0 8px rgba(34,197,94,0); }
            100% { box-shadow: 0 0 0 0 rgba(34,197,94,0); }
        }

        @keyframes liveGlow {
            0%, 100% { box-shadow: 0 0 14px rgba(16,185,129,.06); }
            50% { box-shadow: 0 0 24px rgba(16,185,129,.15); }
        }

        /* ---------- KPI cards ---------- */
        .kpi-card {
            position: relative;
            overflow: hidden;
            background: linear-gradient(145deg, rgba(255,255,255,.98), rgba(248,250,252,.98));
            border: 1px solid #dbe4ef;
            border-radius: 18px;
            padding: 14px 15px;
            min-height: 112px;
            box-shadow: 0 10px 28px rgba(15,23,42,.07);
            transition: all .18s ease;
        }

        .kpi-card:hover {
            transform: translateY(-2px);
            box-shadow: 0 14px 34px rgba(15,23,42,.11);
        }

        .kpi-card::after {
            content: "";
            position: absolute;
            right: -24px;
            bottom: -30px;
            width: 88px;
            height: 88px;
            border-radius: 50%;
            background: var(--kpi-glow, rgba(37,99,235,.08));
        }

        .kpi-top {
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .kpi-icon {
            width: 34px;
            height: 34px;
            min-width: 34px;
            border-radius: 11px;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            font-size: 17px;
            background: var(--kpi-icon-bg, #dbeafe);
            border: 1px solid rgba(15,23,42,.06);
            box-shadow: 0 5px 13px rgba(15,23,42,.08);
        }

        .kpi-label {
            color: #334155;
            font-size: 11px;
            font-weight: 850;
            text-transform: uppercase;
            letter-spacing: 1px;
        }

        .kpi-value {
            color: #0f172a;
            font-size: 25px;
            font-weight: 850;
            margin-top: 10px;
            line-height: 1.1;
        }

        .kpi-caption {
            color: #94a3b8;
            font-size: 11px;
            margin-top: 5px;
        }

        /* ---------- Section headers ---------- */

        .native-dept-icon {
            width: 48px;
            height: 48px;
            border-radius: 14px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 25px;
            background: linear-gradient(145deg, #eff6ff, #dbeafe);
            border: 1px solid #bfdbfe;
            box-shadow: 0 8px 20px rgba(37,99,235,.16);
            margin-bottom: 10px;
        }

        /* Make native department containers visually pop */
        div[data-testid="stVerticalBlockBorderWrapper"] {
            border-radius: 16px !important;
            border: 1px solid #dbe4ef !important;
            background: linear-gradient(145deg, #ffffff, #f8fafc) !important;
            box-shadow: 0 8px 22px rgba(15,23,42,.06);
        }

        .section-head {
            display: flex;
            align-items: center;
            gap: 10px;
            margin: 13px 0 5px 0;
        }

        .section-icon {
            width: 34px;
            height: 34px;
            min-width: 34px;
            border-radius: 10px;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            font-size: 17px;
            background: linear-gradient(145deg, #eff6ff, #dbeafe);
            border: 1px solid #cfe0f4;
            box-shadow: 0 6px 16px rgba(37,99,235,.10);
        }

        .section-title {
            color: #0f172a;
            font-size: 21px;
            font-weight: 900;
            margin: 0;
            letter-spacing: -.3px;
        }

        .section-subtitle {
            color: #64748b;
            font-size: 12px;
            margin: 0 0 12px 44px;
        }

        /* ---------- Insight cards ---------- */
        .insight-card {
            position: relative;
            background: linear-gradient(145deg, #ffffff, #f8fafc);
            border-radius: 16px;
            border: 1px solid #e1e8f0;
            padding: 14px 15px 14px 16px;
            margin-bottom: 10px;
            box-shadow: 0 7px 20px rgba(15,23,42,.055);
            transition: all .16s ease;
        }

        .insight-card:hover {
            transform: translateY(-1px);
            box-shadow: 0 10px 24px rgba(15,23,42,.09);
        }

        .insight-card::before {
            content: "";
            position: absolute;
            left: 0;
            top: 12px;
            bottom: 12px;
            width: 4px;
            border-radius: 5px;
            background: linear-gradient(180deg, #2563eb, #8b5cf6);
        }

        /* ---------- Health score ---------- */
        .health-card {
            background: linear-gradient(135deg, #ffffff 0%, #f8fafc 100%);
            border: 1px solid #e2e8f0;
            border-radius: 20px;
            padding: 18px;
            box-shadow: 0 8px 24px rgba(15,23,42,.06);
        }

        .health-label {
            color: #64748b;
            font-size: 12px;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: .7px;
        }

        /* ---------- Hide Streamlit default footer ---------- */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}

        /* ============================================================
           FINAL RESPONSIVE / READABILITY OVERRIDES
           ============================================================ */

        .block-container {
            width: 100% !important;
            max-width: 100% !important;
            padding-left: 1.15rem !important;
            padding-right: 1.15rem !important;
            padding-top: 1rem !important;
        }

        section.main > div {
            max-width: 100% !important;
        }

        .hero {
            min-height: 155px;
            display: flex;
            flex-direction: column;
            justify-content: center;
        }

        .hero-title {
            font-size: clamp(30px, 3vw, 46px);
            line-height: 1.05;
        }

        .hero-subtitle {
            font-size: 15px;
            line-height: 1.5;
            max-width: 980px;
        }

        .hero-pill {
            width: fit-content;
            min-height: 34px;
        }

        .kpi-card {
            min-height: 132px;
            padding: 17px 16px;
        }

        .kpi-icon {
            width: 40px;
            height: 40px;
            min-width: 40px;
            font-size: 20px;
            border-radius: 12px;
        }

        .kpi-label {
            font-size: 12px;
            letter-spacing: .9px;
        }

        .kpi-value {
            font-size: clamp(22px, 2vw, 30px);
            margin-top: 12px;
        }

        .kpi-caption {
            font-size: 11px;
        }

        .dept-grid {
            display: grid;
            grid-template-columns: repeat(5, minmax(0, 1fr));
            gap: 12px;
            margin-top: 3px;
        }

        .dept-card {
            position: relative;
            overflow: hidden;
            min-height: 132px;
            padding: 15px 15px 14px 15px;
            border-radius: 16px;
            background: linear-gradient(145deg, #ffffff 0%, #f8fafc 100%);
            border: 1px solid #d9e2ec;
            box-shadow: 0 8px 22px rgba(15,23,42,.07);
            transition: transform .18s ease, box-shadow .18s ease, border-color .18s ease;
        }

        .dept-card:hover {
            transform: translateY(-4px);
            box-shadow: 0 15px 30px rgba(15,23,42,.12);
            border-color: #c4d4e7;
        }

        .dept-card-top {
            height: 4px;
            width: 100%;
            border-radius: 999px;
            margin-bottom: 12px;
        }

        .dept-card-top.blue, .dept-icon.blue {
            background: linear-gradient(135deg, #2563eb, #60a5fa);
        }

        .dept-card-top.red, .dept-icon.red {
            background: linear-gradient(135deg, #dc2626, #fb7185);
        }

        .dept-card-top.green, .dept-icon.green {
            background: linear-gradient(135deg, #059669, #34d399);
        }

        .dept-card-top.purple, .dept-icon.purple {
            background: linear-gradient(135deg, #7c3aed, #a78bfa);
        }

        .dept-card-top.amber, .dept-icon.amber {
            background: linear-gradient(135deg, #d97706, #fbbf24);
        }

        .dept-icon {
            width: 42px;
            height: 42px;
            border-radius: 13px;
            display: flex;
            align-items: center;
            justify-content: center;
            color: #ffffff !important;
            font-size: 21px;
            box-shadow: 0 8px 18px rgba(15,23,42,.16);
            margin-bottom: 11px;
        }

        .dept-card-title {
            color: #0f172a !important;
            font-size: 13px;
            line-height: 1.2;
            font-weight: 850;
            letter-spacing: -.1px;
        }

        .dept-card-desc {
            color: #64748b !important;
            font-size: 10.5px;
            line-height: 1.45;
            margin-top: 6px;
            max-width: 92%;
        }

        .dept-card-arrow {
            position: absolute;
            right: 13px;
            bottom: 12px;
            width: 25px;
            height: 25px;
            border-radius: 8px;
            display: flex;
            align-items: center;
            justify-content: center;
            color: #334155 !important;
            background: #f1f5f9;
            font-size: 18px;
            font-weight: 800;
        }

        .dept-heading {
            display:flex;
            align-items:center;
            justify-content:space-between;
            gap:16px;
            margin:4px 0 9px 0;
        }

        .dept-heading-title {
            color:#0f172a;
            font-size:20px;
            font-weight:900;
            letter-spacing:-.3px;
        }

        .dept-heading-sub {
            color:#64748b;
            font-size:12px;
            margin-top:2px;
        }

        .dept-heading-badge {
            display:inline-flex;
            align-items:center;
            min-height:28px;
            padding:0 10px;
            border-radius:999px;
            background:#eff6ff;
            color:#1d4ed8;
            border:1px solid #bfdbfe;
            font-size:10px;
            font-weight:850;
            letter-spacing:.7px;
        }

        .dept-accent {
            height:4px;
            border-radius:999px;
            margin:0 5px -3px 5px;
            position:relative;
            z-index:2;
        }

        .dept-accent.blue { background:#2563eb; }
        .dept-accent.red { background:#ef4444; }
        .dept-accent.green { background:#10b981; }
        .dept-accent.purple { background:#8b5cf6; }
        .dept-accent.amber { background:#f59e0b; }

                div[data-baseweb="tab-list"] {
            gap: 8px !important;
            background: #eaf0f7;
            padding: 6px !important;
            border-radius: 14px;
        }

        button[data-baseweb="tab"] {
            min-height: 46px !important;
            border-radius: 10px !important;
            padding: 0 15px !important;
            font-size: 13px !important;
            font-weight: 850 !important;
        }

        button[data-baseweb="tab"][aria-selected="true"] {
            background: #ffffff !important;
            color: #1d4ed8 !important;
            box-shadow: 0 4px 12px rgba(15,23,42,.08);
        }

        div[data-testid="stPlotlyChart"] {
            background: rgba(255,255,255,.72);
            border: 1px solid #e2e8f0;
            border-radius: 16px;
            padding: 4px 6px 0 6px;
            box-shadow: 0 7px 18px rgba(15,23,42,.035);
        }

        [data-testid="stDataFrame"] {
            border: 1px solid #dbe4ef;
            border-radius: 14px;
            overflow: hidden;
            box-shadow: 0 7px 18px rgba(15,23,42,.035);
        }

        .live-status-card {
            display: inline-flex;
            align-items: center;
            gap: 9px;
            background: #ecfdf5;
            color: #166534;
            border: 1px solid #86efac;
            border-radius: 999px;
            padding: 7px 12px;
            font-size: 12px;
            font-weight: 850;
            box-shadow: 0 5px 15px rgba(22,163,74,.10);
        }

         live-status-dot {
            width: 9px;
            height: 9px;
            border-radius: 50%;
            background: #22c55e;
            box-shadow: 0 0 0 0 rgba(34,197,94,.45);
            animation: livePulse 1.5s infinite;
        }

        @media (max-width: 900px) {
            .dept-heading { flex-direction:column; align-items:flex-start; }
        }

        /* ---------- Premium navigation tabs ---------- */
        button[data-baseweb="tab"] {
            border-radius: 14px !important;
            padding: 10px 16px !important;
            margin-right: 4px !important;
            font-weight: 800 !important;
            color: #475569 !important;
            transition: all .18s ease !important;
        }

        button[data-baseweb="tab"]:hover {
            background: rgba(255,255,255,.72) !important;
            color: #0f172a !important;
        }

        button[data-baseweb="tab"][aria-selected="true"] {
            background: linear-gradient(145deg, #ffffff, #eef4ff) !important;
            color: #0b1324 !important;
            box-shadow:
                0 9px 18px rgba(15,23,42,.08),
                inset 0 1px 0 rgba(255,255,255,.9);
        }

        /* ---------- Tabs ---------- */
        button[data-baseweb="tab"] {
            font-weight: 750 !important;
            color: #64748b !important;
            padding-top: 8px !important;
            padding-bottom: 10px !important;
        }

        button[data-baseweb="tab"][aria-selected="true"] {
            color: #1d4ed8 !important;
        }

        /* ---------- Streamlit buttons ---------- */
        div.stButton > button,
        div.stDownloadButton > button {
            border-radius: 12px;
            font-weight: 750;
            border: 1px solid #cbd5e1;
            box-shadow: 0 5px 14px rgba(15,23,42,.06);
        }

        div.stDownloadButton > button {
            background: linear-gradient(135deg, #111827, #1f2937);
            color: #ffffff;
            border-color: #111827;
        }

        div.stDownloadButton > button:hover {
            background: linear-gradient(135deg, #1d4ed8, #2563eb);
            color: #ffffff;
        }

            @media (max-width: 700px) {
            .dept-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); }
            .dept-card { min-height: 124px; }
            .dept-card-title { font-size: 12px; }
            .dept-card-desc { font-size: 10px; }
        }

        /* ============================================================
           FIN-SIGHT PREMIUM LIGHT THEME
           ============================================================ */

        :root {
            --ink: #10233f;
            --muted: #64748b;
            --line: #dbe4ef;
            --surface: #ffffff;
            --surface-2: #f8fbff;
            --blue: #2563eb;
            --blue-soft: #eaf2ff;
            --green: #10b981;
            --green-soft: #eafaf4;
            --red: #ef4444;
            --red-soft: #fff0f0;
            --purple: #7c3aed;
            --purple-soft: #f3efff;
            --amber: #f59e0b;
            --amber-soft: #fff7e8;
        }

        /* ---------- App background ---------- */
        [data-testid="stAppViewContainer"] {
            background:
                radial-gradient(circle at 8% 0%, rgba(37,99,235,.055), transparent 23%),
                radial-gradient(circle at 92% 4%, rgba(124,58,237,.045), transparent 20%),
                linear-gradient(180deg, #f7faff 0%, #eef4fa 100%) !important;
        }

        .block-container {
            max-width: 1480px !important;
            padding: 1rem 1.05rem 2.5rem 1.05rem !important;
        }

        /* ---------- Sidebar: light ---------- */
        section[data-testid="stSidebar"] {
            background:
                linear-gradient(180deg, #ffffff 0%, #f7faff 100%) !important;
            border-right: 1px solid #d9e3ef !important;
            box-shadow: 10px 0 28px rgba(15,23,42,.055) !important;
        }

        section[data-testid="stSidebar"] * {
            color: var(--ink) !important;
        }

        section[data-testid="stSidebar"] .stCaption,
        section[data-testid="stSidebar"] small {
            color: var(--muted) !important;
        }

        .sidebar-brand {
            background: linear-gradient(145deg, #ffffff, #f4f8fd) !important;
            border: 1px solid #dce6f1 !important;
            box-shadow: 0 8px 20px rgba(15,23,42,.055) !important;
        }

        .sidebar-brand-icon {
            background: linear-gradient(145deg, #ffffff, #dbeafe) !important;
            color: #1d4ed8 !important;
            border: 1px solid #cfe0f6 !important;
        }

        .sidebar-brand-title {
            color: var(--ink) !important;
        }

        .sidebar-brand-sub {
            color: var(--muted) !important;
        }

        section[data-testid="stSidebar"] hr {
            border-color: #dbe4ef !important;
        }

        /* ---------- Select boxes ---------- */
        section[data-testid="stSidebar"] div[data-baseweb="select"] > div {
            background: #ffffff !important;
            border: 1px solid #cfdbea !important;
            color: var(--ink) !important;
            border-radius: 12px !important;
            min-height: 44px !important;
            box-shadow: inset 0 1px 0 rgba(255,255,255,.9) !important;
        }

        section[data-testid="stSidebar"] div[data-baseweb="select"] > div:hover {
            border-color: #8fb4ef !important;
            box-shadow: 0 0 0 3px rgba(37,99,235,.06) !important;
        }

        section[data-testid="stSidebar"] [role="listbox"],
        section[data-testid="stSidebar"] [role="option"] {
            background: #ffffff !important;
            color: #10233f !important;
        }

        section[data-testid="stSidebar"] [role="option"]:hover {
            background: #eef5ff !important;
        }

        section[data-testid="stSidebar"] [role="option"][aria-selected="true"] {
            background: #e8f1ff !important;
            color: #1d4ed8 !important;
            font-weight: 800 !important;
        }

        section[data-testid="stSidebar"] div.stButton > button {
            background: #ffffff !important;
            color: #10233f !important;
            border: 1px solid #cfdbea !important;
            border-radius: 12px !important;
            box-shadow: 0 7px 16px rgba(15,23,42,.05) !important;
        }

        section[data-testid="stSidebar"] div.stButton > button:hover {
            border-color: #8fb4ef !important;
            background: #f5f9ff !important;
        }

        /* ---------- Hero ---------- */
        .hero {
            background:
                radial-gradient(circle at 85% 10%, rgba(96,165,250,.20), transparent 22%),
                linear-gradient(135deg, #12233d 0%, #193152 100%) !important;
            border-radius: 22px !important;
            padding: 24px 26px !important;
            margin-bottom: 14px !important;
            box-shadow: 0 18px 42px rgba(15,23,42,.15) !important;
        }

        .hero-title {
            color: #ffffff !important;
            font-size: clamp(32px, 3.4vw, 44px) !important;
            font-weight: 900 !important;
        }

        .hero-subtitle,
        .hero-subtitle * {
            color: #dbeafe !important;
        }

        .hero-pill {
            background: rgba(16,185,129,.13) !important;
            border: 1px solid rgba(110,231,183,.42) !important;
            color: #bbf7d0 !important;
        }

        /* ---------- Live status ---------- */
        .live-status-card {
            background: #ecfdf5 !important;
            border: 1px solid #a7f3d0 !important;
            color: #047857 !important;
            box-shadow: 0 7px 16px rgba(16,185,129,.09) !important;
        }

        .live-status-card * {
            color: #047857 !important;
        }

        /* ---------- KPI cards ---------- */
        .kpi-card {
            background: linear-gradient(145deg, #ffffff 0%, #f9fbff 100%) !important;
            border: 1px solid #dbe5f0 !important;
            border-radius: 18px !important;
            min-height: 126px !important;
            box-shadow:
                0 10px 22px rgba(15,23,42,.055),
                inset 0 1px 0 rgba(255,255,255,.95) !important;
        }

        .kpi-card:hover {
            box-shadow:
                0 14px 30px rgba(15,23,42,.09),
                inset 0 1px 0 rgba(255,255,255,.95) !important;
        }

        .kpi-icon {
            border: 1px solid rgba(255,255,255,.95) !important;
            box-shadow:
                0 8px 15px rgba(15,23,42,.10),
                inset 0 1px 2px rgba(255,255,255,.95) !important;
        }

        .kpi-label {
            color: #52637a !important;
            font-size: 10px !important;
            font-weight: 900 !important;
        }

        .kpi-value {
            color: #0f2744 !important;
            font-weight: 900 !important;
        }

        .kpi-caption {
            color: #7d8da3 !important;
        }

        /* ---------- Business department cards ---------- */
        .native-dept-icon {
            border: 1px solid #cfe0f6 !important;
            box-shadow:
                0 9px 18px rgba(15,23,42,.08),
                inset 0 1px 2px rgba(255,255,255,.98) !important;
        }

        .native-dept-icon.blue {
            background: linear-gradient(145deg, #ffffff, #dbeafe) !important;
        }

        .native-dept-icon.red {
            background: linear-gradient(145deg, #ffffff, #fee2e2) !important;
        }

        .native-dept-icon.green {
            background: linear-gradient(145deg, #ffffff, #dcfce7) !important;
        }

        .native-dept-icon.purple {
            background: linear-gradient(145deg, #ffffff, #ede9fe) !important;
        }

        .native-dept-icon.amber {
            background: linear-gradient(145deg, #ffffff, #fef3c7) !important;
        }

        div[data-testid="stVerticalBlockBorderWrapper"] {
            background: rgba(255,255,255,.96) !important;
            border: 1px solid #dbe5f0 !important;
            border-radius: 16px !important;
            box-shadow: 0 8px 20px rgba(15,23,42,.055) !important;
        }

        /* ---------- Tabs ---------- */
        button[data-baseweb="tab"] {
            color: #50627a !important;
            border-radius: 12px !important;
            font-weight: 800 !important;
        }

        button[data-baseweb="tab"]:hover {
            background: #f5f9ff !important;
            color: #16385f !important;
        }

        button[data-baseweb="tab"][aria-selected="true"] {
            background: #ffffff !important;
            color: #16385f !important;
            box-shadow: 0 7px 15px rgba(15,23,42,.06) !important;
        }

        /* ---------- Section titles ---------- */
        .section-head {
            margin-top: 12px !important;
        }

        .section-icon {
            background: linear-gradient(145deg, #ffffff, #eaf2ff) !important;
            border: 1px solid #cfdff4 !important;
            box-shadow: 0 8px 15px rgba(15,23,42,.07) !important;
        }

        .section-title,
        .dept-heading-title {
            color: #122a48 !important;
        }

        .section-subtitle,
        .dept-heading-sub {
            color: #6b7d93 !important;
        }

        .dept-heading-badge {
            background: #eef5ff !important;
            color: #2563eb !important;
            border: 1px solid #cfe0fb !important;
        }

        /* ---------- Chart panels ---------- */
        div[data-testid="stPlotlyChart"] {
            background: rgba(255,255,255,.96) !important;
            border: 1px solid #dbe5f0 !important;
            border-radius: 16px !important;
            box-shadow: 0 8px 20px rgba(15,23,42,.05) !important;
            padding: 3px !important;
        }

        /* Force high chart contrast */
        div[data-testid="stPlotlyChart"] text {
            fill: #475569 !important;
        }

        /* ---------- Insight cards ---------- */
        .insight-card {
            background: linear-gradient(145deg, #ffffff, #f9fbff) !important;
            border: 1px solid #dbe5f0 !important;
            box-shadow: 0 8px 20px rgba(15,23,42,.055) !important;
        }

        .insight-title {
            color: #122a48 !important;
        }

        .insight-text {
            color: #44566d !important;
        }

        /* ---------- Health card ---------- */
        .health-card {
            background: linear-gradient(145deg, #ffffff, #f7faff) !important;
            border: 1px solid #dbe5f0 !important;
            box-shadow: 0 9px 22px rgba(15,23,42,.055) !important;
        }

        .health-label {
            color: #71839a !important;
        }

        /* ---------- Tables ---------- */
        div[data-testid="stDataFrame"] {
            border: 1px solid #dbe5f0 !important;
            border-radius: 14px !important;
            box-shadow: 0 7px 18px rgba(15,23,42,.05) !important;
        }

        /* ---------- Generic text readability ---------- */
        [data-testid="stAppViewContainer"] p,
        [data-testid="stAppViewContainer"] label,
        [data-testid="stAppViewContainer"] .stCaption {
            color: #4e627a !important;
        }

        /* ---------- Footer ---------- */
        [data-testid="stAppViewContainer"] hr {
            border-color: #dbe5f0 !important;
            
        }


        /* ============================================================
           FINAL TEXT HIGHLIGHT + LIVE STATUS SYSTEM
           ============================================================ */

        /* ---------- Global readable typography ---------- */
        .hero-title,
        .section-title,
        .dept-heading-title,
        .kpi-value,
        .kpi-label,
        .insight-title {
            text-rendering: geometricPrecision;
            -webkit-font-smoothing: antialiased;
        }

        .hero-title {
            letter-spacing: -1.5px !important;
            text-shadow: 0 2px 16px rgba(0,0,0,.24) !important;
        }

        .hero-subtitle {
            font-weight: 700 !important;
            letter-spacing: .05px !important;
        }

        .section-title,
        .dept-heading-title {
            font-weight: 900 !important;
            color: #102a47 !important;
        }

        .section-subtitle,
        .dept-heading-sub {
            color: #657890 !important;
            font-weight: 550 !important;
        }

        .kpi-label {
            color: #314866 !important;
            font-weight: 900 !important;
            letter-spacing: 1px !important;
        }

        .kpi-value {
            color: #0b2642 !important;
            font-weight: 950 !important;
            text-shadow: 0 1px 0 rgba(255,255,255,.9) !important;
        }

        .kpi-caption {
            color: #71839a !important;
            font-weight: 550 !important;
        }

        /* ============================================================
           HERO LIVE PORTFOLIO — DARK PREMIUM POP
           ============================================================ */

        .hero-pill {
            display: inline-flex !important;
            align-items: center !important;
            gap: 9px !important;
            margin-top: 14px !important;

            padding: 8px 15px !important;
            min-height: 36px !important;

            border-radius: 999px !important;

            background:
                linear-gradient(
                    135deg,
                    rgba(16,185,129,.22),
                    rgba(6,78,59,.30)
                ) !important;

            border: 1px solid rgba(52,211,153,.72) !important;

            color: #d1fae5 !important;

            font-size: 11.5px !important;
            font-weight: 900 !important;
            letter-spacing: .15px !important;

            box-shadow:
                0 0 0 1px rgba(16,185,129,.08),
                0 7px 20px rgba(16,185,129,.20),
                inset 0 1px 0 rgba(255,255,255,.12) !important;

            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);

            animation: heroLiveGlow 2.4s ease-in-out infinite;
        }

        .hero-pill span {
            color: inherit !important;
        }

        .hero-pill span:nth-child(2) {
            color: #ecfdf5 !important;
            font-weight: 950 !important;
            letter-spacing: .7px !important;
        }

        .hero-pill span:nth-child(4) {
            color: #bbf7d0 !important;
            font-weight: 750 !important;
        }

        /* ============================================================
           LIVE REAL-TIME FILTERED VIEW — LIGHT POP CARD
           ============================================================ */

        .live-status-card {
            display: inline-flex !important;
            align-items: center !important;
            gap: 9px !important;

            padding: 8px 14px !important;
            min-height: 38px !important;

            border-radius: 999px !important;

            background:
                linear-gradient(
                    135deg,
                    #ffffff 0%,
                    #f0fdf4 100%
                ) !important;

            border: 1px solid #86efac !important;

            color: #047857 !important;

            font-size: 11.5px !important;
            font-weight: 850 !important;

            box-shadow:
                0 7px 18px rgba(16,185,129,.12),
                0 0 0 1px rgba(16,185,129,.04),
                inset 0 1px 0 rgba(255,255,255,.95) !important;

            transition:
                transform .18s ease,
                box-shadow .18s ease,
                border-color .18s ease !important;
        }

        .live-status-card:hover {
            transform: translateY(-2px) !important;
            border-color: #34d399 !important;

            box-shadow:
                0 11px 26px rgba(16,185,129,.20),
                0 0 0 3px rgba(16,185,129,.06),
                inset 0 1px 0 rgba(255,255,255,.98) !important;
        }

        .live-status-card span {
            color: #047857 !important;
        }

        .live-status-card .live-status-dot {
            width: 9px !important;
            height: 9px !important;
            min-width: 9px !important;
            border-radius: 50% !important;

            background: #22c55e !important;
            border: 2px solid #ffffff !important;

            box-shadow:
                0 0 0 3px rgba(34,197,94,.13),
                0 0 13px rgba(34,197,94,.72) !important;

            animation: liveDotPulseFinal 1.55s ease-in-out infinite !important;
        }

        .live-status-card span:nth-child(2) {
            font-size: 10px !important;
            font-weight: 950 !important;
            letter-spacing: 1px !important;
            color: #047857 !important;
        }

        .live-status-card span:nth-child(3) {
            color: #166534 !important;
            font-weight: 800 !important;
        }

        /* ---------- Small status icon ---------- */
        live-status-card::before {
            content: "●";
            display: inline-flex;
            align-items: center;
            justify-content: center;

            width: 22px;
            height: 22px;

            border-radius: 7px;

            background: #dcfce7;
            color: #16a34a;

            font-size: 9px;
            font-weight: 950;

            box-shadow:
                inset 0 1px 2px rgba(255,255,255,.95),
                0 3px 8px rgba(16,185,129,.12);
        }

        @keyframes liveDotPulseFinal {
            0%, 100% {
                transform: scale(1);
                box-shadow:
                    0 0 0 3px rgba(34,197,94,.13),
                    0 0 13px rgba(34,197,94,.60);
            }

            50% {
                transform: scale(1.22);
                box-shadow:
                    0 0 0 7px rgba(34,197,94,.055),
                    0 0 21px rgba(34,197,94,.95);
            }
        }

        @keyframes heroLiveGlow {
            0%, 100% {
                box-shadow:
                    0 0 0 1px rgba(16,185,129,.08),
                    0 7px 20px rgba(16,185,129,.18),
                    inset 0 1px 0 rgba(255,255,255,.12);
            }

            50% {
                box-shadow:
                    0 0 0 2px rgba(52,211,153,.10),
                    0 10px 26px rgba(16,185,129,.30),
                    inset 0 1px 0 rgba(255,255,255,.16);
            }
        }

        /* ---------- Highlight filter status text ---------- */
         filter-update-text {
            display: inline-flex;
            align-items: center;
            gap: 6px;

            padding: 6px 10px;
            border-radius: 9px;

            background: #f1f5f9;
            border: 1px solid #dbe4ef;

            color: #52657c !important;

            font-size: 10px;
            font-weight: 800;

            box-shadow: inset 0 1px 0 rgba(255,255,255,.90);
        }

        .filter-update-text strong {
            color: #1d4ed8 !important;
            font-weight: 950;
        }

        /* ---------- Department title/description highlight ---------- */
        .native-dept-icon {
            transition:
                transform .18s ease,
                box-shadow .18s ease !important;
        }

        div[data-testid="stVerticalBlockBorderWrapper"]:hover .native-dept-icon {
            transform:
                perspective(600px)
                rotateX(7deg)
                rotateY(-6deg)
                translateY(-2px)
                scale(1.04) !important;

            box-shadow:
                0 13px 24px rgba(37,99,235,.14),
                inset 0 1px 2px rgba(255,255,255,.98) !important;
        }


        /* ============================================================
           FIN-SIGHT GRAPHIC DESIGNER OVERRIDE — FINAL UI/UX
           ============================================================ */

        /* ---------- GLOBAL LIGHT CANVAS ---------- */

        .stApp,
        [data-testid="stAppViewContainer"] {
            background:
                radial-gradient(circle at 8% 0%, rgba(37,99,235,.045), transparent 22%),
                radial-gradient(circle at 92% 0%, rgba(124,58,237,.035), transparent 20%),
                linear-gradient(180deg, #f9fbfe 0%, #eef4f9 100%) !important;
        }

        .block-container {
            max-width: 1500px !important;
            padding: 0.95rem 1.15rem 2.5rem !important;
        }

        /* ---------- SIDEBAR ---------- */

        section[data-testid="stSidebar"] {
            background: linear-gradient(180deg, #fbfdff 0%, #f2f7fb 100%) !important;
            border-right: 1px solid #d5e0eb !important;
            box-shadow: 10px 0 28px rgba(16,42,67,.05) !important;
        }

        section[data-testid="stSidebar"] * {
            color: #17324f !important;
        }

        section[data-testid="stSidebar"] hr {
            border-color: #dbe5ef !important;
        }

        .sidebar-brand {
            background: linear-gradient(145deg, #ffffff, #f4f8fc) !important;
            border: 1px solid #dbe5ef !important;
            border-radius: 17px !important;
            box-shadow: 0 8px 20px rgba(16,42,67,.06) !important;
        }

        .sidebar-brand-icon {
            background: linear-gradient(145deg, #ffffff, #dbeafe) !important;
            border: 1px solid #cfe0f5 !important;
            box-shadow: 0 8px 18px rgba(37,99,235,.12), inset 0 1px 2px #fff !important;
        }

        .sidebar-brand-title {
            color: #102a43 !important;
        }

        .sidebar-brand-sub {
            color: #71849a !important;
        }

        section[data-testid="stSidebar"] div[data-baseweb="select"] > div {
            background: #ffffff !important;
            border: 1px solid #cbd9e7 !important;
            border-radius: 12px !important;
            min-height: 44px !important;
            box-shadow:
                inset 0 1px 0 rgba(255,255,255,.98),
                0 4px 12px rgba(16,42,67,.035) !important;
        }

        section[data-testid="stSidebar"] div[data-baseweb="select"] > div:hover {
            border-color: #79a4df !important;
            box-shadow:
                0 0 0 3px rgba(37,99,235,.055),
                0 5px 14px rgba(16,42,67,.04) !important;
        }

        section[data-testid="stSidebar"] [role="listbox"],
        section[data-testid="stSidebar"] [role="option"] {
            background: #ffffff !important;
            color: #17324f !important;
        }

        section[data-testid="stSidebar"] [role="option"]:hover {
            background: #edf4ff !important;
        }

        section[data-testid="stSidebar"] [role="option"][aria-selected="true"] {
            background: #e6f0ff !important;
            color: #1d4ed8 !important;
            font-weight: 850 !important;
        }

        section[data-testid="stSidebar"] div.stButton > button {
            background: #ffffff !important;
            color: #17324f !important;
            border: 1px solid #cbd9e7 !important;
            border-radius: 12px !important;
            box-shadow: 0 7px 16px rgba(16,42,67,.05) !important;
        }

        section[data-testid="stSidebar"] div.stButton > button:hover {
            background: #f4f8ff !important;
            border-color: #7aa7e4 !important;
        }

        /* ---------- HERO ---------- */

        .hero {
            min-height: 168px !important;
            padding: 27px 30px !important;
            border-radius: 24px !important;
            margin-bottom: 13px !important;
            background:
                radial-gradient(circle at 88% 15%, rgba(96,165,250,.24), transparent 23%),
                radial-gradient(circle at 18% 115%, rgba(124,58,237,.16), transparent 28%),
                linear-gradient(135deg, #132742 0%, #1a385c 100%) !important;
            border: 1px solid rgba(255,255,255,.10) !important;
            box-shadow: 0 20px 45px rgba(16,42,67,.16) !important;
        }

        .hero-title {
            color: #ffffff !important;
            font-size: clamp(34px, 4vw, 48px) !important;
            font-weight: 950 !important;
            letter-spacing: -1.7px !important;
            text-shadow: 0 3px 15px rgba(0,0,0,.20) !important;
        }

        .hero-subtitle,
        .hero-subtitle * {
            color: #dceaff !important;
            font-weight: 700 !important;
        }

        .hero-pill {
            display: inline-flex !important;
            align-items: center !important;
            gap: 8px !important;
            min-height: 37px !important;
            padding: 8px 14px !important;
            border-radius: 999px !important;
            background: linear-gradient(135deg, rgba(16,185,129,.20), rgba(6,95,70,.25)) !important;
            border: 1px solid rgba(74,222,128,.70) !important;
            color: #dcfce7 !important;
            box-shadow:
                0 0 0 1px rgba(16,185,129,.05),
                0 8px 22px rgba(16,185,129,.18),
                inset 0 1px 0 rgba(255,255,255,.12) !important;
            animation: heroLiveGlowUI 2.2s ease-in-out infinite;
        }

        .hero-pill * {
            color: #dcfce7 !important;
        }

        .hero-pill span:nth-child(2) {
            font-weight: 950 !important;
            letter-spacing: 1px !important;
        }

        .hero-note {
            color: #c7d6e7 !important;
            font-weight: 650 !important;
        }

        .live-dot,
        .live-status-dot {
            background: #22c55e !important;
            box-shadow:
                0 0 0 4px rgba(34,197,94,.10),
                0 0 15px rgba(34,197,94,.78) !important;
            animation: liveDotUI 1.55s ease-in-out infinite !important;
        }

        @keyframes liveDotUI {
            0%,100% { transform: scale(1); }
            50% { transform: scale(1.20); }
        }

        @keyframes heroLiveGlowUI {
            0%,100% {
                box-shadow:
                    0 0 0 1px rgba(16,185,129,.05),
                    0 8px 22px rgba(16,185,129,.16),
                    inset 0 1px 0 rgba(255,255,255,.12);
            }
            50% {
                box-shadow:
                    0 0 0 2px rgba(52,211,153,.10),
                    0 11px 27px rgba(16,185,129,.28),
                    inset 0 1px 0 rgba(255,255,255,.15);
            }
        }

        /* ---------- LIVE REAL-TIME CARD ---------- */

        .live-bar {
            margin: -1px 0 14px !important;
        }

        .live-status-card {
            display: inline-flex !important;
            align-items: center !important;
            gap: 8px !important;
            padding: 8px 14px !important;
            min-height: 38px !important;
            border-radius: 999px !important;
            background: linear-gradient(135deg, #ffffff, #effdf6) !important;
            border: 1px solid #87e5b8 !important;
            color: #047857 !important;
            box-shadow:
                0 7px 18px rgba(16,185,129,.11),
                inset 0 1px 0 #fff !important;
        }

        .live-status-card * {
            color: #047857 !important;
        }

        .live-status-word {
            font-size: 10px !important;
            font-weight: 950 !important;
            letter-spacing: 1px !important;
        }

        .live-status-text {
            font-size: 11px !important;
            font-weight: 800 !important;
        }

        .filter-update-text {
            display: inline-flex !important;
            align-items: center !important;
            gap: 6px !important;
            padding: 7px 11px !important;
            border-radius: 10px !important;
            background: #f7fbff !important;
            border: 1px solid #dce6ef !important;
            color: #60748a !important;
            font-size: 10px !important;
            font-weight: 800 !important;
        }

        .filter-update-text strong {
            color: #2563eb !important;
        }

        /* ---------- KPI CARDS ---------- */

        .kpi-card {
            min-height: 134px !important;
            border-radius: 18px !important;
            background: linear-gradient(145deg, #ffffff, #f8fbff) !important;
            border: 1px solid #dce6f0 !important;
            box-shadow:
                0 9px 22px rgba(16,42,67,.055),
                inset 0 1px 0 #fff !important;
        }

        .kpi-card:hover {
            transform: translateY(-3px) !important;
            box-shadow: 0 15px 32px rgba(16,42,67,.10) !important;
        }

        .kpi-accent {
            height: 3px !important;
        }

        .kpi-icon {
            width: 45px !important;
            height: 45px !important;
            min-width: 45px !important;
            border-radius: 14px !important;
            box-shadow:
                0 8px 16px rgba(16,42,67,.10),
                inset 0 1px 2px rgba(255,255,255,.98) !important;
            transform: perspective(600px) rotateX(6deg) rotateY(-5deg);
        }

        .kpi-label {
            color: #3d5570 !important;
            font-size: 10px !important;
            font-weight: 950 !important;
            letter-spacing: 1px !important;
        }

        .kpi-value {
            color: #102a43 !important;
            font-size: clamp(24px, 2vw, 30px) !important;
            font-weight: 950 !important;
        }

        .kpi-caption {
            color: #7b8ea3 !important;
            font-size: 10px !important;
        }

        /* ---------- DEPARTMENT CARDS ---------- */

        div[data-testid="stVerticalBlockBorderWrapper"]:has(.native-dept-icon) {
            background: linear-gradient(145deg, #ffffff, #f9fbff) !important;
            border: 1px solid #dce6f0 !important;
            border-radius: 17px !important;
            box-shadow: 0 9px 22px rgba(16,42,67,.055), inset 0 1px 0 #fff !important;
            transition: transform .18s ease, box-shadow .18s ease !important;
        }

        div[data-testid="stVerticalBlockBorderWrapper"]:has(.native-dept-icon):hover {
            transform: translateY(-4px) !important;
            box-shadow: 0 16px 34px rgba(16,42,67,.10) !important;
        }

        .native-dept-icon {
            width: 52px !important;
            height: 52px !important;
            border-radius: 16px !important;
            box-shadow:
                0 10px 20px rgba(16,42,67,.10),
                inset 0 1px 2px #fff !important;
            transform: perspective(650px) rotateX(7deg) rotateY(-7deg);
        }

        /* Force department text to be readable */
        div[data-testid="stVerticalBlockBorderWrapper"]:has(.native-dept-icon) strong,
        div[data-testid="stVerticalBlockBorderWrapper"]:has(.native-dept-icon) [data-testid="stMarkdownContainer"] p {
            color: #17324f !important;
        }

        div[data-testid="stVerticalBlockBorderWrapper"]:has(.native-dept-icon) .stCaption {
            color: #72859a !important;
        }

        /* ---------- TABS ---------- */

        div[data-baseweb="tab-list"] {
            gap: 5px !important;
            padding: 5px !important;
            border-radius: 14px !important;
            background: #e8eef5 !important;
            margin-bottom: 9px !important;
        }

        button[data-baseweb="tab"] {
            min-height: 43px !important;
            padding: 0 14px !important;
            border-radius: 10px !important;
            color: #5c7087 !important;
            font-size: 12px !important;
            font-weight: 850 !important;
        }

        button[data-baseweb="tab"]:hover {
            background: #f7fbff !important;
            color: #17324f !important;
        }

        button[data-baseweb="tab"][aria-selected="true"] {
            background: #ffffff !important;
            color: #1d4ed8 !important;
            box-shadow: 0 5px 14px rgba(16,42,67,.07) !important;
        }

        /* ---------- SECTION TITLES ---------- */

        .section-head {
            margin-top: 10px !important;
        }

        .section-icon {
            width: 42px !important;
            height: 42px !important;
            min-width: 42px !important;
            border-radius: 13px !important;
            background: linear-gradient(145deg, #ffffff, #edf4ff) !important;
            border: 1px solid #cfdef0 !important;
            box-shadow: 0 7px 16px rgba(16,42,67,.08), inset 0 1px 2px #fff !important;
        }

        .section-title {
            color: #102a43 !important;
            font-size: 19px !important;
            font-weight: 950 !important;
        }

        .section-subtitle {
            color: #6f8297 !important;
        }

        /* ---------- CHART CONTAINERS ---------- */

        div[data-testid="stPlotlyChart"] {
            background: #ffffff !important;
            border: 1px solid #dbe5ef !important;
            border-radius: 16px !important;
            box-shadow: 0 8px 20px rgba(16,42,67,.055) !important;
            padding: 3px !important;
        }

        /* ---------- AI COPILOT ---------- */

        .ai-header {
            display: flex !important;
            justify-content: space-between !important;
            align-items: center !important;
            gap: 12px !important;
            margin-top: 16px !important;
            margin-bottom: 9px !important;
        }

        .ai-heading {
            display: flex !important;
            align-items: center !important;
            gap: 11px !important;
        }

        .ai-icon {
            width: 43px !important;
            height: 43px !important;
            border-radius: 13px !important;
            background: linear-gradient(145deg, #ffffff, #eee9ff) !important;
            border: 1px solid #d9d0fb !important;
            box-shadow: 0 8px 17px rgba(124,58,237,.10), inset 0 1px 2px #fff !important;
        }

        .ai-title {
            color: #102a43 !important;
            font-size: 20px !important;
            font-weight: 950 !important;
        }

        .ai-subtitle {
            color: #71849a !important;
            font-size: 11px !important;
        }

        .ai-active {
            display: inline-flex !important;
            align-items: center !important;
            gap: 7px !important;
            padding: 7px 11px !important;
            border-radius: 999px !important;
            background: #ecfdf5 !important;
            border: 1px solid #a7f3d0 !important;
            color: #047857 !important;
            font-size: 9px !important;
            font-weight: 950 !important;
            letter-spacing: .9px !important;
        }

        .insight-card {
            background: linear-gradient(145deg, #ffffff, #f8fbff) !important;
            border: 1px solid #dce6f0 !important;
            border-radius: 16px !important;
            box-shadow: 0 8px 20px rgba(16,42,67,.055) !important;
        }

        .insight-title {
            color: #163452 !important;
            font-weight: 950 !important;
        }

        .insight-text {
            color: #53677d !important;
        }

        /* ---------- GENERAL TEXT CONTRAST ---------- */

        [data-testid="stAppViewContainer"] p,
        [data-testid="stAppViewContainer"] label,
        [data-testid="stAppViewContainer"] .stCaption {
            color: #5e7289;
        }

        /* ---------- TABLES ---------- */

        div[data-testid="stDataFrame"] {
            border: 1px solid #dbe5ef !important;
            border-radius: 14px !important;
            box-shadow: 0 8px 18px rgba(16,42,67,.05) !important;
        }

        /* ---------- MOBILE ---------- */

        @media (max-width: 900px) {
            .hero { min-height: 150px; }
            .dept-header { flex-direction: column; align-items: flex-start; }
        }

    
        /* ============================================================
           FIN-SIGHT FINAL ART-DIRECTION SYSTEM
           ============================================================ */

        /* ---------- Full-width professional canvas ---------- */
        .block-container {
            width: 100% !important;
            max-width: none !important;
            padding: 0.75rem 1.15rem 2.5rem 1.15rem !important;
        }

        section.main > div {
            max-width: none !important;
        }

        /* ---------- Sidebar: compact, premium, readable ---------- */
        section[data-testid="stSidebar"] {
            width: 255px !important;
            background: linear-gradient(180deg, #ffffff 0%, #f7faff 100%) !important;
            border-right: 1px solid #dce6f1 !important;
            box-shadow: 10px 0 28px rgba(15,23,42,.06) !important;
        }

        section[data-testid="stSidebar"] > div:first-child {
            padding: 1rem 0.85rem 1.25rem 0.85rem !important;
        }

        .sidebar-brand {
            padding: 11px 10px !important;
            border-radius: 14px !important;
            background: #ffffff !important;
            border: 1px solid #e0e8f2 !important;
            box-shadow: 0 7px 16px rgba(15,23,42,.05) !important;
        }

        .sidebar-brand-icon {
            width: 38px !important;
            height: 38px !important;
            border-radius: 11px !important;
            font-size: 19px !important;
        }

        .sidebar-brand-title {
            color: #102a47 !important;
            font-size: 16px !important;
        }

        .sidebar-brand-sub {
            color: #72849b !important;
            font-size: 9px !important;
        }

        section[data-testid="stSidebar"] label {
            color: #35506e !important;
            font-size: 12px !important;
            font-weight: 800 !important;
        }

        section[data-testid="stSidebar"] div[data-baseweb="select"] > div {
            min-height: 42px !important;
            border-radius: 11px !important;
            background: #ffffff !important;
            border: 1px solid #cfdaea !important;
            box-shadow: 0 3px 9px rgba(15,23,42,.035) !important;
        }

        section[data-testid="stSidebar"] div.stButton > button {
            min-height: 40px !important;
            border-radius: 11px !important;
            font-weight: 800 !important;
            background: #ffffff !important;
            border: 1px solid #cfdaea !important;
        }

        /* ---------- Hero: executive command header ---------- */
        .hero {
            min-height: 142px !important;
            display: flex !important;
            flex-direction: column !important;
            justify-content: center !important;
            padding: 24px 28px !important;
            margin-bottom: 12px !important;
            border-radius: 22px !important;
            background:
                radial-gradient(circle at 90% 20%, rgba(96,165,250,.20), transparent 23%),
                linear-gradient(135deg, #10243e 0%, #19375a 100%) !important;
            box-shadow: 0 18px 38px rgba(15,23,42,.16) !important;
        }

        .hero-title {
            font-size: clamp(34px, 3.3vw, 47px) !important;
            line-height: 1 !important;
            letter-spacing: -1.7px !important;
        }

        .hero-subtitle {
            font-size: 14px !important;
            font-weight: 700 !important;
            margin-top: 8px !important;
        }

        /* ---------- LIVE badge ---------- */
        .hero-pill {
            width: fit-content !important;
            margin-top: 13px !important;
            padding: 8px 14px !important;
            min-height: 34px !important;
            border-radius: 999px !important;
            background: linear-gradient(135deg, rgba(16,185,129,.22), rgba(6,78,59,.28)) !important;
            border: 1px solid rgba(52,211,153,.72) !important;
            color: #d1fae5 !important;
            box-shadow: 0 8px 20px rgba(16,185,129,.16) !important;
        }

        .live-status-card {
            padding: 8px 13px !important;
            min-height: 36px !important;
            background: #effcf5 !important;
            color: #047857 !important;
            border: 1px solid #9ce8be !important;
            box-shadow: 0 6px 16px rgba(16,185,129,.10) !important;
        }

        /* ---------- KPI row: executive, compact ---------- */
        .kpi-card {
            min-height: 118px !important;
            padding: 15px 14px 13px 14px !important;
            border-radius: 17px !important;
            background: linear-gradient(145deg, #ffffff, #f8fbff) !important;
            border: 1px solid #dbe5f0 !important;
            box-shadow:
                0 8px 19px rgba(15,23,42,.055),
                inset 0 1px 0 rgba(255,255,255,.95) !important;
        }

        .kpi-top {
            gap: 9px !important;
        }

        .kpi-icon {
            width: 38px !important;
            height: 38px !important;
            min-width: 38px !important;
            border-radius: 12px !important;
            font-size: 18px !important;
        }

        .kpi-label {
            font-size: 10px !important;
            letter-spacing: .85px !important;
            color: #49617d !important;
        }

        .kpi-value {
            font-size: clamp(23px, 2.2vw, 30px) !important;
            margin-top: 9px !important;
            color: #0f2947 !important;
        }

        .kpi-caption {
            font-size: 10px !important;
            color: #8293a8 !important;
            margin-top: 4px !important;
        }

        /* ---------- Executive strip ---------- */
        .exec-strip {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 10px;
            margin: 4px 0 12px 0;
        }

        .exec-strip-item {
            display: flex;
            align-items: center;
            gap: 10px;
            min-height: 58px;
            padding: 9px 11px;
            border-radius: 13px;
            background: #ffffff;
            border: 1px solid #dbe5f0;
            box-shadow: 0 5px 13px rgba(15,23,42,.04);
        }

        .exec-strip-icon {
            width: 30px;
            height: 30px;
            min-width: 30px;
            display: flex;
            align-items: center;
            justify-content: center;
            border-radius: 9px;
            background: #eff5ff;
            color: #2563eb;
            border: 1px solid #cfe0f6;
            font-size: 9px;
            font-weight: 950;
        }

        .exec-strip-title {
            color: #183554;
            font-size: 11px;
            font-weight: 900;
        }

        .exec-strip-text {
            color: #8090a4;
            font-size: 9.5px;
            margin-top: 2px;
        }

        /* ---------- Department navigation ---------- */
        .dept-heading {
            margin: 2px 0 8px 0 !important;
        }

        .dept-heading-title {
            font-size: 20px !important;
            color: #122a48 !important;
        }

        .dept-heading-sub {
            font-size: 11px !important;
            color: #71839a !important;
        }

        .dept-heading-badge {
            padding: 0 9px !important;
            min-height: 26px !important;
            font-size: 9px !important;
        }

        div[data-testid="stVerticalBlockBorderWrapper"] {
            border-radius: 15px !important;
            border: 1px solid #dbe5f0 !important;
            background: #ffffff !important;
            box-shadow: 0 7px 16px rgba(15,23,42,.045) !important;
        }

        .native-dept-icon {
            width: 44px !important;
            height: 44px !important;
            min-width: 44px !important;
            border-radius: 13px !important;
            font-size: 22px !important;
            margin-bottom: 8px !important;
        }

        /* ---------- Navigation tabs ---------- */
        div[data-baseweb="tab-list"] {
            gap: 5px !important;
            padding: 5px !important;
            background: #edf3f9 !important;
            border-radius: 14px !important;
            margin-bottom: 2px !important;
        }

        button[data-baseweb="tab"] {
            min-height: 42px !important;
            padding: 0 14px !important;
            border-radius: 10px !important;
            color: #51677f !important;
            font-size: 11px !important;
            font-weight: 850 !important;
        }

        button[data-baseweb="tab"][aria-selected="true"] {
            background: #ffffff !important;
            color: #1d4ed8 !important;
            box-shadow: 0 5px 12px rgba(15,23,42,.07) !important;
        }

        /* ---------- Analytics sections ---------- */
        .section-head {
            gap: 10px !important;
            margin: 11px 0 4px 0 !important;
        }

        .section-icon {
            width: 38px !important;
            height: 38px !important;
            min-width: 38px !important;
            border-radius: 11px !important;
            font-size: 18px !important;
        }

        .section-title {
            font-size: 19px !important;
            color: #122a48 !important;
        }

        .section-subtitle {
            font-size: 10.5px !important;
            margin-left: 48px !important;
            color: #71839a !important;
        }

        /* ---------- Chart cards ---------- */
        div[data-testid="stPlotlyChart"] {
            background: #ffffff !important;
            border: 1px solid #dbe5f0 !important;
            border-radius: 15px !important;
            padding: 2px 5px 0 5px !important;
            box-shadow: 0 7px 17px rgba(15,23,42,.045) !important;
        }

        /* ---------- AI copilot ---------- */
        .insight-card {
            min-height: 100px !important;
            padding: 13px 15px !important;
            border-radius: 15px !important;
            background: #ffffff !important;
            border: 1px solid #dbe5f0 !important;
            box-shadow: 0 7px 17px rgba(15,23,42,.045) !important;
        }

        .insight-title {
            font-size: 13px !important;
            color: #173553 !important;
        }

        .insight-text {
            font-size: 11px !important;
            line-height: 1.5 !important;
            color: #53677f !important;
        }

        /* ---------- Responsive ---------- */
        @media (max-width: 1150px) {
            .exec-strip {
                grid-template-columns: 1fr;
            }
        }

        @media (max-width: 900px) {
            section[data-testid="stSidebar"] {
                width: 230px !important;
            }

            .hero-title {
                font-size: 32px !important;
            }
        }

        @media (max-width: 720px) {
            .block-container {
                padding-left: .65rem !important;
                padding-right: .65rem !important;
            }
        }


        /* ============================================================
           FIN-SIGHT 10/10 ART DIRECTION
           ============================================================ */

        .block-container {
            width: 100% !important;
            max-width: none !important;
            padding: .7rem 1.15rem 2.4rem 1.15rem !important;
        }

        section.main > div {
            max-width: none !important;
        }

        section[data-testid="stSidebar"] {
            width: 250px !important;
            background: linear-gradient(180deg,#ffffff 0%,#f7faff 100%) !important;
            border-right: 1px solid #dce5ef !important;
            box-shadow: 9px 0 26px rgba(15,23,42,.045) !important;
        }

        section[data-testid="stSidebar"] > div:first-child {
            padding: .95rem .8rem 1.2rem .8rem !important;
        }

        section[data-testid="stSidebar"] label {
            color: #35506e !important;
            font-size: 11px !important;
            font-weight: 850 !important;
        }

        section[data-testid="stSidebar"] div[data-baseweb="select"] > div {
            min-height: 42px !important;
            border-radius: 11px !important;
            background: #ffffff !important;
            border: 1px solid #cfdbea !important;
        }

        .hero {
            min-height: 140px !important;
            padding: 23px 27px !important;
            border-radius: 22px !important;
            margin-bottom: 10px !important;
            background:
                radial-gradient(circle at 90% 10%,rgba(96,165,250,.22),transparent 22%),
                linear-gradient(135deg,#10243f 0%,#19375a 100%) !important;
            box-shadow: 0 17px 36px rgba(15,23,42,.14) !important;
        }

        .hero-title {
            font-size: clamp(34px,3.15vw,46px) !important;
            line-height: 1 !important;
            letter-spacing: -1.7px !important;
        }

        .hero-pill {
            padding: 8px 14px !important;
            min-height: 34px !important;
            box-shadow: 0 7px 18px rgba(16,185,129,.16) !important;
        }

        .live-status-card {
            padding: 8px 13px !important;
            min-height: 36px !important;
            background: #effcf5 !important;
            border-color: #9ce8be !important;
        }

        .kpi-card {
            min-height: 116px !important;
            padding: 14px 13px 12px 13px !important;
            border-radius: 16px !important;
            box-shadow: 0 8px 18px rgba(15,23,42,.05) !important;
        }

        .kpi-icon {
            width: 38px !important;
            height: 38px !important;
            min-width: 38px !important;
            font-size: 18px !important;
            border-radius: 11px !important;
        }

        .kpi-label {
            font-size: 9.5px !important;
            letter-spacing: .8px !important;
            color: #49617d !important;
        }

        .kpi-value {
            font-size: clamp(23px,2.15vw,30px) !important;
            margin-top: 8px !important;
            color: #0f2947 !important;
        }

        .kpi-caption {
            font-size: 9.5px !important;
            color: #8293a8 !important;
        }

        .exec-strip {
            display:grid;
            grid-template-columns:repeat(3,minmax(0,1fr));
            gap:10px;
            margin:3px 0 11px 0;
        }

        .exec-strip-item {
            min-height:56px;
            display:flex;
            align-items:center;
            gap:10px;
            padding:8px 10px;
            border:1px solid #dce6f0;
            border-radius:12px;
            background:#ffffff;
            box-shadow:0 5px 12px rgba(15,23,42,.035);
        }

        .exec-strip-icon {
            width:28px;
            height:28px;
            min-width:28px;
            border-radius:8px;
            display:flex;
            align-items:center;
            justify-content:center;
            background:#eef5ff;
            color:#2563eb;
            border:1px solid #cfe0f6;
            font-size:9px;
            font-weight:950;
        }

        .exec-strip-title {
            color:#173553;
            font-size:10.5px;
            font-weight:900;
        }

        .exec-strip-text {
            color:#8292a7;
            font-size:9px;
            margin-top:2px;
        }

        .dept-heading {
            margin:2px 0 7px 0 !important;
        }

        .dept-heading-title {
            color:#122a48 !important;
            font-size:19px !important;
        }

        .dept-heading-sub {
            color:#72839a !important;
            font-size:10.5px !important;
        }

        .dept-heading-badge {
            min-height:25px !important;
            padding:0 9px !important;
            font-size:9px !important;
        }

        div[data-testid="stVerticalBlockBorderWrapper"] {
            background:#ffffff !important;
            border:1px solid #dce6f0 !important;
            border-radius:14px !important;
            box-shadow:0 6px 14px rgba(15,23,42,.035) !important;
        }

        .native-dept-icon {
            width:43px !important;
            height:43px !important;
            min-width:43px !important;
            border-radius:12px !important;
            font-size:21px !important;
        }

        div[data-baseweb="tab-list"] {
            gap:5px !important;
            background:#edf3f9 !important;
            border-radius:13px !important;
            padding:5px !important;
            margin-bottom:8px !important;
        }

        button[data-baseweb="tab"] {
            min-height:41px !important;
            padding:0 14px !important;
            font-size:10.5px !important;
            border-radius:10px !important;
        }

        button[data-baseweb="tab"][aria-selected="true"] {
            color:#1d4ed8 !important;
            background:#ffffff !important;
        }

        .section-head {
            margin:10px 0 3px 0 !important;
            gap:9px !important;
        }

        .section-icon {
            width:36px !important;
            height:36px !important;
            min-width:36px !important;
            border-radius:10px !important;
            font-size:17px !important;
        }

        .section-title {
            color:#122a48 !important;
            font-size:18px !important;
            font-weight:900 !important;
        }

        .section-subtitle {
            margin-left:45px !important;
            font-size:10px !important;
            color:#71839a !important;
        }

        div[data-testid="stPlotlyChart"] {
            background:#ffffff !important;
            border:1px solid #dce6f0 !important;
            border-radius:14px !important;
            box-shadow:0 6px 15px rgba(15,23,42,.035) !important;
            padding:2px 4px 0 4px !important;
        }

        .health-card {
            background:linear-gradient(145deg,#ffffff,#f8fbff) !important;
            border:1px solid #dce6f0 !important;
            border-radius:15px !important;
            padding:14px 15px !important;
            box-shadow:0 7px 16px rgba(15,23,42,.04) !important;
        }

        .health-status-row {
            display:flex;
            align-items:center;
            justify-content:space-between;
            gap:10px;
            margin-top:5px;
        }

        .health-status {
            color:#102a47;
            font-size:22px;
            font-weight:900;
        }

        .health-score-chip {
            padding:5px 8px;
            border-radius:8px;
            background:#eef5ff;
            color:#1d4ed8;
            border:1px solid #cfe0f6;
            font-size:10px;
            font-weight:900;
        }

        .health-explain {
            color:#6c7d93;
            font-size:10px;
            line-height:1.45;
            margin-top:5px;
        }

        .health-mini {
            display:grid;
            grid-template-columns:repeat(3,1fr);
            gap:6px;
            margin-top:9px;
        }

        .health-mini span {
            padding:6px 7px;
            border-radius:8px;
            background:#f5f8fc;
            border:1px solid #e1e8f0;
            color:#6b7c91;
            font-size:9px;
        }

        .health-mini b {
            display:block;
            color:#23415e;
            font-size:9px;
            margin-bottom:1px;
        }

        .snapshot-grid {
            display:grid;
            grid-template-columns:repeat(2,minmax(0,1fr));
            gap:9px;
        }

        .snapshot-card {
            position:relative;
            min-height:88px;
            padding:11px 12px;
            border-radius:12px;
            background:#ffffff;
            border:1px solid #dce6f0;
            box-shadow:0 6px 14px rgba(15,23,42,.035);
            overflow:hidden;
        }

        .snapshot-card::after {
            content:"";
            position:absolute;
            right:-18px;
            bottom:-22px;
            width:62px;
            height:62px;
            border-radius:50%;
            opacity:.75;
        }

        .snapshot-card.blue::after { background:#dbeafe; }
        .snapshot-card.purple::after { background:#ede9fe; }
        .snapshot-card.amber::after { background:#fef3c7; }
        .snapshot-card.green::after { background:#dcfce7; }

        .snapshot-title {
            color:#6b7d93;
            font-size:9px;
            font-weight:850;
            text-transform:uppercase;
            letter-spacing:.7px;
        }

        .snapshot-value {
            color:#102a47;
            font-size:20px;
            font-weight:900;
            margin-top:6px;
        }

        .snapshot-caption {
            color:#8a99aa;
            font-size:9px;
            margin-top:2px;
        }

        .insight-card {
            background:#ffffff !important;
            border:1px solid #dce6f0 !important;
            border-radius:14px !important;
            box-shadow:0 6px 15px rgba(15,23,42,.035) !important;
        }

        .insight-title {
            color:#173553 !important;
            font-size:12px !important;
        }

        .insight-text {
            color:#53677f !important;
            font-size:10.5px !important;
            line-height:1.48 !important;
        }

        @media (max-width: 1000px) {
            .exec-strip { grid-template-columns:1fr; }
            .snapshot-grid { grid-template-columns:1fr; }
        }

        @media (max-width: 720px) {
            .block-container { padding-left:.6rem !important; padding-right:.6rem !important; }
            section[data-testid="stSidebar"] { width:220px !important; }
        }


        /* ============================================================
           FINAL 10/10 READABILITY PASS
           Balanced desktop density — no microscopic text
           ============================================================ */

        .block-container {
            width: 100% !important;
            max-width: 1550px !important;
            margin: 0 auto !important;
            padding: 0.8rem 1.0rem 2.4rem 1.0rem !important;
        }

        /* HERO */
        .hero {
            min-height: 152px !important;
            padding: 25px 28px !important;
        }

        .hero-title {
            font-size: clamp(36px, 3.4vw, 48px) !important;
        }

        .hero-subtitle {
            font-size: 14px !important;
            line-height: 1.5 !important;
        }

        .hero-pill {
            font-size: 12px !important;
            min-height: 36px !important;
            padding: 8px 15px !important;
        }

        /* LIVE FILTER BAR */
        .live-status-card {
            font-size: 12px !important;
            min-height: 38px !important;
            padding: 8px 14px !important;
        }

        .filter-update-text {
            font-size: 11px !important;
            padding: 7px 11px !important;
        }

        /* KPI CARDS */
        .kpi-card {
            min-height: 128px !important;
            padding: 16px 15px 14px 15px !important;
        }

        .kpi-icon {
            width: 42px !important;
            height: 42px !important;
            min-width: 42px !important;
            font-size: 19px !important;
        }

        .kpi-label {
            font-size: 10px !important;
            letter-spacing: .9px !important;
        }

        .kpi-value {
            font-size: clamp(24px, 2.25vw, 31px) !important;
            margin-top: 9px !important;
        }

        .kpi-caption {
            font-size: 10px !important;
        }

        /* BUSINESS DEPARTMENTS */
        .dept-heading-title {
            font-size: 21px !important;
        }

        .dept-heading-sub {
            font-size: 11px !important;
        }

        .native-dept-icon {
            width: 47px !important;
            height: 47px !important;
            min-width: 47px !important;
            font-size: 23px !important;
        }

        div[data-testid="stVerticalBlockBorderWrapper"] {
            min-height: 132px !important;
        }

        /* TABS */
        button[data-baseweb="tab"] {
            min-height: 44px !important;
            padding: 0 15px !important;
            font-size: 11.5px !important;
        }

        /* EXECUTIVE STRIP */
        .exec-strip-item {
            min-height: 64px !important;
            padding: 10px 12px !important;
        }

        .exec-strip-title {
            font-size: 11.5px !important;
        }

        .exec-strip-text {
            font-size: 10px !important;
        }

        .exec-strip-icon {
            width: 31px !important;
            height: 31px !important;
            min-width: 31px !important;
            font-size: 10px !important;
        }

        /* SECTION HEADINGS */
        .section-title {
            font-size: 20px !important;
        }

        .section-subtitle {
            font-size: 11px !important;
            margin-left: 46px !important;
        }

        .section-icon {
            width: 39px !important;
            height: 39px !important;
            min-width: 39px !important;
            font-size: 18px !important;
        }

        /* CHARTS */
        div[data-testid="stPlotlyChart"] {
            border-radius: 15px !important;
        }

        /* HEALTH CARD */
        .health-status {
            font-size: 24px !important;
        }

        .health-explain {
            font-size: 10.5px !important;
        }

        .health-mini span {
            font-size: 9.5px !important;
        }

        /* SNAPSHOT */
        .snapshot-card {
            min-height: 96px !important;
            padding: 12px 13px !important;
        }

        .snapshot-title {
            font-size: 9.5px !important;
        }

        .snapshot-value {
            font-size: 21px !important;
        }

        .snapshot-caption {
            font-size: 9.5px !important;
        }

        /* AI COPILOT */
        .insight-card {
            min-height: 104px !important;
            padding: 14px 16px !important;
        }

        .insight-title {
            font-size: 12.5px !important;
        }

        .insight-text {
            font-size: 11px !important;
            line-height: 1.55 !important;
        }

        /* FOOTER */
        .stCaption {
            font-size: 10.5px !important;
        }

        /* Responsive safety */
        @media (max-width: 1100px) {
            .block-container {
                max-width: 100% !important;
            }
        }

        @media (max-width: 800px) {
            .block-container {
                padding-left: .65rem !important;
                padding-right: .65rem !important;
            }

            .hero-title {
                font-size: 34px !important;
            }
        }


        /* ============================================================
           TRUE FULL-VIEWPORT DESKTOP MODE
           Prevents dashboard from appearing tiny/centered on large
           browser viewports or non-100% browser zoom.
           ============================================================ */

        .stApp,
        [data-testid="stAppViewContainer"],
        [data-testid="stMain"],
        section.main {
            width: 100% !important;
            min-width: 0 !important;
        }

        .block-container {
            width: 100% !important;
            max-width: none !important;
            margin-left: 0 !important;
            margin-right: 0 !important;
            padding-left: 18px !important;
            padding-right: 18px !important;
            padding-top: 12px !important;
            padding-bottom: 34px !important;
        }

        section.main > div {
            width: 100% !important;
            max-width: none !important;
        }

        /* Keep dashboard content visually centered without shrinking it. */
        .hero,
        .kpi-card,
        .dept-heading,
        .exec-strip,
        .section-head,
        .insight-card,
        .health-card,
        .snapshot-grid,
        .live-status-card {
            box-sizing: border-box !important;
        }

        /* Use the available width for all chart rows. */
        [data-testid="stHorizontalBlock"] {
            width: 100% !important;
        }

        /* KPI row */
        .kpi-card {
            width: 100% !important;
        }

        /* Department row */
        div[data-testid="stVerticalBlockBorderWrapper"] {
            width: 100% !important;
        }

        /* Chart containers should fill their Streamlit column. */
        div[data-testid="stPlotlyChart"] {
            width: 100% !important;
            min-width: 0 !important;
        }

        /* Prevent the dashboard from becoming visually microscopic */
        @media (min-width: 1600px) {
            .hero-title {
                font-size: 48px !important;
            }

            .kpi-value {
                font-size: 31px !important;
            }

            .section-title {
                font-size: 21px !important;
            }
        }

        /* Compact at normal laptop widths */
        @media (max-width: 1280px) {
            .block-container {
                padding-left: 12px !important;
                padding-right: 12px !important;
            }

            .hero-title {
                font-size: 36px !important;
            }

            .kpi-value {
                font-size: 25px !important;
            }
        }


        /* ============================================================
           FINAL VISUAL SCALE FIX
           The previous version used overly small 9–11px typography.
           This layer makes the dashboard readable at normal desktop
           zoom while preserving the responsive layout.
           ============================================================ */

        html {
            font-size: 16px !important;
        }

        body,
        .stApp,
        [data-testid="stAppViewContainer"] {
            font-size: 15px !important;
        }

        /* ---------- Sidebar ---------- */
        section[data-testid="stSidebar"] {
            min-width: 270px !important;
            width: 270px !important;
            max-width: 270px !important;
        }

        section[data-testid="stSidebar"] > div:first-child {
            padding: 1rem 0.95rem 1.3rem 0.95rem !important;
        }

        section[data-testid="stSidebar"] label {
            font-size: 13px !important;
            font-weight: 800 !important;
        }

        section[data-testid="stSidebar"] .stCaption,
        section[data-testid="stSidebar"] small {
            font-size: 11.5px !important;
        }

        section[data-testid="stSidebar"] div[data-baseweb="select"] > div {
            min-height: 46px !important;
            font-size: 14px !important;
        }

        /* ---------- Brand ---------- */
        .sidebar-brand-title {
            font-size: 17px !important;
        }

        .sidebar-brand-sub {
            font-size: 10.5px !important;
        }

        /* ---------- Hero ---------- */
        .hero {
            min-height: 165px !important;
            padding: 28px 32px !important;
        }

        .hero-title {
            font-size: clamp(40px, 3.6vw, 52px) !important;
            letter-spacing: -1.8px !important;
        }

        .hero-subtitle {
            font-size: 16px !important;
            line-height: 1.55 !important;
            margin-top: 8px !important;
        }

        .hero-pill {
            font-size: 12.5px !important;
            min-height: 39px !important;
            padding: 9px 16px !important;
        }

        /* ---------- Live status ---------- */
        .live-status-card {
            font-size: 12.5px !important;
            min-height: 40px !important;
            padding: 9px 15px !important;
        }

        .filter-update-text {
            font-size: 11.5px !important;
            padding: 8px 12px !important;
        }

        /* ---------- KPI cards ---------- */
        .kpi-card {
            min-height: 142px !important;
            padding: 17px 16px 15px 16px !important;
            border-radius: 18px !important;
        }

        .kpi-icon {
            width: 44px !important;
            height: 44px !important;
            min-width: 44px !important;
            font-size: 20px !important;
            border-radius: 13px !important;
        }

        .kpi-label {
            font-size: 11px !important;
            letter-spacing: .95px !important;
        }

        .kpi-value {
            font-size: clamp(26px, 2.4vw, 34px) !important;
            margin-top: 10px !important;
        }

        .kpi-caption {
            font-size: 11px !important;
        }

        /* ---------- Departments ---------- */
        .dept-heading-title {
            font-size: 22px !important;
        }

        .dept-heading-sub {
            font-size: 12px !important;
        }

        .native-dept-icon {
            width: 50px !important;
            height: 50px !important;
            min-width: 50px !important;
            font-size: 25px !important;
        }

        .dept-heading-badge {
            font-size: 10px !important;
            min-height: 28px !important;
        }

        div[data-testid="stVerticalBlockBorderWrapper"] {
            min-height: 145px !important;
        }

        /* ---------- Tabs ---------- */
        button[data-baseweb="tab"] {
            min-height: 46px !important;
            padding: 0 16px !important;
            font-size: 12.5px !important;
        }

        /* ---------- Executive strip ---------- */
        .exec-strip-item {
            min-height: 70px !important;
            padding: 11px 13px !important;
        }

        .exec-strip-title {
            font-size: 12.5px !important;
        }

        .exec-strip-text {
            font-size: 10.5px !important;
        }

        .exec-strip-icon {
            width: 33px !important;
            height: 33px !important;
            min-width: 33px !important;
            font-size: 10.5px !important;
        }

        /* ---------- Section headings ---------- */
        .section-title {
            font-size: 22px !important;
        }

        .section-subtitle {
            font-size: 12px !important;
        }

        .section-icon {
            width: 42px !important;
            height: 42px !important;
            min-width: 42px !important;
            font-size: 19px !important;
        }

        /* ---------- Business Snapshot ---------- */
        .snapshot-card {
            min-height: 104px !important;
            padding: 13px 14px !important;
        }

        .snapshot-title {
            font-size: 10px !important;
        }

        .snapshot-value {
            font-size: 23px !important;
        }

        .snapshot-caption {
            font-size: 10px !important;
        }

        /* ---------- Portfolio health ---------- */
        .health-status {
            font-size: 26px !important;
        }

        .health-explain {
            font-size: 11px !important;
        }

        .health-mini span {
            font-size: 10px !important;
        }

        .health-mini b {
            font-size: 10px !important;
        }

        /* ---------- AI Copilot ---------- */
        .insight-card {
            min-height: 112px !important;
            padding: 15px 17px !important;
        }

        .insight-title {
            font-size: 13.5px !important;
        }

        .insight-text {
            font-size: 12px !important;
            line-height: 1.58 !important;
        }

        /* ---------- General app text ---------- */
        [data-testid="stAppViewContainer"] .stCaption {
            font-size: 11px !important;
        }

        /* ---------- Do NOT apply global CSS zoom — it causes overflow.
           Use real component sizing instead. ---------- */
        @media (max-width: 1200px) {
            section[data-testid="stSidebar"] {
                min-width: 245px !important;
                width: 245px !important;
                max-width: 245px !important;
            }

            .kpi-value {
                font-size: 27px !important;
            }

            .section-title {
                font-size: 20px !important;
            }
        }

        @media (max-width: 800px) {
            section[data-testid="stSidebar"] {
                min-width: 220px !important;
                width: 220px !important;
                max-width: 220px !important;
            }

            .hero-title {
                font-size: 34px !important;
            }
        }

</style>

        </style>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# CHART STYLE HELPER
# ============================================================

PLOTLY_LAYOUT = dict(
    font=dict(
        family="Inter, Segoe UI, Arial, sans-serif",
        size=12,
        color="#334155",
    ),
    margin=dict(l=22, r=22, t=28, b=22),
    hoverlabel=dict(
        bgcolor="#0b1324",
        font_size=12,
        font_color="#ffffff",
    ),
)

def apply_chart_style(fig, height=430, title=None):
    fig.update_layout(
        height=height,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(
            family="Inter, Segoe UI, Arial, sans-serif",
            color="#314866",
            size=12,
        ),
        margin=dict(l=18, r=22, t=38, b=24),
        hoverlabel=dict(
            bgcolor="#102a43",
            font_color="#ffffff",
            font_size=12,
        ),
    )

    if title:
        fig.update_layout(
            title=dict(
                text=title,
                x=0.02,
                xanchor="left",
                y=0.98,
                yanchor="top",
                font=dict(
                    family="Inter, Segoe UI, Arial, sans-serif",
                    size=15,
                    color="#17324f",
                ),
            )
        )

    fig.update_xaxes(
        showline=False,
        zeroline=False,
        gridcolor="rgba(148,163,184,.16)",
        tickfont=dict(color="#42566f", size=11),
        title_font=dict(color="#64778e", size=11),
    )

    fig.update_yaxes(
        showline=False,
        zeroline=False,
        gridcolor="rgba(148,163,184,.16)",
        tickfont=dict(color="#42566f", size=11),
        title_font=dict(color="#64778e", size=11),
    )

    return fig

# ============================================================
# PATHS + DATA
# ============================================================

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"


@st.cache_data
def load_data():
    customers = pd.read_csv(RAW / "customers.csv")
    loans = pd.read_csv(RAW / "loans.csv")
    repayments = pd.read_csv(RAW / "repayments.csv")
    insurance = pd.read_csv(RAW / "insurance_policies.csv")
    return customers, loans, repayments, insurance


customers, loans, repayments, insurance = load_data()


# ============================================================
# SAFE COLUMN VALIDATION
# ============================================================

required_columns = {
    "customers": ["customer_id", "state", "segment"],
    "loans": [
        "loan_id",
        "customer_id",
        "product",
        "original_amount",
        "outstanding_principal",
        "dpd",
    ],
    "repayments": ["loan_id", "amount_due", "amount_paid"],
    "insurance": ["customer_id", "policy_active"],
}

for df_name, cols in required_columns.items():
    df = {
        "customers": customers,
        "loans": loans,
        "repayments": repayments,
        "insurance": insurance,
    }[df_name]

    missing = [c for c in cols if c not in df.columns]

    if missing:
        st.error(
            f"Missing columns in `{df_name}.csv`: {', '.join(missing)}"
        )
        st.stop()


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:
    st.markdown(
        """
        <div class="sidebar-brand">
            <div class="sidebar-brand-icon">🏦</div>
            <div>
                <div class="sidebar-brand-title">FinSight <span style="color:#60a5fa;">AI</span></div>
                <div class="sidebar-brand-sub">BFSI Decision Intelligence</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.divider()

    st.markdown("### 🎛️ Portfolio Filters")

    states = ["All"] + sorted(
        customers["state"].dropna().astype(str).unique().tolist()
    )

    products = ["All"] + sorted(
        loans["product"].dropna().astype(str).unique().tolist()
    )

    segments = ["All"] + sorted(
        customers["segment"].dropna().astype(str).unique().tolist()
    )

    state = st.selectbox("📍 State", states)
    product = st.selectbox("💳 Loan Product", products)
    segment = st.selectbox("👥 Customer Segment", segments)

    st.divider()

    st.markdown("### 📌 Dashboard Scope")
    st.caption("Synthetic BFSI portfolio simulation")
    st.caption("Loan • Risk • Collections • Insurance")

    if st.button("🔄 Reset Filters", width="stretch"):
        st.rerun()


# ============================================================
# FILTER DATA
# ============================================================

loans_f = loans.copy()

if state != "All":
    customer_ids = customers.loc[
        customers["state"] == state, "customer_id"
    ]
    loans_f = loans_f[
        loans_f["customer_id"].isin(customer_ids)
    ]

if product != "All":
    loans_f = loans_f[
        loans_f["product"] == product
    ]

if segment != "All":
    customer_ids = customers.loc[
        customers["segment"] == segment, "customer_id"
    ]
    loans_f = loans_f[
        loans_f["customer_id"].isin(customer_ids)
    ]

l = loans_f.copy()


if l.empty:
    st.markdown(
        """
        <div class="hero">
            <div class="hero-title">🔎 No Matching Portfolio</div>
            <div class="hero-subtitle">
                The selected filters returned no loan records.
                Change the State, Loan Product, or Customer Segment.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.stop()


# ============================================================
# KPI CALCULATIONS
# ============================================================

AUM = l["outstanding_principal"].sum()
disb = l["original_amount"].sum()
loan_count = len(l)

delin = (l["dpd"] > 0).mean()
npl = (l["dpd"] >= 90).mean()

r_f = repayments[
    repayments["loan_id"].isin(l["loan_id"])
].copy()

amount_due = r_f["amount_due"].sum()
amount_paid = r_f["amount_paid"].sum()

collection_efficiency = (
    amount_paid / amount_due if amount_due else 0
)

insurance_filtered = insurance[
    insurance["customer_id"].isin(l["customer_id"])
].copy()

insurance_penetration = (
    insurance_filtered["policy_active"].mean()
    if not insurance_filtered.empty
    else 0
)

avg_ticket = (
    disb / loan_count if loan_count else 0
)

active_dpd = int((l["dpd"] > 0).sum())


# ============================================================
# PORTFOLIO HEALTH SCORE
# ============================================================

# This is a portfolio presentation metric, not a regulatory score.
risk_penalty = (
    min(npl / 0.15, 1.0) * 40
    + min(delin / 0.40, 1.0) * 20
    + min(max(1 - collection_efficiency, 0) / 0.35, 1.0) * 20
)

health_score = max(0, min(100, 100 - risk_penalty))

if health_score >= 80:
    health_label = "Strong"
elif health_score >= 65:
    health_label = "Stable"
elif health_score >= 50:
    health_label = "Watch"
else:
    health_label = "High Risk"


# ============================================================
# HERO
# ============================================================

scope_text = (
    f"{state if state != 'All' else 'All India'} • "
    f"{product if product != 'All' else 'All Products'} • "
    f"{segment if segment != 'All' else 'All Segments'}"
)

st.markdown(
    f"""
    <div class="hero">
        <div class="hero-title">🏦 FinSight <span style="color:#60a5fa;">AI</span></div>
        <div class="hero-subtitle">
            <span style="font-weight:700;color:#e2e8f0;">BFSI Decision Intelligence</span>
            &nbsp;•&nbsp; Lending • Risk • Collections • Customer Intelligence
        </div>
        <div class="hero-pill">
            <span class="live-dot"></span>
            <span>LIVE PORTFOLIO</span>
            <span style="opacity:.65;">•</span>
            <span>{scope_text}</span>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    '''
    <div style="display:flex;justify-content:space-between;align-items:center;gap:12px;margin:-7px 0 14px 2px;flex-wrap:wrap;">
        <div class="live-status-card">
            <span class="live-status-dot"></span>
            <span>LIVE</span>
            <span>Real-time filtered portfolio view</span>
        </div>
        <div class="filter-update-text">
            🔄 <strong>LIVE</strong> Filters update instantly
        </div>
    </div>
    ''',
    unsafe_allow_html=True,
)


# ============================================================
# KPI CARDS
# ============================================================

kpis = [
    ("AUM", f"₹{AUM / 1e7:.2f} Cr", "Outstanding", "💰", "#dbeafe", "rgba(37,99,235,.08)"),
    ("DISBURSALS", f"₹{disb / 1e7:.2f} Cr", "Original value", "📈", "#dcfce7", "rgba(16,185,129,.08)"),
    ("LOANS", f"{loan_count:,}", "Accounts", "🏦", "#ede9fe", "rgba(139,92,246,.08)"),
    ("DELINQUENCY", f"{delin:.1%}", f"{active_dpd:,} overdue", "⏱️", "#ffedd5", "rgba(249,115,22,.08)"),
    ("NPL PROXY", f"{npl:.1%}", "90+ DPD", "⚠️", "#fee2e2", "rgba(239,68,68,.08)"),
    ("COLLECTIONS", f"{collection_efficiency:.1%}", "Recovery rate", "✅", "#dcfce7", "rgba(16,185,129,.08)"),
]

kpi_cols = st.columns(6)

for col, (label, value, caption, icon, icon_bg, glow) in zip(kpi_cols, kpis):
    with col:
        st.markdown(
            f"""
            <div class="kpi-card" style="--kpi-icon-bg:{icon_bg};--kpi-glow:{glow};">
                <div class="kpi-top">
                    <div class="kpi-icon">{icon}</div>
                    <div class="kpi-label">{label}</div>
                </div>
                <div class="kpi-value">{value}</div>
                <div class="kpi-caption">{caption}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

st.write("")

# ============================================================
# DEPARTMENT MAP
# ============================================================

st.markdown(
    """
    <div class="dept-heading">
        <div>
            <div class="dept-heading-title">Business Departments</div>
            <div class="dept-heading-sub">
                Clear BFSI workflow • each module represents a business decision area
            </div>
        </div>
        <div class="dept-heading-badge">● EXECUTIVE VIEW</div>
    </div>
    """,
    unsafe_allow_html=True,
)

dept_items = [
    ("📊", "Executive Overview", "AUM, portfolio mix & management KPIs", "blue"),
    ("🛡️", "Credit Risk", "DPD, NPL proxy & risk concentration", "red"),
    ("💸", "Collections", "Recovery, leakage & priority accounts", "green"),
    ("👥", "Customer & Insurance", "Segments, penetration & cross-sell", "purple"),
    ("🤖", "AI Copilot", "Risk alerts & decision-ready insights", "amber"),
]

dept_cols = st.columns(5)

for col, (icon, title, desc, tone) in zip(dept_cols, dept_items):
    with col:
        with st.container(border=True):
            st.markdown(
                f"<div class='native-dept-icon {tone}'>{icon}</div>",
                unsafe_allow_html=True,
            )
            st.markdown(f"**{title}**")
            st.caption(desc)

st.write("")


# ============================================================
# EXECUTIVE OVERVIEW
# ============================================================

tab1, tab2, tab3, tab4 = st.tabs(
    [
        "📊 Executive Overview",
        "🛡️ Credit Risk",
        "💸 Collections",
        "👥 Customer & Insurance",
    ]
)


# ============================================================
# TAB 1 — EXECUTIVE OVERVIEW
# ============================================================

with tab1:

    st.markdown(
        """
        <div class="exec-strip">
            <div class="exec-strip-item">
                <div class="exec-strip-icon">01</div>
                <div>
                    <div class="exec-strip-title">Capital Deployment</div>
                    <div class="exec-strip-text">Where the portfolio is concentrated</div>
                </div>
            </div>
            <div class="exec-strip-item">
                <div class="exec-strip-icon">02</div>
                <div>
                    <div class="exec-strip-title">Risk Health</div>
                    <div class="exec-strip-text">Delinquency & NPL exposure</div>
                </div>
            </div>
            <div class="exec-strip-item">
                <div class="exec-strip-icon">03</div>
                <div>
                    <div class="exec-strip-title">Management Action</div>
                    <div class="exec-strip-text">Collections & cross-sell priorities</div>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    left, right = st.columns([2.25, 1])

    with left:
        st.markdown(
            '<div class="section-head"><div class="section-icon">📊</div><div class="section-title">Portfolio Performance</div></div>',
            unsafe_allow_html=True,
        )
        st.markdown(
            '<div class="section-subtitle">'
            "Concentration, capital deployment and portfolio performance."
            "</div>",
            unsafe_allow_html=True,
        )

        by_product = (
            l.groupby("product", as_index=False)
            .agg(
                AUM=("outstanding_principal", "sum"),
                Disbursals=("original_amount", "sum"),
                Loans=("loan_id", "count"),
            )
            .sort_values("AUM", ascending=True)
        )

        fig = px.bar(
            by_product,
            x="AUM",
            y="product",
            orientation="h",
            text="AUM",
        )

        fig.update_traces(
            marker_color="#2563eb",
            texttemplate="₹%{text:.2s}",
            textposition="outside",
        )

        fig.update_layout(
            height=430,
            margin=dict(l=10, r=25, t=20, b=10),
            plot_bgcolor="rgba(0,0,0,0)",
            paper_bgcolor="rgba(0,0,0,0)",
            font=dict(color="#1f334d"),
            xaxis=dict(color="#334155", title_font=dict(color="#1f334d"), tickfont=dict(color="#475569")),
            yaxis=dict(color="#334155", title_font=dict(color="#1f334d"), tickfont=dict(color="#475569")),
            xaxis_title="Outstanding AUM",
            yaxis_title="",
            showlegend=False,
        )

        apply_chart_style(fig, 410, "AUM by Loan Product")

        st.plotly_chart(fig, width="stretch", config={"displaylogo": False, "responsive": True})

    with right:

        gauge = go.Figure(
            go.Indicator(
                mode="gauge+number",
                value=health_score,
                number={"suffix": "/100"},
                title={"text": "<b>Portfolio Health</b>"},
                gauge={
                    "axis": {"range": [0, 100]},
                    "bar": {"color": "#2563eb"},
                    "bgcolor": "#eef2f7",
                    "borderwidth": 0,
                    "steps": [
                        {"range": [0, 50], "color": "#fee2e2"},
                        {"range": [50, 65], "color": "#fef3c7"},
                        {"range": [65, 80], "color": "#dbeafe"},
                        {"range": [80, 100], "color": "#dcfce7"},
                    ],
                },
            )
        )

        gauge.update_layout(
            height=300,
            margin=dict(l=15, r=15, t=35, b=10),
            paper_bgcolor="rgba(0,0,0,0)",
        )

        apply_chart_style(gauge, 300, "Portfolio Health")

        st.plotly_chart(gauge, width="stretch", config={"displaylogo": False, "responsive": True})

        st.markdown(
            f"""
            <div class="health-card">
                <div class="health-label">Portfolio Status</div>
                <div class="health-status-row">
                    <div class="health-status">{health_label}</div>
                    <div class="health-score-chip">{health_score:.0f}/100</div>
                </div>
                <div class="health-explain">
                    Presentation-level score using NPL, delinquency and collection efficiency.
                    Management indicator only — not a regulatory credit-risk measure.
                </div>
                <div class="health-mini">
                    <span><b>NPL</b>{npl:.1%}</span>
                    <span><b>DPD</b>{delin:.1%}</span>
                    <span><b>Collection</b>{collection_efficiency:.1%}</span>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # Second row
    left2, right2 = st.columns(2)

    with left2:
        st.markdown(
            '<div class="section-head"><div class="section-icon">🧩</div><div class="section-title">Product Mix</div></div>',
            unsafe_allow_html=True,
        )

        mix = (
            l.groupby("product", as_index=False)
            .agg(AUM=("outstanding_principal", "sum"))
        )

        fig_mix = px.pie(
            mix,
            names="product",
            values="AUM",
            hole=0.58,
        )

        fig_mix.update_layout(
            height=330,
            margin=dict(l=8, r=8, t=18, b=8),
            paper_bgcolor="rgba(0,0,0,0)",
            legend=dict(
                orientation="v",
                yanchor="middle",
                y=0.5,
                xanchor="left",
                x=1.0,
                font=dict(size=10, color="#42566f"),
            ),
        )

        fig_mix.update_traces(
            textposition="inside",
            textfont=dict(size=10, color="#ffffff"),
            hole=0.62,
        )

        apply_chart_style(fig_mix, 330, "Portfolio Product Mix")

        st.plotly_chart(
            fig_mix,
            width="stretch",
            config={"displaylogo": False, "responsive": True},
        )

    with right2:
        st.markdown(
            '<div class="section-head"><div class="section-icon">📌</div><div class="section-title">Business Snapshot</div></div>',
            unsafe_allow_html=True,
        )

        # Use native Streamlit columns and single-line HTML cards.
        # This avoids Markdown interpreting indented multiline HTML as a code block.
        snapshot_cards = [
            ("Average Ticket", f"₹{avg_ticket / 1e5:.2f} L", "Avg. loan size", "blue"),
            ("Insurance", f"{insurance_penetration:.1%}", "Policy penetration", "purple"),
            ("Active DPD", f"{active_dpd:,}", "Overdue accounts", "amber"),
            ("Collection", f"{collection_efficiency:.1%}", "Recovery efficiency", "green"),
        ]

        snapshot_cols = st.columns(2)

        for idx, (title, value, caption, tone) in enumerate(snapshot_cards):
            with snapshot_cols[idx % 2]:
                st.markdown(
                    f'<div class="snapshot-card {tone}"><div class="snapshot-title">{title}</div><div class="snapshot-value">{value}</div><div class="snapshot-caption">{caption}</div></div>',
                    unsafe_allow_html=True,
                )



# ============================================================
# TAB 2 — CREDIT RISK
# ============================================================

with tab2:

    st.markdown(
        '<div class="section-head"><div class="section-icon">🛡️</div><div class="section-title">Credit Risk Command Center</div></div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="section-subtitle">'
        "Monitor overdue migration, 90+ DPD exposure and concentration by product."
        "</div>",
        unsafe_allow_html=True,
    )

    risk = l.copy()

    risk["risk_band"] = pd.cut(
        risk["dpd"],
        bins=[-1, 0, 30, 90, 100000],
        labels=[
            "Current",
            "1-30 DPD",
            "31-90 DPD",
            "90+ DPD",
        ],
    )

    risk_counts = (
        risk.groupby(
            "risk_band",
            observed=False,
        )
        .size()
        .reset_index(name="Loans")
    )

    c1, c2 = st.columns(2)

    with c1:

        fig_risk = px.bar(
            risk_counts,
            x="risk_band",
            y="Loans",
            text="Loans",
        )

        fig_risk.update_traces(
            marker_color="#f97316",
            textposition="outside",
        )

        fig_risk.update_layout(
            height=390,
            plot_bgcolor="rgba(0,0,0,0)",
            paper_bgcolor="rgba(0,0,0,0)",
            font=dict(color="#1f334d"),
            xaxis=dict(color="#334155", title_font=dict(color="#1f334d"), tickfont=dict(color="#475569")),
            yaxis=dict(color="#334155", title_font=dict(color="#1f334d"), tickfont=dict(color="#475569")),
            xaxis_title="DPD Bucket",
            yaxis_title="Loan Accounts",
        )

        fig_risk.update_layout(title=dict(text="DPD Risk Distribution", x=0.02, xanchor="left", y=0.98, yanchor="top", font=dict(size=15, color="#0b1324")))

        st.plotly_chart(
            fig_risk,
            width="stretch",
        )

    with c2:

        risk_matrix = (
            l.groupby("product", as_index=False)
            .agg(
                Delinquency=(
                    "dpd",
                    lambda s: (s > 0).mean(),
                ),
                NPL=(
                    "dpd",
                    lambda s: (s >= 90).mean(),
                ),
                AUM=(
                    "outstanding_principal",
                    "sum",
                ),
                Loans=("loan_id", "count"),
            )
        )

        fig_matrix = px.scatter(
            risk_matrix,
            x="Delinquency",
            y="NPL",
            size="AUM",
            color="product",
            hover_name="product",
            hover_data={
                "AUM": ":,.0f",
                "Loans": True,
            },
        )

        fig_matrix.update_xaxes(tickformat=".0%")
        fig_matrix.update_yaxes(tickformat=".0%")

        fig_matrix.update_layout(legend=dict(font=dict(color="#334155", size=11)),
            height=390,
            plot_bgcolor="rgba(0,0,0,0)",
            paper_bgcolor="rgba(0,0,0,0)",
            xaxis_title="Delinquency Rate",
            yaxis_title="NPL Proxy Rate",
        )

        fig_matrix.update_layout(title=dict(text="Product Risk Matrix", x=0.02, xanchor="left", y=0.98, yanchor="top", font=dict(size=15, color="#0b1324")))

        st.plotly_chart(
            fig_matrix,
            width="stretch",
        )

    st.markdown("#### 🔎 Highest-Risk Products")

    product_risk_table = risk_matrix.copy()
    product_risk_table["Delinquency"] = (
        product_risk_table["Delinquency"] * 100
    ).round(2)
    product_risk_table["NPL"] = (
        product_risk_table["NPL"] * 100
    ).round(2)

    product_risk_table["AUM"] = (
        product_risk_table["AUM"] / 1e7
    ).round(2)

    product_risk_table = product_risk_table.rename(
        columns={
            "product": "Product",
            "AUM": "AUM (Cr)",
            "Loans": "Loans",
            "Delinquency": "Delinquency (%)",
            "NPL": "NPL Proxy (%)",
        }
    )

    st.dataframe(
        product_risk_table.sort_values(
            "NPL Proxy (%)",
            ascending=False,
        ),
        width="stretch",
        hide_index=True,
    )


# ============================================================
# TAB 3 — COLLECTIONS
# ============================================================

with tab3:

    st.markdown(
        '<div class="section-head"><div class="section-icon">💸</div><div class="section-title">Collections & Recovery</div></div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="section-subtitle">'
        "Track recovery performance, unpaid gaps and collector priorities."
        "</div>",
        unsafe_allow_html=True,
    )

    if not r_f.empty:

        collection_by_loan = (
            r_f.groupby("loan_id", as_index=False)
            .agg(
                Amount_Due=("amount_due", "sum"),
                Amount_Paid=("amount_paid", "sum"),
            )
        )

        collection_by_loan["Collection_Rate"] = np.where(
            collection_by_loan["Amount_Due"] > 0,
            collection_by_loan["Amount_Paid"]
            / collection_by_loan["Amount_Due"],
            0,
        )

        collection_by_loan = collection_by_loan.merge(
            l[
                [
                    "loan_id",
                    "customer_id",
                    "product",
                    "dpd",
                    "outstanding_principal",
                ]
            ],
            on="loan_id",
            how="left",
        )

        c1, c2 = st.columns(2)

        with c1:

            collection_by_product = (
                collection_by_loan.groupby(
                    "product",
                    as_index=False,
                )
                .agg(
                    Collection_Rate=(
                        "Collection_Rate",
                        "mean",
                    )
                )
            )

            collection_by_product["Collection_Rate"] *= 100

            fig_col = px.bar(
                collection_by_product.sort_values(
                    "Collection_Rate"
                ),
                x="Collection_Rate",
                y="product",
                orientation="h",
                text="Collection_Rate",
            )

            fig_col.update_traces(
                marker_color="#10b981",
                texttemplate="%{text:.1f}%",
                textposition="outside",
            )

            fig_col.update_layout(
                height=400,
                plot_bgcolor="rgba(0,0,0,0)",
                paper_bgcolor="rgba(0,0,0,0)",
                xaxis_title="Average Collection Rate",
                yaxis_title="",
            )

            st.plotly_chart(
                fig_col,
                width="stretch",
            )

        with c2:

            gap = collection_by_loan.copy()
            gap["Collection_Gap"] = (
                gap["Amount_Due"] - gap["Amount_Paid"]
            )

            top_gap = (
                gap.groupby(
                    "product",
                    as_index=False,
                )
                .agg(
                    Collection_Gap=(
                        "Collection_Gap",
                        "sum",
                    )
                )
                .sort_values(
                    "Collection_Gap",
                    ascending=False,
                )
            )

            fig_gap = px.bar(
                top_gap,
                x="product",
                y="Collection_Gap",
                text="Collection_Gap",
            )

            fig_gap.update_traces(
                marker_color="#ef4444",
                texttemplate="₹%{text:.2s}",
                textposition="outside",
            )

            fig_gap.update_layout(
                height=400,
                plot_bgcolor="rgba(0,0,0,0)",
                paper_bgcolor="rgba(0,0,0,0)",
                xaxis_title="Loan Product",
                yaxis_title="Collection Gap",
            )

            st.plotly_chart(
                fig_gap,
                width="stretch",
            )

        st.markdown("#### 🚨 Collection Priority Queue")

        # Create Collection Gap before calculating the priority score.
        priority = collection_by_loan.copy()

        priority["Collection_Gap"] = (
            priority["Amount_Due"] - priority["Amount_Paid"]
        ).clip(lower=0)

        # Normalize the three collection-priority drivers.
        gap_rank = (
            priority["Collection_Gap"]
            .rank(pct=True)
            .fillna(0)
        )

        dpd_rank = (
            priority["dpd"]
            .rank(pct=True)
            .fillna(0)
        )

        outstanding_rank = (
            priority["outstanding_principal"]
            .rank(pct=True)
            .fillna(0)
        )

        # 50% unpaid amount + 30% DPD severity + 20% exposure.
        priority["Priority_Score"] = (
            gap_rank * 0.50
            + dpd_rank * 0.30
            + outstanding_rank * 0.20
        )

        # Business-friendly priority bands.
        priority["Priority"] = pd.cut(
            priority["Priority_Score"],
            bins=[-0.01, 0.50, 0.75, 1.01],
            labels=["Medium", "High", "Critical"],
        )

        priority = (
            priority
            .sort_values("Priority_Score", ascending=False)
            .head(20)
        )

        display_priority = priority[
            [
                "loan_id",
                "customer_id",
                "product",
                "dpd",
                "outstanding_principal",
                "Amount_Due",
                "Amount_Paid",
                "Collection_Gap",
                "Priority",
                "Priority_Score",
            ]
        ].copy()

        display_priority["outstanding_principal"] = (
            display_priority["outstanding_principal"]
            .round(2)
        )

        display_priority["Amount_Due"] = (
            display_priority["Amount_Due"]
            .round(2)
        )

        display_priority["Amount_Paid"] = (
            display_priority["Amount_Paid"]
            .round(2)
        )

        display_priority["Collection_Gap"] = (
            display_priority["Collection_Gap"]
            .round(2)
        )

        display_priority["Priority_Score"] = (
            display_priority["Priority_Score"]
            .round(3)
        )

        st.dataframe(
            display_priority,
            width="stretch",
            hide_index=True,
        )

    else:
        st.info(
            "No repayment records are available for the selected portfolio."
        )


# ============================================================
# TAB 4 — CUSTOMER + INSURANCE
# ============================================================

with tab4:

    st.markdown(
        '<div class="section-head"><div class="section-icon">👥</div><div class="section-title">Customer & Insurance Intelligence</div></div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="section-subtitle">'
        "Measure penetration, customer segments and cross-sell whitespace."
        "</div>",
        unsafe_allow_html=True,
    )

    ins_m = insurance.merge(
        customers[["customer_id", "state", "segment"]],
        on="customer_id",
        how="left",
    )

    ins_m = ins_m[
        ins_m["customer_id"].isin(l["customer_id"])
    ].copy()

    c1, c2 = st.columns(2)

    with c1:

        cross = (
            ins_m.groupby("state", as_index=False)
            .agg(
                penetration=(
                    "policy_active",
                    "mean",
                )
            )
        )

        cross["penetration"] *= 100

        fig_cross = px.bar(
            cross.sort_values("penetration"),
            x="penetration",
            y="state",
            orientation="h",
            text="penetration",
        )

        fig_cross.update_traces(
            marker_color="#8b5cf6",
            texttemplate="%{text:.1f}%",
            textposition="outside",
        )

        fig_cross.update_layout(
            height=440,
            plot_bgcolor="rgba(0,0,0,0)",
            paper_bgcolor="rgba(0,0,0,0)",
            xaxis_title="Insurance Penetration (%)",
            yaxis_title="",
        )

        fig_cross.update_layout(title=dict(text="Insurance Penetration by State", x=0.02, xanchor="left", y=0.98, yanchor="top", font=dict(size=15, color="#0b1324")))

        st.plotly_chart(
            fig_cross,
            width="stretch",
        )

    with c2:

        segment_insurance = (
            ins_m.groupby("segment", as_index=False)
            .agg(
                penetration=(
                    "policy_active",
                    "mean",
                )
            )
        )

        segment_insurance["penetration"] *= 100

        fig_segment = px.pie(
            segment_insurance,
            names="segment",
            values="penetration",
            hole=0.58,
        )

        fig_segment.update_layout(
            height=440,
            paper_bgcolor="rgba(0,0,0,0)",
        )

        fig_segment.update_layout(title=dict(text="Insurance Penetration by Segment", x=0.02, xanchor="left", y=0.98, yanchor="top", font=dict(size=15, color="#0b1324")))

        st.plotly_chart(
            fig_segment,
            width="stretch",
        )


# ============================================================
# AI INSIGHT COPILOT
# ============================================================

st.markdown(
    '''
    <div class="section-head">
        <div class="section-icon" style="background:linear-gradient(145deg,#ede9fe,#ddd6fe);border-color:#c4b5fd;">🤖</div>
        <div class="section-title">AI Insight Copilot</div>
        <div class="live-status-card" style="margin-left:auto;padding:5px 9px;font-size:10px;">
            <span class="live-status-dot"></span> ACTIVE
        </div>
    </div>
    ''',
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="section-subtitle">'
    "Management-ready insights generated from the currently filtered portfolio."
    "</div>",
    unsafe_allow_html=True,
)


insights = []


if npl > 0.08:
    insights.append(
        (
            "🚨 Risk Alert",
            f"NPL proxy is {npl:.1%}. Prioritize 90+ DPD accounts and "
            "investigate the products carrying the highest outstanding AUM."
        )
    )
else:
    insights.append(
        (
            "✅ Portfolio Risk",
            f"NPL proxy is {npl:.1%}. Early-stage delinquency should still "
            "be monitored for migration into higher DPD buckets."
        )
    )


if not by_product.empty:

    largest_product = by_product.sort_values(
        "AUM",
        ascending=False,
    ).iloc[-1]

    insights.append(
        (
            "📊 Concentration",
            f"{largest_product['product']} is the largest AUM contributor "
            f"at ₹{largest_product['AUM'] / 1e7:.2f} Cr. Review concentration "
            "against product-level delinquency."
        )
    )


if collection_efficiency < 0.90:
    insights.append(
        (
            "💰 Collections",
            f"Collection efficiency is {collection_efficiency:.1%}. "
            "Focus collectors on missed or partial payments before accounts "
            "roll into higher DPD buckets."
        )
    )
else:
    insights.append(
        (
            "💰 Collections",
            f"Collection efficiency is strong at {collection_efficiency:.1%}. "
            "Protect performance by monitoring high-value overdue accounts."
        )
    )


if insurance_penetration < 0.25:
    insights.append(
        (
            "🛡️ Cross-Sell Opportunity",
            f"Insurance penetration is only {insurance_penetration:.1%}. "
            "Target eligible loan customers with low policy coverage."
        )
    )
else:
    insights.append(
        (
            "🛡️ Insurance",
            f"Insurance penetration is {insurance_penetration:.1%}. "
            "Explore incremental cross-sell in low-penetration segments."
        )
    )


insight_cols = st.columns(2)

for idx, (title, text) in enumerate(insights):

    with insight_cols[idx % 2]:

        st.markdown(
            f"""
            <div class="insight-card">
                <div class="insight-title">{title}</div>
                <div class="insight-text">{text}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )


st.markdown(
    '<div style="display:flex;align-items:center;gap:8px;margin-top:3px;'
    'color:#475569;font-size:11px;font-weight:700;">'
    '<span style="width:8px;height:8px;border-radius:50%;'
    'background:#22c55e;display:inline-block;'
    'box-shadow:0 0 0 4px rgba(34,197,94,.10);"></span>'
    'Insight engine active • grounded on filtered portfolio KPIs'
    '</div>',
    unsafe_allow_html=True,
)


# ============================================================
# OPTIONAL LLM LAYER
# ============================================================

if os.getenv("OPENAI_API_KEY"):
    st.caption(
        "🧠 LLM integration can be connected through OPENAI_API_KEY. "
        "Keep prompts grounded in aggregate KPI data and never send customer PII."
    )
else:
    st.caption(
        "ℹ️ AI Insight Copilot is currently deterministic and works without an API key."
    )


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "FinSight AI • BFSI Analytics Portfolio • Synthetic Data • 2026"
)
