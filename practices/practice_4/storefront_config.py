class StorefrontConfig:

    data = {
        "expiration_time": int,
        "id": int,
        "product": str,
        "storefront": {
            "banner_enabled": bool,
            "banner_text": str,
            "description": str,
            "enabled": bool,
            "purchase_options": [
                {
                    "button_text": str,
                    "description": str,
                    "id": str,
                    "price": str,
                    "price_text": str,
                    "session_count": str,
                    "subtitle": str,
                    "title": str,
                    "suffix": str,
                    "trial_duration": int,
                    "min_member_count": int,
                    "max_member_count": int,
                    "action": str,
                    "frequency_view": str,
                    "free_learning_subscription": bool,
                    "team_type": str,
                    "frequency": None,
                }
            ],
        },
        "utm_campaign": str,
        "utm_source": str,
        }

    # storefront = data.get("storefront")
    # purchase_option = storefront.get("purchase_options")

    storefront = None
    purchase_option = None

    def __init__(self, data):
        """
        Constructor
        :param data: JSON string (dict type)
        """
        self.data = data
        self.storefront = data.get("storefront")
        self.purchase_option = data.get("storefront").get("purchase_options")

    # def __init__(self, data, storefront, purchase_option):
    #     """
    #     Constructor
    #     :param data: JSON string (dict type)
    #     """
    #     self.data = data
    #     self.storefront = storefront
    #     self.purchase_option = purchase_option

    def update_data(self, data):
        self.data.update(data)


