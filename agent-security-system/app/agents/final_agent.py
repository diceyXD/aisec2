from app.state import AgentState, append_log


def final_node(state: AgentState) -> dict:
    if state.get("research_result"):
        answer = f"Research result: {state['research_result']}"
    elif state.get("action_result"):
        answer = f"Action result: {state['action_result']}"
    else:
        answer = (
            "I can help with company policy research, mock actions, and employee "
            "status checks. Please ask a specific question."
        )

    return {
        "final_answer": answer,
        "logs": append_log(
            state,
            "final_agent",
            "response_created",
            {"answer_preview": answer[:200]},
        ),
    }
