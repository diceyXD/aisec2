from langgraph.graph import END, StateGraph

from app.agents.action_agent import action_node
from app.agents.final_agent import final_node
from app.agents.orchestrator import orchestrator_node
from app.agents.research_agent import research_node
from app.state import AgentState, Route


def route_decision(state: AgentState) -> Route:
    return state["route"]


def build_graph():
    graph = StateGraph(AgentState)

    graph.add_node("orchestrator", orchestrator_node)
    graph.add_node("research", research_node)
    graph.add_node("action", action_node)
    graph.add_node("final", final_node)

    graph.set_entry_point("orchestrator")
    graph.add_conditional_edges(
        "orchestrator",
        route_decision,
        {
            "research": "research",
            "action": "action",
            "final": "final",
        },
    )
    graph.add_edge("research", "final")
    graph.add_edge("action", "final")
    graph.add_edge("final", END)

    return graph.compile()


compiled_graph = build_graph()
