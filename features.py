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

def extract_languages(text: str) -> List[Dict[str, str]]:
    text = text.lower().strip()
    
    # قائمة اللغات مع الكلمات المفتاحية (موسعة)
    languages = {
        "English": ["english", "anglais", "angl", "gb", "uk", "🇬🇧", "🇺🇸"],
        "French": ["french", "français", "francais", "fr", "🇫🇷"],
        "Arabic": ["arabic", "arabe", "عربي", "ar", "🇸🇦", "🇲🇦"],
        "Spanish": ["spanish", "espagnol", "espagnole", "español", "es", "🇪🇸"],
        "German": ["german", "deutsch", "allemand", "de", "🇩🇪"],
        "Italian": ["italian", "italien", "italiano", "it", "🇮🇹"],
        "Dutch": ["dutch", "néerlandais", "nederlands", "nl", "🇳🇱"]
    }
    
    # مستويات CEFR مع regex للكشف الدقيق
    cefr_levels = {
        r'\bc2\b|\bmatern(e|el)|\bnative|\bfluent\b|\bمستوى متقدم جداً?\b': "C2",
        r'\bc1\b|\badvanced\b|\bمتقدم\b': "C1",
        r'\bc2?\b|\bupper intermediate\b|\bمتوسط عليا?\b': "B2",
        r'\bb1\b|\bintermediate\b|\bمتوسط\b': "B1",
        r'\ba2?\b|\belementary\b|\bbeginner\b|\bمبتدئ\b': "A2",
        r'\ba1\b|\bbasic\b|\bأساسيات?\b': "A1"
    }
    
    results = []
    
    # تقسيم النص للكلمات والسطور
    words = re.findall(r'\b\w+\b', text)
    lines = text.split('\n')
    
    for lang_name, keywords in languages.items():
        found = False
        
        # البحث في الكلمات
        for keyword in keywords:
            if keyword.lower() in words:
                found = True
                break
        
        if found:
            # البحث عن المستوى في السطر اللي فيه اللغة
            level = "Unknown"
            
            for line in lines:
                line_lower = line.lower()
                
                # إذا كان السطر يحتوي على اسم اللغة
                lang_found = any(keyword in line_lower for keyword in keywords)
                
                if lang_found:
                    # فحص جميع مستويات CEFR
                    for pattern, lvl in cefr_levels.items():
                        if re.search(pattern, line_lower):
                            level = lvl
                            break
                    break
            
            # إذا ما لقاش مستوى في نفس السطر، نبحث في النص كامل
            if level == "Unknown":
                for pattern, lvl in cefr_levels.items():
                    if re.search(pattern, text):
                        level = lvl
                        break
            
            results.append({
                "name": lang_name,
                "level": level,
                "confidence": "high" if level != "Unknown" else "low"
            })
    
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
