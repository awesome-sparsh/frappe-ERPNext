import frappe
from frappe import _
import base64

@frappe.whitelist(allow_guest=False)
def create_employee(data):
    try:
        # Parse the JSON data received
        employee_data = frappe.parse_json(data)
        a = employee_data[0]

        # Create a new employee
        employee = frappe.get_doc({
            "doctype": "Employee",
            "first_name": a.get("first_name"),
            "last_name": a.get("last_name"),
            "gender": a.get("gender"),
            "date_of_birth": a.get("date_of_birth"),
            "date_of_joining": a.get("date_of_joining"),
            "designation": a.get("designation"),
            "department": a.get("department"),
            # Add other fields as required
        })
        employee.save(ignore_permissions=False)

        filedata = a.get("attachment_pdf")
        filename = "resume.pdf"  # Use a meaningful filename

        if filedata and filename:
            file = frappe.get_doc({
                "doctype": "File",
                "file_name": filename,
                "content": base64.b64decode(filedata),
                "attached_to_doctype": "Employee",
                "attached_to_name": employee.name
            })
            file.save()

            # Link the file to the Employee record
            employee.attachment_pdf = file.file_url
            employee.save(ignore_permissions=False)

        # Return success message or data if needed
        return {
            "status": "success",
            "message": _("Employee created successfully"),
            "employee_id": employee.name
        }
    except Exception as e:
        frappe.log_error(frappe.get_traceback(), _("API Error"))
        return {"status": "failed", "message": _("Failed to create employee. Error: {0}").format(str(e))}
