from app.state import AgentState, append_log, append_tool_call
from app.tools.document_reader import search_documents


def research_node(state: AgentState) -> dict:
    query = state["user_input"]
    result = search_documents(query)

    return {
        "research_result": result,
        "tool_calls": append_tool_call(
            state,
            "search_documents",
            {"query": query},
            result,
        ),
        "logs": append_log(
            state,
            "research_agent",
            "documents_searched",
            {"query": query, "result_preview": result[:200]},
        ),
    }
