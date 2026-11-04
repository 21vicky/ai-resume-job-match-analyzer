
from matcher import calculate_similarity


resume_text = """
Python developer with experience in SQL,
React.js, JavaScript, Power BI and
Machine Learning.
I have worked on web applications
and data analytics projects.
"""

job_description = """
We are hiring a Python developer
with knowledge of SQL, React.js
and Machine Learning.

Experience in web development
and data analytics is preferred.
"""


score = calculate_similarity(
    resume_text,
    job_description
)


print("===== AI RESUME MATCH ANALYZER =====")

print(f"\nResume Match Score: {score}%")

if score >= 75:
    print("Strong Text Similarity")

elif score >= 50:
    print("Moderate Text Similarity")

else:
    print("Low Text Similarity")
