from app.state import AgentState, append_log


RESEARCH_KEYWORDS = {
    "policy",
    "document",
    "handbook",
    "leave",
    "benefit",
    "summarize",
    "read",
}

ACTION_KEYWORDS = {
    "send",
    "email",
    "write",
    "file",
    "create",
    "check employee",
    "employee",
    "database",
    "status",
}


def orchestrator_node(state: AgentState) -> dict:
    user_input = state["user_input"]
    lowered = user_input.lower()

    if any(keyword in lowered for keyword in ACTION_KEYWORDS):
        route = "action"
    elif any(keyword in lowered for keyword in RESEARCH_KEYWORDS):
        route = "research"
    else:
        route = "final"

    return {
        "route": route,
        "logs": append_log(
            state,
            "orchestrator",
            "route_selected",
            {"user_input": user_input, "route": route},
        ),
    }
