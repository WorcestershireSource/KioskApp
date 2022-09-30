
from square.client import Client
import os
import uuid
import json

client = Client(
    access_token=os.environ['SQUARE_ACCESS_TOKEN'],
    environment='sandbox')

result = client.devices.create_device_code(
    body = {
        "idempotency_key": "4bffb735-5ea9-45b4-889a-d33200b12ad2",
        "device_code": {
        "name": "Counter 1",
        "product_type": "TERMINAL_API",
        "location_id": "L1G4EVF77D81D"
    }})
    
if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)

print(type(result.body["device_code"]["id"]))
# print(result.json())


# Indented version of dict object returned by catalogue request to Square - just to explore contents / understand structure 

# menu = 
# {'objects': 
#     [
#         {'type': 'ITEM', 'id': 'H2HYX5CCK4KRFIOO33M73NJZ', 'updated_at': '2022-09-29T01:30:40.754Z', 'created_at': '2022-09-29T01:30:40.754Z', 'version': 1664415040754, 'is_deleted': False, 'present_at_all_locations': True, 'item_data': {'name': 'Tea', 'description': 'Hot Leaf Juice', 'category_id': '4LV3LUKDW2YTRCQQ367QHJWC', 
#             'variations': [
#                                 {'type': 'ITEM_VARIATION', 'id': 'M3AB4BHJYHBU32MMDRZ6PRJF', 'updated_at': '2022-09-29T01:30:40.754Z', 'created_at': '2022-09-29T01:30:40.754Z', 'version': 1664415040754, 'is_deleted': False, 'present_at_all_locations': True, 'item_variation_data': {'item_id': 'H2HYX5CCK4KRFIOO33M73NJZ', 'name': 'Mug', 'ordinal': 0, 'pricing_type': 'FIXED_PRICING', 'price_money': {'amount': 150, 'currency': 'GBP'}, 'sellable': True, 'stockable': True}}
#                             ], 'product_type': 'REGULAR', 'description_html': 'Hot Leaf Juice', 'description_plaintext': 'Hot Leaf Juice'}}, 
        
#         {'type': 'ITEM', 'id': 'YOU6RIQQUO2P6PKH7ZKZPDQ6', 'updated_at': '2022-09-29T01:30:40.754Z', 'created_at': '2022-09-29T01:30:40.754Z', 'version': 1664415040754, 'is_deleted': False, 'present_at_all_locations': True, 'item_data': {'name': 'Coffee', 'description': 'Hot Bean Juice', 'category_id': '4LV3LUKDW2YTRCQQ367QHJWC', 
#             'variations': [
#                                 {'type': 'ITEM_VARIATION', 'id': '6WLL2O4CJXTZS4RHPFGL2273', 'updated_at': '2022-09-29T01:30:40.754Z', 'created_at': '2022-09-29T01:30:40.754Z', 'version': 1664415040754, 'is_deleted': False, 'present_at_all_locations': True, 'item_variation_data': {'item_id': 'YOU6RIQQUO2P6PKH7ZKZPDQ6', 'name': 'Regular', 'ordinal': 0, 'pricing_type': 'FIXED_PRICING', 'price_money': {'amount': 250, 'currency': 'GBP'}, 'sellable': True, 'stockable': True}}, 
#                                 {'type': 'ITEM_VARIATION', 'id': 'UULEVNLD2XF6WFXZNEGZGJHF', 'updated_at': '2022-09-29T01:30:40.754Z', 'created_at': '2022-09-29T01:30:40.754Z', 'version': 1664415040754, 'is_deleted': False, 'present_at_all_locations': True, 'item_variation_data': {'item_id': 'YOU6RIQQUO2P6PKH7ZKZPDQ6', 'name': 'Large', 'ordinal': 1, 'pricing_type': 'FIXED_PRICING', 'price_money': {'amount': 350, 'currency': 'GBP'}, 'sellable': True, 'stockable': True}}
#                             ],'product_type': 'REGULAR', 'description_html': 'Hot Bean Juice', 'description_plaintext': 'Hot Bean Juice'}}
#     ]
# }




# Dict returned by the API to connect to the terminal - includes ID to be used in checkout:

# {
#   "device_code": {
#     "id": "AF7AJW6VM31P3",
#     "name": "Terminal API Device created on Sep 14, 2022",
#     "code": "JHHYHH",
#     "product_type": "TERMINAL_API",
#     "location_id": "NHTLE2589dCGJ",
#     "pair_by": "2022-09-15T00:01:18.000Z",
#     "created_at": "2022-09-14T23:56:18.000Z",
#     "status": "UNPAIRED",
#     "status_changed_at": "2022-09-14T23:56:18.000Z"
#   }
# }
