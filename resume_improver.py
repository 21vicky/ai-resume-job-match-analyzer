
import re


# ==========================================
# RESUME IMPROVER - RULE BASED
# ==========================================

SECTION_HEADINGS = {
    "professional summary": "PROFESSIONAL SUMMARY",
    "summary": "PROFESSIONAL SUMMARY",
    "career objective": "CAREER OBJECTIVE",
    "objective": "CAREER OBJECTIVE",
    "technical skills": "TECHNICAL SKILLS",
    "skills": "TECHNICAL SKILLS",
    "work experience": "WORK EXPERIENCE",
    "experience": "WORK EXPERIENCE",
    "professional experience": "WORK EXPERIENCE",
    "education": "EDUCATION",
    "projects": "PROJECTS",
    "academic projects": "PROJECTS",
    "certifications": "CERTIFICATIONS",
    "certificates": "CERTIFICATIONS",
    "achievements": "ACHIEVEMENTS"
}


def clean_line(line):

    line = line.strip()

    # Remove repeated spaces
    line = re.sub(r"\s+", " ", line)

    # Fix common spacing around punctuation
    line = re.sub(r"\s+([,.])", r"\1", line)

    return line


def improve_resume(resume_text):

    if not resume_text or not resume_text.strip():
        return ""

    improved_lines = []

    for line in resume_text.splitlines():

        line = clean_line(line)

        if not line:
            improved_lines.append("")
            continue

        heading_key = line.lower().strip(" :")

        # Standardize recognized section headings
        if heading_key in SECTION_HEADINGS:

            improved_lines.append("")
            improved_lines.append(
                SECTION_HEADINGS[heading_key]
            )
            improved_lines.append("")
            continue

        # Improve bullet formatting
        if line.startswith(("-", "*", "•")):

            line = re.sub(
                r"^[-*•]\s*",
                "• ",
                line
            )

        improved_lines.append(line)

    # Remove excessive blank lines
    result = "\n".join(improved_lines)

    result = re.sub(r"\n{3,}", "\n\n", result)

    return result.strip()
