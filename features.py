import re

# -------------------------
# SKILLS
# -------------------------
def extract_skills(text):
    skills_list = [
        "python", "excel", "communication", "management",
        "recruitment", "hr", "powerpoint", "word"
    ]

    text = text.lower()
    found_skills = []

    for skill in skills_list:
        if skill in text:
            found_skills.append(skill)

    return found_skills


# -------------------------
# LANGUAGES + LEVEL
# -------------------------
-def extract_languages(text):
    text = text.lower()

    patterns = {
        "english": r"(english|anglais)\s*[:\-]?\s*(a1|a2|b1|b2|c1|c2)?",
        "french": r"(français|french)\s*[:\-]?\s*(a1|a2|b1|b2|c1|c2)?",
        "arabic": r"(arabe|arabic)\s*[:\-]?\s*(a1|a2|b1|b2|c1|c2)?"
    }

    level_mapping = {
        "a1": "A1",
        "a2": "A2",
        "b1": "B1",
        "b2": "B2",
        "c1": "C1",
        "c2": "C2"
    }

    languages = []

    for lang, pattern in patterns.items():
        matches = re.findall(pattern, text)

        for match in matches:
            level = match[1]

            if "maternel" in match[0] or "native" in match[0]:
                level = "C2"

            elif level in level_mapping:
                level = level_mapping[level]

            else:
                level = "Unknown"

            languages.append({
                "name": lang.capitalize(),
                "level": level
            })

    return languages

    


# -------------------------
# COMPANIES
# -------------------------
def extract_companies(text):
    words = text.split()
    companies = []

    for word in words:
        if word.istitle():
            companies.append(word)

    return list(set(companies))


# -------------------------
# SECTOR
# -------------------------
def extract_sector(text):
    text = text.lower()

    if "finance" in text:
        return "Finance"
    elif "hr" in text or "ressources humaines" in text:
        return "HR"
    elif "engineering" in text or "industrial" in text:
        return "Engineering"

    return "Unknown"
