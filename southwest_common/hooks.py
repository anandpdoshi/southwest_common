app_name = "southwest_common"
app_title = "Southwest Common"
app_publisher = "Anand Doshi"
app_description = "Common code for Southwest ERPNext"
app_icon = "icon-compass"
app_color = "#DF0598"
app_email = "anand@frappe.io"
app_url = "https://github.com/anandpdoshi/southwest_common"
app_version = "0.0.1"
hide_in_installer = True

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/southwest_common/css/southwest_common.css"
# app_include_js = "/assets/southwest_common/js/southwest_common.js"

# include js, css files in header of web template
# web_include_css = "/assets/southwest_common/css/southwest_common.css"
# web_include_js = "/assets/southwest_common/js/southwest_common.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Installation
# ------------

# before_install = "southwest_common.install.before_install"
# after_install = "southwest_common.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "southwest_common.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.core.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.core.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"Sales Invoice": {
		"autoname": "southwest_common.southwest_common.sales_invoice.autoname",
	}
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"southwest_common.tasks.all"
# 	],
# 	"daily": [
# 		"southwest_common.tasks.daily"
# 	],
# 	"hourly": [
# 		"southwest_common.tasks.hourly"
# 	],
# 	"weekly": [
# 		"southwest_common.tasks.weekly"
# 	]
# 	"monthly": [
# 		"southwest_common.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "southwest_common.install.before_tests"

