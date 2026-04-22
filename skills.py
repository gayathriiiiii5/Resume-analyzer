SKILLS_DB=[
     "python","machine learning","data analysis",
     "nlp","pandas","numpy","scikit-learn"
]
def extract_skills(text):
    text=text.lower()
    found=[skill for skill in SKILLS_DB if skill in text]
    return found