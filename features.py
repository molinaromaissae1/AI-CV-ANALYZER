import re

# =========================
# SKILLS
# =========================
def extract_skills(text):
    skills_list = [
        "python", "excel", "communication", "management",
        "recruitment", "hr", "powerpoint", "word",
        "organisation", "gestion", "teamwork"
    ]

    text = text.lower()
    found_skills = []

    for skill in skills_list:
        if skill in text:
            found_skills.append(skill)

    return list(set(found_skills))


# =========================
# LANGUAGES
# =========================
def extract_languages(text):
    text = text.lower()

    languages_list = {
        "English": ["english", "anglais"],
        "French": ["french", "français"],
        "Arabic": ["arabic", "arabe"],
        "Spanish": ["spanish", "espagnol", "espagnole"]
    }

    levels = ["a1", "a2", "b1", "b2", "c1", "c2"]

    results = []

    for lang, keywords in languages_list.items():
        for word in keywords:
            if word in text:

                level = "Unknown"

                # 🧠 ناخدو window صغير حول الكلمة
                index = text.find(word)
                context = text[max(0, index-30): index+30]

                # 🔍 check levels
                for lvl in levels:
                    if lvl in context:
                        level = lvl.upper()

                # 🔥 maternel غير لهد اللغة
                if "maternel" in context or "native" in context:
                    level = "C2"

                results.append({
                    "name": lang,
                    "level": level
                })

                break

    return results

   

          


# =========================
# COMPANIES
# =========================
def extract_companies(text):
    companies = [
        "safran", "deloitte", "capgemini", "google",
        "amazon", "microsoft", "apple"
    ]

    text = text.lower()
    found = []

    for c in companies:
        if c in text:
            found.append(c)

    return found


# =========================
# SECTOR
# =========================
def extract_sector(text):
    text = text.lower()

    if "hr" in text or "ressources humaines" in text:
        return "HR"
    elif "finance" in text:
        return "Finance"
    elif "engineering" in text:
        return "Engineering"
    else:
        return "Other"
