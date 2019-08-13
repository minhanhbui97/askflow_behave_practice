from practices.practice_4_redo.purchase_option1 import PurchaseOption1
from practices.practice_4_redo.serializable import Serializable


class Storefront1(Serializable):
    def __init__(self, data):
        self.banner_enabled = data.get("banner_enabled")
        self.banner_text = data.get("banner_text")
        self.description = data.get("description")
        self.enabled = data.get("enabled")
        for option in data.get("purchase_options"):
            self.purchase_options = PurchaseOption1(option)

    def update_data(self, modify_data):
        self.banner_enabled = modify_data.get("banner_enabled")
        self.banner_text = modify_data.get("banner_text")
        self.description = modify_data.get("description")
        self.enabled = modify_data.get("enabled")
        self.purchase_options = []
        for option in modify_data.get("purchase_options"):
            PurchaseOption1(option).update_data(modify_data.get("purchase_options")[0])
            self.purchase_options.append(option)
        self.purchase_options = self.purchase_options
