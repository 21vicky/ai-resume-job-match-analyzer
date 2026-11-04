
from io import BytesIO
import re

from xml.sax.saxutils import escape

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    HRFlowable
)


# ==========================================
# RESUME SECTION HEADINGS
# ==========================================

SECTION_HEADINGS = {
    "professional summary",
    "summary",
    "career objective",
    "objective",
    "technical skills",
    "skills",
    "work experience",
    "experience",
    "professional experience",
    "education",
    "projects",
    "academic projects",
    "certifications",
    "certificates",
    "achievements",
    "languages",
    "interests",
    "personal details"
}


# ==========================================
# PDF GENERATOR
# ==========================================

def generate_resume_pdf(
    resume_text,
    template="ATS Professional"
):

    if not resume_text or not resume_text.strip():
        raise ValueError("Resume text cannot be empty.")

    buffer = BytesIO()

    # Validate template
    if template not in [
        "ATS Professional",
        "Modern Minimal"
    ]:
        template = "ATS Professional"

    # ======================================
    # DOCUMENT SETTINGS
    # ======================================

    document = SimpleDocTemplate(
        buffer,
        pagesize=A4,
        rightMargin=18 * mm,
        leftMargin=18 * mm,
        topMargin=18 * mm,
        bottomMargin=18 * mm
    )

    styles = getSampleStyleSheet()

    # ======================================
    # TEMPLATE COLORS
    # ======================================

    if template == "ATS Professional":

        primary_color = colors.HexColor("#1E3A8A")
        text_color = colors.HexColor("#1F2937")
        heading_color = colors.HexColor("#1E3A8A")

        title_alignment = TA_LEFT

    else:

        primary_color = colors.HexColor("#0F766E")
        text_color = colors.HexColor("#334155")
        heading_color = colors.HexColor("#0F766E")

        title_alignment = TA_CENTER

    # ======================================
    # TEXT STYLES
    # ======================================

    title_style = ParagraphStyle(
        "ResumeTitle",
        parent=styles["Title"],
        fontName="Helvetica-Bold",
        fontSize=22,
        leading=27,
        textColor=primary_color,
        alignment=title_alignment,
        spaceAfter=8
    )

    body_style = ParagraphStyle(
        "ResumeBody",
        parent=styles["BodyText"],
        fontName="Helvetica",
        fontSize=9,
        leading=13,
        textColor=text_color,
        alignment=TA_LEFT,
        spaceAfter=5
    )

    section_style = ParagraphStyle(
        "ResumeSection",
        parent=styles["Heading2"],
        fontName="Helvetica-Bold",
        fontSize=11,
        leading=15,
        textColor=heading_color,
        spaceBefore=12,
        spaceAfter=5,
        keepWithNext=True
    )

    bullet_style = ParagraphStyle(
        "ResumeBullet",
        parent=body_style,
        leftIndent=12,
        firstLineIndent=-8,
        spaceAfter=4
    )

    contact_style = ParagraphStyle(
        "ResumeContact",
        parent=body_style,
        fontSize=8,
        leading=11,
        alignment=title_alignment,
        textColor=colors.HexColor("#64748B"),
        spaceAfter=10
    )

    # ======================================
    # BUILD RESUME CONTENT
    # ======================================

    story = []

    lines = [
        line.strip()
        for line in resume_text.splitlines()
    ]

    lines = [
        line for line in lines
        if line
    ]

    if not lines:
        raise ValueError("No readable resume content found.")

    # First line becomes the resume name/title
    name = escape(lines[0])

    story.append(
        Paragraph(name, title_style)
    )

    # Modern template gets a decorative divider
    if template == "Modern Minimal":

        story.append(
            HRFlowable(
                width="100%",
                thickness=2,
                color=primary_color,
                spaceBefore=3,
                spaceAfter=12
            )
        )

    # Remaining resume content
    for index, line in enumerate(lines[1:]):

        # Normalize whitespace
        line = re.sub(r"\s+", " ", line).strip()

        if not line:
            story.append(Spacer(1, 5))
            continue

        # Identify section headings
        heading_key = line.lower().strip(" :")

        if heading_key in SECTION_HEADINGS:

            story.append(
                Paragraph(
                    escape(line.strip(" :")).upper(),
                    section_style
                )
            )

            # Modern template section divider
            if template == "Modern Minimal":

                story.append(
                    HRFlowable(
                        width="100%",
                        thickness=0.7,
                        color=colors.HexColor("#CBD5E1"),
                        spaceBefore=0,
                        spaceAfter=6
                    )
                )

            continue

        # Identify bullet points
        if re.match(r"^[-*•]\s*", line):

            clean_bullet = re.sub(
                r"^[-*•]\s*",
                "",
                line
            )

            story.append(
                Paragraph(
                    "&#8226; " + escape(clean_bullet),
                    bullet_style
                )
            )

        else:

            # First content line after name can be contact details
            if index == 0:

                story.append(
                    Paragraph(
                        escape(line),
                        contact_style
                    )
                )

            else:

                story.append(
                    Paragraph(
                        escape(line),
                        body_style
                    )
                )

    # ======================================
    # PAGE NUMBER FOOTER
    # ======================================

    def add_page_number(canvas, doc):

        canvas.saveState()

        canvas.setFont("Helvetica", 8)
        canvas.setFillColor(
            colors.HexColor("#94A3B8")
        )

        canvas.drawRightString(
            A4[0] - 18 * mm,
            10 * mm,
            f"Page {doc.page}"
        )

        canvas.restoreState()

    # ======================================
    # GENERATE PDF
    # ======================================

    document.build(
        story,
        onFirstPage=add_page_number,
        onLaterPages=add_page_number
    )

    buffer.seek(0)

    return buffer
