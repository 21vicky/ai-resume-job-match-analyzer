
# AI Resume & Job Match Analyzer

An AI-powered application that analyzes PDF resumes
and compares candidate skills with job descriptions.

## Features

- PDF Resume Text Extraction
- NLP Text Preprocessing
- Technical Skill Extraction
- TF-IDF Vectorization
- Cosine Similarity Matching
- Matching Skills Identification
- Missing Skills Identification
- Resume Improvement Suggestions
- Interactive Streamlit Dashboard

## Tech Stack

- Python
- Streamlit
- PyPDF
- Pandas
- Scikit-learn
- NLTK
- Matplotlib

## Project Structure

```text
ai-resume-job-match-analyzer/
├── app.py
├── resume_parser.py
├── text_processor.py
├── skill_extractor.py
├── matcher.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation

Clone the repository:

```bash
git clone https://github.com/21vicky
```

Navigate into the project:

```bash
cd ai-resume-job-match-analyzer
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

## How It Works

1. Upload a PDF resume.
2. Enter a job description.
3. Extract resume text.
4. Identify technical skills.
5. Calculate text similarity using TF-IDF
   and Cosine Similarity.
6. Display matching and missing skills.

## Disclaimer

The matching score represents text similarity.
It is not a hiring probability or a guarantee
of job suitability.

## Author

Vignesh U
