import frappe
from frappe import auth
from frappe.utils.password import get_decrypted_password


@frappe.whitelist(allow_guest=True)
def login(usr, pwd):
    try:
        login_manager=frappe.auth.LoginManager()
        login_manager.authenticate(user=usr, pwd=pwd)
        login_manager.post_login()
    except frappe.exceptions.AuthenticationError:
        frappe.clear_messages()
        frappe.local.response["message"]={
            "success_key":0,
            "message":"Authentication Failed"
        }
        return
    keys=generate_keys(frappe.session.user)
    api_secret=keys[0]
    api_key=keys[1]
    user=frappe.get_doc('User', frappe.session.user)
    print(get_decrypted_password("User","administrator", fieldname="api_secret"), " kkkkkkkkkkkkkkkkk")
    if user.api_key==None:
        api="none"
    frappe.response["message"]={
        "success_key": 100,
        "message": "Authentication Success",
        "sid": frappe.session.sid,
        "api_key": api_key,
        "api_secret": api_secret,
        "user_name": user.username
    }
    
def generate_keys(user):
    user_details=frappe.get_doc('User', user)
    api_secret= frappe.generate_hash(length=15)

    api_key=None

    if not user_details.api_key:
        api_key=frappe.generate_hash(length=15)
        user_details.api_key=api_key
    else:
        api_key=user_details.api_key
    
    user_details.api_secret=api_secret
    user_details.save()
    frappe.db.commit()
    return [api_secret, api_key]

