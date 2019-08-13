
class Serializable(object):
    __serializable__ = True

    def transform(self, instance):
        result = {}

        for key, value in instance.__dict__.items():
            if type(value) is list:
                list_items = []

                for item in value:
                    list_items = self.transform(item)

                result.update({
                    key: list_items
                })
            else:
                if hasattr(value, "__serializable__"):
                    result.update({
                        key: value.transform_to_serializable()
                    })
                else:
                    result.update({
                        key: value
                    })

        return result

    def transform_to_serializable(self):
        return self.transform(self)