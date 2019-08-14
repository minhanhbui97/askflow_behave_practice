from practices.practice_4_redo.purchase_option1 import PurchaseOption1
from practices.practice_4_redo.serializable import Serializable


class Storefront1(dict):
    def __init__(self, data):
        self.banner_enabled = data.get("banner_enabled")
        self.banner_text = data.get("banner_text")
        self.description = data.get("description")
        self.enabled = data.get("enabled")
        option_list = data.get("purchase_options")
        for i, option in enumerate(option_list):
            option_list[i] = PurchaseOption1(option)
            option_list.append(option_list[i])
        self.purchase_options = option_list


    def update_data(self, modify_data):
        self.banner_enabled = modify_data.get("banner_enabled")
        self.banner_text = modify_data.get("banner_text")
        self.description = modify_data.get("description")
        self.enabled = modify_data.get("enabled")

        option_list = modify_data.get("purchase_options")
        for i, option in enumerate(option_list):
            option_list[i] = PurchaseOption1(option).update_data(option_list[i])
            option_list.append(option_list[i])
        self.purchase_options = option_list

    def convert_to_dict(self):
        for i, option in enumerate(self.purchase_options):
            self.purchase_options[i] = PurchaseOption1(option).convert_to_dict()
            self.purchase_options.append(self.purchase_options[i])
        return {
            "banner_enabled": self.banner_enabled,
            "banner_text": self.banner_text,
            "description": self.description,
            "enabled": self.enabled,
            "purchase_options": self.purchase_options
        }
