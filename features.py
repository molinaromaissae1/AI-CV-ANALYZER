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

def extract_languages(text):
    text = text.lower()

    results = []

    # Arabic
    if "arabe" in text or "arabic" in text:
        if "arabe (maternelle)" in text or "arabic native" in text:
            results.append({"name": "Arabic", "level": "C2"})
        else:
            results.append({"name": "Arabic", "level": "Unknown"})

    # French
    if "français" in text or "french" in text:
        if "c1" in text:
            results.append({"name": "French", "level": "C1"})
        else:
            results.append({"name": "French", "level": "Unknown"})

    # English
    if "anglais" in text or "english" in text:
        if "c1" in text:
            results.append({"name": "English", "level": "C1"})
        else:
            results.append({"name": "English", "level": "Unknown"})

    # Spanish
    if "espagnole" in text or "spanish" in text:
        if "a2" in text:
            results.append({"name": "Spanish", "level": "A2"})
        else:
            results.append({"name": "Spanish", "level": "Unknown"})

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
