from practices.practice_4_redo.storefront1 import Storefront1
from practices.practice_4_redo.serializable import Serializable


class StorefrontConfig1(dict):

    def __init__(self, data):
        self.expiration_time = data.get("expiration_time")
        self.id = data.get("id")
        self.product = data.get("product")
        self.storefront = Storefront1(data.get("storefront"))
        self.utm_campaign = data.get("utm_campaign")
        self.utm_source = data.get("utm_source")

    def update_data(self, modify_data):
        self.expiration_time = modify_data.get("expiration_time")
        self.id = modify_data.get("id")
        self.product = modify_data.get("product")
        self.storefront.update_data(modify_data.get("storefront"))
        self.utm_campaign = modify_data.get("utm_campaign")
        self.utm_source = modify_data.get("utm_source")

    def convert_to_dict(self):
        return {
            "expiration_time": self.expiration_time,
            "id": self.id,
            "product": self.product,
            "storefront": self.storefront.convert_to_dict(),
            "utm_campaign": self.utm_campaign,
            "utm_source": self.utm_source
        }