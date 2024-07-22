# Copyright (c) 2024, sparsh and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class clientsidescripting(Document):
	def set_field_value(docname, fieldname, new_value):
		doc = frappe.get_doc('client_side_scripting', 'test_doc')
		doc.set(fieldname, new_value)
		doc.save()
	def validate(self):	
		frappe.msgprint("hello frappe")
	def on_update(self):
		frappe.msgprint("on update event is called")
	def before_submit(self):
		frappe.msgprint("before submit")
	def on_submit(self):
		frappe.msgprint("on submit")
	def on_cancel(self):
		frappe.msgprint("on cancel")
	def on_trash(self):
		frappe.msgprint("doc deleted")
	def after_delete(self):
		frappe.msgprint("doc delete complete")

