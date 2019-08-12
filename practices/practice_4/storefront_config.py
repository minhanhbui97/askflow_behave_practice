class StorefrontConfig:

    def __init__(self, data):
        """
        Constructor
        :param data: JSON string (dict type)
        """
        self.data = data

    def update_data(self, data):
        self.data.update(data)
