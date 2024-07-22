// // Copyright (c) 2024, sparsh and contributors
// // For license information, please see license.txt

// frappe.ui.form.on("client side scripting", {
//  	//refresh(frm) {
//       //  frappe.msgprint("hello sparsh");
//  	//},
//     on_submit:function(frm){
//         //trigger when form is saved
//         debugger
//         frappe.msgprint(__("the full name is "+frm.doc.first_name+" "+ frm.doc.last_name));
//     },
//     set_field_value:function(frm){

//     }
// });


frappe.ui.form.on('client side scripting', {
    first_name: function(frm) {
        updateFullName(frm);
    },
    last_name: function(frm) {
        updateFullName(frm);
    }
});

function updateFullName(frm) {
    if (frm.doc.first_name && frm.doc.last_name) {
        var full_name = frm.doc.first_name + ' ' + frm.doc.last_name;
        frm.set_value('full_name', full_name);
    }
}