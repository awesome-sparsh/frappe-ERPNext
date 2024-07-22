import frappe
from frappe import _

@frappe.whitelist(allow_guest=False)
def get_employee_details(employee_id):
    try:
        employee = frappe.get_doc("Employee", employee_id)
        if employee:
            # Customize the data you want to return
            return {
                "employee_name": employee.employee_name,
                "designation": employee.designation,
                "department": employee.department,
                # Add more fields as needed
            }
        else:
            return _("Employee not found")
    except Exception as e:
        frappe.log_error(frappe.get_traceback(), _("API Error"))
        return _("Error fetching employee details")


@frappe.whitelist(allow_guest=True)
def get_all_employee_details():
    try:
        # Fetch all employee records from ERPNext
        employees = frappe.get_all("Employee", fields=["*"])
        if employees:
            # Customize the data you want to return
            employee_details = []
            for employee in employees:
                employee_details.append({
                    "employee_name": employee.get("employee_name"),
                    "designation": employee.get("designation"),
                    "department": employee.get("department"),
                    # Add more fields as needed
                })
            return employee_details
        else:
            return _("No employees found")
    except Exception as e:
        frappe.log_error(frappe.get_traceback(), _("API Error"))
        return _("Error fetching employee details")

