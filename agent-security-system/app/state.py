from typing import Any, Literal, TypedDict


Route = Literal["research", "action", "final"]


class ToolCall(TypedDict):
    tool: str
    parameters: dict[str, Any]
    result: str


class AgentLog(TypedDict):
    agent: str
    event: str
    details: dict[str, Any]


class AgentState(TypedDict):
    user_input: str
    route: Route
    research_result: str
    action_result: str
    final_answer: str
    tool_calls: list[ToolCall]
    logs: list[AgentLog]


def initial_state(user_input: str) -> AgentState:
    return {
        "user_input": user_input,
        "route": "final",
        "research_result": "",
        "action_result": "",
        "final_answer": "",
        "tool_calls": [],
        "logs": [],
    }


def append_log(
    state: AgentState,
    agent: str,
    event: str,
    details: dict[str, Any],
) -> list[AgentLog]:
    return [*state.get("logs", []), {"agent": agent, "event": event, "details": details}]


def append_tool_call(
    state: AgentState,
    tool: str,
    parameters: dict[str, Any],
    result: str,
) -> list[ToolCall]:
    return [
        *state.get("tool_calls", []),
        {"tool": tool, "parameters": parameters, "result": result},
    ]
