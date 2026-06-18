EMPLOYEES = {
    "101": {"name": "Asha", "role": "HR Coordinator", "status": "active"},
    "102": {"name": "Rahul", "role": "Intern", "status": "certificate pending"},
    "103": {"name": "Minu", "role": "Security Analyst", "status": "active"},
}


def query_employee_status(employee_id: str) -> str:
    employee = EMPLOYEES.get(employee_id)
    if not employee:
        return f"No employee found for ID {employee_id}."

    return (
        f"Employee {employee_id}: {employee['name']}, "
        f"role={employee['role']}, status={employee['status']}."
    )
