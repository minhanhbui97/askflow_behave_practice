from practices.storefront_config import StorefrontConfig
import json


class FileController:
    @staticmethod
    def read_file(file_name: str):
        with open(file_name) as json_file:
            data = json.load(json_file)
            # print("Data from read_file method:")
            # print(data)
            # for x in json_file:
            #     print("%s: %d" % (x, json_file[x]))
        return StorefrontConfig(data)

    @staticmethod
    def write_file(storefront_object: StorefrontConfig, file_name: str):
        with open(file_name, 'w') as json_file:
            data = json.dump(storefront_object.__dict__, json_file, indent=2)
            # data = json.dumps(storefront_object.__dict__, indent=2)
            # print("Data from write_file method:")
            # print(str(data))
        return str(data)
