BLOCKED_PATTERNS = [
    "ignore previous instructions",
    "bypass",
    "cheat",
    "do my homework",
    "just give me the answer",
    "give me the final answer only",
    "forget your rules",
]


def safety_check(question: str) -> dict:
    q = question.lower()

    for pattern in BLOCKED_PATTERNS:
        if pattern in q:
            return {
                "allowed": False,
                "reason": f"Blocked phrase detected: {pattern}",
                "message": (
                    "I can help you learn the concept, but I won't bypass the tutoring process "
                    "or simply complete homework for you. I can give a hint, explain the concept, "
                    "or walk through the reasoning step by step."
                ),
            }

    return {"allowed": True, "reason": "No policy issue detected."}
