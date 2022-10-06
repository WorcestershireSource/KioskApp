
from square.client import Client
import os
import uuid
import time


# Access token needed: add in terminal: export SQUARE_ACCESS_TOKEN=EAAAEAY2ifebRBl5JPP4VOZt1cDGFSeQQOhKD9SLjTSNwhoxxnJMOzRPhYXyXDmy
# Rename sandbox to 'production' and change token when ready 
client = Client(
    access_token=os.environ['SQUARE_ACCESS_TOKEN'],
    environment='sandbox')

# Globals
location_id = "L1G4EVF77D81D"








# CHECK OUT Need to add input variables and link to front end 
def check_out(basket, total, idempotency_key):

  # Connect to the terminal and set up an order - funcs below
  device_id = "9fa747a2-25ff-48ee-b078-04381f7c828f"    # connect2terminal(idempotency_key)["device_code"]["id"]
  order_id = create_order(basket)

  # Only for testing - REMOVE FOR PRODUCTION
  time.sleep(7)
  
  print(order_id)
  # Request a checkout - uses the ID created above: https://developer.squareup.com/docs/terminal-api/square-terminal-payments
  result = client.terminal.create_terminal_checkout(
    body = {
      "idempotency_key": idempotency_key,
      "checkout": {
        "amount_money": {
          "amount": total,
          "currency": "GBP"
        },
        "order_id": order_id,
        "device_options": {
          "device_id": device_id  
        }
      }
    }
  )


  if result.is_success():
    return result.body["checkout"]["id"]
  elif result.is_error():
    print(result.errors)






# MENU fetch all catalogue items from square and return them to main app as a list of dicts
def fetch_menu():
  cat_result = client.catalog.list_catalog(
    types = "item"
  )

  if cat_result.is_success():
    # This is a dict object returned by the Square API 
    raw_menu = cat_result.body
    menu = []

    # Parse dict object returned by Square and transform into smaller list of dicts
    for i, item in enumerate(raw_menu["objects"]):
      variations = []

      try:
          for variation in item["item_data"]["variations"]:
              variations.append({
                "id" : variation["id"],
                "name" : variation["item_variation_data"]["name"],
                "price" : variation["item_variation_data"]["price_money"]["amount"],
              })
      except KeyError:
          pass
      
      # Default price is the first option if there are variations else it is the price - CHECK LOGIC WORKS FOR LATTER
      if len(variations) > 0: 
        price = variations[0]["price"]
      else: price = item["item_data"]["price_money"]["amount"]
      
      try: 
        description = item["item_data"]["description_plaintext"]
      except KeyError: 
        description = ""

      menu.append({
          "id" : item["id"],
          "name": item["item_data"]["name"],
          "price": price,
          "variations": variations,
          "description": description,
          "variation_chosen": []
      })

    # Pass the smaller list of dicts back to the app
    return menu

  elif cat_result.is_error():
    print(cat_result.errors)











def connect2terminal(idempotency_key):
  # Connect to the square terminal: https://developer.squareup.com/docs/terminal-api/pos-integration
  result = client.devices.create_device_code(
    body = {
      "idempotency_key": idempotency_key,
      "device_code": {
        "name": "Counter 1",
        "product_type": "TERMINAL_API",
        "location_id": location_id
  }})
  if result.is_success():
    print(result.body)
    return result.body
  elif result.is_error():
    print(result.errors)



def create_order(basket):
  # Format the items in the basket to a list of dicts for the API
  order = []
  for item in basket:
    
    #Check which variations have been applied
    modify = []
    try:
      for variation in item["variation_chosen"]:
          modify.append({"catalogue_object_id": variation})
    except KeyError:
      pass
    
    # Add each item to the order
    order.append({
        "quantity": "1",
        "catalog_object_id": item["id"], # item["id"],
        "modifiers": modify,
    })
  
  print(order)

  # Call API and pass basket/order
  result = client.orders.create_order(
    body = {
      "order": {
        "location_id": location_id,
        "reference_id": str(uuid.uuid4()),
        "line_items": order,
      },
      "idempotency_key": str(uuid.uuid4())
    }
  )

  if result.is_success():
    print(result.body)
    return result.body["order"]["id"]
  elif result.is_error():
    print(result.errors)



def cancel_checkout(id):
  result = client.terminal.cancel_terminal_checkout(
    checkout_id = id
  )

  if result.is_success():
    print(result.body)
    return 1
  elif result.is_error():
    print(result.errors)
    return 0





# # Create example catalogue
# result = client.catalog.batch_upsert_catalog_objects(
#   body = {
#     "idempotency_key": "789ff020-f723-43a9-b4b5-43b5dc1fa3df", 
#     "batches": [
#       {
#         "objects": [
#           {
#             "type": "ITEM",
#             "id": "#MintTea",
#             "present_at_all_locations": True,
#             "item_data": {
#               "name": "Mint Tea",
#               "description": "Mint tea",
#               "category_id": "#Beverages",
#               "variations": [
#                 {
#                   "type": "ITEM_VARIATION",
#                   "id": "#Mint_Tea_Mug",
#                   "present_at_all_locations": True,
#                   "item_variation_data": {
#                     "item_id": "#MintTea",
#                     "name": "Mug",
#                     "pricing_type": "FIXED_PRICING",
#                     "price_money": {
#                       "amount": 150,
#                       "currency": "GBP"
#                     }
#                   }
#                 }
#               ]
#             }
#           },
#           {
#             "type": "ITEM",
#             "id": "#ECoffee",
#             "present_at_all_locations": True,
#             "item_data": {
#               "name": "Espresso",
#               "description": "Espresso",
#               "category_id": "#Beverages",
#               "variations": [
#                 {
#                   "type": "ITEM_VARIATION",
#                   "id": "#SingleE",
#                   "present_at_all_locations": True,
#                   "item_variation_data": {
#                     "item_id": "#ECoffee",
#                     "name": "Single",
#                     "pricing_type": "FIXED_PRICING",
#                     "price_money": {
#                       "amount": 200,
#                       "currency": "GBP"
#                     }
#                   }
#                 }
#               ]
#             }
#           },
#           {
#             "type": "CATEGORY",
#             "id": "#Beverages",
#             "present_at_all_locations": True,
#             "category_data": {
#               "name": "Beverages"
#             }
#           },
#         ]
#       }
#     ]
#   }
# )

# if result.is_success():
#   print(result.body)
# elif result.is_error():
#   print(result.errors)







