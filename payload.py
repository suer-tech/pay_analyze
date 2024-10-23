pay = {
    "type": "list",
    "items": [
        {
            "id": "01928ec4-59f5-7258-b000-962db15f0abc",
            "status": "succeeded",
            "paid": True,
            "amount": {
                "value": "200.00",
                "currency": "RUB"
            },
            "income_amount": None,
            "payment_method": {
                "type": "bank_card",
                "id": "01928ec4-59f5-7258-b000-962db15f0abc",
                "saved": False,
                "title": "Банковская карта",
                "card": {
                    "first6": "510092",
                    "last4": "3998",
                    "expiry_month": "",
                    "expiry_year": "",
                    "card_type": "",
                    "card_product": {
                        "code": "",
                        "name": ""
                    },
                    "issuer_country": "",
                    "issuer_name": ""
                }
            },
            "confirmation": {
                "type": "redirect",
                "enforce": False,
                "locale": "",
                "return_url": "https://www.example.com/return_url",
                "confirmation_url": "*"
            },
            "receipt": {
                "customer": {},
                "items": [
                    {
                        "description": "1",
                        "amount": {
                            "value": "2.00",
                            "currency": "RUB"
                        },
                        "vat_code": 1,
                        "quantity": 1,
                        "measure": ""
                    }
                ]
            },
            "authorization_details": {
                "bank_transaction_id": "ZNFjfJmYkI1wihjCoYqTEVwtzRg=",
                "rrn": "428906193307",
                "auth_code": "233986",
                "three_d_secure": {
                    "applied": True
                }
            },
            "created_at": "2024-10-15T06:01:25.749243Z",
            "expires_at": "2024-10-16T09:02:04.781085Z",
            "captured_at": "2024-10-15T06:04:18.43934Z",
            "succeeded_at": "2024-10-15T06:04:19.358417Z",
            "canceled_at": None,
            "recipient": {
                "account_id": "27",
                "gateway_id": ""
            },
            "description": "Заказ №72",
            "metadata": None,
            "cancellation_details": None,
            "refundable": False,
            "test": True
        },
        {
            "id": "01927bad-92aa-71a1-a3ce-5e587bd83bf5",
            "status": "canceled",
            "paid": False,
            "amount": {
                "value": "200.00",
                "currency": "RUB"
            },
            "income_amount": None,
            "payment_method": {
                "type": "bank_card",
                "id": "01927bab-c8ff-71a1-a50e-6be6955869d8",
                "saved": False,
                "title": "Банковская карта"
            },
            "confirmation": {
                "type": "redirect",
                "enforce": False,
                "locale": "",
                "return_url": "https://www.example.com/return_url",
                "confirmation_url": "*"
            },
            "receipt": {
                "customer": {},
                "items": [
                    {
                        "description": "1",
                        "amount": {
                            "value": "2.00",
                            "currency": "RUB"
                        },
                        "vat_code": 1,
                        "quantity": 1,
                        "measure": ""
                    }
                ]
            },
            "authorization_details": None,
            "created_at": "2024-10-11T13:03:45.834585Z",
            "expires_at": None,
            "captured_at": None,
            "succeeded_at": None,
            "canceled_at": "2024-10-11T13:03:46.345255Z",
            "recipient": {
                "account_id": "27",
                "gateway_id": ""
            },
            "description": "Заказ №72",
            "metadata": None,
            "cancellation_details": {
                "party": "payment_network",
                "reason": "Perspayee data expired or missing"
            },
            "refundable": False,
            "test": True
        },

]
}