
from skill_extractor import extract_skills


resume_text = """
I am a Python Developer with experience
in SQL, React.js, JavaScript and Power BI.

I also have knowledge of Machine Learning,
Git, GitHub and Flask.
"""

job_description = """
We are looking for a Python Developer.

Required skills:
Python, SQL, React.js, Flask,
Docker and AWS.
"""


# Extract resume skills
resume_skills = extract_skills(resume_text)

# Extract job description skills
job_skills = extract_skills(job_description)


print("===== RESUME SKILLS =====")
print(resume_skills)

print("\n===== JOB REQUIRED SKILLS =====")
print(job_skills)

