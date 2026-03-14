import re
from datetime import datetime

# -----------------------------
# EDUCATION - محسن
# -----------------------------
def extract_education(text):
    text = text.lower()
    
    # أولويات الدراسة حسب الطول
    if any(word in text for word in ["master", "bac+5", "ingenieur", "engineer", "mastère"]):
        return "Bac+5"
    
    if any(word in text for word in [
        "licence", "bachelor", "bac+3", "3ème année", "3eme annee", 
        "troisième année", "3rd year", "l3"
    ]):
        return "Bac+3"
    
    if any(word in text for word in ["bts", "dut", "bac+2", "deug"]):
        return "Bac+2"
    
    if any(word in text for word in ["bac", "baccalauréat"]):
        return "Bac"
    
    return "Unknown"

# -----------------------------
# EXPERIENCE - محسن بزاف! 🔥
# -----------------------------
months_map = {
    "janvier":1,"février":2,"mars":3,"avril":4,"mai":5,"juin":6,
    "juillet":7,"août":8,"septembre":9,"octobre":10,"novembre":11,"décembre":12,
    "january":1,"february":2,"march":3,"april":4,"may":5,"june":6,
    "july":7,"august":8,"september":9,"october":10,"november":11,"december":12,
    "jan":1,"feb":2,"mar":3,"apr":4,"may":5,"jun":6,
    "jul":7,"aug":8,"sep":9,"oct":10,"nov":11,"dec":12
}

def extract_experience_months(text):
    text = text.lower()
    total_months = 0
    
    # 1. البحث على التواريخ الكاملة (شهر سنة - شهر سنة)
    date_pattern = r"(?:du\s+|de\s+|from\s+|since\s+)?([a-zàâäéèêëîïôöùûüç]+)\s+(\d{4})\s*(?:au?\s+|to\s+|until\s+|-|–)\s*([a-zàâäéèêëîïôöùûüç]+)\s+(\d{4})"
    
    matches = re.findall(date_pattern, text)
    
    for match in matches:
        try:
            start_month_name, start_year, end_month_name, end_year = match
            start_month = months_map.get(start_month_name, 1)
            end_month = months_map.get(end_month_name, 12)
            
            months = (int(end_year) - int(start_year)) * 12 + (end_month - start_month) + 1
            if months > 0:
                total_months += months
        except:
            continue
    
    # 2. السطاج اللي ماعندهوش تاريخ محدد (افتراضي 3 أشهر)
    if total_months == 0 and any(word in text for word in ["stage", "internship", "stagiaire"]):
        total_months = 3
    
    # 3. حاليا (من تاريخ البداية لليوم)
    current_pattern = r"(?:du\s+|de\s+|from\s+|since\s+)([a-zàâäéèêëîïôöùûüç]+)\s+(\d{4})\s*(?:aujourd'?hui|actuellement|الى\s+الآن|الى\s+حد\s+الآن|الآن)"
    current_matches = re.findall(current_pattern, text)
    
    for match in current_matches:
        try:
            start_month_name, start_year = match
            start_month = months_map.get(start_month_name, 1)
            
            # حساب المدة من تاريخ البداية لليوم
            start_date = datetime(int(start_year), start_month, 1)
            today = datetime.now()
            months_current = (today.year - start_date.year) * 12 + (today.month - start_date.month)
            
            if months_current > 0:
                total_months += months_current
        except:
            continue
    
    return max(0, total_months)

def extract_experience(text):
    months = extract_experience_months(text)
    
    if months >= 12:
        years = months // 12
        remaining_months = months % 12
        if remaining_months == 0:
            return f"{years} ans"
        else:
            return f"{years} ans et {remaining_months} mois"
    else:
        return f"{months} mois"

# -----------------------------
# TEST الكود
# -----------------------------
if __name__ == "__main__":
    # مثال CV
    cv_text = """
    Formation: Licence professionnelle Bac+3
    Expérience: Stage chez IBM du Janvier 2023 à Juin 2023
    Stage actuel depuis Septembre 2024 actuellement
    """
    
    print("🎓 Formation:", extract_education(cv_text))
    print("💼 Expérience:", extract_experience(cv_text))
