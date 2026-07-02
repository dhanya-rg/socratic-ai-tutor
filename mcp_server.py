from mcp.server.fastmcp import FastMCP
from tools.calculator import solve_known_problem

mcp = FastMCP("socratic-ai-tutor-tools")


@mcp.tool()
def verify_math_problem(question: str) -> str:
    """
    Verify selected algebra/probability problems for the SocraticAI Tutor.
    """
    result = solve_known_problem(question)

    if result["verified"]:
        return result["explanation"]

    return "No deterministic verification rule matched for this problem."


if __name__ == "__main__":
    mcp.run()
