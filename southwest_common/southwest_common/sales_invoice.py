# Copyright (c) 2014, Contributors
# License: GNU General Public License v3. See license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.utils import cstr
from frappe.model.naming import make_autoname

def autoname(doc, method):
	sales_order = cstr(doc.get("entries")[0].sales_order)
	if not sales_order:
		frappe.throw(_("Sales Invoice must be made against a valid Sales Order"))

	doc.name = make_autoname("INV/{}/.###".format(sales_order))
