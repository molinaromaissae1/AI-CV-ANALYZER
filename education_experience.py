import re
from datetime import datetime

def extract_education(text):
    text = text.lower()

    if "phd" in text or "doctorat" in text:
        return "Bac+8"

    if "master" in text or "bac+5" in text or "5ème année" in text or "5eme annee" in text:
        return "Bac+5"

    if "bac+4" in text or "4ème année" in text or "4eme annee" in text:
        return "Bac+4"

    if (
        "bac+3" in text
        or "licence" in text
        or "3ème année" in text
        or "3eme annee" in text
        or "3eme année" in text
        or "3ème annee" in text
        or "3e année" in text
        or "3e annee" in text
    ):
        return "Bac+3"

    if "bac+2" in text or "bts" in text or "dut" in text:
        return "Bac+2"

    if "baccalauréat" in text or "baccalaureat" in text or re.search(r"\bbac\b", text):
        return "Bac"

    return "Unknown"


def extract_experience_months(text):
    text = text.lower()

    months_map = {
        "janvier": 1,
        "février": 2,
        "fevrier": 2,
        "mars": 3,
        "avril": 4,
        "mai": 5,
        "juin": 6,
        "juillet": 7,
        "août": 8,
        "aout": 8,
        "septembre": 9,
        "octobre": 10,
        "novembre": 11,
        "décembre": 12,
        "decembre": 12,
    }

    pattern = r"(janvier|février|fevrier|mars|avril|mai|juin|juillet|août|aout|septembre|octobre|novembre|décembre|decembre)\s+(\d{4})"

    matches = re.findall(pattern, text)

    if len(matches) >= 2:
        start_month_name, start_year = matches[0]
        end_month_name, end_year = matches[1]

        start_date = datetime(int(start_year), months_map[start_month_name], 1)
        end_date = datetime(int(end_year), months_map[end_month_name], 1)

        diff = (end_date.year - start_date.year) * 12 + (end_date.month - start_date.month)

        if diff < 0:
            return 0

        return diff + 1

    return 0


def extract_experience(text):
    months = extract_experience_months(text)

    if months == 1:
        return "1 month"

    return f"{months} months"
