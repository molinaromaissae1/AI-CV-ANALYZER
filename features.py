import re

def extract_skills(text):
    skills_list = ["python", "excel", "communication", "management"]
    text = text.lower()
    found = []
    for s in skills_list:
        if s in text:
            found.append(s)
    return found


import re
from typing import List, Dict, Any

import re

def extract_languages(text):
    text = text.lower()
    results = []

    # pattern بحال: Français (C1)
    pattern = r"(arabic|arabe|french|français|english|anglais|spanish|espagnole)\s*\((.*?)\)"

    matches = re.findall(pattern, text)

    for lang, level in matches:
        level = level.upper()

        if "arab" in lang:
            name = "Arabic"
            if "maternelle" in level:
                level = "C2"

        elif "franç" in lang or "french" in lang:
            name = "French"

        elif "angl" in lang or "english" in lang:
            name = "English"

        elif "espagn" in lang or "spanish" in lang:
            name = "Spanish"

        else:
            continue

        results.append({"name": name, "level": level})

    return results
   
        
    


def extract_companies(text):
    companies = ["safran", "airbus", "deloitte"]
    text = text.lower()
    found = []
    for c in companies:
        if c in text:
            found.append(c.capitalize())
    return found


def extract_experience(text):
    matches = re.findall(r'(\d+)\s*(year|years|month|months)', text.lower())
    total = 0
    for num, unit in matches:
        if "year" in unit:
            total += int(num) * 12
        else:
            total += int(num)
    return total
