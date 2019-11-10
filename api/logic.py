from datetime import datetime
from pytz import timezone
from datetime import time
from restaurant.models import FoodDetail


def query_timing_pattern(food):
    query = FoodDetail.objects.filter(name=food)
    query_date = ""
    for i in query:
        query_date = i.available_timing 
    k = query_date.split(",")
    l = k[0].split("-")
    m = k[1].split("-")
    time1 = l[0];time2 = l[1];time3 = m[0];time4 = m[1]
    time1 = time1.strip();time2 = time2.strip();time3 = time3.strip();time4 = time4.strip()
    g,h = time1.split(":");g1,h1 = time2.split(":")
    g2, h2 = time3.split(":");g3, h3 = time4.split(":")
    compare_timing1 = time(int(g),int(h));compare_timing2 = time(int(g1),int(h1))
    compare_timing3 = time(int(g2),int(h2));compare_timing4 = time(int(g3),int(h3))
    return compare_timing1,compare_timing2,compare_timing3,compare_timing4


    
def get_time_now():    
    format = "%Y-%m-%d %H:%M:%S %Z%z"
    now_utc = datetime.now(timezone('UTC'))
    now_asia = now_utc.astimezone(timezone('Asia/Kolkata'))
    now_asia = str(now_asia)
    time_asia = now_asia.split()
    time_now = time_asia[1][:5]
    e,f = time_now.split(":")
    current_timing = time(int(e),int(f))
    return current_timing


    
def order_available(current_timing, compare_timing1,
                    compare_timing2, compare_timing3, compare_timing4):
    
    if (
        (current_timing >= compare_timing1 and current_timing <= compare_timing2)
        or 
        (current_timing >= compare_timing3 and current_timing <= compare_timing4)):
        print("Order available")
        return "Order Available"
    else:
        return "Order Not Available"  