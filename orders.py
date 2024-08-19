class Order:
    def __init__(self):
        self.counter_id = 1
        self.orders = []

    def place_order(self, name, items, menu):
        index = []
        total_price = 0
        for item in items:
            this_item = menu.get_items(item)
            if this_item:
                index.append(this_item)
                total_price = total_price + this_item['price']
        orginal = {
            'order_id': self.counter_id,
            'costumer': name,
            'items': index,
            'total_price': total_price
        }
        self.counter_id = self.counter_id + 1
        self.orders.append(orginal)

        return f'your name is{name},your Order Id is {orginal["order_id"]}'

    def show_all_orders(self):
        ordering = ""
        for order in self.orders:
            ordering += f"Order ID: {order['order_id']}, Customer: {order['costumer']}, Total: ${order['total_price']}"
        return ordering

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
