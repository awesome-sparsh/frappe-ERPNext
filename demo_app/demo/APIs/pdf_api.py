from __future__ import unicode_literals
import frappe
from frappe import _

@frappe.whitelist(allow_guest=True)
def fetch_employee_pdf(employee_id):
    try:
        print("helloooooooo")
        # Fetch employee details from ERPNext
        employee = frappe.get_doc("Employee", {'name':employee_id})
        print(employee)
        print("eeeeeeeeeeeeeeeeeeee")
        if employee:
            # Render the employee details in the standard print format as PDF
            html = frappe.get_print('Employee', employee_id, 'Standard')
            
            # Convert HTML to string if it's in bytes format
            if isinstance(html, bytes):
                html = html.decode('utf-8', 'ignore')  # Handle decoding with error handling
            
            # Generate the PDF from the HTML
            pdf = frappe.utils.pdf.get_pdf(html)
            
            # Set the Content-Type header to indicate that you are returning a PDF
            frappe.local.response.filename = f"{employee_id}.pdf"
            frappe.local.response.filecontent = pdf
            frappe.local.response.type = "download"
            
            return
        else:
            frappe.throw(_('Employee not found with ID: {0}'.format(employee_id)))
    except Exception as e:
        print("eeeeeeeeeeeeeeeeeee")
        print(e)
        print("eeeeeeeeeeeeeeeeeeeeeeeeeee")
        frappe.log_error(frappe.get_traceback(), _("Error fetching employee PDF"))
        frappe.throw(_('Error fetching employee PDF'))
