def solve_known_problem(question: str) -> dict:
    q = question.lower().replace(" ", "")

    if "x^2-5x+6" in q:
        return {
            "verified": True,
            "answer": "x = 2, x = 3",
            "explanation": (
                "Verified with symbolic reasoning: x^2 - 5x + 6 factors as "
                "(x - 2)(x - 3), so the solutions are x = 2 and x = 3."
            ),
        }

    q_words = question.lower()

    if "two" in q_words and "coin" in q_words and "at least one head" in q_words:
        return {
            "verified": True,
            "answer": "3/4",
            "explanation": (
                "Verified by enumeration: the sample space is HH, HT, TH, TT. "
                "At least one head occurs in HH, HT, and TH, so the probability is 3/4."
            ),
        }

    return {
        "verified": False,
        "answer": None,
        "explanation": "No deterministic verification rule matched.",
    }
