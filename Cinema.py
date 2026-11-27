class Hall:
    def __init__(self, name, seats):
        self.name = name
        self.__seats = seats

    def get_seats(self):
        return self.__seats

    def __has_seats(self):
        return self.__seats > 0

    def has_seats(self):
        return self.__has_seats()

    def set_seats(self, n):
        if 0 <= n <= 100:
            self.__seats = n
        else:
            print("Invalid seats.")

    def __str__(self):
        return "Hall " + self.name + ": " + str(self.__seats) + " seats"


class Guest:
    def __init__(self, name, tickets):
        self.name = name
        self.__tickets = tickets

    def get_tickets(self):
        return self.__tickets

    def add_tickets(self, n):
        if n > 0:
            self.__tickets += n
        else:
            print("Invalid amount.")

    def __str__(self):
        return self.name + ": " + str(self.__tickets) + " tickets"


def reserve(hall, guest, n):
    if hall.has_seats():
        guest.add_tickets(n)
    else:
        print("Hall is full.")


def main():
    # 1.a
    hall = Hall("A", 40)
    print(hall)
    hall.set_seats(-5)
    print(hall.get_seats())
    hall.set_seats(150)
    print(hall.get_seats())
    hall.set_seats(0)
    print(hall)

    # 1.b
    maya = Guest("Maya", 8)
    print(maya)
    maya.add_tickets(-2)
    print(maya.get_tickets())
    maya.add_tickets(3)
    print(maya)

    # 1.c
    print(hall.has_seats())
    reserve(hall, maya, 5)
    print(maya.get_tickets())
    hall.set_seats(40)
    reserve(hall, maya, 5)
    print(maya)
    print(hall)


main()
