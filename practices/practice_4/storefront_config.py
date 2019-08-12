import time

class StorefrontConfig:
    config = {
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
                    "frequency": None
                }
            ]
        },
        "utm_campaign": str,
        "utm_source": str
    }

    def __init__(self, data: dict):
        self.__dict__ = data

    def update_file(self, modify_data: dict):
        # get configs in storefront_config -> update modify_data -> config should be modified with modify_data
        # modify_data = {
        #     "expiration_time": 200,
        #     "product": "qchat",
        #     "utm_campaign": str(time.time()),
        #     "storefront": {
        #         "banner_enabled": False,
        #         "purchase_options": [
        #             {
        #                 "button_text": "Dynamic offer 1 - button_text",
        #                 "description": "Dynamic offer 1 - description",
        #                 "id": "",
        #                 "price": "99.99",
        #                 "price_text": "price_text",
        #                 "session_count": "0",
        #                 "subtitle": "Dynamic offer - subtitle",
        #                 "title": "Dynamic offer - title",
        #                 "suffix": "Dynamic offer - suffix",
        #                 "trial_duration": 0,
        #                 "min_member_count": 1,
        #                 "max_member_count": 1,
        #                 "action": "purchase",
        #                 "frequency_view": "monthly",
        #                 "free_learning_subscription": False,
        #                 "team_type": "personal",
        #                 "frequency": None
        #             }
        #         ]
        #     }
        # }
        # ...
        # config = {
        #     modify_data,
        #     "frequency": 30
        # }
        self.config.update(modify_data)
        return self.config
