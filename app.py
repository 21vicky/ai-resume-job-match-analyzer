
from resume_generator import generate_resume_pdf
from resume_improver import improve_resume

import streamlit as st
import plotly.graph_objects as go
import html

from resume_parser import extract_text_from_pdf
from text_processor import clean_text
from skill_extractor import extract_skills
from matcher import calculate_similarity


# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="ResumeIQ | AI Resume Analyzer",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ==========================================
# SESSION STATE
# ==========================================

if "analysis" not in st.session_state:
    st.session_state.analysis = None

if "improved_resume" not in st.session_state:
    st.session_state.improved_resume = None

if "selected_template" not in st.session_state:
    st.session_state.selected_template = "ATS Professional"


# ==========================================
# CUSTOM CSS
# ==========================================

st.markdown("""
<style>

.stApp {
    background-color: #0B1120;
    color: #E2E8F0;
}

[data-testid="stSidebar"] {
    background-color: #111827;
    border-right: 1px solid #263449;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
    max-width: 1400px;
}

h1, h2, h3 {
    color: #F8FAFC !important;
}

p, label {
    color: #CBD5E1;
}

[data-testid="stMetric"] {
    background: linear-gradient(135deg, #172338, #1E293B);
    padding: 20px;
    border: 1px solid #334155;
    border-radius: 14px;
}

[data-testid="stMetricLabel"] {
    color: #94A3B8 !important;
}

[data-testid="stMetricValue"] {
    color: #38BDF8 !important;
}

.stButton > button {
    background: linear-gradient(90deg, #2563EB, #06B6D4);
    color: white;
    border: none;
    border-radius: 10px;
    padding: 12px;
    font-weight: 600;
}

.stButton > button:hover {
    color: white;
}

div[data-testid="stFileUploader"] {
    background-color: #172338;
    padding: 15px;
    border-radius: 12px;
}

div[data-testid="stTextArea"] textarea {
    background-color: #172338;
    color: white;
    border: 1px solid #334155;
    border-radius: 10px;
}

.skill-chip {
    display: inline-block;
    padding: 8px 13px;
    margin: 5px 5px 5px 0;
    border-radius: 20px;
    font-size: 13px;
    font-weight: 600;
}

.matched {
    background-color: #064E3B;
    color: #6EE7B7;
    border: 1px solid #059669;
}

.missing {
    background-color: #7F1D1D;
    color: #FCA5A5;
    border: 1px solid #DC2626;
}

.additional {
    background-color: #1E3A8A;
    color: #BFDBFE;
    border: 1px solid #3B82F6;
}

.info-card {
    background: #172338;
    padding: 18px;
    border-radius: 12px;
    border: 1px solid #334155;
    margin-bottom: 12px;
}

.footer {
    text-align: center;
    color: #64748B;
    padding: 30px;
    font-size: 13px;
}

</style>
""", unsafe_allow_html=True)


# ==========================================
# HELPER FUNCTIONS
# ==========================================

def render_skill_chips(skills, css_class):

    if skills:

        chips = "".join(
            f'<span class="skill-chip {css_class}">'
            f'{html.escape(str(skill))}</span>'
            for skill in skills
        )

        st.markdown(chips, unsafe_allow_html=True)

    else:
        st.info("No skills identified.")


def render_match_gauge(score):

    gauge = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=score,
            number={
                "suffix": "%",
                "font": {
                    "size": 45,
                    "color": "#38BDF8"
                }
            },
            gauge={
                "axis": {
                    "range": [0, 100],
                    "tickcolor": "#94A3B8"
                },
                "bar": {
                    "color": "#38BDF8"
                },
                "bgcolor": "#172338",
                "borderwidth": 0,
                "steps": [
                    {"range": [0, 40], "color": "#7F1D1D"},
                    {"range": [40, 70], "color": "#78350F"},
                    {"range": [70, 100], "color": "#064E3B"}
                ]
            }
        )
    )

    gauge.update_layout(
        height=280,
        paper_bgcolor="#0B1120",
        font_color="#E2E8F0",
        margin=dict(t=30, b=10, l=30, r=30)
    )

    st.plotly_chart(gauge, use_container_width=True)


def render_footer():

    st.markdown("""
    <div class="footer">
        ResumeIQ | AI Resume & Job Match Analyzer<br>
        Built with Python, NLP, TF-IDF, Streamlit and Plotly<br>
        Developed by Vignesh U | 30 Days 30 AI Projects
    </div>
    """, unsafe_allow_html=True)


# ==========================================
# SIDEBAR NAVIGATION
# ==========================================

with st.sidebar:

    st.markdown("# 📄 ResumeIQ")
    st.caption("AI-POWERED CAREER ANALYTICS")

    st.divider()

    page = st.radio(
        "Navigation",
        [
            "🏠 Dashboard",
            "📊 Skill Analytics",
            "🎯 Improvement Tips",
            "📝 Resume Builder",
            "📥 Download Resume"
        ],
        label_visibility="collapsed"
    )

    st.divider()

    st.markdown("### About")

    st.write(
        "ResumeIQ analyzes your resume against "
        "a job description using NLP, TF-IDF "
        "and skill extraction."
    )

    st.divider()

    st.caption("Built by Vignesh U")
    st.caption("Day 04 | 30 Days 30 AI Projects")


# ==========================================
# DASHBOARD PAGE
# ==========================================

if page == "🏠 Dashboard":

    st.markdown("# Welcome to ResumeIQ 👋")

    st.write(
        "Analyze your resume. Discover skill gaps. "
        "Improve your career opportunities."
    )

    st.divider()

    st.markdown("## 📝 Resume Analysis")

    col1, col2 = st.columns(2, gap="large")

    with col1:

        st.markdown("### 📄 Upload Resume")

        uploaded_file = st.file_uploader(
            "Upload your resume in PDF format",
            type=["pdf"],
            key="resume_upload"
        )

    with col2:

        st.markdown("### 💼 Job Description")

        job_description = st.text_area(
            "Paste the job description",
            height=190,
            placeholder="Paste job responsibilities, requirements and skills here...",
            key="job_description"
        )

    if st.button(
        "🚀 Analyze My Resume",
        use_container_width=True
    ):

        if uploaded_file is None:

            st.error("Please upload your resume PDF.")

        elif not job_description.strip():

            st.error("Please enter a job description.")

        else:

            try:

                with st.spinner("Analyzing your resume..."):

                    uploaded_file.seek(0)

                    resume_text = extract_text_from_pdf(
                        uploaded_file
                    )

                    if not resume_text.strip():

                        st.error(
                            "Could not extract readable text from this PDF."
                        )

                        st.stop()

                    cleaned_resume = clean_text(resume_text)
                    cleaned_job = clean_text(job_description)

                    resume_skills = extract_skills(resume_text)
                    job_skills = extract_skills(job_description)

                    match_score = calculate_similarity(
                        cleaned_resume,
                        cleaned_job
                    )

                    matching_skills = sorted(
                        set(resume_skills) & set(job_skills)
                    )

                    missing_skills = sorted(
                        set(job_skills) - set(resume_skills)
                    )

                    extra_skills = sorted(
                        set(resume_skills) - set(job_skills)
                    )

                    st.session_state.analysis = {
                        "resume_text": resume_text,
                        "job_description": job_description,
                        "filename": uploaded_file.name,
                        "match_score": match_score,
                        "resume_skills": resume_skills,
                        "job_skills": job_skills,
                        "matching_skills": matching_skills,
                        "missing_skills": missing_skills,
                        "extra_skills": extra_skills
                    }

                    # Clear previous improved resume
                    st.session_state.improved_resume = None

                    st.session_state.selected_template = (
                        "ATS Professional"
                    )

                st.success("Resume analysis completed!")

            except Exception as e:

                st.error(f"Analysis failed: {e}")

    # Display saved analysis

    data = st.session_state.analysis

    if data:

        st.divider()

        st.markdown("## 📊 Analysis Dashboard")

        st.caption(f"Analyzed resume: {data['filename']}")

        col1, col2, col3, col4 = st.columns(4)

        col1.metric(
            "🎯 Match Score",
            f"{data['match_score']}%"
        )

        col2.metric(
            "✅ Matched Skills",
            len(data["matching_skills"])
        )

        col3.metric(
            "❌ Missing Skills",
            len(data["missing_skills"])
        )

        col4.metric(
            "💡 Extra Skills",
            len(data["extra_skills"])
        )

        st.caption(
            "Match score represents TF-IDF text similarity, "
            "not a hiring probability."
        )

        st.divider()

        st.markdown("### 🎯 Resume Match Score")

        render_match_gauge(data["match_score"])

        st.divider()

        st.markdown("## ✅ Matching Skills")

        render_skill_chips(
            data["matching_skills"],
            "matched"
        )

        st.markdown("## ❌ Missing Skills")

        render_skill_chips(
            data["missing_skills"],
            "missing"
        )

        st.markdown("## 💡 Additional Skills")

        render_skill_chips(
            data["extra_skills"],
            "additional"
        )

        with st.expander("📄 View Extracted Resume Text"):

            st.text(data["resume_text"])

    else:

        st.info(
            "Upload your resume and a job description "
            "to start your first analysis."
        )


# ==========================================
# SKILL ANALYTICS PAGE
# ==========================================

elif page == "📊 Skill Analytics":

    st.title("📊 Skill Analytics")

    data = st.session_state.analysis

    if data is None:

        st.warning(
            "Please analyze your resume from the Dashboard first."
        )

    else:

        st.markdown("### Skill Comparison")

        categories = [
            "Matched Skills",
            "Missing Skills",
            "Additional Skills"
        ]

        values = [
            len(data["matching_skills"]),
            len(data["missing_skills"]),
            len(data["extra_skills"])
        ]

        col1, col2 = st.columns(2)

        with col1:

            bar_chart = go.Figure(
                go.Bar(
                    x=categories,
                    y=values,
                    text=values,
                    textposition="auto",
                    marker_color=[
                        "#10B981",
                        "#EF4444",
                        "#3B82F6"
                    ]
                )
            )

            bar_chart.update_layout(
                paper_bgcolor="#0B1120",
                plot_bgcolor="#172338",
                font_color="#CBD5E1",
                yaxis_title="Number of Skills",
                height=350,
                yaxis=dict(
                    rangemode="tozero",
                    gridcolor="#334155"
                )
            )

            st.plotly_chart(
                bar_chart,
                use_container_width=True
            )

        with col2:

            total_job_skills = len(data["job_skills"])

            if total_job_skills > 0:

                pie_chart = go.Figure(
                    go.Pie(
                        labels=["Matched", "Missing"],
                        values=[
                            len(data["matching_skills"]),
                            len(data["missing_skills"])
                        ],
                        hole=0.65,
                        marker=dict(
                            colors=["#10B981", "#EF4444"]
                        ),
                        textinfo="label+value"
                    )
                )

                pie_chart.update_layout(
                    paper_bgcolor="#0B1120",
                    font_color="#CBD5E1",
                    height=350
                )

                st.plotly_chart(
                    pie_chart,
                    use_container_width=True
                )

            else:

                st.info("No predefined job skills identified.")

        st.divider()

        st.markdown("### Skill Details")

        st.write("**Matched Skills**")

        render_skill_chips(
            data["matching_skills"],
            "matched"
        )

        st.write("**Missing Skills**")

        render_skill_chips(
            data["missing_skills"],
            "missing"
        )

        st.write("**Additional Skills**")

        render_skill_chips(
            data["extra_skills"],
            "additional"
        )


# ==========================================
# IMPROVEMENT TIPS PAGE
# ==========================================

elif page == "🎯 Improvement Tips":

    st.title("🎯 Resume Improvement Tips")

    data = st.session_state.analysis

    if data is None:

        st.warning(
            "Analyze your resume from the Dashboard first."
        )

    else:

        missing_skills = data["missing_skills"]

        st.markdown("### Recommended Improvements")

        if missing_skills:

            st.write(
                "The following skills appear in the job description "
                "but were not detected in your resume."
            )

            for skill in missing_skills:

                st.markdown(
                    f"- **{html.escape(str(skill))}**"
                )

            st.info(
                "Only add a missing skill if you genuinely have "
                "that knowledge or experience."
            )

        else:

            st.success(
                "All predefined job-description skills "
                "were detected in your resume."
            )

        st.divider()

        st.markdown("### General Resume Tips")

        tips = [
            "Use clear and professional section headings.",
            "Highlight measurable achievements where accurate.",
            "Use relevant technical keywords from the job description.",
            "Keep your experience and project descriptions concise.",
            "Check spelling, grammar and formatting.",
            "Never add skills or achievements you cannot support."
        ]

        for tip in tips:

            st.markdown(f"- {tip}")


# ==========================================
# RESUME BUILDER PAGE
# ==========================================

elif page == "📝 Resume Builder":

    st.title("📝 Resume Builder")

    st.write(
        "Transform your existing resume into a clearer, "
        "more professional and ATS-friendly version."
    )

    data = st.session_state.analysis

    if data is None:

        st.warning(
            "First upload and analyze your existing resume "
            "from the Dashboard."
        )

    else:

        st.success(
            f"Resume available: {data['filename']}"
        )

        st.divider()

        st.markdown("### Choose Resume Template")

        template = st.selectbox(
            "Select a template",
            [
                "ATS Professional",
                "Modern Minimal"
            ],
            key="selected_template"
        )

        st.caption(
            "ATS Professional is designed for a simple, "
            "readable resume layout. Modern Minimal is "
            "intended for a cleaner visual style."
        )

        st.divider()

        if st.button(
            "✨ Improve My Resume",
            use_container_width=True
        ):

            with st.spinner("Improving your resume..."):

                improved_text = improve_resume(
                    data["resume_text"]
                )

                st.session_state.improved_resume = improved_text

            if improved_text:

                st.success(
                    "Resume formatting improved successfully!"
                )

            else:

                st.error(
                    "Could not generate an improved resume."
                )

        if st.session_state.improved_resume:

            st.divider()

            st.markdown("### Improved Resume Preview")

            st.text_area(
                "Preview",
                value=st.session_state.improved_resume,
                height=400,
                disabled=True
            )

            st.caption(
                f"Selected template: "
                f"{st.session_state.selected_template}"
            )

            st.info(
                "Your improved resume is ready. "
                "Go to Download Resume to export it as a PDF."
            )


# ==========================================
# DOWNLOAD RESUME PAGE
# ==========================================

elif page == "📥 Download Resume":

    st.title("📥 Download Your Resume")

    data = st.session_state.analysis

    if data is None:

        st.warning(
            "Please analyze your resume from Dashboard first."
        )

    elif not st.session_state.improved_resume:

        st.warning(
            "Please improve your resume in Resume Builder first."
        )

        st.info(
            "Go to Resume Builder, select a template "
            "and click Improve My Resume."
        )

    else:

        st.success("Your improved resume is ready!")

        st.markdown("### Resume Details")

        st.write(
            f"**Original File:** {data['filename']}"
        )

        st.write(
            f"**Selected Template:** "
            f"{st.session_state.selected_template}"
        )

        st.divider()

        st.markdown("### Resume Preview")

        st.text_area(
            "Improved Resume",
            value=st.session_state.improved_resume,
            height=350,
            disabled=True
        )

        st.divider()

        try:

            pdf_file = generate_resume_pdf(
                st.session_state.improved_resume,
                template=st.session_state.selected_template
            )
            st.download_button(
                label="📥 Download Improved Resume PDF",
                data=pdf_file,
                file_name="ResumeIQ_Improved_Resume.pdf",
                mime="application/pdf",
                use_container_width=True
            )

        except Exception as e:

            st.error(f"PDF generation failed: {e}")


# ==========================================
# FOOTER
# ==========================================

render_footer()
