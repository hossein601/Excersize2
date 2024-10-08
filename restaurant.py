from menu import Menu
from reserve import Reserve
from staffs import Staff
from orders import Order


class Restaurant:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.menu = Menu()
        self.staff = Staff()
        self.reserve = Reserve()
        self.order = Order()

    def __str__(self):
        return f'restaurant: {self.name}, address: {self.address}, menu: {self.menu}'

    def showMenu(self):
        self.menu.show()

    def showReserve(self):
        self.reserve.show_reserve()

    def make_reservation(self, customer_name, number_of_people, time):
        return self.reserve.reservation(customer_name, number_of_people, time)

    def add_staff(self, name, position):
        self.staff.add_staff(name, position)

    def get_order(self, customer_name, items):
        self.order.place_order(customer_name, items, self.menu)

    def show_orders(self):
        return self.order.show_all_orders()

    def generate_bill(self, order_id):
        self.order.generate_bill(order_id)

