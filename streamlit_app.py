import streamlit as st
from pathlib import Path
import pandas as pd

st.set_page_config(
    page_title="Prajval Srivastava | Finance Portfolio",
    page_icon="PS",
    layout="wide",
    initial_sidebar_state="collapsed",
)

ROOT = Path(__file__).parent
ASSETS = ROOT / "assets"

# ---------------- THEME ----------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Mono:wght@400;500&family=Inter:wght@400;500;600;700;800&display=swap');

:root{
  --bg:#f4f5f2; --card:#ffffff; --ink:#17212b; --muted:#68737c; --line:#dce1de;
  --accent:#16735a; --accent-soft:#e7f1ed; --navy:#17212b; --warm:#edece7;
}
html{scroll-behavior:smooth}
body,[class*="css"]{font-family:Inter,sans-serif}
.stApp{background:var(--bg);color:var(--ink)}
.block-container{max-width:1280px;padding:0 2rem 4rem}
#MainMenu,footer{visibility:hidden}
header[data-testid="stHeader"]{background:rgba(244,245,242,.92)}
a{text-decoration:none!important}

/* Header */
.topnav{height:74px;border-bottom:1px solid var(--line);display:flex;align-items:center;justify-content:space-between;gap:20px}
.brand{font-size:1.05rem;font-weight:800;letter-spacing:-.05em}
.brand span{color:var(--accent)}
.navlinks{display:flex;gap:20px;flex-wrap:wrap}
.navlinks a{color:#4d5961!important;font-size:.68rem;font-weight:700;text-transform:uppercase;letter-spacing:.07em}
.navlinks a:hover{color:var(--accent)!important}
.nav-cta{padding:9px 13px;border-radius:999px;background:var(--navy);color:#fff!important;font-size:.65rem;font-weight:800;text-transform:uppercase}

/* Hero */
.hero{padding:76px 0 44px;border-bottom:1px solid var(--line)}
.hero-grid{display:grid;grid-template-columns:1.3fr .7fr;gap:40px;align-items:end}
.hero-kicker{font-family:"DM Mono",monospace;color:var(--accent);font-size:.66rem;letter-spacing:.1em;text-transform:uppercase;margin-bottom:16px}
.hero h1{font-size:clamp(4.5rem,10vw,9.2rem);line-height:.8;letter-spacing:-.095em;margin:0;color:var(--ink);font-weight:800}
.hero-title{font-size:clamp(1.35rem,2.8vw,1.9rem);font-weight:700;letter-spacing:-.04em;margin:25px 0 12px}
.hero-copy{max-width:780px;color:var(--muted);font-size:.93rem;line-height:1.85}
.hero-photo{width:100%;max-width:400px;margin-left:auto;border:1px solid var(--line);background:var(--warm)}
.hero-photo img{width:100%;aspect-ratio:4/5;object-fit:cover;display:block}
.photo-caption{padding:12px 14px;font-family:"DM Mono",monospace;font-size:.57rem;letter-spacing:.08em;text-transform:uppercase;color:var(--muted)}
.hero-bottom{display:flex;gap:40px;flex-wrap:wrap;margin-top:35px}
.hero-stat{padding-top:12px;border-top:2px solid var(--ink);min-width:150px}
.hero-stat small{font-family:"DM Mono",monospace;color:var(--muted);font-size:.56rem;text-transform:uppercase;letter-spacing:.06em}
.hero-stat strong{display:block;font-size:.84rem;margin-top:4px}

/* Sections */
.section{padding:72px 0 8px}
.section-top{display:flex;justify-content:space-between;gap:30px;align-items:end;border-bottom:1px solid var(--line);padding-bottom:17px}
.section-no{font-family:"DM Mono",monospace;color:var(--accent);font-size:.58rem;letter-spacing:.09em;text-transform:uppercase;margin-bottom:6px}
.section-title{font-size:clamp(2.2rem,5vw,4.8rem);line-height:.88;letter-spacing:-.07em;margin:0;font-weight:800}
.section-note{max-width:500px;color:var(--muted);font-size:.77rem;line-height:1.7}

/* Capability cards */
.cap-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin-top:14px}
.cap-card{background:var(--card);border:1px solid var(--line);padding:20px;min-height:195px;position:relative}
.cap-card:after{content:"";position:absolute;left:20px;bottom:20px;width:28px;height:2px;background:var(--accent)}
.cap-num{font-family:"DM Mono",monospace;color:var(--accent);font-size:.62rem}
.cap-card h3{font-size:1.08rem;margin:34px 0 10px;letter-spacing:-.03em}
.cap-card p{color:var(--muted);font-size:.8rem;line-height:1.7}

/* Projects */
.project-card{background:var(--card);border:1px solid var(--line);margin-top:14px;padding:0}
.project-top{display:grid;grid-template-columns:70px 1fr auto;gap:18px;align-items:start;padding:22px;border-bottom:1px solid var(--line)}
.project-num{font-family:"DM Mono",monospace;color:var(--accent);font-size:.7rem}
.project-kicker{font-family:"DM Mono",monospace;color:#8b959b;font-size:.56rem;letter-spacing:.09em;text-transform:uppercase}
.project-title{font-size:clamp(1.45rem,2.7vw,2.45rem);line-height:1.02;letter-spacing:-.05em;font-weight:800;margin-top:6px}
.project-meta{font-family:"DM Mono",monospace;color:var(--muted);font-size:.55rem;text-align:right;line-height:1.55;text-transform:uppercase}
.project-body{padding:22px}
.project-columns{display:grid;grid-template-columns:1.15fr .85fr;gap:18px}
.project-summary{color:#5f696f;font-size:.82rem;line-height:1.75}
.project-label{font-family:"DM Mono",monospace;color:var(--accent);font-size:.56rem;text-transform:uppercase;letter-spacing:.08em;margin-bottom:8px}
.project-metrics{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;margin-bottom:18px}
.metric{background:var(--accent-soft);padding:12px}
.metric strong{display:block;font-size:1.1rem;letter-spacing:-.04em}
.metric span{display:block;color:var(--muted);font-size:.57rem;margin-top:2px;line-height:1.35}
.project-side{border-left:1px solid var(--line);padding-left:18px}
.view{display:inline-block;padding:9px 11px;background:var(--navy);color:#fff!important;font-size:.62rem;font-weight:800;text-transform:uppercase;letter-spacing:.06em;margin-top:12px}
.view:hover{background:var(--accent)!important}
.detail{margin:14px 22px 22px;border-top:1px solid var(--line);padding-top:22px}
.detail-grid{display:grid;grid-template-columns:1fr 1fr;gap:1px;background:var(--line);border:1px solid var(--line)}
.detail-block{background:#fff;padding:18px;min-height:150px}
.detail-block.full{grid-column:1/-1;min-height:auto}
.detail-copy{color:#5f696f;font-size:.78rem;line-height:1.75}
.download-row{padding-top:16px;display:flex;gap:10px;align-items:center;flex-wrap:wrap}
.file-note{color:var(--muted);font-size:.7rem}
.stDownloadButton button{border-radius:999px!important;background:var(--navy)!important;color:white!important;border:0!important;font-size:.64rem!important;font-weight:800!important}
.preview-label{font-family:"DM Mono",monospace;color:#8b959b;font-size:.56rem;text-transform:uppercase;letter-spacing:.08em;margin:22px 0 8px}

/* Experience / education / skills */
.timeline-item{display:grid;grid-template-columns:220px 1fr;gap:24px;border-bottom:1px solid var(--line);padding:20px 0}
.timeline-title{font-size:1rem;font-weight:800}
.date{font-family:"DM Mono",monospace;color:var(--accent);font-size:.58rem;margin-top:5px}
.meta{color:var(--muted);font-size:.8rem;line-height:1.75}
.edu-grid{display:grid;grid-template-columns:1fr 1fr;gap:12px}
.edu-card{background:#fff;border:1px solid var(--line);padding:20px}
.edu-card h3{font-size:1rem;margin:0 0 6px}
.edu-card p{font-size:.75rem;line-height:1.65;color:var(--muted)}
.skill-grid{display:grid;grid-template-columns:1fr 1fr 1fr;gap:12px}
.skill-card{background:#fff;border:1px solid var(--line);padding:20px;min-height:160px}
.skill-card h3{font-size:.9rem;margin:0 0 10px}
.pill{display:inline-block;border:1px solid var(--line);background:#fafbf9;color:#566067;padding:6px 7px;margin:3px 3px 0 0;font-family:"DM Mono",monospace;font-size:.52rem}

/* Contact */
.contact{margin-top:72px;padding:55px 0 15px;border-top:1px solid var(--ink)}
.contact h2{font-size:clamp(3.4rem,7vw,7rem);line-height:.82;letter-spacing:-.085em;margin:12px 0}
.contact p{color:var(--muted);font-size:.8rem}.contact-links{display:flex;gap:10px;flex-wrap:wrap;margin-top:20px}.contact-links a{border:1px solid var(--line);padding:10px 13px;color:var(--ink)!important;font-size:.63rem;font-weight:800;text-transform:uppercase}.contact-links a.primary{background:var(--navy);color:#fff!important;border-color:var(--navy)}
.footer{border-top:1px solid var(--line);padding-top:14px;color:#9ba1a4;font-family:"DM Mono",monospace;font-size:.53rem;margin-top:30px}

/* mobile */
@media(max-width:900px){
 .block-container{padding:0 1rem 3rem}.navlinks{display:none}.hero{padding:42px 0 30px}.hero-grid{grid-template-columns:1fr}.hero-photo{margin:20px 0 0;max-width:340px}.hero h1{font-size:clamp(4rem,19vw,6.5rem)}
 .cap-grid{grid-template-columns:1fr 1fr}.cap-card{min-height:175px}.section{padding-top:55px}.section-top{display:block}.section-note{margin-top:10px}
 .project-top{grid-template-columns:45px 1fr}.project-meta{grid-column:2;text-align:left;margin-top:3px}.project-columns{grid-template-columns:1fr}.project-side{border-left:0;border-top:1px solid var(--line);padding:16px 0 0}.project-metrics{grid-template-columns:1fr 1fr}.detail-grid{grid-template-columns:1fr}.detail-block.full{grid-column:auto}.timeline-item{grid-template-columns:1fr;gap:8px}.edu-grid,.skill-grid{grid-template-columns:1fr}
}
</style>
""", unsafe_allow_html=True)

def section_head(num, title, note):
    st.markdown(
        f'<div class="section-top"><div><div class="section-no">{num:02d} / Portfolio</div><h2 class="section-title">{title}</h2></div><div class="section-note">{note}</div></div>',
        unsafe_allow_html=True
    )

# Top navigation
st.markdown("""
<div class="topnav">
  <div class="brand">PS<span>®</span></div>
  <div class="navlinks">
    <a href="#capabilities">Capabilities</a><a href="#projects">Projects</a><a href="#experience">Experience</a><a href="#education">Education</a><a href="#skills">Skills</a>
  </div>
  <a class="nav-cta" href="#contact">Contact</a>
</div>
""", unsafe_allow_html=True)

# Hero
st.markdown('<section class="hero">', unsafe_allow_html=True)
c1,c2=st.columns([1.25,.75],vertical_alignment="center")
with c1:
    st.markdown('<div class="hero-kicker">Corporate Finance · Financial Analysis · Excel</div>',unsafe_allow_html=True)
    st.markdown('<h1>Prajval<br>Srivastava</h1>',unsafe_allow_html=True)
    st.markdown('<div class="hero-title">Corporate Finance &amp; Financial Analysis</div>',unsafe_allow_html=True)
    st.markdown('<div class="hero-copy">PGDM Finance candidate at FIIB with Corporate Finance internship experience at Arizon Network India. I focus on translating financial statements into performance insights through financial benchmarking, ratio analysis, DuPont decomposition, red-flag assessment, and Excel-based analysis. I am seeking a Corporate Finance role where structured financial evaluation supports strategic business decisions.</div>',unsafe_allow_html=True)
with c2:
    if (ASSETS/"profile.png").exists():
        st.markdown('<div class="hero-photo">',unsafe_allow_html=True)
        st.image(str(ASSETS/"profile.png"),use_container_width=True)
        st.markdown('<div class="photo-caption">Prajval Srivastava · New Delhi · FIIB</div></div>',unsafe_allow_html=True)
st.markdown("""
<div class="hero-bottom">
  <div class="hero-stat"><small>Focus</small><strong>Financial Analysis</strong></div>
  <div class="hero-stat"><small>Focus</small><strong>Valuation</strong></div>
  <div class="hero-stat"><small>Focus</small><strong>Excel / Analytics</strong></div>
  <div class="hero-stat"><small>Target</small><strong>Corporate Finance</strong></div>
</div>
</section>
""",unsafe_allow_html=True)

# Capabilities
st.markdown('<div id="capabilities"></div><div class="section">',unsafe_allow_html=True)
section_head(2,"Core Capabilities","Financial analysis first, then valuation, analytics, and project evidence.")
st.markdown('<div class="cap-grid">',unsafe_allow_html=True)
for n,t,b in [
("01","Financial Analysis","Financial Statement Analysis · Financial Reporting & Analysis · Ratio Analysis · DuPont Analysis"),
("02","Valuation","Valuation is an area of interest; no specific valuation project or evidence was provided, so none is claimed."),
("03","Excel & Analytics","Financial Benchmarking · Financial Modelling in Excel · Data Analysis · Business Research"),
("04","Projects","Financial benchmarking, financial statement analysis, Excel KPI dashboards, and comparative company assessment"),
]:
    st.markdown(f'<div class="cap-card"><div class="cap-num">{n}</div><h3>{t}</h3><p>{b}</p></div>',unsafe_allow_html=True)
st.markdown('</div></div>',unsafe_allow_html=True)

# Projects
st.markdown('<div id="projects"></div><div class="section">',unsafe_allow_html=True)
section_head(3,"Featured Projects","Evidence-led finance work. Open a project to inspect its workbook and previews.")
projects={
"sun-pharma":{"number":"01","kicker":"Financial Statement Analysis","title":"Financial Statement Analysis of Sun Pharmaceutical Industries","tag":"FIIB · Aug–Sep 2025","metrics":[("5 years","audited financials analysed"),("8–15%","YoY swings identified"),("40%","faster recurring metric checks")],"problem":"Understand changes in Sun Pharma's revenue, profitability, and cost structure across five years of audited financials.","did":"Analysed five years of audited Sun Pharma financials using Vertical and Horizontal Analysis and built an Excel KPI dashboard covering Revenue Growth, Net Profit Margin, ROE, and ROA.","tools":"Microsoft Excel","output":"Identified 8–15% YoY swings in revenue, profitability, and cost structure, while the KPI dashboard cut analysis time for recurring metric checks by 40%.","evidence":"The original Sun Pharma Excel workbook is included in this portfolio, along with selected project preview images.","file":"Sun_Pharma_Financial_Analysis.xlsx","previews":["sunpharma_report.png","sunpharma_dupont.png"]},
"media-benchmarking":{"number":"02","kicker":"Financial Benchmarking","title":"Financial Benchmarking of Listed Media Companies","tag":"Arizon Network India","metrics":[("3","listed media companies"),("4 years","comparative analysis"),("5-step","DuPont decomposition")],"problem":"Assess comparative financial health and identify profitability, efficiency, earnings-quality, and leverage risks across three listed media companies.","did":"Built a four-year benchmarking model for ZEEL, Jagran Prakashan, and DB Corp using ratio analysis, five-step DuPont decomposition, and financial red-flag assessment.","tools":"Microsoft Excel · Financial benchmarking model","output":"Surfaced profitability and efficiency gaps and flagged earnings-quality and leverage risks, producing investment-oriented risk insights.","evidence":"The original media benchmarking Excel workbook is included in this portfolio, along with selected project preview images.","file":"Media_Industry_Financial_Benchmarking.xlsx","previews":["media_comparison.png","media_ratio_analysis.png"]},
"portfolio-pipeline":{"number":"03","kicker":"Data Pipeline & Portfolio Analytics","title":"Portfolio Benchmarking Data Pipeline","tag":"Python · pandas · openpyxl","metrics":[("4","time-series datasets"),("5 years","daily price data"),("1","common date index")],"problem":"Reconcile four independent time-series datasets — three mutual funds and the Nifty 50 index — whose five years of daily price data had inconsistent date coverage because of source-specific gaps.","did":"Built a Python-based reconciliation process to detect and remove non-overlapping dates, creating a single common date index across all instruments.","tools":"Python · pandas · openpyxl","output":"Delivered a clean, analysis-ready Excel workbook enabling accurate return comparisons and correlation analysis between actively managed funds and the market benchmark.","evidence":"The original portfolio benchmarking Excel workbook is included in this portfolio, along with a selected project preview.","file":"Portfolio_Benchmarking_Data_Pipeline.xlsx","previews":["portfolio_comparison.png"]}}

for key,p in projects.items():
    st.markdown(f"""
    <div class="project-card">
      <div class="project-top"><div class="project-num">{p["number"]}</div><div><div class="project-kicker">{p["kicker"]}</div><div class="project-title">{p["title"]}</div></div><div class="project-meta">{p["tag"]}</div></div>
      <div class="project-body">
        <div class="project-metrics">{''.join([f'<div class="metric"><strong>{v}</strong><span>{l}</span></div>' for v,l in p["metrics"]])}</div>
        <div class="project-columns">
          <div><div class="project-label">Why it matters</div><div class="project-summary">{p["problem"]}</div></div>
          <div class="project-side"><div class="project-label">Portfolio evidence</div><div class="project-summary">Case study, selected preview images, and original Excel workbook.</div><a class="view" href="?project={key}#project-detail">View Project ↗</a></div>
        </div>
      </div>
    </div>
    """,unsafe_allow_html=True)

selected=st.query_params.get("project")
if selected in projects:
    p=projects[selected]
    st.markdown('<div id="project-detail"></div>',unsafe_allow_html=True)
    metrics=''.join([f'<div class="metric"><strong>{v}</strong><span>{l}</span></div>' for v,l in p["metrics"]])
    st.markdown(f"""
    <div class="detail">
      <div class="project-kicker">{p["number"]} · {p["kicker"]}</div>
      <div class="project-title" style="margin-bottom:16px;">{p["title"]}</div>
      <div class="project-metrics">{metrics}</div>
      <div class="detail-grid">
        <div class="detail-block"><div class="project-label">Problem</div><div class="detail-copy">{p["problem"]}</div></div>
        <div class="detail-block"><div class="project-label">What I did</div><div class="detail-copy">{p["did"]}</div></div>
        <div class="detail-block"><div class="project-label">Tools used</div><div class="detail-copy">{p["tools"]}</div></div>
        <div class="detail-block"><div class="project-label">Output</div><div class="detail-copy">{p["output"]}</div></div>
        <div class="detail-block full evidence"><div class="project-label">Evidence</div><div class="detail-copy">{p["evidence"]}</div></div>
      </div>
      <div class="download-row"><span class="file-note">Original workbook included in the repository:</span></div>
    </div>
    """,unsafe_allow_html=True)

    fpath=ASSETS/p["file"]
    if fpath.exists():
        with open(fpath,"rb") as f:
            st.download_button("Download original Excel workbook",f,file_name=fpath.name,mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",key=f"download_{selected}")
        st.markdown('<div class="preview-label">Workbook preview</div>',unsafe_allow_html=True)
        try:
            xls=pd.ExcelFile(fpath,engine="openpyxl")
            names=xls.sheet_names[:8]
            tabs=st.tabs(names)
            for tab,sheet in zip(tabs,names):
                with tab:
                    df=pd.read_excel(fpath,sheet_name=sheet,engine="openpyxl")
                    st.caption(f"{len(df):,} rows × {len(df.columns):,} columns")
                    st.dataframe(df.head(30),use_container_width=True,height=380)
        except Exception:
            st.info("Workbook preview is unavailable, but the original workbook can still be downloaded.")
    else:
        st.warning("Workbook missing from assets/. Upload the complete repository.")
    prevs=[ASSETS/"project_previews"/x for x in p["previews"] if (ASSETS/"project_previews"/x).exists()]
    if prevs:
        st.markdown('<div class="preview-label">Selected evidence previews</div>',unsafe_allow_html=True)
        cols=st.columns(len(prevs))
        for col,img in zip(cols,prevs):
            with col: st.image(str(img),use_container_width=True)
    st.markdown('<a href="?project=#projects" style="display:inline-block;margin:16px 0;color:#17212b!important;font-weight:800;font-size:.62rem;text-transform:uppercase;">← Back to projects</a>',unsafe_allow_html=True)
st.markdown('</div>',unsafe_allow_html=True)

# Experience
st.markdown('<div id="experience"></div><div class="section">',unsafe_allow_html=True)
section_head(4,"Experience","Relevant professional work.")
st.markdown("""
<div class="timeline-item"><div><div class="timeline-title">Finance Intern — Arizon Network India</div><div class="date">Apr – Jun 2026</div></div><div class="meta"><ul><li>Built a 50-company, seven-industry financial research database, cutting manual data-pulling time by 30%.</li><li>Delivered a comparative financial health assessment across ZEEL, Jagran Prakashan, and DB Corp using a four-year Excel benchmarking model.</li><li>Flagged earnings-quality and leverage risks through five-step DuPont decomposition and red-flag screening.</li></ul></div></div>
<div class="timeline-item"><div><div class="timeline-title">Social Intern — Giftable India</div><div class="date">Jan 2026</div></div><div class="meta"><ul><li>Conducted structured telephonic outreach with 150–200 PWD candidates, validating and segmenting profiles across education, employability readiness, and role preferences.</li><li>Co-designed and delivered a grooming and interview-prep workshop for 20–30 PWD candidates.</li><li>Contributed to inclusive job description drafts used in employer outreach.</li></ul></div></div>
""",unsafe_allow_html=True)
st.markdown('</div>',unsafe_allow_html=True)

# Education
st.markdown('<div id="education"></div><div class="section">',unsafe_allow_html=True)
section_head(5,"Education","Academic background.")
st.markdown('<div class="edu-grid"><div class="edu-card"><h3>Post Graduate Diploma in Management (Finance)</h3><p>Fortune Institute of International Business (FIIB), New Delhi<br>2025 – Present · CGPA: 7.6</p></div><div class="edu-card"><h3>Bachelor of Commerce</h3><p>Mahatma Gandhi Kashi Vidyapith, Varanasi<br>2021 – 2024 · CGPA: 7.6</p></div></div></div>',unsafe_allow_html=True)

# Skills
st.markdown('<div id="skills"></div><div class="section">',unsafe_allow_html=True)
section_head(6,"Skills & Certifications","Technical and business capabilities supporting the project evidence.")
st.markdown('<div class="skill-grid"><div class="skill-card"><h3>Technical Skills</h3><span class="pill">Financial Statement Analysis</span><span class="pill">Financial Reporting & Analysis</span><span class="pill">Ratio Analysis</span><span class="pill">DuPont Analysis</span><span class="pill">Financial Benchmarking</span><span class="pill">Financial Modelling (Excel)</span><span class="pill">Business Research</span><span class="pill">Data Analysis</span></div><div class="skill-card"><h3>Tools</h3><span class="pill">Microsoft Excel</span><span class="pill">PivotTables</span><span class="pill">XLOOKUP</span><span class="pill">HLOOKUP</span><span class="pill">INDEX-MATCH</span><span class="pill">Conditional Formatting</span><span class="pill">Power BI</span><span class="pill">Python</span><span class="pill">PowerPoint</span><span class="pill">Word</span><span class="pill">AI Tools</span></div><div class="skill-card"><h3>Business Skills</h3><span class="pill">Analytical Thinking</span><span class="pill">Problem Solving</span><span class="pill">Communication</span><span class="pill">Team Collaboration</span><span class="pill">Adaptability</span></div></div></div>',unsafe_allow_html=True)

# Contact
st.markdown('<div id="contact"></div><div class="contact"><div class="contact-kicker">07 / Contact</div><h2>Let’s connect.</h2><p>For Corporate Finance opportunities and finance-focused collaborations.</p><div class="contact-links"><a class="primary" href="mailto:27-prajval.srivastava@fiib.edu.in">Email me</a><a href="https://www.linkedin.com/in/prajvalsrivastava">LinkedIn ↗</a></div></div>',unsafe_allow_html=True)
resume=ASSETS/"Prajval_Srivastava_Resume.docx"
if resume.exists():
    with open(resume,"rb") as f:
        st.download_button("Download Resume",f,file_name=resume.name,mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document")
st.markdown('<div class="footer">© 2026 Prajval Srivastava · Corporate Finance & Financial Analysis</div>',unsafe_allow_html=True)
