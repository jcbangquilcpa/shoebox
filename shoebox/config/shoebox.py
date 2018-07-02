from __future__ import unicode_literals
from frappe import _

def get_data():
        return [
                {
                        "label": _("My Transactions"),
                        "items": [
                                {
                                        "type": "doctype",
                                        "name": "Sales Transaction",
					"label": "Sales"
                                },
                                {
                                        "type": "doctype",
                                        "name": "Purchase Transaction",
					"label": "Purchases"
                                },
				{
				        "type": "doctype",
                                        "name": "Receipt Transaction",
					"label": "Receipts"
				},
				{
				        "type": "doctype",
                                        "name": "Payment Transaction",
					"label": "Payments"
				},
                        ]
                },
                {
                        "label": _("My Compliance"),
                        "items": [
                                {
                                        "type": "doctype",
                                        "name": "Tax Return"
                                },
                                {
                                        "type": "doctype",
                                        "name": "Books of Accounts"
                                },
                                {
                                        "type": "doctype",
                                        "name": "Registration"
                                },
                        ]
                },

		]
