import streamlit as st
from pathlib import Path
import pandas as pd

st.set_page_config(
    page_title="Prajval Srivastava — Finance Portfolio",
    page_icon="PS",
    layout="wide",
    initial_sidebar_state="collapsed",
)

ROOT = Path(__file__).parent
ASSETS = ROOT / "assets"

# -------------------- State --------------------
if "selected_project" not in st.session_state:
    st.session_state.selected_project = None

def open_project(key: str):
    st.session_state.selected_project = key

def close_project():
    st.session_state.selected_project = None

# -------------------- Design --------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Mono:wght@400;500&family=Manrope:wght@400;500;600;700;800&family=Playfair+Display:wght@600;700&display=swap');

:root{
  --night:#07152f;
  --night-2:#0b2145;
  --sky:#17396b;
  --violet:#40548f;
  --mist:#d8dcec;
  --white:#f6f7fb;
  --muted:#b6bfd1;
  --line:rgba(255,255,255,.17);
  --accent:#f26a63;
  --accent-2:#cdb7ff;
  --panel:rgba(8,19,43,.77);
}
html { scroll-behavior:smooth; }
body, [class*="css"] { font-family:Manrope,sans-serif; }
.stApp{
  background:
    radial-gradient(ellipse at 74% 37%, rgba(112,91,157,.22), transparent 27%),
    radial-gradient(ellipse at 28% 20%, rgba(70,109,180,.16), transparent 26%),
    linear-gradient(180deg,#06152f 0%,#0a1c3e 39%,#101f48 63%,#11172d 100%);
  color:var(--white);
}
.block-container{max-width:1480px;padding:0 44px 46px 44px;}
#MainMenu, footer { visibility:hidden; }
header[data-testid="stHeader"]{background:rgba(6,20,43,.55);}
a{text-decoration:none!important;color:inherit!important;}

/* stars / horizon / skyline motif */
.stApp:before{
  content:""; position:fixed; inset:0; pointer-events:none; opacity:.9;
  background-image:
    radial-gradient(circle at 8% 11%, rgba(255,255,255,.9) 0 1px, transparent 1.6px),
    radial-gradient(circle at 18% 34%, rgba(255,255,255,.55) 0 1px, transparent 1.5px),
    radial-gradient(circle at 31% 9%, rgba(255,255,255,.75) 0 1px, transparent 1.5px),
    radial-gradient(circle at 46% 27%, rgba(255,255,255,.55) 0 1px, transparent 1.5px),
    radial-gradient(circle at 62% 12%, rgba(255,255,255,.7) 0 1px, transparent 1.5px),
    radial-gradient(circle at 73% 25%, rgba(255,255,255,.45) 0 1px, transparent 1.4px),
    radial-gradient(circle at 87% 13%, rgba(255,255,255,.7) 0 1px, transparent 1.5px),
    radial-gradient(circle at 94% 32%, rgba(255,255,255,.5) 0 1px, transparent 1.4px),
    radial-gradient(circle at 55% 7%, rgba(255,255,255,.4) 0 1px, transparent 1.4px);
}
.stApp:after{
  content:""; position:fixed; left:0; right:0; bottom:0; height:20vh; pointer-events:none;
  background:
    linear-gradient(to top, rgba(2,6,18,.94), transparent 75%),
    linear-gradient(90deg, transparent 0 10%, rgba(12,16,30,.96) 10% 12%, transparent 12% 15%, rgba(9,14,29,.95) 15% 19%, transparent 19% 22%, rgba(10,15,31,.97) 22% 28%, transparent 28% 31%, rgba(8,14,30,.97) 31% 37%, transparent 37% 40%, rgba(10,16,31,.95) 40% 44%, transparent 44% 48%, rgba(8,14,29,.97) 48% 53%, transparent 53% 56%, rgba(9,15,31,.96) 56% 61%, transparent 61% 66%, rgba(8,14,30,.98) 66% 70%, transparent 70% 74%, rgba(9,14,31,.96) 74% 80%, transparent 80% 84%, rgba(8,13,29,.98) 84% 90%, transparent 90% 94%, rgba(7,12,27,.98) 94% 100%);
  z-index:0;
}

/* navigation */
.topnav{
  position:relative; z-index:3; height:80px; display:flex; align-items:center;
  justify-content:space-between; border-bottom:1px solid var(--line);
}
.logo{font-weight:800; font-size:1.08rem; letter-spacing:-.06em;}
.logo span{color:var(--accent);}
.navitems{display:flex;gap:22px;align-items:center;flex-wrap:wrap;}
.navitems a{font-family:"DM Mono",monospace;font-size:.59rem;letter-spacing:.07em;text-transform:uppercase;color:var(--mist)!important;}
.navitems a:hover{color:white!important;}
.contact-pill{padding:9px 12px;border:1px solid rgba(255,255,255,.32);border-radius:999px;}

/* hero */
.hero{position:relative;z-index:1;min-height:calc(100vh - 80px);display:flex;align-items:center;padding:62px 0 48px;}
.hero-grid{display:grid;grid-template-columns:1.05fr .95fr;gap:64px;align-items:center;width:100%;}
.hero-kicker{font-family:"DM Mono",monospace;font-size:.66rem;letter-spacing:.12em;text-transform:uppercase;color:var(--accent-2);margin-bottom:20px;}
.hero h1{
  font-family:"Playfair Display",Georgia,serif;font-weight:600;color:var(--white);
  font-size:clamp(4.7rem,10vw,10.2rem);line-height:.79;letter-spacing:-.065em;margin:0;
}
.hero-title{font-size:clamp(1.35rem,2.6vw,2rem);font-weight:700;letter-spacing:-.035em;margin:30px 0 14px;color:#edf0f8;}
.hero-copy{max-width:700px;color:var(--muted);font-size:.95rem;line-height:1.9;}
.hero-meta{display:flex;gap:34px;flex-wrap:wrap;margin-top:33px;}
.meta-item{padding-top:11px;border-top:1px solid rgba(255,255,255,.32);min-width:135px;}
.meta-item small{display:block;font-family:"DM Mono",monospace;color:#aeb7c8;font-size:.54rem;text-transform:uppercase;letter-spacing:.07em;}
.meta-item strong{display:block;color:#fff;font-size:.82rem;margin-top:4px;}
.hero-photo-wrap{position:relative;max-width:460px;margin-left:auto;}
.hero-photo-wrap:before{
  content:"";position:absolute;inset:-20px -18px 26px 28px;border:1px solid rgba(255,255,255,.17);
}
.hero-photo{
  position:relative;width:100%;display:block;aspect-ratio:4/5;object-fit:cover;
  border:1px solid rgba(255,255,255,.20);filter:saturate(.72) contrast(1.06);
}
.photo-caption{position:relative;background:rgba(5,16,36,.92);border:1px solid rgba(255,255,255,.14);padding:11px 13px;margin-top:-1px;font-family:"DM Mono",monospace;font-size:.57rem;text-transform:uppercase;letter-spacing:.08em;color:#c5cbda;}
.red-marker{position:absolute;left:-15px;bottom:68px;width:11px;height:11px;border-radius:50%;background:var(--accent);box-shadow:0 0 24px rgba(242,106,99,.45);}

/* sections */
.section{position:relative;z-index:1;padding-top:78px;}
.section-head{display:flex;justify-content:space-between;align-items:end;gap:30px;border-bottom:1px solid var(--line);padding-bottom:15px;margin-bottom:6px;}
.section-no{font-family:"DM Mono",monospace;font-size:.58rem;color:var(--accent-2);letter-spacing:.09em;text-transform:uppercase;margin-bottom:7px;}
.section-title{font-family:"Playfair Display",Georgia,serif;font-size:clamp(2.8rem,5vw,5.2rem);line-height:.88;letter-spacing:-.05em;font-weight:600;margin:0;color:#fff;}
.section-note{max-width:530px;color:var(--muted);font-size:.78rem;line-height:1.7;}

/* capabilities */
.cap-grid{display:grid;grid-template-columns:repeat(4,1fr);border-bottom:1px solid var(--line);}
.cap{padding:20px 18px 24px 0;border-right:1px solid var(--line);min-height:185px;}
.cap:last-child{border-right:0;padding-right:0;}
.cap-num{font-family:"DM Mono",monospace;color:var(--accent);font-size:.61rem;}
.cap h3{font-family:"Playfair Display",Georgia,serif;font-size:1.45rem;font-weight:600;margin:34px 0 9px;color:white;}
.cap p{color:var(--muted);font-size:.82rem;line-height:1.72;}

/* projects */
.project-list{border-bottom:1px solid var(--line);}
.project-row{display:grid;grid-template-columns:72px 1fr 195px;gap:20px;align-items:center;min-height:142px;border-top:1px solid var(--line);}
.project-row:first-child{border-top:0;}
.project-no{font-family:"DM Mono",monospace;color:var(--accent);font-size:.7rem;}
.project-kicker{font-family:"DM Mono",monospace;color:#aab3c2;font-size:.57rem;letter-spacing:.09em;text-transform:uppercase;}
.project-title{font-family:"Playfair Display",Georgia,serif;font-size:clamp(1.65rem,2.75vw,2.7rem);line-height:1.0;letter-spacing:-.045em;font-weight:600;margin-top:6px;color:#fff;}
.project-side{text-align:right;font-family:"DM Mono",monospace;color:#aab3c2;font-size:.55rem;line-height:1.45;text-transform:uppercase;}
.project-side button{margin-top:9px!important;}

/* detail */
.detail{background:rgba(3,13,31,.82);border:1px solid rgba(255,255,255,.16);margin-top:24px;}
.detail-head{padding:22px;border-bottom:1px solid var(--line);}
.detail-title{font-family:"Playfair Display",Georgia,serif;font-size:clamp(2rem,4vw,4.1rem);line-height:.91;letter-spacing:-.06em;color:#fff;margin-top:8px;}
.detail-metrics{display:grid;grid-template-columns:repeat(3,1fr);border-bottom:1px solid var(--line);}
.metric{padding:17px 20px;border-right:1px solid var(--line);}
.metric:last-child{border-right:0;}
.metric b{display:block;color:#fff;font-size:1.4rem;letter-spacing:-.04em;}
.metric span{display:block;color:#aeb7c8;font-size:.59rem;margin-top:3px;}
.detail-grid{display:grid;grid-template-columns:1fr 1fr;gap:1px;background:var(--line);}
.detail-block{background:rgba(11,28,60,.82);padding:20px;min-height:170px;}
.detail-block.full{grid-column:1/-1;min-height:auto;background:rgba(16,25,53,.86);}
.detail-label{font-family:"DM Mono",monospace;color:var(--accent);font-size:.57rem;letter-spacing:.08em;text-transform:uppercase;margin-bottom:8px;}
.detail-copy{color:#c0c7d5;font-size:.8rem;line-height:1.75;}
.workbook-label{font-family:"DM Mono",monospace;color:#aeb7c8;font-size:.57rem;letter-spacing:.08em;text-transform:uppercase;margin:22px 0 8px;}
.stDownloadButton button{background:var(--accent)!important;color:white!important;border:0!important;border-radius:999px!important;font-weight:800!important;font-size:.65rem!important;letter-spacing:.04em;}
.back-btn button{border:1px solid rgba(255,255,255,.2)!important;background:transparent!important;color:#e5e8f0!important;border-radius:999px!important;font-size:.62rem!important;}

/* native streamlit button styling */
.stButton button{
  border:1px solid rgba(255,255,255,.27)!important;
  background:rgba(7,16,35,.72)!important;
  color:white!important;
  border-radius:999px!important;
  font-size:.63rem!important;
  font-weight:800!important;
  padding:.48rem .72rem!important;
}
.stButton button:hover{border-color:var(--accent)!important;color:#fff!important;background:rgba(242,106,99,.12)!important;}

/* workbook tables */
[data-testid="stDataFrame"]{border:1px solid rgba(255,255,255,.14)!important;}
div[data-testid="stDataFrame"] div[role="columnheader"]{background:#152c56!important;}
div[data-testid="stDataFrame"] div[role="gridcell"]{background:#0c1e3e!important;color:#e7ebf2!important;}

/* experience */
.timeline-item{display:grid;grid-template-columns:230px 1fr;gap:24px;padding:22px 0;border-bottom:1px solid var(--line);}
.timeline-title{font-size:1rem;font-weight:800;color:#fff;}
.date{font-family:"DM Mono",monospace;color:var(--accent-2);font-size:.57rem;margin-top:5px;}
.meta{color:var(--muted);font-size:.8rem;line-height:1.75;}

/* education */
.edu-grid{display:grid;grid-template-columns:1fr 1fr;gap:12px;}
.edu-card{background:rgba(7,18,40,.72);border:1px solid var(--line);padding:21px;}
.edu-card h3{font-family:"Playfair Display",Georgia,serif;font-size:1.35rem;font-weight:600;margin:0 0 7px;color:#fff;}
.edu-card p{font-size:.75rem;line-height:1.65;color:var(--muted);}

/* skills */
.skill-grid{display:grid;grid-template-columns:1fr 1fr 1fr;gap:1px;background:var(--line);}
.skill-card{background:rgba(7,18,40,.78);padding:20px;min-height:155px;}
.skill-card h3{font-size:.9rem;margin:0 0 9px;color:#fff;}
.pill{display:inline-block;border:1px solid rgba(255,255,255,.17);padding:6px 7px;margin:3px 3px 0 0;font-family:"DM Mono",monospace;font-size:.51rem;color:#c0c7d5;}

/* contact */
.contact{position:relative;z-index:1;border-top:1px solid rgba(255,255,255,.3);margin-top:78px;padding:56px 0 14px;}
.contact-kicker{font-family:"DM Mono",monospace;color:var(--accent);font-size:.58rem;letter-spacing:.08em;text-transform:uppercase;}
.contact h2{font-family:"Playfair Display",Georgia,serif;font-weight:600;font-size:clamp(3.6rem,7.3vw,7.8rem);line-height:.82;letter-spacing:-.065em;margin:13px 0;}
.contact p{color:var(--muted);font-size:.8rem;}
.contact-links{display:flex;gap:10px;flex-wrap:wrap;margin-top:21px;}
.contact-links a{border:1px solid rgba(255,255,255,.22);padding:11px 14px;border-radius:999px;font-size:.62rem;font-weight:800;text-transform:uppercase;letter-spacing:.06em;}
.contact-links a.primary{background:var(--accent);border-color:var(--accent);color:#fff!important;}
.footer{margin-top:30px;border-top:1px solid var(--line);padding-top:14px;color:#8590a3;font-family:"DM Mono",monospace;font-size:.52rem;}

/* responsive */
@media(max-width:900px){
  .block-container{padding:0 1rem 3rem;}
  .topnav{height:66px}.navitems{gap:11px}.navitems a{font-size:.5rem}.contact-pill{padding:7px 9px;}
  .hero{min-height:auto;padding:48px 0 32px}.hero-grid{grid-template-columns:1fr;gap:30px}.hero h1{font-size:clamp(4.1rem,19vw,7rem)}
  .hero-photo-wrap{margin:0;max-width:330px}.hero-meta{gap:12px}.meta-item{min-width:120px}
  .section{padding-top:56px}.section-head{display:block}.section-note{margin-top:10px}
  .cap-grid{grid-template-columns:1fr 1fr}.cap{min-height:160px;border-right:0;border-bottom:1px solid var(--line)}.cap h3{font-size:1.2rem;}
  .project-row{grid-template-columns:46px 1fr;min-height:128px;gap:9px}.project-side{grid-column:2;text-align:left}.detail-metrics{grid-template-columns:1fr 1fr}
  .metric{border-bottom:1px solid var(--line)}.metric:nth-child(2){border-right:0}.detail-grid{grid-template-columns:1fr}.detail-block.full{grid-column:auto}
  .timeline-item{grid-template-columns:1fr;gap:7px}.edu-grid,.skill-grid{grid-template-columns:1fr}
}
</style>
""", unsafe_allow_html=True)

# -------------------- TOP NAV --------------------
st.markdown("""
<div class="topnav">
  <div class="logo">PS<span>®</span></div>
  <div class="navitems">
    <a href="#capabilities">01 · LOOK</a>
    <a href="#projects">02 · ANALYSE</a>
    <a href="#experience">03 · EXPERIENCE</a>
    <a href="#education">04 · BECOME</a>
    <a class="contact-pill" href="#contact">CONTACT</a>
  </div>
</div>
""", unsafe_allow_html=True)

# -------------------- HERO --------------------
st.markdown('<section class="hero"><div class="hero-grid">', unsafe_allow_html=True)
c1,c2=st.columns([1.12,.88],vertical_alignment="center")
with c1:
    st.markdown('<div class="hero-kicker">Corporate Finance · Financial Analysis · Excel</div>',unsafe_allow_html=True)
    st.markdown('<h1>Prajval<br>Srivastava</h1>',unsafe_allow_html=True)
    st.markdown('<div class="hero-title">Corporate Finance &amp; Financial Analysis</div>',unsafe_allow_html=True)
    st.markdown('<div class="hero-copy">PGDM Finance candidate at FIIB with Corporate Finance internship experience at Arizon Network India. I focus on translating financial statements into performance insights through financial benchmarking, ratio analysis, DuPont decomposition, red-flag assessment, and Excel-based analysis. I am seeking a Corporate Finance role where structured financial evaluation supports strategic business decisions.</div>',unsafe_allow_html=True)
    st.markdown("""
    <div class="hero-meta">
      <div class="meta-item"><small>Focus</small><strong>Financial Analysis</strong></div>
      <div class="meta-item"><small>Focus</small><strong>Valuation</strong></div>
      <div class="meta-item"><small>Tools</small><strong>Excel / Analytics</strong></div>
      <div class="meta-item"><small>Target</small><strong>Corporate Finance</strong></div>
    </div>
    """,unsafe_allow_html=True)
with c2:
    if (ASSETS/"profile.png").exists():
        st.markdown('<div class="hero-photo-wrap">',unsafe_allow_html=True)
        st.image(str(ASSETS/"profile.png"),use_container_width=True)
        st.markdown('<div class="photo-caption">Prajval Srivastava · New Delhi · FIIB</div><div class="red-marker"></div></div>',unsafe_allow_html=True)
st.markdown('</div></section>',unsafe_allow_html=True)

# -------------------- CAPABILITIES --------------------
st.markdown('<div id="capabilities"></div><section class="section">',unsafe_allow_html=True)
section_head(2,"Core Capabilities","Financial analysis first, then valuation, analytics, and project evidence.")
st.markdown('<div class="cap-grid">',unsafe_allow_html=True)
for n,t,b in [
("01","Financial Analysis","Financial Statement Analysis · Financial Reporting & Analysis · Ratio Analysis · DuPont Analysis"),
("02","Valuation","Valuation is an area of interest; no specific valuation project or evidence was provided, so none is claimed."),
("03","Excel & Analytics","Financial Benchmarking · Financial Modelling in Excel · Data Analysis · Business Research"),
("04","Projects","Financial benchmarking, financial statement analysis, Excel KPI dashboards, and comparative company assessment"),
]:
    st.markdown(f'<div class="cap"><div class="cap-num">{n}</div><h3>{t}</h3><p>{b}</p></div>',unsafe_allow_html=True)
st.markdown('</div></section>',unsafe_allow_html=True)

# -------------------- PROJECTS --------------------
st.markdown('<div id="projects"></div><section class="section">',unsafe_allow_html=True)
section_head(3,"Featured Projects","Open a project to stay on this same portfolio page and inspect the actual workbook.")
projects={
"sun-pharma":{"number":"01","kicker":"Financial Statement Analysis","title":"Financial Statement Analysis of Sun Pharmaceutical Industries","tag":"FIIB · Aug–Sep 2025","metrics":[("5 years","audited financials analysed"),("8–15%","YoY swings identified"),("40%","faster recurring metric checks")],"problem":"Understand changes in Sun Pharma's revenue, profitability, and cost structure across five years of audited financials.","did":"Analysed five years of audited Sun Pharma financials using Vertical and Horizontal Analysis and built an Excel KPI dashboard covering Revenue Growth, Net Profit Margin, ROE, and ROA.","tools":"Microsoft Excel","output":"Identified 8–15% YoY swings in revenue, profitability, and cost structure, while the KPI dashboard cut analysis time for recurring metric checks by 40%.","evidence":"The original Sun Pharma Excel workbook is included in this portfolio.","file":"Sun_Pharma_Financial_Analysis.xlsx"},
"media-benchmarking":{"number":"02","kicker":"Financial Benchmarking","title":"Financial Benchmarking of Listed Media Companies","tag":"Arizon Network India","metrics":[("3","listed media companies"),("4 years","comparative analysis"),("5-step","DuPont decomposition")],"problem":"Assess comparative financial health and identify profitability, efficiency, earnings-quality, and leverage risks across three listed media companies.","did":"Built a four-year benchmarking model for ZEEL, Jagran Prakashan, and DB Corp using ratio analysis, five-step DuPont decomposition, and financial red-flag assessment.","tools":"Microsoft Excel · Financial benchmarking model","output":"Surfaced profitability and efficiency gaps and flagged earnings-quality and leverage risks, producing investment-oriented risk insights.","evidence":"The original media benchmarking Excel workbook is included in this portfolio.","file":"Media_Industry_Financial_Benchmarking.xlsx"},
"portfolio-pipeline":{"number":"03","kicker":"Data Pipeline & Portfolio Analytics","title":"Portfolio Benchmarking Data Pipeline","tag":"Python · pandas · openpyxl","metrics":[("4","time-series datasets"),("5 years","daily price data"),("1","common date index")],"problem":"Reconcile four independent time-series datasets — three mutual funds and the Nifty 50 index — whose five years of daily price data had inconsistent date coverage because of source-specific gaps.","did":"Built a Python-based reconciliation process to detect and remove non-overlapping dates, creating a single common date index across all instruments.","tools":"Python · pandas · openpyxl","output":"Delivered a clean, analysis-ready Excel workbook enabling accurate return comparisons and correlation analysis between actively managed funds and the market benchmark.","evidence":"The original portfolio benchmarking Excel workbook is included in this portfolio.","file":"Portfolio_Benchmarking_Data_Pipeline.xlsx"}}

for key,p in projects.items():
    st.markdown('<div class="project-row">',unsafe_allow_html=True)
    col1,col2,col3=st.columns([.08,.68,.24],vertical_alignment="center")
    with col1:
        st.markdown(f'<div class="project-no">{p["number"]}</div>',unsafe_allow_html=True)
    with col2:
        st.markdown(f'<div class="project-kicker">{p["kicker"]}</div><div class="project-title">{p["title"]}</div>',unsafe_allow_html=True)
    with col3:
        st.markdown(f'<div class="project-side">{p["tag"]}</div>',unsafe_allow_html=True)
        if st.button("VIEW PROJECT ↗", key=f"open_{key}"):
            open_project(key)
            st.rerun()
    st.markdown('</div>',unsafe_allow_html=True)

if st.session_state.selected_project in projects:
    p=projects[st.session_state.selected_project]
    st.markdown('<div class="detail">',unsafe_allow_html=True)
    st.markdown(f'<div class="detail-head"><div class="project-kicker">{p["number"]} · {p["kicker"]}</div><div class="detail-title">{p["title"]}</div><div class="project-kicker" style="margin-top:10px;">{p["tag"]}</div></div>',unsafe_allow_html=True)
    metrics=''.join([f'<div class="metric"><b>{v}</b><span>{l}</span></div>' for v,l in p["metrics"]])
    st.markdown(f'<div class="detail-metrics">{metrics}</div>',unsafe_allow_html=True)
    st.markdown(f"""
    <div class="detail-grid">
      <div class="detail-block"><div class="detail-label">Problem</div><div class="detail-copy">{p["problem"]}</div></div>
      <div class="detail-block"><div class="detail-label">What I did</div><div class="detail-copy">{p["did"]}</div></div>
      <div class="detail-block"><div class="detail-label">Tools used</div><div class="detail-copy">{p["tools"]}</div></div>
      <div class="detail-block"><div class="detail-label">Output</div><div class="detail-copy">{p["output"]}</div></div>
      <div class="detail-block full"><div class="detail-label">Evidence</div><div class="detail-copy">{p["evidence"]}</div></div>
    </div>
    """,unsafe_allow_html=True)
    fpath=ASSETS/p["file"]
    if fpath.exists():
        with open(fpath,"rb") as f:
            st.download_button("Download original Excel workbook",f,file_name=fpath.name,mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",key=f"download_{st.session_state.selected_project}")
        st.markdown('<div class="workbook-label">Workbook inspection</div>',unsafe_allow_html=True)
        try:
            xls=pd.ExcelFile(fpath,engine="openpyxl")
            with st.expander("Open workbook sheets", expanded=False):
                names=xls.sheet_names[:8]
                selected_sheet=st.selectbox("Sheet",names,key=f"sheet_{st.session_state.selected_project}")
                df=pd.read_excel(fpath,sheet_name=selected_sheet,engine="openpyxl")
                st.caption(f"{len(df):,} rows × {len(df.columns):,} columns")
                st.dataframe(df.head(40),use_container_width=True,height=420)
        except Exception:
            st.info("The original workbook is available for download.")
    st.markdown('<div class="back-btn">',unsafe_allow_html=True)
    if st.button("← BACK TO PROJECTS",key="back_projects"):
        close_project()
        st.rerun()
    st.markdown('</div>',unsafe_allow_html=True)
st.markdown('</section>',unsafe_allow_html=True)

# -------------------- EXPERIENCE --------------------
st.markdown('<div id="experience"></div><section class="section">',unsafe_allow_html=True)
section_head(4,"Experience","Relevant professional work.")
st.markdown("""
<div class="timeline-item"><div><div class="timeline-title">Finance Intern — Arizon Network India</div><div class="date">Apr – Jun 2026</div></div><div class="meta"><ul><li>Built a 50-company, seven-industry financial research database, cutting manual data-pulling time by 30%.</li><li>Delivered a comparative financial health assessment across ZEEL, Jagran Prakashan, and DB Corp using a four-year Excel benchmarking model.</li><li>Flagged earnings-quality and leverage risks through five-step DuPont decomposition and red-flag screening.</li></ul></div></div>
<div class="timeline-item"><div><div class="timeline-title">Social Intern — Giftable India</div><div class="date">Jan 2026</div></div><div class="meta"><ul><li>Conducted structured telephonic outreach with 150–200 PWD candidates, validating and segmenting profiles across education, employability readiness, and role preferences.</li><li>Co-designed and delivered a grooming and interview-prep workshop for 20–30 PWD candidates.</li><li>Contributed to inclusive job description drafts used in employer outreach.</li></ul></div></div>
""",unsafe_allow_html=True)
st.markdown('</section>',unsafe_allow_html=True)

# -------------------- EDUCATION --------------------
st.markdown('<div id="education"></div><section class="section">',unsafe_allow_html=True)
section_head(5,"Education","Academic background.")
st.markdown('<div class="edu-grid"><div class="edu-card"><h3>Post Graduate Diploma in Management (Finance)</h3><p>Fortune Institute of International Business (FIIB), New Delhi<br>2025 – Present · CGPA: 7.6</p></div><div class="edu-card"><h3>Bachelor of Commerce</h3><p>Mahatma Gandhi Kashi Vidyapith, Varanasi<br>2021 – 2024 · CGPA: 7.6</p></div></div>',unsafe_allow_html=True)
st.markdown('</section>',unsafe_allow_html=True)

# -------------------- SKILLS --------------------
st.markdown('<div id="skills"></div><section class="section">',unsafe_allow_html=True)
section_head(6,"Skills & Certifications","Technical and business capabilities supporting the project evidence.")
st.markdown('<div class="skill-grid"><div class="skill-card"><h3>Technical Skills</h3><span class="pill">Financial Statement Analysis</span><span class="pill">Financial Reporting & Analysis</span><span class="pill">Ratio Analysis</span><span class="pill">DuPont Analysis</span><span class="pill">Financial Benchmarking</span><span class="pill">Financial Modelling (Excel)</span><span class="pill">Business Research</span><span class="pill">Data Analysis</span></div><div class="skill-card"><h3>Tools</h3><span class="pill">Microsoft Excel</span><span class="pill">PivotTables</span><span class="pill">XLOOKUP</span><span class="pill">HLOOKUP</span><span class="pill">INDEX-MATCH</span><span class="pill">Conditional Formatting</span><span class="pill">Power BI</span><span class="pill">Python</span><span class="pill">PowerPoint</span><span class="pill">Word</span><span class="pill">AI Tools</span></div><div class="skill-card"><h3>Business Skills</h3><span class="pill">Analytical Thinking</span><span class="pill">Problem Solving</span><span class="pill">Communication</span><span class="pill">Team Collaboration</span><span class="pill">Adaptability</span></div></div>',unsafe_allow_html=True)
st.markdown('</section>',unsafe_allow_html=True)

# -------------------- CONTACT --------------------
st.markdown('<div id="contact"></div><div class="contact"><div class="contact-kicker">07 / Contact</div><h2>Let’s connect.</h2><p>For Corporate Finance opportunities and finance-focused collaborations.</p><div class="contact-links"><a class="primary" href="mailto:27-prajval.srivastava@fiib.edu.in">Email me</a><a href="https://www.linkedin.com/in/prajvalsrivastava">LinkedIn ↗</a></div></div>',unsafe_allow_html=True)
resume=ASSETS/"Prajval_Srivastava_Resume.docx"
if resume.exists():
    with open(resume,"rb") as f:
        st.download_button("Download Resume",f,file_name=resume.name,mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",key="resume_download")
st.markdown('<div class="footer">© 2026 Prajval Srivastava · Corporate Finance & Financial Analysis</div>',unsafe_allow_html=True)
