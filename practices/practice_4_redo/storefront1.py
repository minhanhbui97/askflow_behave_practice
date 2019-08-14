from practices.practice_4_redo.purchase_option1 import PurchaseOption1
import copy


class Storefront1:
    def __init__(self, data):
        self.banner_enabled = data.get("banner_enabled")
        self.banner_text = data.get("banner_text")
        self.description = data.get("description")
        self.enabled = data.get("enabled")

        option_list = data.get("purchase_options")
        for i, option in enumerate(option_list):
            option_list[i] = PurchaseOption1(option)

        self.purchase_options = option_list

    def update_data(self, modify_data):
        self.banner_enabled = modify_data.get("banner_enabled", self.banner_enabled)
        self.banner_text = modify_data.get("banner_text", self.banner_text)
        self.description = modify_data.get("description", self.description)
        self.enabled = modify_data.get("enabled", self.enabled)

        option_list = modify_data.get("purchase_options", self.purchase_options)

        for i, option in enumerate(option_list):
            option_list[i] = self.purchase_options[i].update_data(option)

        self.purchase_options = option_list

    def convert_to_dict(self):

        storefront = copy.deepcopy(self.__dict__)
        # make a copy of storefront object to convert that object only

        option_list = storefront["purchase_options"]
        for i, option in enumerate(option_list):
            option_list[i] = option.convert_to_dict()
        storefront["purchase_options"] = option_list

        return storefront
