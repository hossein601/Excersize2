
from restaurant import Restaurant

my_restaurant = Restaurant("azarbaijan", "jomhori")
while True:
    print("Enter your operation")
    print("1. menu\n"
          "2. menu items\n"
          "3. Make Reservation\n"
          "4. Show Reservations\n"
          "5. Add Staff\n"
          "6. Show Staff\n"
          "7. Make an Order\n"
          "8. Show Orders\n"
          "9. bill generate\n"
          "10. End\n"
          )

    choice = input("Please enter your choice: ")

    if choice == '1':
        print("\nMenu:")
        print(my_restaurant.showMenu())

    elif choice == '2':
        item_name = input("Enter the name of food you want")
        item_price = int(input("Enter the price of your food: "))
        my_restaurant.menu.add_food(item_name, item_price)
        print(f"{item_name} with price of{item_price} was added.")

    elif choice == '3':
        customer_name = input("Enter your name: ")
        number_of_people = int(input("Enter the number of people: "))
        time = input("Enter the resevation time for your reserve ")
        print(my_restaurant.make_reservation(customer_name, number_of_people, time))

    elif choice == '4':
        print("\nReservations:")
        print(my_restaurant.showReserve())

    elif choice == '5':
        staff_name = input("Enter the staff name ")
        position = input("Enter the position of your staff: ")
        print(my_restaurant.add_staff(staff_name, position))

    elif choice == '6':
        print("\nStaff:")
        print(my_restaurant.staff.get_staffs())

    elif choice == '7':
        customer_name = input("Enter your name: ")
        items = input("Enter the food items you want to order : ").split(',')
        print(my_restaurant.get_order(customer_name, [item.strip() for item in items]))

    elif choice == '8':
        print("\nOrders:")
        print(my_restaurant.show_orders())

    elif choice == '9':
        order_id = int(input("Enter the order ID to generate the bill: "))
        print(my_restaurant.generate_bill(order_id))

    elif choice == '10':
        print("good by!")
        break

    else:
        print("enter between 1 to 10")
