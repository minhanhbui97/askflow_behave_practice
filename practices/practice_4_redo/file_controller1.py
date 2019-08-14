import json
from practices.practice_4_redo.storefront_config1 import StorefrontConfig1


class FileController1:

    @staticmethod
    def read_file(file_name):
        """
        Read a file
        :param file_name: string (input file)
        :return: data as a Storefront
        """
        with open(file_name) as file:
            data = json.load(file)
        return StorefrontConfig1(data)

    @staticmethod
    def write_file(storefront_object, file_name):
        """
        Write to a file
        :param storefront_object:
        :param file_name: string (output file)
        """
        with open(file_name, 'w') as file:
            data = json.dump(storefront_object.convert_to_dict(), file, indent=4)
            return data
