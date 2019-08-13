import json
from practices.practice_4.storefront_config import StorefrontConfig
from practices.practice_4.storefront import Storefront
from practices.practice_4.purchase_option import PurchaseOption



class FileController:

    @staticmethod
    def read_file(file_name):
        """
        Read a file
        :param file_name: string (input file)
        :return: file's content: string
        """
        with open(file_name) as file:
            # return file.read()
            data = json.load(file)
            # return StorefrontConfig(data, data.get("storefront"), data.get("storefront").get("purchase_options"))

        return StorefrontConfig(data)

    @staticmethod
    def write_file(storefront_object, file_name):
        """
        Write to a file
        :param storefront_object:
        :param file_name: string (output file)
        """
        with open(file_name, 'w') as file:
            # file.write(data)
            data = json.dump(storefront_object, file, indent=4)
            # data = json.dumps(storefront_object.__dict__, indent=4)
            print(type(data))
            # data = json.dumps(storefront_object, default=lambda o: o.__dict__, sort_keys=True, indent=4)
            return data
