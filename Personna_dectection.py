def detect_persona(query):

    query = query.lower()

    technical_keywords = [
        "api",
        "logs",
        "authentication",
        "configuration",
        "server",
        "error"
    ]

    frustrated_keywords = [
        "angry",
        "frustrated",
        "nothing works",
        "worst",
        "urgent"
    ]

    executive_keywords = [
        "business impact",
        "operations",
        "revenue",
        "timeline"
    ]

    if any(word in query for word in technical_keywords):
        return "Technical Expert"

    if any(word in query for word in frustrated_keywords):
        return "Frustrated User"

    if any(word in query for word in executive_keywords):
        return "Business Executive"

    return "General User"
