import streamlit as st
from pathlib import Path
import pandas as pd

st.set_page_config(
    page_title="Prajval Srivastava — Portfolio",
    page_icon="PS",
    layout="wide",
    initial_sidebar_state="collapsed",
)

ROOT = Path(__file__).parent
ASSETS = ROOT / "assets"

# --------------------------- STATE ---------------------------
if "chapter" not in st.session_state:
    st.session_state.chapter = "home"
if "project" not in st.session_state:
    st.session_state.project = None

def go(chapter):
    st.session_state.chapter = chapter
    if chapter != "projects":
        st.session_state.project = None
    st.rerun()

def open_project(key):
    st.session_state.chapter = "projects"
    st.session_state.project = key
    st.rerun()

# --------------------------- CSS ---------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Mono:wght@400;500&family=Manrope:wght@400;500;600;700;800&family=Playfair+Display:wght@600;700&display=swap');

:root{
  --bg:#07142c;
  --bg2:#0b1f43;
  --bg3:#11164a;
  --ink:#eef2fb;
  --muted:#aeb8ca;
  --faint:#75829b;
  --line:rgba(255,255,255,.13);
  --accent:#ff6a63;
  --accent2:#bda9ff;
  --panel:rgba(8,20,44,.72);
  --panel2:rgba(14,31,66,.75);
}
html{scroll-behavior:smooth}
body,[class*="css"]{font-family:Manrope,sans-serif}
.stApp{
  min-height:100vh;
  background:
    radial-gradient(circle at 22% 18%, rgba(93,112,207,.20), transparent 23%),
    radial-gradient(circle at 77% 32%, rgba(89,42,124,.18), transparent 25%),
    linear-gradient(180deg,var(--bg) 0%, var(--bg2) 42%, #101744 72%, #0c1026 100%);
  color:var(--ink);
}
.block-container{max-width:1500px;padding:0 48px 44px}
header[data-testid="stHeader"]{background:rgba(7,20,44,.55)}
#MainMenu, footer{visibility:hidden}
a{text-decoration:none!important;color:inherit!important}

.stApp:before{
  content:"";
  position:fixed; inset:0; pointer-events:none; z-index:0;
  background-image:
   radial-gradient(circle at 6% 10%, rgba(255,255,255,.85) 0 1px, transparent 1.6px),
   radial-gradient(circle at 17% 27%, rgba(255,255,255,.45) 0 1px, transparent 1.6px),
   radial-gradient(circle at 32% 9%, rgba(255,255,255,.7) 0 1px, transparent 1.5px),
   radial-gradient(circle at 46% 21%, rgba(255,255,255,.40) 0 1px, transparent 1.4px),
   radial-gradient(circle at 57% 11%, rgba(255,255,255,.65) 0 1px, transparent 1.5px),
   radial-gradient(circle at 73% 28%, rgba(255,255,255,.42) 0 1px, transparent 1.5px),
   radial-gradient(circle at 88% 12%, rgba(255,255,255,.74) 0 1px, transparent 1.5px),
   radial-gradient(circle at 96% 29%, rgba(255,255,255,.4) 0 1px, transparent 1.5px);
  opacity:.85;
}

.topnav{
  position:relative; z-index:10; height:78px; display:flex; align-items:center;
  justify-content:space-between; border-bottom:1px solid var(--line);
}
.brand{font-weight:800;font-size:1.02rem;letter-spacing:-.06em}.brand span{color:var(--accent)}
.navwrap{display:flex;align-items:center;gap:24px}
.navnote{font-family:"DM Mono",monospace;color:var(--faint);font-size:.55rem;text-transform:uppercase;letter-spacing:.09em}
.navbtn{border:0!important;background:transparent!important;color:var(--muted)!important;font-size:.62rem!important;font-weight:700!important;text-transform:uppercase;letter-spacing:.08em!important;padding:.3rem .2rem!important}
.navbtn:hover{color:#fff!important}
.navbtn.active{color:#fff!important}

.hero{
  position:relative; z-index:1; min-height:calc(100vh - 78px); display:flex; align-items:center;
  padding:70px 0 60px;
}
.hero-grid{display:grid;grid-template-columns:1.18fr .82fr;gap:70px;align-items:center;width:100%}
.kicker{font-family:"DM Mono",monospace;color:var(--accent2);font-size:.62rem;letter-spacing:.12em;text-transform:uppercase;margin-bottom:20px}
.hero h1{font-family:"Playfair Display",Georgia,serif;font-size:clamp(4.5rem,10.4vw,10.8rem);line-height:.78;letter-spacing:-.065em;font-weight:600;margin:0;color:var(--ink)}
.hero-title{font-size:clamp(1.15rem,2.2vw,1.7rem);font-weight:700;letter-spacing:-.035em;margin:28px 0 14px}
.hero-copy{max-width:735px;color:var(--muted);font-size:.9rem;line-height:1.9}
.hero-links{display:flex;gap:10px;flex-wrap:wrap;margin-top:30px}
.hero-link{border:1px solid rgba(255,255,255,.22);padding:10px 13px;border-radius:999px;font-size:.62rem;font-weight:800;text-transform:uppercase;letter-spacing:.06em;color:#fff!important}
.hero-link.primary{background:var(--accent);border-color:var(--accent)}
.photo-wrap{position:relative;max-width:450px;margin-left:auto}
.photo-wrap:before{content:"";position:absolute;inset:-18px 18px 20px -18px;border:1px solid rgba(255,255,255,.14)}
.photo{position:relative;width:100%;display:block;border:1px solid rgba(255,255,255,.17);filter:saturate(.7) contrast(1.04)}
.photo-caption{padding:10px 11px;background:rgba(6,16,37,.88);border:1px solid rgba(255,255,255,.10);font-family:"DM Mono",monospace;font-size:.54rem;letter-spacing:.08em;text-transform:uppercase;color:#bdc6d7}
.dot{position:absolute;width:9px;height:9px;border-radius:50%;background:var(--accent);left:-15px;bottom:62px;box-shadow:0 0 25px rgba(255,106,99,.48)}
.hero-bottom{display:flex;gap:25px;flex-wrap:wrap;margin-top:42px;padding-top:14px;border-top:1px solid var(--line)}
.meta{min-width:135px}.meta small{display:block;font-family:"DM Mono",monospace;color:var(--faint);font-size:.54rem;text-transform:uppercase}.meta strong{display:block;color:#fff;font-size:.78rem;margin-top:4px}

.chapter{
  position:relative;z-index:1;min-height:82vh;padding:78px 0 60px;display:flex;flex-direction:column;justify-content:center;
}
.chapter-head{display:grid;grid-template-columns:.95fr 1.05fr;gap:40px;align-items:end;border-bottom:1px solid var(--line);padding-bottom:18px}
.chapter-no{font-family:"DM Mono",monospace;color:var(--accent);font-size:.60rem;letter-spacing:.10em;text-transform:uppercase}
.chapter-title{font-family:"Playfair Display",Georgia,serif;color:#fff;font-size:clamp(3rem,5.8vw,6rem);line-height:.86;letter-spacing:-.055em;font-weight:600;margin:.55rem 0 0}
.chapter-note{color:var(--muted);font-size:.78rem;line-height:1.75;max-width:600px}

.capgrid{display:grid;grid-template-columns:repeat(4,1fr);border-bottom:1px solid var(--line)}
.cap{padding:19px 20px 20px 0;border-right:1px solid var(--line);min-height:190px}
.cap:last-child{border-right:0;padding-right:0}
.capnum{font-family:"DM Mono",monospace;color:var(--accent2);font-size:.58rem}
.cap h3{font-family:"Playfair Display",Georgia,serif;color:#fff;font-size:1.35rem;font-weight:600;margin:37px 0 9px}
.cap p{color:var(--muted);font-size:.77rem;line-height:1.7}

.project-index{border-bottom:1px solid var(--line)}
.project-row{display:grid;grid-template-columns:70px 1fr 175px;gap:20px;align-items:center;min-height:145px;border-top:1px solid var(--line)}
.project-row:first-child{border-top:0}
.project-num{font-family:"DM Mono",monospace;color:var(--accent);font-size:.70rem}
.project-kicker{font-family:"DM Mono",monospace;color:#a9b3c5;font-size:.56rem;letter-spacing:.1em;text-transform:uppercase}
.project-name{font-family:"Playfair Display",Georgia,serif;color:#fff;font-size:clamp(1.55rem,3vw,2.85rem);line-height:.98;letter-spacing:-.045em;font-weight:600;margin-top:6px}
.project-meta{font-family:"DM Mono",monospace;color:#a9b3c5;font-size:.53rem;line-height:1.55;text-transform:uppercase;text-align:right}
.stButton button{border:1px solid rgba(255,255,255,.25)!important;background:rgba(8,18,39,.7)!important;color:#fff!important;border-radius:999px!important;font-size:.60rem!important;font-weight:800!important;letter-spacing:.06em!important}
.stButton button:hover{background:var(--accent)!important;border-color:var(--accent)!important}

.detail{background:var(--panel);border:1px solid rgba(255,255,255,.13);margin-top:24px}
.detail-head{padding:22px;border-bottom:1px solid var(--line)}
.detail-title{font-family:"Playfair Display",Georgia,serif;font-size:clamp(2.1rem,4.5vw,4.8rem);line-height:.9;letter-spacing:-.06em;color:#fff;margin-top:8px}
.metrics{display:grid;grid-template-columns:repeat(3,1fr);border-bottom:1px solid var(--line)}
.metric{padding:17px 20px;border-right:1px solid var(--line)}.metric:last-child{border-right:0}
.metric b{display:block;font-size:1.35rem;color:#fff}.metric span{display:block;color:#aeb8c9;font-size:.58rem;margin-top:3px}
.detail-grid{display:grid;grid-template-columns:1fr 1fr;gap:1px;background:var(--line)}
.detail-block{background:var(--panel2);padding:20px;min-height:175px}.detail-block.full{grid-column:1/-1;min-height:auto}
.detail-label{font-family:"DM Mono",monospace;color:var(--accent);font-size:.56rem;text-transform:uppercase;letter-spacing:.08em;margin-bottom:8px}
.detail-copy{color:#c0c8d6;font-size:.78rem;line-height:1.75}
.workbook-label{font-family:"DM Mono",monospace;color:#9faabd;font-size:.55rem;text-transform:uppercase;letter-spacing:.08em;margin:22px 0 8px}
.preview-note{color:var(--muted);font-size:.70rem;line-height:1.5;margin-bottom:8px}
[data-testid="stDataFrame"]{border:1px solid rgba(255,255,255,.12)!important}
.close-label{font-family:"DM Mono",monospace;color:#aeb8ca;font-size:.56rem;text-transform:uppercase;letter-spacing:.07em;margin:15px 0 20px}

.timeline-item{display:grid;grid-template-columns:230px 1fr;gap:24px;border-bottom:1px solid var(--line);padding:20px 0}
.timeline-title{font-weight:800;color:#fff;font-size:.95rem}.date{font-family:"DM Mono",monospace;color:var(--accent2);font-size:.56rem;margin-top:5px}
.edu-grid,.skill-grid{display:grid;grid-template-columns:1fr 1fr;gap:12px}
.card{background:rgba(9,24,51,.73);border:1px solid var(--line);padding:20px;height:100%}.card h3{font-family:"Playfair Display",Georgia,serif;color:#fff;font-size:1.25rem;margin:0 0 7px}.card p{color:var(--muted);font-size:.74rem;line-height:1.65}
.skill-grid{grid-template-columns:repeat(3,1fr)}.pill{display:inline-block;border:1px solid rgba(255,255,255,.16);padding:5px 7px;margin:3px 3px 0 0;font-family:"DM Mono",monospace;font-size:.50rem;color:#c5ccd8}
.contact{position:relative;z-index:1;border-top:1px solid rgba(255,255,255,.22);padding:60px 0 10px;margin-top:50px}
.contact h2{font-family:"Playfair Display",Georgia,serif;font-size:clamp(3.5rem,7vw,7.8rem);line-height:.82;letter-spacing:-.07em;color:#fff;margin:11px 0 14px}
.contact p{color:var(--muted);font-size:.78rem}.contact-links{display:flex;gap:10px;flex-wrap:wrap;margin-top:22px}.contact-links a{border:1px solid rgba(255,255,255,.2);border-radius:999px;padding:10px 13px;font-size:.62rem;font-weight:800;text-transform:uppercase}
.contact-links a.primary{background:var(--accent);border-color:var(--accent)}
.footer{border-top:1px solid var(--line);margin-top:28px;padding-top:14px;color:#7d889d;font-family:"DM Mono",monospace;font-size:.52rem}

@media(max-width:900px){
  .block-container{padding:0 1rem 3rem}.topnav{height:68px}.navnote{display:none}.navwrap{gap:11px}.navbtn{font-size:.50rem!important}
  .hero{min-height:auto;padding:46px 0 35px}.hero-grid,.chapter-head{grid-template-columns:1fr;gap:30px}.hero h1{font-size:clamp(4rem,20vw,7rem)}
  .photo-wrap{margin:0;max-width:335px}.hero-bottom{gap:12px}.meta{min-width:115px}
  .chapter{min-height:auto;padding-top:58px}.capgrid{grid-template-columns:1fr 1fr}.cap{min-height:165px;border-right:0;border-bottom:1px solid var(--line)}
  .project-row{grid-template-columns:43px 1fr;gap:9px;min-height:135px}.project-meta{grid-column:2;text-align:left}
  .detail-head{padding:18px}.metrics{grid-template-columns:1fr 1fr}.metric:nth-child(2){border-right:0}.metric{border-bottom:1px solid var(--line)}
  .detail-grid{grid-template-columns:1fr}.detail-block.full{grid-column:auto}.timeline-item{grid-template-columns:1fr;gap:7px}.edu-grid,.skill-grid{grid-template-columns:1fr}
}
</style>
""", unsafe_allow_html=True)

# -------------------- TOP NAV --------------------
st.markdown("""
<div class="topnav">
  <div class="brand">PS<span>®</span></div>
  <div class="navwrap">
    <div class="navnote">Finance Portfolio · New Delhi</div>
    <a class="navbtn" href="#capabilities">01 LOOK</a>
    <a class="navbtn" href="#projects">02 ANALYSE</a>
    <a class="navbtn" href="#experience">03 EXPERIENCE</a>
    <a class="navbtn" href="#education">04 BECOME</a>
    <a class="navbtn" href="#contact">CONTACT</a>
  </div>
</div>
""", unsafe_allow_html=True)

# -------------------- HERO --------------------
st.markdown('<section class="hero"><div class="hero-grid">', unsafe_allow_html=True)
c1,c2=st.columns([1.12,.88],vertical_alignment="center")
with c1:
    st.markdown('<div class="kicker">Corporate Finance · Financial Analysis · Excel</div>',unsafe_allow_html=True)
    st.markdown('<h1>Prajval<br>Srivastava</h1>',unsafe_allow_html=True)
    st.markdown('<div class="hero-title">Corporate Finance &amp; Financial Analysis</div>',unsafe_allow_html=True)
    st.markdown('<div class="hero-copy">PGDM Finance candidate at FIIB with Corporate Finance internship experience at Arizon Network India. I focus on translating financial statements into performance insights through financial benchmarking, ratio analysis, DuPont decomposition, red-flag assessment, and Excel-based analysis. I am seeking a Corporate Finance role where structured financial evaluation supports strategic business decisions.</div>',unsafe_allow_html=True)
    st.markdown("""
    <div class="hero-links">
      <a class="hero-link primary" href="#projects">Explore Projects ↘</a>
      <a class="hero-link" href="https://www.linkedin.com/in/prajvalsrivastava">LinkedIn ↗</a>
    </div>
    """,unsafe_allow_html=True)
with c2:
    p=ASSETS/"profile.png"
    if p.exists():
        st.markdown('<div class="photo-wrap">',unsafe_allow_html=True)
        st.image(str(p),use_container_width=True)
        st.markdown('<div class="photo-caption">Prajval Srivastava · New Delhi · FIIB</div><div class="dot"></div></div>',unsafe_allow_html=True)
st.markdown("""
<div class="hero-bottom">
 <div class="meta"><small>Focus</small><strong>Financial Analysis</strong></div>
 <div class="meta"><small>Focus</small><strong>Valuation</strong></div>
 <div class="meta"><small>Tools</small><strong>Excel / Analytics</strong></div>
 <div class="meta"><small>Target</small><strong>Corporate Finance</strong></div>
</div>
</section>
""",unsafe_allow_html=True)

# -------------------- CAPABILITIES --------------------
st.markdown('<div id="capabilities"></div><section class="chapter">',unsafe_allow_html=True)
st.markdown('<div class="chapter-head"><div><div class="chapter-no">01 / LOOK</div><div class="chapter-title">Core<br>Capabilities</div></div><div class="chapter-note">The sequence mirrors the way a finance recruiter should scan the portfolio: financial analysis first, valuation next, then Excel / analytics and project evidence.</div></div>',unsafe_allow_html=True)
st.markdown('<div class="capgrid">',unsafe_allow_html=True)
for n,t,b in [
("01","Financial Analysis","Financial Statement Analysis · Financial Reporting & Analysis · Ratio Analysis · DuPont Analysis"),
("02","Valuation","Valuation is an area of interest; no specific valuation project or evidence was provided, so none is claimed."),
("03","Excel & Analytics","Financial Benchmarking · Financial Modelling in Excel · Data Analysis · Business Research"),
("04","Projects","Financial benchmarking, financial statement analysis, Excel KPI dashboards, and comparative company assessment")
]:
    st.markdown(f'<div class="cap"><div class="capnum">{n}</div><h3>{t}</h3><p>{b}</p></div>',unsafe_allow_html=True)
st.markdown('</div></section>',unsafe_allow_html=True)

# -------------------- PROJECTS --------------------
st.markdown('<div id="projects"></div><section class="chapter">',unsafe_allow_html=True)
st.markdown('<div class="chapter-head"><div><div class="chapter-no">02 / ANALYSE</div><div class="chapter-title">Featured<br>Projects</div></div><div class="chapter-note">The project index keeps the homepage clean. Open any project to stay on this same portfolio and inspect its case study plus original workbook.</div></div>',unsafe_allow_html=True)

projects={
"sun-pharma":{"number":"01","kicker":"Financial Statement Analysis","title":"Financial Statement Analysis of Sun Pharmaceutical Industries","tag":"FIIB · Aug–Sep 2025","metrics":[("5 years","audited financials analysed"),("8–15%","YoY swings identified"),("40%","faster recurring metric checks")],"problem":"Understand changes in Sun Pharma's revenue, profitability, and cost structure across five years of audited financials.","did":"Analysed five years of audited Sun Pharma financials using Vertical and Horizontal Analysis and built an Excel KPI dashboard covering Revenue Growth, Net Profit Margin, ROE, and ROA.","tools":"Microsoft Excel","output":"Identified 8–15% YoY swings in revenue, profitability, and cost structure, while the KPI dashboard cut analysis time for recurring metric checks by 40%.","evidence":"The original Sun Pharma Excel workbook is included in this portfolio.","file":"Sun_Pharma_Financial_Analysis.xlsx"},
"media-benchmarking":{"number":"02","kicker":"Financial Benchmarking","title":"Financial Benchmarking of Listed Media Companies","tag":"Arizon Network India","metrics":[("3","listed media companies"),("4 years","comparative analysis"),("5-step","DuPont decomposition")],"problem":"Assess comparative financial health and identify profitability, efficiency, earnings-quality, and leverage risks across three listed media companies.","did":"Built a four-year benchmarking model for ZEEL, Jagran Prakashan, and DB Corp using ratio analysis, five-step DuPont decomposition, and financial red-flag assessment.","tools":"Microsoft Excel · Financial benchmarking model","output":"Surfaced profitability and efficiency gaps and flagged earnings-quality and leverage risks, producing investment-oriented risk insights.","evidence":"The original media benchmarking Excel workbook is included in this portfolio.","file":"Media_Industry_Financial_Benchmarking.xlsx"},
"portfolio-pipeline":{"number":"03","kicker":"Data Pipeline & Portfolio Analytics","title":"Portfolio Benchmarking Data Pipeline","tag":"Python · pandas · openpyxl","metrics":[("4","time-series datasets"),("5 years","daily price data"),("1","common date index")],"problem":"Reconcile four independent time-series datasets — three mutual funds and the Nifty 50 index — whose five years of daily price data had inconsistent date coverage because of source-specific gaps.","did":"Built a Python-based reconciliation process to detect and remove non-overlapping dates, creating a single common date index across all instruments.","tools":"Python · pandas · openpyxl","output":"Delivered a clean, analysis-ready Excel workbook enabling accurate return comparisons and correlation analysis between actively managed funds and the market benchmark.","evidence":"The original portfolio benchmarking Excel workbook is included in this portfolio.","file":"Portfolio_Benchmarking_Data_Pipeline.xlsx"}}

for key,p in projects.items():
    st.markdown('<div class="project-row">',unsafe_allow_html=True)
    a,b,c=st.columns([.07,.73,.20],vertical_alignment="center")
    with a:
        st.markdown(f'<div class="project-num">{p["number"]}</div>',unsafe_allow_html=True)
    with b:
        st.markdown(f'<div class="project-kicker">{p["kicker"]}</div><div class="project-name">{p["title"]}</div>',unsafe_allow_html=True)
    with c:
        st.markdown(f'<div class="project-meta">{p["tag"]}</div>',unsafe_allow_html=True)
        if st.button("VIEW PROJECT ↗", key=f"open_{key}"):
            open_project(key)
    st.markdown('</div>',unsafe_allow_html=True)

if st.session_state.project in projects:
    p=projects[st.session_state.project]
    metrics=''.join([f'<div class="metric"><b>{v}</b><span>{l}</span></div>' for v,l in p["metrics"]])
    st.markdown('<div class="detail">',unsafe_allow_html=True)
    st.markdown(f'<div class="detail-head"><div class="chapter-no">{p["number"]} / {p["kicker"]}</div><div class="detail-title">{p["title"]}</div><div class="project-meta">{p["tag"]}</div></div><div class="metrics">{metrics}</div><div class="detail-grid"><div class="detail-block"><div class="detail-label">Problem</div><div class="detail-copy">{p["problem"]}</div></div><div class="detail-block"><div class="detail-label">What I did</div><div class="detail-copy">{p["did"]}</div></div><div class="detail-block"><div class="detail-label">Tools used</div><div class="detail-copy">{p["tools"]}</div></div><div class="detail-block"><div class="detail-label">Output</div><div class="detail-copy">{p["output"]}</div></div><div class="detail-block full"><div class="detail-label">Evidence</div><div class="detail-copy">{p["evidence"]}</div></div></div></div>',unsafe_allow_html=True)
    f=ASSETS/p["file"]
    if f.exists():
        with open(f,"rb") as fh:
            st.download_button("Download original Excel workbook",fh,file_name=f.name,mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",key=f"download_{st.session_state.project}")
        st.markdown('<div class="workbook-label">Workbook inspection</div><div class="preview-note">The workbook stays inside this portfolio. Choose a sheet to inspect its data below.</div>',unsafe_allow_html=True)
        try:
            xls=pd.ExcelFile(f,engine="openpyxl")
            names=xls.sheet_names[:8]
            sheet=st.selectbox("Sheet",names,key=f"sheet_{st.session_state.project}")
            df=pd.read_excel(f,sheet_name=sheet,engine="openpyxl")
            st.caption(f"{len(df):,} rows × {len(df.columns):,} columns")
            st.dataframe(df.head(40),use_container_width=True,height=410)
        except Exception:
            st.info("The original Excel workbook is available for download.")
    st.markdown('<div class="close-label">Use the project index above to switch projects.</div>',unsafe_allow_html=True)
st.markdown('</section>',unsafe_allow_html=True)

# -------------------- EXPERIENCE --------------------
st.markdown('<div id="experience"></div><section class="chapter">',unsafe_allow_html=True)
st.markdown('<div class="chapter-head"><div><div class="chapter-no">03 / EXPERIENCE</div><div class="chapter-title">Professional<br>Work</div></div><div class="chapter-note">Relevant professional experience that gives context to the portfolio projects.</div></div>',unsafe_allow_html=True)
st.markdown("""
<div class="timeline-item"><div><div class="timeline-title">Finance Intern — Arizon Network India</div><div class="date">Apr – Jun 2026</div></div><div class="meta"><ul><li>Built a 50-company, seven-industry financial research database, cutting manual data-pulling time by 30%.</li><li>Delivered a comparative financial health assessment across ZEEL, Jagran Prakashan, and DB Corp using a four-year Excel benchmarking model.</li><li>Flagged earnings-quality and leverage risks through five-step DuPont decomposition and red-flag screening.</li></ul></div></div>
<div class="timeline-item"><div><div class="timeline-title">Social Intern — Giftable India</div><div class="date">Jan 2026</div></div><div class="meta"><ul><li>Conducted structured telephonic outreach with 150–200 PWD candidates, validating and segmenting profiles across education, employability readiness, and role preferences.</li><li>Co-designed and delivered a grooming and interview-prep workshop for 20–30 PWD candidates.</li><li>Contributed to inclusive job description drafts used in employer outreach.</li></ul></div></div>
""",unsafe_allow_html=True)
st.markdown('</section>',unsafe_allow_html=True)

# -------------------- EDUCATION --------------------
st.markdown('<div id="education"></div><section class="chapter">',unsafe_allow_html=True)
st.markdown('<div class="chapter-head"><div><div class="chapter-no">04 / BECOME</div><div class="chapter-title">Education</div></div><div class="chapter-note">Academic background supporting the finance focus.</div></div>',unsafe_allow_html=True)
st.markdown('<div class="edu-grid"><div class="card"><h3>Post Graduate Diploma in Management (Finance)</h3><p>Fortune Institute of International Business (FIIB), New Delhi<br>2025 – Present · CGPA: 7.6</p></div><div class="card"><h3>Bachelor of Commerce</h3><p>Mahatma Gandhi Kashi Vidyapith, Varanasi<br>2021 – 2024 · CGPA: 7.6</p></div></div>',unsafe_allow_html=True)
st.markdown('</section>',unsafe_allow_html=True)

# -------------------- SKILLS --------------------
st.markdown('<div id="skills"></div><section class="chapter">',unsafe_allow_html=True)
st.markdown('<div class="chapter-head"><div><div class="chapter-no">05 / SKILLS</div><div class="chapter-title">Skills &<br>Tools</div></div><div class="chapter-note">Skills and tools supporting the project evidence.</div></div>',unsafe_allow_html=True)
st.markdown('<div class="skill-grid"><div class="card"><h3>Technical Skills</h3><span class="pill">Financial Statement Analysis</span><span class="pill">Financial Reporting & Analysis</span><span class="pill">Ratio Analysis</span><span class="pill">DuPont Analysis</span><span class="pill">Financial Benchmarking</span><span class="pill">Financial Modelling (Excel)</span><span class="pill">Business Research</span><span class="pill">Data Analysis</span></div><div class="card"><h3>Tools</h3><span class="pill">Microsoft Excel</span><span class="pill">PivotTables</span><span class="pill">XLOOKUP</span><span class="pill">HLOOKUP</span><span class="pill">INDEX-MATCH</span><span class="pill">Conditional Formatting</span><span class="pill">Power BI</span><span class="pill">Python</span><span class="pill">PowerPoint</span><span class="pill">Word</span><span class="pill">AI Tools</span></div><div class="card"><h3>Business Skills</h3><span class="pill">Analytical Thinking</span><span class="pill">Problem Solving</span><span class="pill">Communication</span><span class="pill">Team Collaboration</span><span class="pill">Adaptability</span></div></div>',unsafe_allow_html=True)
st.markdown('</section>',unsafe_allow_html=True)

# -------------------- CONTACT --------------------
st.markdown('<div id="contact"></div><div class="contact"><div class="chapter-no">06 / CONTACT</div><h2>Let’s connect.</h2><p>For Corporate Finance opportunities and finance-focused collaborations.</p><div class="contact-links"><a class="primary" href="mailto:27-prajval.srivastava@fiib.edu.in">Email me</a><a href="https://www.linkedin.com/in/prajvalsrivastava">LinkedIn ↗</a></div></div>',unsafe_allow_html=True)
resume=ASSETS/"Prajval_Srivastava_Resume.docx"
if resume.exists():
    with open(resume,"rb") as f:
        st.download_button("Download Resume",f,file_name=resume.name,mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",key="resume")
st.markdown('<div class="footer">© 2026 Prajval Srivastava · Corporate Finance & Financial Analysis</div>',unsafe_allow_html=True)
