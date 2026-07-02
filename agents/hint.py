def generate_hint(question: str, plan_result: dict) -> str:
    topic = plan_result["topic"]

    if topic == "Algebra":
        return "Try finding two numbers that multiply to 6 and add to -5."

    if topic == "Probability":
        return "For two fair coin flips, list the outcomes: HH, HT, TH, TT."

    if topic == "Computer Science":
        return "Before coding, write down what data structure should hold the intermediate result."

    return "Rewrite the problem in your own words, then identify the first operation you need."
