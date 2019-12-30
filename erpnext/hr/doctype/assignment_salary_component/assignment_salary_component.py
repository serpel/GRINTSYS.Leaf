# -*- coding: utf-8 -*-
# Copyright (c) 2019, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.model.document import Document

class AssignmentSalaryComponent(Document):
	
	def validate(self):
		details = frappe.get_all("Salary Detail",["name","salary_component","abbr","statistical_component","is_tax_applicable","is_flexible_benefit", "variable_based_on_taxable_salary", "depends_on_payment_days", "deduct_full_tax_on_selected_payroll_date", "default_amount", "additional_amount", "tax_on_flexible_benefit", "tax_on_additional_salary"], filters = {"name": "fb7e010297"})
		salary_slip = frappe.get_all("Salary Slip")
		frappe.throw(_("details: {}, nomina: {}".format(details, salary_slip)))
