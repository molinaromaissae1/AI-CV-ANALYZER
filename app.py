import streamlit as st
from reader import extract_text_from_pdf
from preprocess import preprocess_text

from features import (
    extract_experience,
    extract_education,
    extract_skills,
    extract_languages,
    extract_sector,
    extract_companies
)

from ats_scoring import calculate_ats_score


st.set_page_config(
    page_title="AI CV Analyzer",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI CV Analyzer for HR")
st.write("Upload a CV and the system will automatically analyze it.")


uploaded_file = st.file_uploader(
    "📄 Upload CV (PDF format)",
    type=["pdf"]
)


if uploaded_file is not None:

    text = extract_text_from_pdf(uploaded_file)

    clean_text = preprocess_text(text)


    experience = extract_experience(clean_text)
    education = extract_education(clean_text)
    skills = extract_skills(clean_text)
    languages = extract_languages(clean_text)
    sector = extract_sector(clean_text)
    companies = extract_companies(clean_text)

    score = calculate_ats_score(
        experience,
        skills,
        languages,
        education
    )


    st.subheader("📊 Extracted Information")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Years of Experience", experience)
        st.metric("Education Level", education)

    with col2:
        st.metric("Sector", sector)
        st.metric("Companies", companies)


    st.subheader("💼 Skills")

    for skill in skills:
        st.success(skill)


    st.subheader("🌍 Languages")

    for lang in languages:
        st.info(lang)


    st.subheader("📈 ATS Score")

    st.progress(score)

    st.write("Score:", score)

    if score > 60:
        st.success("Candidate Selected")
    else:
        st.warning("Candidate Not Selected")
