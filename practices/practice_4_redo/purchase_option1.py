from practices.practice_4_redo.serializable import Serializable


class PurchaseOption1(dict):
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
        # self.__dict__.update(modify_data)
        self.button_text = modify_data.get("button_text")
        self.description = modify_data.get("description")
        self.id = modify_data.get("id")
        self.price = modify_data.get("price")
        self.price_text = modify_data.get("price_text")
        self.session_count = modify_data.get("session_count")
        self.subtitle = modify_data.get("subtitle")
        self.title = modify_data.get("title")
        self.suffix = modify_data.get("suffix")
        self.trial_duration = modify_data.get("trial_duration")
        self.min_member_count = modify_data.get("min_member_count")
        self.max_member_count = modify_data.get("max_member_count")
        self.action = modify_data.get("action")
        self.frequency_view = modify_data.get("frequency_view")
        self.free_learning_subscription = modify_data.get("free_learning_subscription")
        self.team_type = modify_data.get("team_type")
        self.frequency = modify_data.get("frequency")

    def convert_to_dict(self):
        return {
              "button_text": self.button_text,
              "description": self.description,
              "id": self.id,
              "price": self.price,
              "price_text": self.price_text,
              "session_count": self.session_count,
              "subtitle": self.subtitle,
              "title": self.title,
              "suffix": self.suffix,
              "trial_duration": self.trial_duration,
              "min_member_count": self.min_member_count,
              "max_member_count": self.max_member_count,
              "action":self.action,
              "frequency_view": self.frequency_view,
              "free_learning_subscription": self.free_learning_subscription,
              "team_type": self.team_type,
              "frequency": self.frequency
          }
