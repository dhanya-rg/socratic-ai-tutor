from tools.calculator import solve_known_problem


def verify(question: str, plan_result: dict) -> dict:
    result = solve_known_problem(question)

    if result["verified"]:
        return {
            "status": "verified",
            "message": result["explanation"],
        }

    return {
        "status": "needs_review",
        "message": (
            "The verifier does not have a deterministic checker for this exact problem yet. "
            "The tutor response should be reviewed or checked with an external tool."
        ),
    }
