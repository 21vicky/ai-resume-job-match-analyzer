
import re


# Our predefined technical skill dictionary
SKILL_DICTIONARY = {

    "Python": ["python"],
    "Java": ["java"],
    "JavaScript": ["javascript"],
    "C++": ["c++"],
    "C#": ["c#"],

    "HTML": ["html"],
    "CSS": ["css"],
    "React.js": ["react.js", "reactjs"],
    "Node.js": ["node.js", "nodejs"],
    "Flask": ["flask"],

    "SQL": ["sql"],
    "MySQL": ["mysql"],
    "MongoDB": ["mongodb"],

    "Power BI": ["power bi"],
    "Tableau": ["tableau"],
    "Excel": ["excel"],

    "Machine Learning": ["machine learning"],
    "Deep Learning": ["deep learning"],
    "Natural Language Processing": ["natural language processing", "nlp"],
    "Artificial Intelligence": ["artificial intelligence"],
    "TensorFlow": ["tensorflow"],
    "PyTorch": ["pytorch"],
    "Scikit-learn": ["scikit-learn", "sklearn"],

    "Git": ["git"],
    "GitHub": ["github"],
    "Docker": ["docker"],
    "AWS": ["aws"],
    "Azure": ["azure"]
}


def extract_skills(text):

    extracted_skills = []

    # Check every skill in our dictionary
    for skill, keywords in SKILL_DICTIONARY.items():

        for keyword in keywords:

            # Match complete words, not partial words
            pattern = (
                r'(?<![A-Za-z0-9])'
                + re.escape(keyword)
                + r'(?![A-Za-z0-9])'
            )

            if re.search(pattern, text, re.IGNORECASE):

                extracted_skills.append(skill)

                # Avoid duplicate skills
                break

    return extracted_skills
