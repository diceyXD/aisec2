from app.state import AgentState, append_log, append_tool_call
from app.tools.database_tool import query_employee_status
from app.tools.file_writer import write_mock_file
from app.tools.mock_email import send_mock_email


def action_node(state: AgentState) -> dict:
    user_input = state["user_input"]
    lowered = user_input.lower()

    if "email" in lowered or "send" in lowered:
        result = send_mock_email(
            recipient="hr@example.com",
            subject="Request from Agent System",
            body=user_input,
        )
        tool_name = "send_mock_email"
        parameters = {"recipient": "hr@example.com", "subject": "Request from Agent System"}
    elif "write" in lowered or "file" in lowered or "create" in lowered:
        result = write_mock_file("agent_output.txt", user_input)
        tool_name = "write_mock_file"
        parameters = {"filename": "agent_output.txt"}
    else:
        employee_id = "102" if "102" in lowered else "101"
        result = query_employee_status(employee_id)
        tool_name = "query_employee_status"
        parameters = {"employee_id": employee_id}

    return {
        "action_result": result,
        "tool_calls": append_tool_call(state, tool_name, parameters, result),
        "logs": append_log(
            state,
            "action_agent",
            "tool_executed",
            {"tool": tool_name, "parameters": parameters, "result_preview": result[:200]},
        ),
    }
