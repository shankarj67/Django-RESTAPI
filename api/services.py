import ast
import json
from .logic import order_available, get_time_now, query_timing_pattern   
from collections import OrderedDict

class APILogic:

    @staticmethod
    def restaurant_wise_sales(entry_list):
        count = 0
        entry_list = entry_list
        for entry in entry_list:
            a = entry.ordered_items
            c = ast.literal_eval(a)
            for item in c:
                if item['quantity']:
                    count+=item['quantity']
        sales_dict = json.dumps({"Total_Sales": count})         
        return sales_dict 

    @staticmethod
    def trending_items(query_list):
        entry_list = query_list
        item_dict = {}
        for entry in entry_list:
            a = entry.ordered_items
            c = ast.literal_eval(a)
            for i in c:
                for key, value in i.items():
                    if key=="itemname":
                        if value not in item_dict:
                            item_dict.update({value:0})

        for entry in entry_list:
            a = entry.ordered_items
            c = ast.literal_eval(a)
            for i in c:
                for key, value in i.items():
                    if key=="itemname":
                        if value in item_dict:
                            item_dict[value] += i['quantity']
        
        d = sorted(item_dict.items(), key=lambda x: x[1], reverse=True)
        d = dict(d)
        return json.dumps(d)
        
    
    @staticmethod
    def food_availablility(food, entry_list):
        compare_timing1, compare_timing2, compare_timing3, compare_timing4 = query_timing_pattern(food)
        current_timing = get_time_now()
        availability = order_available(current_timing, compare_timing1, 
                compare_timing2, compare_timing3, compare_timing4 )

        count1 = 0
        for entry in entry_list:
            a = entry.ordered_items
            c = ast.literal_eval(a)
            for item in c:
                if item['itemname'] == food:
                    if item['quantity']:
                        count1+=item['quantity']
        availability_dict = json.dumps({"Availability": availability, "Quantity_sold": count1})                 
        return availability_dict

  