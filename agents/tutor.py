def explain_concept(question: str, plan_result: dict) -> str:
    topic = plan_result["topic"]

    if topic == "Algebra":
        return (
            "This is an algebra problem involving a quadratic equation. For a quadratic like "
            "x^2 - 5x + 6 = 0, one useful method is factoring: find two numbers that multiply "
            "to the constant term and add to the coefficient of x."
        )

    if topic == "Probability":
        return (
            "This is a probability problem. A reliable strategy is to list the full sample space, "
            "identify the favorable outcomes, and divide favorable outcomes by total outcomes."
        )

    if topic == "Computer Science":
        return (
            "This is a programming problem. Break it into three parts: the input, the transformation, "
            "and the output. Then write pseudocode before implementing."
        )

    return (
        "Start by identifying what information is given, what the problem asks for, and which method "
        "connects the two."
    )
