import json
from practices.practice_4_redo.storefront_config1 import StorefrontConfig1
from practices.practice_4_redo.serializable import Serializable



class FileController1:

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

        return StorefrontConfig1(data)

    @staticmethod
    def write_file(storefront_object, file_name):
        """
        Write to a file
        :param storefront_object:
        :param file_name: string (output file)
        """
        with open(file_name, 'w') as file:
            # file.write(data)
            data = json.dump(storefront_object.transform_to_serializable(), file, indent=4)
            # data = json.dumps(storefront_object.__dict__, indent=4)
            # data = json.dumps(storefront_object, default=lambda o: o.__dict__, sort_keys=True, indent=4)
            return data
