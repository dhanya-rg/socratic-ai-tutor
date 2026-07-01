def plan(question: str):
    q = question.lower()

    if "probability" in q or "coin" in q or "dice" in q:
        topic = "probability"
        difficulty = "introductory"
    elif "python" in q or "pandas" in q or "code" in q:
        topic = "computer science"
        difficulty = "intermediate"
    elif "x^2" in q or "quadratic" in q or "solve" in q:
        topic = "algebra"
        difficulty = "introductory"
    else:
        topic = "general math"
        difficulty = "introductory"

    return {
        "topic": topic,
        "difficulty": difficulty,
        "strategy": "teach concept first, then give hint, then verify"
    }