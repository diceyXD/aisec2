import argparse
import json

from app.graph import compiled_graph
from app.state import initial_state


def run_agent(user_input: str) -> dict:
    state = initial_state(user_input)
    return compiled_graph.invoke(state)


def main() -> None:
    parser = argparse.ArgumentParser(description="Run the LangGraph target agent system.")
    parser.add_argument("question", help="User input to send to the target system")
    parser.add_argument(
        "--json",
        action="store_true",
        help="Print full final state as JSON instead of only the answer.",
    )
    args = parser.parse_args()

    result = run_agent(args.question)

    if args.json:
        print(json.dumps(result, indent=2))
        return

    print(result["final_answer"])


if __name__ == "__main__":
    main()
