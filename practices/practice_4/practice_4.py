import time
import json
from practices.practice_4.file_controller import FileController
from practices.practice_4.storefront_config import StorefrontConfig

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


# Files
input_file = "practice_4/data.json"
output_file = "practice_4/result.json"

# Read file
file_content = FileController().read_file(input_file)
# read file and return a JSON string

# Initiate instance of StorefrontConfig
config = StorefrontConfig(data=json.loads(file_content))
# json.loads('a JSON String') parse a JSON string into a dictionary object

# Update data
config.update_data(modify_data)
# update_data('a dict object') will update the instance config (StorefrontConfig object)

# Write file
# config.data = dict object
content_to_write = config.data
FileController().write_file(json.dumps(content_to_write, indent=4), output_file)
# json.dumps('a dict object') converts a dict object to a JSON string
# then write_file write JSON string to a file named "output_file"
