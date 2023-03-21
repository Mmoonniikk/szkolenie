class Person:
    def __init__(self, imie, nazwisko, adres, wiek):
        self.imie = imie
        self.nazwisko = nazwisko
        self.adres = adres
        self.wiek = wiek

    def __str__(self):
        return f"{self.nazwisko}, {self.imie}, {self.adres}"

    def check_is_adult(self):
        return self.wiek >= 18


class Customer(Person):
    def __init__(self, imie, nazwisko, adres, wiek, login):
        super().__init__(imie, nazwisko, adres, wiek)
        self.orders = []
        self.login = login
        self.total_order_cost = 0.0

    def __str__(self):
        return f"{self.login}: {super().__str__()}"

    def add_order(self, product, cost):
        if self.check_is_adult():
            self.orders.append((product, cost))
            self.total_order_cost += cost

    def show_orders(self):
        for order in self.orders:
            print(f"{order[0]} - {order[1]} zł")


