import streamlit as st
from reader import read_cv

from features import (
    extract_experience,
    extract_education,
    extract_skills,
    extract_languages,
    extract_sector,
    extract_companies
)

st.title("AI CV Screening Agent")

uploaded_file = st.file_uploader("Upload CV", type=["pdf","docx"])

if uploaded_file is not None:

    text = read_cv(uploaded_file)

    st.subheader("Text detected in CV")
    st.write(text)

    st.subheader("Extracted Information")

    experience = extract_experience(text)
    education = extract_education(text)
    skills = extract_skills(text)
    languages = extract_languages(text)
    sector = extract_sector(text)
    companies = extract_companies(text)

    st.write("Years of experience:", experience)
    st.write("Education level:", education)
    st.write("Skills:", skills)
    st.write("Languages:", languages)
    st.write("Sector:", sector)
    st.write("Number of companies:", companies)

    score = experience*2 + len(skills)*3 + len(languages)

    st.subheader("ATS Score")
    st.write(score)

    if score > 10:
        st.success("Candidate Selected")
    else:
        st.error("Candidate Rejected")
