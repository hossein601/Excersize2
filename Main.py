from restaurant import Restaurant

restaurant = Restaurant('aboriginal', 'aghast')
restaurant.menu.add_food('kebab', 200)
restaurant.menu.add_food('gheime', 150)
restaurant.menu.add_food('form', 250)
restaurant.add_staff("sara", "chef")
restaurant.add_staff("ali", "assistance chef")

items_to_order = ["kebab", "gheime", 'form']
restaurant.get_order("sara", items_to_order)
restaurant.get_order("hafez", ['gheime', 'form'])
print(restaurant.show_orders())
print(restaurant.generate_bill(1))
print(restaurant.generate_bill(2))