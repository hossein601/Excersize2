class Menu:
    def __init__(self):
        self.items = []

    def add_food(self, item, price):
        self.items.append({'item': item, 'price': price})

    def show(self):
        showing = ''
        for item in self.items:
            showing += f'{item["item"]} - {item["price"]}\n'
        return showing

    def get_items(self, name):
        for item in self.items:
            if item['item'] == name:
                return item
        return None

