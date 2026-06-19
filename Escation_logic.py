def should_escalate(score, query):

    sensitive = [
        "billing",
        "legal",
        "account suspended"
    ]

    if score < 0.3:
        return True

    if any(word in query.lower() for word in sensitive):
        return True

    return False
