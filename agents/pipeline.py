from agents.planner import plan
from agents.safety import safety_check
from agents.tutor import explain_concept
from agents.hint import generate_hint
from agents.verifier import verify


def run_pipeline(question: str) -> str:
    safety = safety_check(question)

    if not safety["allowed"]:
        return f"""
==============================
SocraticAI Tutor
==============================

Policy Check:
{safe_text(safety["message"])}
"""

    plan_result = plan(question)
    concept = explain_concept(question, plan_result)
    hint = generate_hint(question, plan_result)
    verification = verify(question, plan_result)

    return f"""
==============================
SocraticAI Tutor
==============================

Topic: {plan_result["topic"]}
Difficulty: {plan_result["difficulty"]}

Planner Strategy:
{plan_result["strategy"]}

Concept:
{concept}

Socratic Hint:
{hint}

Verification:
[{verification["status"]}] {verification["message"]}

Next Step:
Try the next step yourself. If you're stuck, ask for another hint.
"""


def safe_text(text: str) -> str:
    return text.replace("{", "{{").replace("}", "}}")
