import re

months_map = {
    "janvier":1,"février":2,"fevrier":2,"mars":3,"avril":4,"mai":5,
    "juin":6,"juillet":7,"août":8,"aout":8,"septembre":9,
    "octobre":10,"novembre":11,"décembre":12,"decembre":12,
    "january":1,"february":2,"march":3,"april":4,"may":5,"june":6,
    "july":7,"august":8,"september":9,"october":10,"november":11,"december":12
}

def extract_experience_months(text):

    text = text.lower()

    pattern = r"(janvier|février|fevrier|mars|avril|mai|juin|juillet|août|aout|septembre|octobre|novembre|décembre|decembre|january|february|march|april|may|june|july|august|september|october|november|december)\s*(\d{4}).*?(janvier|février|fevrier|mars|avril|mai|juin|juillet|août|aout|septembre|octobre|novembre|décembre|decembre|january|february|march|april|may|june|july|august|september|october|november|december)\s*(\d{4})"

    matches = re.findall(pattern, text)

    total_months = 0

    for match in matches:

        start_month = months_map[match[0]]
        start_year = int(match[1])

        end_month = months_map[match[2]]
        end_year = int(match[3])

        months = (end_year - start_year) * 12 + (end_month - start_month)

        if months > 0:
            total_months += months

    return total_months


def extract_experience(text):

    months = extract_experience_months(text)

    return str(months) + " months"
