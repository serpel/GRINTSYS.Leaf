// Copyright (c) 2019, Frappe Technologies Pvt. Ltd. and contributors
// For license information, please see license.txt

frappe.ui.form.on('Assignment Salary Component', {
	// refresh: function(frm) {

	// }
	validate_assignment_Salary_Component: function(frm){
		if(frm.doc.amended_from){
			frappe.call({
				method: 'validate_assignment_Salary_Component',
				args: {},
				callback: function(r) {
				},
				doc: frm.doc,
				freeze: true,
				freeze_message: 'Validating assignment Salary Component...'
			});
		}else{
			frm.fields_dict.attendance_detail_html.html("");
		}
	},
});
