def score_cv(text):

    text = text.lower()

    # experience
    experience = text.count("expérience") + text.count("stage") + text.count("emploi")

    # education
    education = (
        text.count("formation")
        + text.count("université")
        + text.count("licence")
        + text.count("master")
        + text.count("baccalauréat")
    )

    # skills
    skills = (
        text.count("compétence")
        + text.count("gestion")
        + text.count("communication")
        + text.count("organisation")
        + text.count("excel")
        + text.count("word")
    )

    # languages
    languages = (
        text.count("français")
        + text.count("anglais")
        + text.count("arabe")
        + text.count("langues")
    )

    return experience, education, skills, languages
