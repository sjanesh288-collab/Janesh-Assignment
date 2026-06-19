import google.generativeai as genai

def generate_response(persona, context, question):

    prompt = f"""
    Persona: {persona}

    Context:
    {context}

    User Question:
    {question}

    Generate answer only from context.

    Tone Rules:

    Technical Expert:
    Detailed explanation

    Frustrated User:
    Empathetic and simple

    Business Executive:
    Concise and impact focused
    """

    model = genai.GenerativeModel("gemini-1.5-flash")

    response = model.generate_content(prompt)

    return response.text
