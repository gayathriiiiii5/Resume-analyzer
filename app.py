import streamlit as st
from parser import extract_text
from utils import clean_text
from skills import extract_skills
from matcher import get_match_score

st.title("Automated Resume Analyzer")

uploaded_file=st.file_uploader("Upload Resume(PDF)", type="pdf")
job_desc=st.text_area("Paste Job Description")

if uploaded_file and job_desc:
    resume_text=extract_text(uploaded_file)

    resume_text=clean_text(resume_text)
    job_desc=clean_text(job_desc)

    score=get_match_score(resume_text,job_desc)
    skills=extract_skills(resume_text)

    st.subheader("Results")
    st.write("Match Score:",score,"%")
    st.write("Skills Found:",skills)
   