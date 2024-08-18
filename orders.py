class Order:
    def __init__(self):
        self.counter_id = 1
        self.orders = []

    def place_order(self, name, items, menu):
        item = []
        total_price = 0
        for item in items:
            this_item = menu.get_items(item)
            if this_item:
                item.append(this_item)
                total_price = total_price + this_item['price']
        orders = {
            'order_id': self.counter_id,
            'costumer': name,
            'items': item,
            'total_price': total_price
        }
        self.counter_id = self.counter_id + 1
        self.orders.append(orders)

        return f'your name is{name},your orderid is {orders["order_id"]}'

    def show_orders(self):
        orders = ''
        for order in self.orders:
            orders += (f'order_id : {order["order"]},'
                       f'customer:{order["costumer"]},'
                       f'items {order["items"]},'
                       f'total_price:{order["total_price"]} ')

    def generate_bill(self, order_id):
        for order in self.orders:
            if order["order_id"] == order_id:
                output = f'bill of orderid{order["order_id"]}\n'
                output += f'bill of customer = {order["costumer"]}\n'
                output += f'bill of items = {order["items"]}\n'
                output += f'bill of total_price = {order["total_price"]}\n'
                for item in order['items']:
                    output += f"{item['name']} - ${item['price']}"
                output += f"Total: ${order['total_price']}"
                return output
            return "Order not found"




