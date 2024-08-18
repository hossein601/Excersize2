class Reserve:
    def __init__(self):
        self.reserve = []

    def reservation(self, name, numbers, duration):
        self.reserve.append(dict(name=name, numbers=numbers, duration=duration))
        return f'congratulation {name} you would reserve{numbers} in {duration} days'

    def show_reserve(self):
        item = ''
        for reserve in self.reserve:
            item += f'{reserve["name"]}: {reserve["numbers"]}\n'
        return item

