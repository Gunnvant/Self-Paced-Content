'''
Adapted from https://fastapi.tiangolo.com/python-types/
'''
## Simple types
# int
# string
# float 
# bool
# bytes

def get_items(item_a: str, item_b: int, item_c: float, item_d: bool, item_e: bytes):
    return item_a, item_b, item_c, item_d, item_d, item_e
get_items("a",4,5.0,False,b'127')


## Lists
def process_items(items: list[str]):
    for item in items:
        print(item)
process_items(['a','b'])


## Tuple and set
def process_items_v1(items_t: tuple[int, int, str], items_s: set[str]):
    return items_t, items_s
process_items_v1(items_t=(1,2,'a'),items_s={'21'})


## Dict
def process_items_v2(prices: dict[str, float]):
    for item_name, item_price in prices.items():
        print(item_name)
        print(item_price)

p = {'a':1.0}
p1 = {1:'a'}
process_items_v2(p)
process_items_v2(p1) ## dynamic checks

##Union
def process_item_v3(item: int | str):
    print(item)

p2 = 2
p3 = 'a'
p4 = 2.0
print(process_item_v3(p2))
print(process_item_v3(p3))
print(process_item_v3(p4)) ## dynamic checks

## Possibly None
from typing import Optional


def say_hi(name: Optional[str] = None):
    if name is not None:
        print(f"Hey {name}!")
    else:
        print("Hello World")
p5 = None
p6 = 'a'
p7 = 1
print(say_hi(p5))
print(say_hi(p6))
print(say_hi(p7)) ## dynamic checks