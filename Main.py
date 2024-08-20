
from restaurant import Restaurant

my_restaurant = Restaurant("azarbaijan", "jomhori")
while True:
    print("\nWelcome to the Restaurant Management System!")
    print("1. Show Menu")
    print("2. Add Menu Item")
    print("3. Make a Reservation")
    print("4. Show Reservations")
    print("5. Add Staff")
    print("6. Show Staff")
    print("7. Place an Order")
    print("8. Show Orders")
    print("9. Generate Bill")
    print("10. Exit")

    choice = input("Please select an option: ")

    if choice == '1':
        print("\nMenu:")
        print(my_restaurant.showMenu())

    elif choice == '2':
        item_name = input("Enter the name of the food item: ")
        item_price = float(input("Enter the price of the food item: "))
        my_restaurant.menu.add_food(item_name, item_price)
        print(f"{item_name} has been added to the menu.")

    elif choice == '3':
        customer_name = input("Enter your name: ")
        number_of_people = int(input("Enter the number of people: "))
        time = input("Enter the reservation time (e.g., 7:00 PM): ")
        print(my_restaurant.make_reservation(customer_name, number_of_people, time))

    elif choice == '4':
        print("\nReservations:")
        print(my_restaurant.showReserve())

    elif choice == '5':
        staff_name = input("Enter the name of the staff: ")
        position = input("Enter the staff position: ")
        print(my_restaurant.add_staff(staff_name, position))

    elif choice == '6':
        print("\nStaff:")
        print(my_restaurant.staff.get_staffs())

    elif choice == '7':
        customer_name = input("Enter your name: ")
        items = input("Enter the food items you want to order (comma separated): ").split(',')
        print(my_restaurant.get_order(customer_name, [item.strip() for item in items]))

    elif choice == '8':
        print("\nOrders:")
        print(my_restaurant.show_orders())

    elif choice == '9':
        order_id = int(input("Enter the order ID to generate the bill: "))
        print(my_restaurant.generate_bill(order_id))

    elif choice == '10':
        print("Exiting the system. Have a nice day!")
        break

    else:
        print("Invalid option, please try again.")
