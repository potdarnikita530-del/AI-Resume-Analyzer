SKILLS = [
    "python",
    "java",
    "c++",
    "javascript",
    "html",
    "css",
    "django",
    "flask",
    "sql",
    "mysql",
    "mongodb",
    "machine learning",
    "deep learning",
    "artificial intelligence",
    "data science",
    "pandas",
    "numpy",
    "scikit-learn",
    "git",
    "github",
    "aws"
]


def find_skills(text):

    text = text.lower()

    found_skills = []

    for skill in SKILLS:

        if skill in text:
            found_skills.append(skill)

    return found_skills
def calculate_match(resume_skills, job_description):

    job_skills = find_skills(job_description)

    if len(job_skills) == 0:
        return 0, [], []

    matched_skills = []

    for skill in job_skills:
        if skill in resume_skills:
            matched_skills.append(skill)

    missing_skills = []

    for skill in job_skills:
        if skill not in resume_skills:
            missing_skills.append(skill)

    score = int((len(matched_skills) / len(job_skills)) * 100)

    return score, matched_skills, missing_skills