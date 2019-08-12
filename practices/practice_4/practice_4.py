import json
import time
from pprint import pprint
from practices.storefront_config import StorefrontConfig
from practices.file_controller import FileController

modify_data = {
  "expiration_time": 200,
  "product": "qchat",
  "utm_campaign": str(time.time()),
  "storefront": {
    "banner_enabled": False,
    "purchase_options": [
          {
              "button_text": "Dynamic offer 1 - button_text",
              "description": "Dynamic offer 1 - description",
              "id": "",
              "price": "99.99",
              "price_text": "price_text",
              "session_count": "0",
              "subtitle": "Dynamic offer - subtitle",
              "title": "Dynamic offer - title",
              "suffix": "Dynamic offer - suffix",
              "trial_duration": 0,
              "min_member_count": 1,
              "max_member_count": 1,
              "action": "purchase",
              "frequency_view": "monthly",
              "free_learning_subscription": False,
              "team_type": "personal",
              "frequency": None
          }
      ]
  }
}
print("Type of modify_data variable")
print(type(modify_data))

# file_controller = FileController()
config = FileController().read_file("data.json")
print("Config object:")
print(config)
print(type(config))
config.update_file(modify_data)
print("After update_file")
print(type(config))
FileController().write_file(config, "result.json")
