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

if "project" not in st.session_state:
    st.session_state.project = None

def open_project(key):
    st.session_state.project = key

def close_project():
    st.session_state.project = None

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Mono:wght@400;500&family=Inter:wght@400;500;600;700;800&family=Newsreader:opsz,wght@6..72,500;6..72,600&display=swap');

:root{
  --bg:#fbfbfa; --paper:#ffffff; --ink:#17191b; --muted:#697075;
  --line:#dedfdd; --soft:#f3f3f0; --accent:#2a57ff; --green:#15805e;
}
html{scroll-behavior:smooth}
body,[class*="css"]{font-family:Inter,sans-serif}
.stApp{background:var(--bg);color:var(--ink)}
.block-container{max-width:1260px;padding:0 42px 70px}
#MainMenu,footer{visibility:hidden}
header[data-testid="stHeader"]{background:rgba(251,251,250,.92)}
a{text-decoration:none!important}

/* top */
.nav{
  height:76px;border-bottom:1px solid var(--line);display:flex;align-items:center;
  justify-content:space-between;gap:20px;
}
.logo{font-size:1rem;font-weight:800;letter-spacing:-.05em}.logo span{color:var(--accent)}
.navlinks{display:flex;gap:24px;align-items:center;flex-wrap:wrap}
.navlinks a{font-family:"DM Mono",monospace;font-size:.56rem;text-transform:uppercase;letter-spacing:.08em;color:#555c60!important}
.navlinks a:hover{color:var(--accent)!important}
.nav-contact{border:1px solid var(--line);padding:8px 10px;border-radius:999px}

/* hero */
.hero{padding:105px 0 85px;border-bottom:1px solid var(--line)}
.hero-top{display:grid;grid-template-columns:1.35fr .65fr;gap:60px;align-items:start}
.eyebrow{font-family:"DM Mono",monospace;font-size:.59rem;color:#7b8286;text-transform:uppercase;letter-spacing:.10em;margin-bottom:22px}
.hero h1{
  font-family:Newsreader,Georgia,serif;font-size:clamp(5rem,11.5vw,11.8rem);
  line-height:.79;letter-spacing:-.075em;font-weight:600;margin:0;color:var(--ink);
}
.hero-sub{
  font-size:clamp(1.15rem,2.3vw,1.6rem);font-weight:700;letter-spacing:-.035em;
  margin:28px 0 14px;max-width:780px;line-height:1.15;
}
.hero-copy{color:var(--muted);font-size:.86rem;line-height:1.9;max-width:760px}
.hero-photo{margin-left:auto;max-width:330px;background:var(--paper);border:1px solid var(--line)}
.hero-photo img{width:100%;display:block;aspect-ratio:1/1;object-fit:cover}
.hero-photo-caption{padding:10px;font-family:"DM Mono",monospace;font-size:.54rem;color:#7b8286;letter-spacing:.08em;text-transform:uppercase}
.hero-meta{display:grid;grid-template-columns:repeat(4,1fr);gap:0;margin-top:58px;border-top:1px solid var(--line)}
.meta-item{padding:15px 18px 0 0;border-right:1px solid var(--line);min-height:70px}
.meta-item:not(:first-child){padding-left:18px}.meta-item:last-child{border-right:0}
.meta-item small{font-family:"DM Mono",monospace;color:#8a9093;font-size:.53rem;letter-spacing:.08em;text-transform:uppercase}
.meta-item strong{display:block;font-size:.75rem;margin-top:4px}

/* sections */
.section{padding-top:92px}
.section-head{display:grid;grid-template-columns:1fr 1fr;gap:30px;border-bottom:1px solid var(--line);padding-bottom:14px}
.section-no{font-family:"DM Mono",monospace;color:#858b8e;font-size:.55rem;text-transform:uppercase;letter-spacing:.09em;margin-bottom:7px}
.section-title{font-family:Newsreader,Georgia,serif;font-size:clamp(2.8rem,5.4vw,5.3rem);font-weight:600;line-height:.88;letter-spacing:-.06em;margin:0}
.section-note{color:var(--muted);font-size:.76rem;line-height:1.75;align-self:end}

/* capability list */
.cap-list{border-bottom:1px solid var(--line)}
.cap-row{display:grid;grid-template-columns:70px 1fr 1fr;gap:20px;padding:20px 0;border-bottom:1px solid var(--line);align-items:start}
.cap-row:last-child{border-bottom:0}
.cap-num{font-family:"DM Mono",monospace;color:var(--accent);font-size:.56rem}
.cap-title{font-weight:800;font-size:1rem;letter-spacing:-.025em}
.cap-copy{color:var(--muted);font-size:.76rem;line-height:1.7}

/* work index */
.work-row{display:grid;grid-template-columns:72px 1fr 170px;gap:20px;align-items:center;border-bottom:1px solid var(--line);padding:26px 0}
.work-row:hover .work-title{color:var(--accent)}
.work-no{font-family:"DM Mono",monospace;color:var(--accent);font-size:.62rem}
.work-kicker{font-family:"DM Mono",monospace;color:#8b9194;font-size:.54rem;letter-spacing:.08em;text-transform:uppercase}
.work-title{font-family:Newsreader,Georgia,serif;font-size:clamp(1.75rem,3vw,3.0rem);font-weight:600;line-height:.95;letter-spacing:-.045em;margin-top:6px;transition:.15s}
.work-meta{text-align:right;font-family:"DM Mono",monospace;color:#7c8387;font-size:.53rem;line-height:1.55;text-transform:uppercase}
.stButton button{
  margin-top:8px!important;background:transparent!important;color:var(--ink)!important;
  border:0!important;border-bottom:1px solid var(--ink)!important;border-radius:0!important;
  padding:.2rem 0!important;font-size:.59rem!important;font-weight:800!important;letter-spacing:.06em!important;
}
.stButton button:hover{color:var(--accent)!important;border-color:var(--accent)!important}

/* project detail */
.project-detail{background:var(--paper);border:1px solid var(--line);padding:25px;margin:30px 0}
.detail-kicker{font-family:"DM Mono",monospace;color:#8b9194;font-size:.55rem;text-transform:uppercase;letter-spacing:.09em}
.detail-title{font-family:Newsreader,Georgia,serif;font-size:clamp(2.3rem,4.5vw,4.5rem);line-height:.9;letter-spacing:-.06em;font-weight:600;margin:7px 0 18px}
.metrics{display:grid;grid-template-columns:repeat(3,1fr);border-top:1px solid var(--line);border-bottom:1px solid var(--line)}
.metric{padding:14px 16px;border-right:1px solid var(--line)}.metric:last-child{border-right:0}
.metric b{display:block;font-size:1.25rem}.metric span{display:block;color:var(--muted);font-size:.57rem;margin-top:3px}
.detail-grid{display:grid;grid-template-columns:1fr 1fr;gap:1px;background:var(--line);margin-top:1px}
.detail-block{background:#fff;padding:18px;min-height:155px}.detail-block.full{grid-column:1/-1;min-height:auto}
.detail-label{font-family:"DM Mono",monospace;color:var(--accent);font-size:.54rem;text-transform:uppercase;letter-spacing:.08em;margin-bottom:8px}
.detail-copy{font-size:.77rem;color:#61686c;line-height:1.75}
.workbook-note{color:var(--muted);font-size:.68rem;margin-top:10px}
.stDownloadButton button{background:var(--ink)!important;color:#fff!important;border:0!important;border-radius:999px!important;padding:.55rem .8rem!important;font-size:.62rem!important}

/* experience */
.exp-row{display:grid;grid-template-columns:230px 1fr;gap:28px;padding:22px 0;border-bottom:1px solid var(--line)}
.exp-title{font-weight:800;font-size:.98rem}.date{font-family:"DM Mono",monospace;color:#81888b;font-size:.55rem;margin-top:5px}
.meta{color:var(--muted);font-size:.76rem;line-height:1.75}

/* education */
.edu-grid{display:grid;grid-template-columns:1fr 1fr;gap:12px}
.edu{background:var(--paper);border:1px solid var(--line);padding:20px}.edu h3{font-family:Newsreader,Georgia,serif;font-size:1.35rem;line-height:1;margin:0 0 7px}.edu p{color:var(--muted);font-size:.72rem;line-height:1.65}

/* skills */
.skill-grid{display:grid;grid-template-columns:repeat(3,1fr);border-top:1px solid var(--line)}
.skill{padding:19px 18px 20px 0;border-right:1px solid var(--line);min-height:155px}.skill:not(:first-child){padding-left:18px}.skill:last-child{border-right:0}
.skill h3{font-size:.85rem;margin:0 0 10px}.pill{display:inline-block;border:1px solid var(--line);padding:5px 6px;margin:3px 3px 0 0;font-family:"DM Mono",monospace;font-size:.48rem;color:#626a6e}

/* contact */
.contact{border-top:1px solid var(--ink);padding:65px 0 10px;margin-top:85px}.contact h2{font-family:Newsreader,Georgia,serif;font-size:clamp(3.8rem,8vw,8rem);line-height:.8;letter-spacing:-.07em;margin:10px 0}
.contact p{color:var(--muted);font-size:.78rem}.contact-links{display:flex;gap:10px;flex-wrap:wrap;margin-top:20px}.contact-links a{padding:10px 12px;border:1px solid var(--line);border-radius:999px;font-size:.6rem;font-weight:800;text-transform:uppercase;letter-spacing:.05em}.contact-links a.primary{background:var(--ink);color:#fff!important;border-color:var(--ink)}
.footer{border-top:1px solid var(--line);padding-top:13px;margin-top:30px;color:#9aa0a3;font-family:"DM Mono",monospace;font-size:.51rem}

/* mobile */
@media(max-width:850px){
 .block-container{padding:0 1rem 3rem}.navlinks{gap:9px}.navlinks a{font-size:.46rem}
 .hero{padding:62px 0 35px}.hero-top{grid-template-columns:1fr;gap:28px}.hero h1{font-size:clamp(4rem,20vw,6.8rem)}.hero-photo{margin:0;max-width:320px}.hero-meta{grid-template-columns:1fr 1fr}.meta-item{border-bottom:1px solid var(--line);}.meta-item:nth-child(2n){border-right:0}
 .section{padding-top:56px}.section-head{grid-template-columns:1fr;gap:12px}.cap-row{grid-template-columns:45px 1fr;gap:10px}.cap-copy{grid-column:2}.work-row{grid-template-columns:42px 1fr;gap:10px}.work-meta{grid-column:2;text-align:left}.metrics{grid-template-columns:1fr 1fr}.metric:nth-child(2){border-right:0}.detail-grid{grid-template-columns:1fr}.detail-block.full{grid-column:auto}.exp-row{grid-template-columns:1fr;gap:7px}.edu-grid,.skill-grid{grid-template-columns:1fr}.skill,.skill:not(:first-child){padding:17px 0;border-right:0;border-bottom:1px solid var(--line)}
}
</style>
""", unsafe_allow_html=True)

def section(title, note, number):
    st.markdown(
        f'<div class="section-head"><div><div class="section-no">{number:02d} / Portfolio</div><h2 class="section-title">{title}</h2></div><div class="section-note">{note}</div></div>',
        unsafe_allow_html=True
    )

# Header
st.markdown("""
<div class="nav">
 <div class="logo">PS<span>®</span></div>
 <div class="navlinks">
  <a href="#capabilities">Capabilities</a>
  <a href="#projects">Selected Work</a>
  <a href="#experience">Experience</a>
  <a href="#education">Education</a>
  <a href="#contact" class="nav-contact">Contact</a>
 </div>
</div>
""",unsafe_allow_html=True)

# Hero
st.markdown('<section class="hero">',unsafe_allow_html=True)
c1,c2=st.columns([1.25,.75],vertical_alignment="center")
with c1:
    st.markdown('<div class="eyebrow">Finance · Financial Analysis · Corporate Finance</div>',unsafe_allow_html=True)
    st.markdown('<h1>Prajval<br>Srivastava</h1>',unsafe_allow_html=True)
    st.markdown('<div class="hero-sub">Corporate Finance &amp; Financial Analysis</div>',unsafe_allow_html=True)
    st.markdown('<div class="hero-copy">PGDM Finance candidate at FIIB with Corporate Finance internship experience at Arizon Network India. I focus on translating financial statements into performance insights through financial benchmarking, ratio analysis, DuPont decomposition, red-flag assessment, and Excel-based analysis. I am seeking a Corporate Finance role where structured financial evaluation supports strategic business decisions.</div>',unsafe_allow_html=True)
with c2:
    p=ASSETS/"profile.png"
    if p.exists():
        st.markdown('<div class="hero-photo">',unsafe_allow_html=True)
        st.image(str(p),use_container_width=True)
        st.markdown('<div class="hero-photo-caption">Prajval Srivastava · New Delhi · FIIB</div></div>',unsafe_allow_html=True)
st.markdown("""
<div class="hero-meta">
 <div class="meta-item"><small>Focus</small><strong>Financial Analysis</strong></div>
 <div class="meta-item"><small>Focus</small><strong>Valuation</strong></div>
 <div class="meta-item"><small>Tools</small><strong>Excel / Analytics</strong></div>
 <div class="meta-item"><small>Target</small><strong>Corporate Finance</strong></div>
</div>
</section>
""",unsafe_allow_html=True)

# Capabilities
st.markdown('<div id="capabilities"></div><section class="section">',unsafe_allow_html=True)
section("Core Capabilities","A restrained, recruiter-first overview of the areas at the center of the portfolio.",2)
st.markdown('<div class="cap-list">',unsafe_allow_html=True)
for n,t,b in [
("01","Financial Analysis","Financial Statement Analysis · Financial Reporting & Analysis · Ratio Analysis · DuPont Analysis"),
("02","Valuation","Valuation is an area of interest; no specific valuation project or evidence was provided, so none is claimed."),
("03","Excel & Analytics","Financial Benchmarking · Financial Modelling in Excel · Data Analysis · Business Research"),
("04","Projects","Financial benchmarking, financial statement analysis, Excel KPI dashboards, and comparative company assessment"),
]:
    st.markdown(f'<div class="cap-row"><div class="cap-num">{n}</div><div class="cap-title">{t}</div><div class="cap-copy">{b}</div></div>',unsafe_allow_html=True)
st.markdown('</div></section>',unsafe_allow_html=True)

# Projects
st.markdown('<div id="projects"></div><section class="section">',unsafe_allow_html=True)
section("Selected Work","Inspired by product/design portfolio indexes: the homepage stays clean while each case study opens in-place.",3)

projects={
"sun-pharma":{"number":"01","kicker":"Financial Statement Analysis","title":"Financial Statement Analysis of Sun Pharmaceutical Industries","tag":"FIIB · Aug–Sep 2025","metrics":[("5 years","audited financials analysed"),("8–15%","YoY swings identified"),("40%","faster recurring metric checks")],"problem":"Understand changes in Sun Pharma's revenue, profitability, and cost structure across five years of audited financials.","did":"Analysed five years of audited Sun Pharma financials using Vertical and Horizontal Analysis and built an Excel KPI dashboard covering Revenue Growth, Net Profit Margin, ROE, and ROA.","tools":"Microsoft Excel","output":"Identified 8–15% YoY swings in revenue, profitability, and cost structure, while the KPI dashboard cut analysis time for recurring metric checks by 40%.","evidence":"The original Sun Pharma Excel workbook is included in this portfolio.","file":"Sun_Pharma_Financial_Analysis.xlsx"},
"media":{"number":"02","kicker":"Financial Benchmarking","title":"Financial Benchmarking of Listed Media Companies","tag":"Arizon Network India","metrics":[("3","listed media companies"),("4 years","comparative analysis"),("5-step","DuPont decomposition")],"problem":"Assess comparative financial health and identify profitability, efficiency, earnings-quality, and leverage risks across three listed media companies.","did":"Built a four-year benchmarking model for ZEEL, Jagran Prakashan, and DB Corp using ratio analysis, five-step DuPont decomposition, and financial red-flag assessment.","tools":"Microsoft Excel · Financial benchmarking model","output":"Surfaced profitability and efficiency gaps and flagged earnings-quality and leverage risks, producing investment-oriented risk insights.","evidence":"The original media benchmarking Excel workbook is included in this portfolio.","file":"Media_Industry_Financial_Benchmarking.xlsx"},
"pipeline":{"number":"03","kicker":"Data Pipeline & Portfolio Analytics","title":"Portfolio Benchmarking Data Pipeline","tag":"Python · pandas · openpyxl","metrics":[("4","time-series datasets"),("5 years","daily price data"),("1","common date index")],"problem":"Reconcile four independent time-series datasets — three mutual funds and the Nifty 50 index — whose five years of daily price data had inconsistent date coverage because of source-specific gaps.","did":"Built a Python-based reconciliation process to detect and remove non-overlapping dates, creating a single common date index across all instruments.","tools":"Python · pandas · openpyxl","output":"Delivered a clean, analysis-ready Excel workbook enabling accurate return comparisons and correlation analysis between actively managed funds and the market benchmark.","evidence":"The original portfolio benchmarking Excel workbook is included in this portfolio.","file":"Portfolio_Benchmarking_Data_Pipeline.xlsx"}}

for key,p in projects.items():
    st.markdown('<div class="work-row">',unsafe_allow_html=True)
    a,b,c=st.columns([.07,.70,.23],vertical_alignment="center")
    with a: st.markdown(f'<div class="work-no">{p["number"]}</div>',unsafe_allow_html=True)
    with b: st.markdown(f'<div class="work-kicker">{p["kicker"]}</div><div class="work-title">{p["title"]}</div>',unsafe_allow_html=True)
    with c:
        st.markdown(f'<div class="work-meta">{p["tag"]}</div>',unsafe_allow_html=True)
        if st.button("Open project ↗",key=f"open_{key}"):
            open_project(key)
            st.rerun()
    st.markdown('</div>',unsafe_allow_html=True)

if st.session_state.project in projects:
    p=projects[st.session_state.project]
    metrics=''.join([f'<div class="metric"><b>{v}</b><span>{l}</span></div>' for v,l in p["metrics"]])
    st.markdown('<div class="project-detail">',unsafe_allow_html=True)
    st.markdown(f'<div class="detail-kicker">{p["number"]} · {p["kicker"]}</div><div class="detail-title">{p["title"]}</div><div class="metrics">{metrics}</div><div class="detail-grid"><div class="detail-block"><div class="detail-label">Problem</div><div class="detail-copy">{p["problem"]}</div></div><div class="detail-block"><div class="detail-label">What I did</div><div class="detail-copy">{p["did"]}</div></div><div class="detail-block"><div class="detail-label">Tools used</div><div class="detail-copy">{p["tools"]}</div></div><div class="detail-block"><div class="detail-label">Output</div><div class="detail-copy">{p["output"]}</div></div><div class="detail-block full"><div class="detail-label">Evidence</div><div class="detail-copy">{p["evidence"]}</div></div></div>',unsafe_allow_html=True)
    fp=ASSETS/p["file"]
    if fp.exists():
        st.markdown('<div class="workbook-note">Original workbook is stored inside the portfolio repository.</div>',unsafe_allow_html=True)
        with open(fp,"rb") as f:
            st.download_button("Download original Excel workbook",f,file_name=fp.name,mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",key=f"dl_{st.session_state.project}")
        st.markdown('<div class="workbook-note">Workbook inspection</div>',unsafe_allow_html=True)
        try:
            xls=pd.ExcelFile(fp,engine="openpyxl")
            sheets=xls.sheet_names[:8]
            with st.expander("Inspect workbook sheets",expanded=False):
                sheet=st.selectbox("Sheet",sheets,key=f"sheet_{st.session_state.project}")
                df=pd.read_excel(fp,sheet_name=sheet,engine="openpyxl")
                st.caption(f"{len(df):,} rows × {len(df.columns):,} columns")
                st.dataframe(df.head(35),use_container_width=True,height=400)
        except Exception:
            pass
    else:
        st.warning("Workbook missing from assets/. Upload the complete repository structure.")
    if st.button("← Back to selected work",key="back"):
        close_project()
        st.rerun()
st.markdown('</section>',unsafe_allow_html=True)

# Experience
st.markdown('<div id="experience"></div><section class="section">',unsafe_allow_html=True)
section("Experience","Professional experience that gives context to the portfolio projects.",4)
st.markdown("""
<div class="exp-row"><div><div class="exp-title">Finance Intern — Arizon Network India</div><div class="date">Apr – Jun 2026</div></div><div class="meta"><ul><li>Built a 50-company, seven-industry financial research database, cutting manual data-pulling time by 30%.</li><li>Delivered a comparative financial health assessment across ZEEL, Jagran Prakashan, and DB Corp using a four-year Excel benchmarking model.</li><li>Flagged earnings-quality and leverage risks through five-step DuPont decomposition and red-flag screening.</li></ul></div></div>
<div class="exp-row"><div><div class="exp-title">Social Intern — Giftable India</div><div class="date">Jan 2026</div></div><div class="meta"><ul><li>Conducted structured telephonic outreach with 150–200 PWD candidates, validating and segmenting profiles across education, employability readiness, and role preferences.</li><li>Co-designed and delivered a grooming and interview-prep workshop for 20–30 PWD candidates.</li><li>Contributed to inclusive job description drafts used in employer outreach.</li></ul></div></div>
""",unsafe_allow_html=True)
st.markdown('</section>',unsafe_allow_html=True)

# Education
st.markdown('<div id="education"></div><section class="section">',unsafe_allow_html=True)
section("Education","Academic background.",5)
st.markdown('<div class="edu-grid"><div class="edu"><h3>Post Graduate Diploma in Management (Finance)</h3><p>Fortune Institute of International Business (FIIB), New Delhi<br>2025 – Present · CGPA: 7.6</p></div><div class="edu"><h3>Bachelor of Commerce</h3><p>Mahatma Gandhi Kashi Vidyapith, Varanasi<br>2021 – 2024 · CGPA: 7.6</p></div></div>',unsafe_allow_html=True)
st.markdown('</section>',unsafe_allow_html=True)

# Skills
st.markdown('<div id="skills"></div><section class="section">',unsafe_allow_html=True)
section("Skills & Certifications","Technical and business capabilities supporting the work shown above.",6)
st.markdown('<div class="skill-grid"><div class="skill"><h3>Technical Skills</h3><span class="pill">Financial Statement Analysis</span><span class="pill">Financial Reporting & Analysis</span><span class="pill">Ratio Analysis</span><span class="pill">DuPont Analysis</span><span class="pill">Financial Benchmarking</span><span class="pill">Financial Modelling (Excel)</span><span class="pill">Business Research</span><span class="pill">Data Analysis</span></div><div class="skill"><h3>Tools</h3><span class="pill">Microsoft Excel</span><span class="pill">PivotTables</span><span class="pill">XLOOKUP</span><span class="pill">HLOOKUP</span><span class="pill">INDEX-MATCH</span><span class="pill">Conditional Formatting</span><span class="pill">Power BI</span><span class="pill">Python</span><span class="pill">PowerPoint</span><span class="pill">Word</span><span class="pill">AI Tools</span></div><div class="skill"><h3>Business Skills</h3><span class="pill">Analytical Thinking</span><span class="pill">Problem Solving</span><span class="pill">Communication</span><span class="pill">Team Collaboration</span><span class="pill">Adaptability</span></div></div>',unsafe_allow_html=True)
st.markdown('</section>',unsafe_allow_html=True)

# Contact
st.markdown('<div id="contact"></div><div class="contact"><div class="section-no">07 / Contact</div><h2>Let’s connect.</h2><p>For Corporate Finance opportunities and finance-focused collaborations.</p><div class="contact-links"><a class="primary" href="mailto:27-prajval.srivastava@fiib.edu.in">Email me</a><a href="https://www.linkedin.com/in/prajvalsrivastava">LinkedIn ↗</a></div></div>',unsafe_allow_html=True)
resume=ASSETS/"Prajval_Srivastava_Resume.docx"
if resume.exists():
    with open(resume,"rb") as f:
        st.download_button("Download Resume",f,file_name=resume.name,mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",key="resume")
st.markdown('<div class="footer">© 2026 Prajval Srivastava · Corporate Finance & Financial Analysis</div>',unsafe_allow_html=True)
