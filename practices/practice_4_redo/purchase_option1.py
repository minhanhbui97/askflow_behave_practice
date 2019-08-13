from practices.practice_4_redo.serializable import Serializable


class PurchaseOption1(Serializable):
    def __init__(self, data):
        self.button_text = data.get("button_text")
        self.description = data.get("description")
        self.id = data.get("id")
        self.price = data.get("price")
        self.price_text = data.get("price_text")
        self.session_count = data.get("session_count")
        self.subtitle = data.get("subtitle")
        self.title = data.get("title")
        self.suffix = data.get("suffix")
        self.trial_duration = data.get("trial_duration")
        self.min_member_count = data.get("min_member_count")
        self.max_member_count = data.get("max_member_count")
        self.action = data.get("action")
        self.frequency_view = data.get("frequency_view")
        self.free_learning_subscription = data.get("free_learning_subscription")
        self.team_type = data.get("team_type")
        self.frequency = data.get("frequency")

    def update_data(self, modify_data):
        self.__dict__.update(modify_data)
