from practices.practice_4_redo.purchase_option1 import PurchaseOption1
import copy


class Storefront1:
    def __init__(self, data):
        '''
        To initialize a Storefront object
        :param data: dict type
        '''
        self.banner_enabled = data.get("banner_enabled")
        self.banner_text = data.get("banner_text")
        self.description = data.get("description")
        self.enabled = data.get("enabled")

        option_list = data.get("purchase_options")
        for i, option in enumerate(option_list):
            # at this point, option hasn't been initialized as a purchase option object
            option_list[i] = PurchaseOption1(option)
        self.purchase_options = option_list

    def update_data(self, modify_data):
        self.banner_enabled = modify_data.get("banner_enabled", self.banner_enabled)
        self.banner_text = modify_data.get("banner_text", self.banner_text)
        self.description = modify_data.get("description", self.description)
        self.enabled = modify_data.get("enabled", self.enabled)
        self.pop("")
        # modify_data.get("purchase_options") returns a list of dict objects
        for i, option in enumerate(modify_data.get("purchase_options")):
            # use option (a dict object) to update self.purchase_options[i] (a PurchaseOption object)
            self.purchase_options[i].update_data(option)

    def convert_to_dict(self):

        storefront = copy.deepcopy(self.__dict__)
        # storefront = self.__dict__.copy()
        # make a copy of storefront object to convert that copy only everytime the code is run
        # if not make copy: 1st time: object => dict; 2nd time: dict => dict (fail)

        option_list = storefront["purchase_options"]
        print(option_list)
        for i, option in enumerate(option_list):
            # at this point, option_list is a list of options objects from the updated data (after update_data method)
            # option object needs to be converted to dict
            option_list[i] = option.convert_to_dict()
        # storefront["purchase_options"] = option_list

        return storefront
