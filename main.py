from agents.pipeline import run_pipeline


def main():
    print("SocraticAI Tutor - type 'quit' to exit.")

    while True:
        question = input("\nStudent: ").strip()

        if question.lower() in {"quit", "exit"}:
            print("Goodbye!")
            break

        response = run_pipeline(question)
        print(response)


if __name__ == "__main__":
    main()
