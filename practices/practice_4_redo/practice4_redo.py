import time
import os
from practices.practice_4_redo.file_controller1 import FileController1


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
          },
{
              "button_text": "Dynamic offer 1 - button_text",
              "description": "Dynamic offer 1 - description",
              "id": "",
              "price": "100.99",
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

input_file = file_location + "/data.json"
output_file = file_location + "/result.json"

config = FileController1().read_file(input_file)
config.update_data(modify_data)
FileController1().write_file(config, output_file)
