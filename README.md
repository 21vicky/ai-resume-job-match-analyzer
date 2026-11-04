# 💼 ResumeIQ – AI Resume & Job Match Analyzer

An intelligent resume analysis application built with Python and Streamlit. ResumeIQ extracts information from PDF resumes, identifies technical skills, compares resumes against job descriptions, and provides actionable improvement suggestions.

## 🚀 Features

- 📄 PDF Resume Text Extraction
- 🧹 NLP Text Preprocessing
- 🛠️ Technical Skill Extraction
- 📊 TF-IDF Vectorization
- 🎯 Cosine Similarity Matching
- ✅ Matching Skills Identification
- ❌ Missing Skills Identification
- 💡 Resume Improvement Suggestions
- 📝 Resume Improvement and Formatting
- 📑 Resume Builder with Two Templates:
  - ATS Professional
  - Modern Minimal
- 📥 Download Generated Resume as PDF
- 📈 Interactive Streamlit Dashboard and Skill Analytics

## 🛠️ Tech Stack

- Python
- Streamlit
- PyPDF
- Pandas
- Scikit-learn
- NLTK
- Plotly
- Matplotlib
- ReportLab

## 📁 Project Structure

```text
ai-resume-job-match-analyzer/
│
├── app.py
├── resume_parser.py
├── text_processor.py
├── skill_extractor.py
├── matcher.py
├── resume_generator.py
├── resume_improver.py
│
├── tests/
│   ├── test_parser.py
│   ├── test_processor.py
│   ├── test_skills.py
│   ├── test_matcher.py
│   └── test_improver.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/21vicky/ai-resume-job-match-analyzer.git
```

### 2. Navigate into the project

```bash
cd ai-resume-job-match-analyzer
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the environment (Windows)

```bash
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the application

```bash
streamlit run app.py
```

## 🔍 How It Works

1. Upload a PDF resume.
2. Enter a job description.
3. Extract resume text from the PDF.
4. Preprocess the extracted text.
5. Identify technical skills in the resume and job description.
6. Calculate text similarity using TF-IDF and Cosine Similarity.
7. Display matching skills and missing skills.
8. Explore improvement suggestions and generate a formatted resume PDF.

## ⚠️ Disclaimer

The matching score represents textual similarity between the resume and job description. It is not a hiring probability, a measure of actual candidate capability, or a guarantee of job suitability.

Resume improvement suggestions are rule-based and should be reviewed before using the generated resume.

## 👨‍💻 Author

**Vignesh U**

GitHub: [@21vicky](https://github.com/21vicky)

---

⭐ If you find this project useful, consider giving it a star!