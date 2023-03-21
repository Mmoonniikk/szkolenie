class  Car:

    def __init__ (self, color, price, brand):
        self.color=color
        self.price=price
        self.brand=brand
        self.running=False


    c1 = 'Car('czerwony', 4500000, 'Ferrari')
    c2 = 'Car('zielony', 75000, "Opel")
    print(c1.color)

