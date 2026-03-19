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

    # Arabic
    if "arabe" in text or "arabic" in text:
        if "maternelle" in text:
            level = "C2"
        else:
            level = "Unknown"
        results.append({"name": "Arabic", "level": level})

    # French
    if "français" in text or "french" in text:
        if "c1" in text:
            level = "C1"
        else:
            level = "Unknown"
        results.append({"name": "French", "level": level})

    # English
    if "anglais" in text or "english" in text:
        if "c1" in text:
            level = "C1"
        else:
            level = "Unknown"
        results.append({"name": "English", "level": level})

    # Spanish
    if "espagnole" in text or "spanish" in text:
        if "a2" in text:
            level = "A2"
        else:
            level = "Unknown"
        results.append({"name": "Spanish", "level": level})

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
