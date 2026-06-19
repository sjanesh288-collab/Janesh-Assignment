def generate_handoff(persona, issue, docs):

    return {
        "persona": persona,
        "issue": issue,
        "documents_used": docs,
        "recommendation":
        "Human support review required."
    }
