class Staff:
    def __init__(self):
        self.staffs = []

    def add_staff(self, name, works):
        self.staffs.append({'name': name, 'works': works})
        return f'Added {name} works for {works} staff'

    def get_staffs(self):
        item = ''
        for staff in self.staffs:
            item += f'{staff["name"]}: {staff["works"]}'
        return item

