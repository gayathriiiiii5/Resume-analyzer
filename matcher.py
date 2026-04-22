from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def get_match_score(resume,job_desc):
    text=[resume,job_desc]
    cv= CountVectorizer().fit_transform(text)
    score=cosine_similarity(cv)[0][1]
    return round(score*100,2)