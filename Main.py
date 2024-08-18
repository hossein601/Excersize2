from restaurant import Restaurant

restaurant = Restaurant(input('Enter your resturan name'), input('Enter your restaurant address'))
restaurant.menu.add_food('kebab', 200)
restaurant.menu.add_food('gheime', 150)
restaurant.menu.add_food('ghorme', 250)
restaurant.add_staff("sara", "chef")
restaurant.add_staff("ali", "assistance chef")
restaurant.show_oder()
restaurant.get_order(input('please enter your name'), ['gheime', 'ghorme'])
