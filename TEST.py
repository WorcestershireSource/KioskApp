
from square.client import Client
import os



client = Client(
    access_token=os.environ['SQUARE_ACCESS_TOKEN'],
    environment='production')


result = client.catalog.list_catalog(
  types = "item"
)

if result.is_success():
  print(result.body)
elif result.is_error():
  print(result.errors)



# result = client.devices.create_device_code(
#     body = {
#         "idempotency_key": "4bffb735-5ea9-45b4-889a-d33200b12ad2",
#         "device_code": {
#         "name": "Counter 1",
#         "product_type": "TERMINAL_API",
#         "location_id": "L1G4EVF77D81D"
#     }})
    
# if result.is_success():
#     print(result.body)
# elif result.is_error():
#     print(result.errors)

# print(type(result.body["device_code"]["id"]))



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



# OFF CANVAS - NOT USED
    # <a class="btn btn-primary btn-sm" data-bs-toggle="offcanvas" href="#offcanvas{{ item['id']}}" role="button" aria-controls="offcanvas{{ item['id']}}">+</a>                    
    # <!-- Customisation menu -->
    # <div class="offcanvas offcanvas-start" tabindex="-1" id="offcanvas{{ item['id']}}" aria-labelledby="offcanvas{{ item['id']}}Label">
    #     <div class="offcanvas-header">
    #         <h5 class="offcanvas-title" id="offcanvas{{ item['id']}}Label">Choices</h5>
    #         <button type="button" class="btn-close" data-bs-dismiss="offcanvas" aria-label="Close"></button>
    #     </div>
    #     <div class="offcanvas-body">
    #         <form action="/addbasket" method="post">
    #             <div>
    #                 <div class="btn-group-vertical" role="group" aria-label="Vertical radio toggle button group">
    #                     {% for choice in item["Variations"] %}
    #                         <input type="radio" class="btn-check" name="addbasket_subchoice" value="{{ choice['id'] }}" id="{{ choice['id'] }}" autocomplete="off">
    #                         <input hidden id="addbasket" name="addbasket" value="{{ item['id'] }}"> 
    #                         <!-- Issue with 'for' label here -->
    #                         <label class="btn btn-outline-primary" for="addbasket"> {{ choice["name"] }} {{ "£%.2f"|format(choice["price"]/100) }} </label>
    #                     {% endfor %}
    #                 </div>
    #             </div>
    #             <button type="submit" class="btn btn-primary btn-sm">Add to order</button>
    #         </form>    
    #     </div>
    # </div>


#   File "/Users/alexwilkes/Documents/Coding/kioskapp/Squarecode.py", line 91, in fetch_menu
#     "name": item["item_data"]["description_plaintext"],

# Actual data
{'objects': 
    [
        {'type': 'ITEM', 'id': '2NDLQVWREHIXP7TOR6NQW7F3', 'updated_at': '2022-10-01T07:29:02.797Z', 'created_at': '2022-09-23T10:22:13.58Z', 'version': 1664609342797, 'is_deleted': False, 'catalog_v1_ids': [{'catalog_v1_id': 'U5O7D45WEGEXONXOFFHEDV4D', 'location_id': 'LHGK4D5XPMBSF'}], 'present_at_all_locations': False, 'present_at_location_ids': ['LHGK4D5XPMBSF'], 'item_data': 
            {'name': 'Cafe Latte', 'is_taxable': True, 'visibility': 'PRIVATE', 'available_online': False, 'available_for_pickup': False, 'available_electronically': False, 'category_id': 'INJ5DM523YY4C5A7NGG5OJMF', 'ordinal': 0, 'tax_ids': ['K6XD5ABZ7YYVMNA545PAMQBZ'], 'variations': [
                {'type': 'ITEM_VARIATION', 'id': 'WP4DNVKB6SJ5QIQFC5NK33QA', 'updated_at': '2022-09-29T01:07:57.48Z', 'created_at': '2022-09-23T10:22:13.58Z', 'version': 1664413677480, 'is_deleted': False, 'catalog_v1_ids': [{'catalog_v1_id': 'L2RYJUURDFTATKSY44KQFQCF', 'location_id': 'LHGK4D5XPMBSF'}], 'present_at_all_locations': False, 'present_at_location_ids': ['LHGK4D5XPMBSF'], 'item_variation_data': 
                    {'item_id': '2NDLQVWREHIXP7TOR6NQW7F3', 'name': 'Plant based blend', 'ordinal': 0, 'pricing_type': 'FIXED_PRICING', 'price_money': {'amount': 250, 'currency': 'GBP'}, 'location_overrides': [{'location_id': 'LHGK4D5XPMBSF', 'track_inventory': False}], 'item_option_values': [{'item_option_id': '523B2PFRKKKYO6IQ6MTA3P2J', 'item_option_value_id': '4CFFZV6Z4SCR64UXDJJF7WY4'}], 'sellable': True, 'stockable': True}
                }, 
                {'type': 'ITEM_VARIATION', 'id': 'M3ZU2OLVVT3RXCFGC6DF5GPJ', 'updated_at': '2022-09-29T01:09:25.883Z', 'created_at': '2022-09-29T01:07:57.48Z', 'version': 1664413765883, 'is_deleted': False, 'present_at_all_locations': False, 'present_at_location_ids': ['LHGK4D5XPMBSF'], 'item_variation_data': 
                {'item_id': '2NDLQVWREHIXP7TOR6NQW7F3', 'name': 'Organic Dairy Milk', 'ordinal': 1, 'pricing_type': 'FIXED_PRICING', 'price_money': {'amount': 350, 'currency': 'GBP'}, 'track_inventory': False, 'item_option_values': [{'item_option_id': '523B2PFRKKKYO6IQ6MTA3P2J', 'item_option_value_id': '454IYB32ZXRJ5YNIGH4OTMKC'}], 'sellable': True, 'stockable': True}
                }], 
                'product_type': 'REGULAR', 'skip_modifier_screen': False, 'item_options': [{'item_option_id': '523B2PFRKKKYO6IQ6MTA3P2J'}], 'ecom_available': False, 'ecom_visibility': 'UNINDEXED'}}, 
            
            {'type': 'ITEM', 'id': 'IMDIWWN5TFA3WXVHBPG5XHMH', 'updated_at': '2022-10-01T07:29:02.797Z', 'created_at': '2022-09-26T08:47:56.034Z', 'version': 1664609342797, 'is_deleted': False, 'catalog_v1_ids': [{'catalog_v1_id': '73OUFNH7IC7X5QWPGUBLDU6A', 'location_id': 'LHGK4D5XPMBSF'}], 'present_at_all_locations': False, 'present_at_location_ids': ['LHGK4D5XPMBSF'], 'item_data': {'name': 'Americano', 'is_taxable': True, 'visibility': 'PRIVATE', 'available_online': False, 'available_for_pickup': False, 'available_electronically': False, 'category_id': 'INJ5DM523YY4C5A7NGG5OJMF', 'ordinal': 0, 'tax_ids': ['K6XD5ABZ7YYVMNA545PAMQBZ'], 'variations': [{'type': 'ITEM_VARIATION', 'id': 'U3DKGSZZLOM27BUYCQG7J4PV', 'updated_at': '2022-09-26T08:47:56.034Z', 'created_at': '2022-09-26T08:47:56.034Z', 'version': 1664182076034, 'is_deleted': False, 'catalog_v1_ids': [{'catalog_v1_id': 'PFGQ46RJLIJCTXOT3BM6WZNU', 'location_id': 'LHGK4D5XPMBSF'}], 'present_at_all_locations': False, 'present_at_location_ids': ['LHGK4D5XPMBSF'], 'item_variation_data': 
                {'item_id': 'IMDIWWN5TFA3WXVHBPG5XHMH', 'name': 'Regular', 'ordinal': 1, 'pricing_type': 'FIXED_PRICING', 'price_money': {'amount': 200, 'currency': 'GBP'}, 'location_overrides': [{'location_id': 'LHGK4D5XPMBSF', 'track_inventory': False}], 'sellable': True, 'stockable': True}}], 'product_type': 'REGULAR', 'skip_modifier_screen': False, 'ecom_available': False, 'ecom_visibility': 'UNINDEXED'}}, 
                
            {'type': 'ITEM', 'id': 'V34XI3MRITDBYL4H5YR332X6', 'updated_at': '2022-10-01T07:29:02.797Z', 'created_at': '2022-09-26T08:47:56.791Z', 'version': 1664609342797, 'is_deleted': False, 'catalog_v1_ids': [{'catalog_v1_id': '75Q2FMNYJY4WESUA2UXMJINC', 'location_id': 'LHGK4D5XPMBSF'}], 'present_at_all_locations': False, 'present_at_location_ids': ['LHGK4D5XPMBSF'], 'item_data': {'name': 'Espresso', 'is_taxable': True, 'visibility': 'PRIVATE', 'available_online': False, 'available_for_pickup': False, 'available_electronically': False, 'category_id': 'INJ5DM523YY4C5A7NGG5OJMF', 'ordinal': 0, 'tax_ids': ['K6XD5ABZ7YYVMNA545PAMQBZ'], 'variations': [{'type': 'ITEM_VARIATION', 'id': 'RUDUEGJQKGBGJJ6KQKKRMJX5', 'updated_at': '2022-09-26T08:47:56.791Z', 'created_at': '2022-09-26T08:47:56.791Z', 'version': 1664182076791, 'is_deleted': False, 'catalog_v1_ids': [{'catalog_v1_id': 'JSKUEC2A755K7ZNJQPM6NPVL', 'location_id': 'LHGK4D5XPMBSF'}], 'present_at_all_locations': False, 'present_at_location_ids': ['LHGK4D5XPMBSF'], 'item_variation_data': 
                {'item_id': 'V34XI3MRITDBYL4H5YR332X6', 'name': 'Regular', 'ordinal': 1, 'pricing_type': 'FIXED_PRICING', 'price_money': {'amount': 150, 'currency': 'GBP'}, 'location_overrides': [{'location_id': 'LHGK4D5XPMBSF', 'track_inventory': False}], 'sellable': True, 'stockable': True}}], 'product_type': 'REGULAR', 'skip_modifier_screen': False, 'ecom_available': False, 'ecom_visibility': 'UNINDEXED'}}, 
            
            {'type': 'ITEM', 'id': 'J7U76XUA2KB4XAUBUNYZGST6', 'updated_at': '2022-10-01T07:35:31.466Z', 'created_at': '2022-09-29T01:04:37.6Z', 'version': 1664609731466, 'is_deleted': False, 'present_at_all_locations': True, 'item_data': {'name': 'Tea', 'is_taxable': True, 'visibility': 'PRIVATE', 'available_online': False, 'available_for_pickup': False, 'available_electronically': False, 'ordinal': 0, 'tax_ids': ['K6XD5ABZ7YYVMNA545PAMQBZ'], 'variations': [{'type': 'ITEM_VARIATION', 'id': 'L3ADTFCT3YVHXICHMDXLRLIK', 'updated_at': '2022-09-29T01:05:54.946Z', 'created_at': '2022-09-29T01:04:37.6Z', 'version': 1664413554946, 'is_deleted': False, 'present_at_all_locations': True, 'item_variation_data': 
                {'item_id': 'J7U76XUA2KB4XAUBUNYZGST6', 'name': 'Regular', 'ordinal': 1, 'pricing_type': 'FIXED_PRICING', 'price_money': {'amount': 100, 'currency': 'GBP'}, 'track_inventory': False, 'sellable': True, 'stockable': True}}], 
            'product_type': 'REGULAR', 'skip_modifier_screen': False, 'ecom_available': False, 'ecom_visibility': 'UNINDEXED'}}, 
            
            {'type': 'ITEM', 'id': 'BCUHEY4BPHC3EBEDGIR54SFM', 'updated_at': '2022-10-01T07:35:31.128Z', 'created_at': '2022-09-29T01:05:22.724Z', 'version': 1664609731128, 'is_deleted': False, 'present_at_all_locations': True, 'item_data': {'name': 'Banana bread', 'is_taxable': True, 'visibility': 'PRIVATE', 'available_online': False, 'available_for_pickup': False, 'available_electronically': False, 'ordinal': 0, 'tax_ids': ['K6XD5ABZ7YYVMNA545PAMQBZ'], 'variations': [{'type': 'ITEM_VARIATION', 'id': 'GCOF3RF23AGLQJD5EXYOU4PB', 'updated_at': '2022-09-29T01:05:22.724Z', 'created_at': '2022-09-29T01:05:22.724Z', 'version': 1664413522724, 'is_deleted': False, 'present_at_all_locations': True, 'item_variation_data': 
                {'item_id': 'BCUHEY4BPHC3EBEDGIR54SFM', 'name': 'Regular', 'ordinal': 1, 'pricing_type': 'FIXED_PRICING', 'price_money': {'amount': 250, 'currency': 'GBP'}, 'sellable': True, 'stockable': True}}], 'product_type': 'REGULAR', 'skip_modifier_screen': False, 'ecom_available': False, 'ecom_visibility': 'UNINDEXED'}}, 
                
            {'type': 'ITEM', 'id': 'SUKGCE5LRTEWSY37YV2BUWEX', 'updated_at': '2022-10-01T07:35:31.286Z', 'created_at': '2022-09-29T01:05:33.389Z', 'version': 1664609731286, 'is_deleted': False, 'present_at_all_locations': True, 'item_data': {'name': 'Chia pudding', 'is_taxable': True, 'visibility': 'PRIVATE', 'available_online': False, 'available_for_pickup': False, 'available_electronically': False, 'ordinal': 0, 'tax_ids': ['K6XD5ABZ7YYVMNA545PAMQBZ'], 'variations': [{'type': 'ITEM_VARIATION', 'id': 'WVFC75SGYOAHVVBRWYNE765A', 'updated_at': '2022-09-29T01:05:33.389Z', 'created_at': '2022-09-29T01:05:33.389Z', 'version': 1664413533389, 'is_deleted': False, 'present_at_all_locations': True, 'item_variation_data': {'item_id': 'SUKGCE5LRTEWSY37YV2BUWEX', 'name': 'Regular', 'ordinal': 1, 'pricing_type': 'FIXED_PRICING', 'price_money': {'amount': 400, 'currency': 'GBP'}, 'sellable': True, 'stockable': True}}], 'product_type': 'REGULAR', 'skip_modifier_screen': False, 'ecom_available': False, 'ecom_visibility': 'UNINDEXED'}},
            
            {'type': 'ITEM', 'id': 'PKFWCZ2EFA52IEEA4QU7RA3C', 'updated_at': '2022-10-01T07:35:31.203Z', 'created_at': '2022-09-29T01:06:16.132Z', 'version': 1664609731203, 'is_deleted': False, 'present_at_all_locations': True, 'item_data': 
                {'name': 'Cappuccino', 'is_taxable': True, 'visibility': 'PRIVATE', 'available_online': False, 'available_for_pickup': False, 'available_electronically': False, 'category_id': 'INJ5DM523YY4C5A7NGG5OJMF', 'ordinal': 0, 'tax_ids': ['K6XD5ABZ7YYVMNA545PAMQBZ'], 'variations': [
                    {'type': 'ITEM_VARIATION', 'id': 'CA7EWFKRPHBRIV4QOAWFD63E', 'updated_at': '2022-09-29T01:08:21.394Z', 'created_at': '2022-09-29T01:06:16.132Z', 'version': 1664413701394, 'is_deleted': False, 'present_at_all_locations': True, 'item_variation_data': 
                        {'item_id': 'PKFWCZ2EFA52IEEA4QU7RA3C', 'name': 'Plant based blend', 'ordinal': 0, 'pricing_type': 'FIXED_PRICING', 'price_money': {'amount': 250, 'currency': 'GBP'}, 'item_option_values': [{'item_option_id': '523B2PFRKKKYO6IQ6MTA3P2J', 'item_option_value_id': '4CFFZV6Z4SCR64UXDJJF7WY4'}], 'sellable': True, 'stockable': True}},
                    {'type': 'ITEM_VARIATION', 'id': 'V4KR36VGTXL4AJYEISQ62NWU', 'updated_at': '2022-09-29T01:09:09.686Z', 'created_at': '2022-09-29T01:08:21.394Z', 'version': 1664413749686, 'is_deleted': False, 'present_at_all_locations': True, 'item_variation_data': 
                        {'item_id': 'PKFWCZ2EFA52IEEA4QU7RA3C', 'name': 'Organic Dairy Milk', 'ordinal': 1, 'pricing_type': 'FIXED_PRICING', 'price_money': {'amount': 350, 'currency': 'GBP'}, 'track_inventory': False, 'item_option_values': [{'item_option_id': '523B2PFRKKKYO6IQ6MTA3P2J', 'item_option_value_id': '454IYB32ZXRJ5YNIGH4OTMKC'}], 'sellable': True, 'stockable': True}}], 
            'product_type': 'REGULAR', 'skip_modifier_screen': False, 'item_options': [{'item_option_id': '523B2PFRKKKYO6IQ6MTA3P2J'}], 'ecom_available': False, 'ecom_visibility': 'UNINDEXED'}},    

            
            {'type': 'ITEM', 'id': 'JZDOON6XJ6NAVS7MEVPOXALR', 'updated_at': '2022-10-01T07:35:31.388Z', 'created_at': '2022-09-29T01:06:28.203Z', 'version': 1664609731388, 'is_deleted': False, 'present_at_all_locations': True, 'item_data': {'name': 'Macchiato', 'is_taxable': True, 'visibility': 'PRIVATE', 'available_online': False, 'available_for_pickup': False, 'available_electronically': False, 'ordinal': 0, 'tax_ids': ['K6XD5ABZ7YYVMNA545PAMQBZ'], 'variations': [{'type': 'ITEM_VARIATION', 'id': 'GEA34Z4V6EQL2II3SUD3KQSH', 'updated_at': '2022-09-29T01:08:37.569Z', 'created_at': '2022-09-29T01:06:28.203Z', 'version': 1664413717569, 'is_deleted': False, 'present_at_all_locations': True, 'item_variation_data': {'item_id': 'JZDOON6XJ6NAVS7MEVPOXALR', 'name': 'Plant based blend', 'ordinal': 0, 'pricing_type': 'FIXED_PRICING', 'price_money': {'amount': 200, 'currency': 'GBP'}, 'item_option_values': [{'item_option_id': '523B2PFRKKKYO6IQ6MTA3P2J', 'item_option_value_id': '4CFFZV6Z4SCR64UXDJJF7WY4'}], 'sellable': True, 'stockable': True}}, 
            
            {'type': 'ITEM_VARIATION', 'id': 'AYHBXVG3PPYPAI5C6UCLYNUP', 'updated_at': '2022-09-29T01:09:39.796Z', 'created_at': '2022-09-29T01:08:37.569Z', 'version': 1664413779796, 'is_deleted': False, 'present_at_all_locations': True, 'item_variation_data': {'item_id': 'JZDOON6XJ6NAVS7MEVPOXALR', 'name': 'Organic Dairy Milk', 'ordinal': 1, 'pricing_type': 'FIXED_PRICING', 'price_money': {'amount': 250, 'currency': 'GBP'}, 'track_inventory': False, 'item_option_values': [{'item_option_id': '523B2PFRKKKYO6IQ6MTA3P2J', 'item_option_value_id': '454IYB32ZXRJ5YNIGH4OTMKC'}], 'sellable': True, 'stockable': True}}],
            'product_type': 'REGULAR', 'skip_modifier_screen': False, 'item_options': [{'item_option_id': '523B2PFRKKKYO6IQ6MTA3P2J'}], 'ecom_available': False, 'ecom_visibility': 'UNINDEXED'}
        }
    ]
}
