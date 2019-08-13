import time
import json
from practices.practice_4.file_controller import FileController
from practices.practice_4.storefront_config import StorefrontConfig
import os


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

file_location = os.path.dirname(os.path.realpath('__file__'))

# Files
input_file = file_location + "/data.json"
output_file = file_location + "/result.json"

# Read file
config = FileController().read_file(input_file)
# read file and return a JSON string


print("config.data: ")
print(config.data)

print("config.data.get('storefront'): ")
print(config.data.get("storefront"))

print("config.storefront: ")
print(config.storefront)

config.update_data(modify_data)
FileController().write_file(config, output_file)
print(type(config))

print("config.data: ")
print(config.data)

print("config.data.get('storefront'): ")
print(config.data.get("storefront"))

print("config.storefront: ")
print(config.storefront)
# print(type(config.data.storefront))
# print("banner_enabled")
# print(str(config.data.get("storefront").get("banner_enabled")))
