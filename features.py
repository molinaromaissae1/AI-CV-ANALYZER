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
    lines = text.lower().split("\n")
    results = []

    for line in lines:
        # Arabic
        if "arabe" in line or "arabic" in line:
            if "maternelle" in line:
                level = "C2"
            elif "c1" in line:
                level = "C1"
            elif "a2" in line:
                level = "A2"
            else:
                level = "Unknown"
            results.append({"name": "Arabic", "level": level})

        # French
        if "français" in line or "french" in line:
            if "c1" in line:
                level = "C1"
            elif "c2" in line:
                level = "C2"
            else:
                level = "Unknown"
            results.append({"name": "French", "level": level})

        # English
        if "anglais" in line or "english" in line:
            if "c1" in line:
                level = "C1"
            elif "c2" in line:
                level = "C2"
            else:
                level = "Unknown"
            results.append({"name": "English", "level": level})

        # Spanish
        if "espagnole" in line or "spanish" in line:
            if "a2" in line:
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
