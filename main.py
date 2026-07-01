from agents.planner import plan
from agents.tutor import explain_concept
from agents.hint import generate_hint
from agents.verifier import verify_solution
from agents.safety import safety_check

def run_tutor(question: str):
    safety = safety_check(question)
    if not safety["allowed"]:
        return safety["message"]

    plan_result = plan(question)
    concept = explain_concept(question, plan_result)
    hint = generate_hint(question, plan_result)
    verification = verify_solution(question, plan_result)

    return f"""
SocraticAI Tutor

Topic: {plan_result["topic"]}
Difficulty: {plan_result["difficulty"]}

Concept:
{concept}

Hint:
{hint}

Verification:
{verification}

Next step:
Try solving the next step yourself. If you're stuck, ask for another hint.
"""

if __name__ == "__main__":
    print("SocraticAI Tutor — type 'quit' to exit.")
    while True:
        q = input("\nStudent: ")
        if q.lower() in ["quit", "exit"]:
            break
        print(run_tutor(q))