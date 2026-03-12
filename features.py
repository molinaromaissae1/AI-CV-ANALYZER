import re


def extract_experience(text):

    years = re.findall(r'20\d{2}', text)

    years = [int(y) for y in years]

    if len(years) < 2:
        return 0

    return max(years) - min(years)



def extract_education(text):

    text = text.lower()

    if "master" in text:
        return "Bac+5"

    if "licence" in text:
        return "Bac+3"

    if "baccalauréat" in text:
        return "Bac"

    return "Unknown"



def extract_languages(text):

    section = re.search(
        r'langues(.*?)(compétences|skills|expérience|formation)',
        text.lower(),
        re.DOTALL
    )

    if section:

        content = section.group(1)

        languages = re.findall(r'[a-zéèêàç]+', content)

        return languages

    return []



def extract_skills(text):

    section = re.search(
        r'(compétences|skills)(.*?)(expérience|formation|langues)',
        text.lower(),
        re.DOTALL
    )

    if section:

        content = section.group(2)

        skills = re.findall(r'[a-zéèêàç]+', content)

        return skills

    return []
