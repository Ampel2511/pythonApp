import json


def write_order_to_json(item, quantity, price, buyer, date):
    orders = {}
    with open('orders.json', 'r') as json_file:
        orders = json.load(json_file)
    orders['orders'].append({
        'item': item,
        'quantity': quantity,
        'price': price,
        'buyer': buyer,
        'date': date
    })
    with open('orders.json', 'w') as json_file:
        json.dump(orders, json_file)


write_order_to_json('product1', 228, 500, 'name1', '11-11-2011')
write_order_to_json('product2', 322, 600, 'name2', '12-11-2011')
write_order_to_json('product3', 777, 800, 'name3', '13-11-2011')
write_order_to_json('product4', 420, 900, 'name4', '14-11-2011')
write_order_to_json('product5', 20, 1000, 'name5', '15-11-2011')

# 3 выполнил скрипт в этом файле, поэтому в файле джейсона 3 раза повторились данные, данные не перезаписываются, а дописываются