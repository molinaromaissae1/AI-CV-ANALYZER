import re

# ---------------- EXPERIENCE ----------------

def extract_experience(text):

    text = text.lower()

    experience = 0

    if "stage" in text or "stagiaire" in text:
        experience += 1

    if "assistant" in text or "chargé" in text or "responsable" in text:
        experience += 1

    return experience


# ---------------- EDUCATION ----------------

def extract_education(text):

    text = text.lower()

    if "master" in text or "bac+5" in text:
        return "Bac+5"

    if "licence" in text or "bac+3" in text or "3e année" in text:
        return "Bac+3"

    if "bts" in text or "dut" in text or "bac+2" in text:
        return "Bac+2"

    if "bac" in text or "baccalauréat" in text:
        return "Bac"

    return "Unknown"


# ---------------- LANGUAGES ----------------

def extract_languages(text):

    text = text.lower()

    languages_list = [
        "français",
        "francais",
        "anglais",
        "english",
        "arabe",
        "arabic"
    ]

    found = []

    for lang in languages_list:
        if lang in text:
            found.append(lang)

    return found


# ---------------- SKILLS RH ----------------

def extract_skills(text):

    text = text.lower()

    skills_list = [

        # RH
        "ressources humaines",
        "recrutement",
        "gestion du personnel",
        "administration du personnel",

        # administratif
        "gestion administrative",
        "gestion des dossiers",
        "saisie de données",

        # soft skills
        "communication",
        "travail d'équipe",
        "organisation",

        # bureautique
        "excel",
        "word",
        "powerpoint",
        "outlook"
    ]

    found = []

    for skill in skills_list:
        if skill in text:
            found.append(skill)

    return found


# ---------------- SECTOR ----------------

def extract_sector(text):

    text = text.lower()

    rh_keywords = [
        "ressources humaines",
        "rh",
        "recrutement",
        "gestion du personnel"
    ]

    for word in rh_keywords:
        if word in text:
            return "Ressources Humaines"

    return "Other"


# ---------------- COMPANIES ----------------

def extract_companies(text):

    companies = re.findall(r'\b(?:sarl|sa|sas|entreprise|groupe)\b', text.lower())

    return len(companies)
