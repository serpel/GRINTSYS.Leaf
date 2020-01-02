# -*- coding: utf-8 -*-
# Copyright (c) 2019, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.model.document import Document

class AssignmentSalaryComponent(Document):
	
	def validate(self):
		self.status = self.get_status()
	
	def get_status(self):
		if self.docstatus == 0:
			status = "Saved"
		elif self.docstatus == 1:
			self.validate_assignment_Salary_Component()
			status = "Finished"
		return status
	
	def on_cancel(self):
		if self.docstatus == 2:
			self.status = "Cancelled"
	
	def validate_assignment_Salary_Component(self):
		type_component = ""
		if self.type == "Earning":
			type_component = "earnings"
		elif self.type == "Deduction":
			type_component = "deductions"

		employees = frappe.get_all("Employee Detail Salary Component", ["employee","moneda", "parent"], filters = {"parent": self.name})
		
		for item in employees:
			salary_slip = frappe.get_all("Salary Slip", ["name"], filters={"payroll_entry":self.payroll_entry, "employee":item.employee})
			
			for salary in salary_slip:
				doc = frappe.get_doc("Salary Slip", salary.name)
				row = doc.append(type_component, {})
				row.salary_component = self.salary_component
				row.amount = item.moneda
				doc.save()