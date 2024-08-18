from menu import Menu
from reserve import Reserve
from staffs import Staff


class Restaurant:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.menu = Menu()
        self.staff = Staff()
        self.reserve = Reserve()

    def __str__(self):
        return f'restaurant: {self.name}, address: {self.address}, menu: {self.menu}'

    def showMenu(self):
        self.menu.show()

    def showReserve(self):
        self.reserve.show_reserve()

    def reservation(self):
        self.reserve.reservation()

    def add_staff(self, name, position):
        self.staff.add_staff(name, position)

