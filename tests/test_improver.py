
from resume_improver import improve_resume

sample_resume = """
john doe

summary

python developer with knowledge in python and sql.

skills

python, sql, power bi

experience

- worked on dashboards
- created reports

education

btech information technology
"""

improved = improve_resume(sample_resume)

print("========== IMPROVED RESUME ==========")
print(improved)
