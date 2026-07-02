def plan(question: str) -> dict:
    q = question.lower()

    if any(term in q for term in ["coin", "dice", "probability", "chance", "odds"]):
        topic = "Probability"
        difficulty = "Introductory"
    elif any(term in q for term in ["python", "pandas", "code", "function", "dataframe"]):
        topic = "Computer Science"
        difficulty = "Intermediate"
    elif any(term in q for term in ["x^2", "quadratic", "factor", "solve"]):
        topic = "Algebra"
        difficulty = "Introductory"
    else:
        topic = "General Math"
        difficulty = "Introductory"

    return {
        "topic": topic,
        "difficulty": difficulty,
        "strategy": "Explain the concept, give a Socratic hint, verify correctness, and avoid answer-dumping.",
    }
