# 5. Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats) 
# and get fare information of train running under Indian Railways.

class Train:
    def __init__(self, name, total_seats=100, fare=100.0):
        self.name = name
        self.total_seats = total_seats
        self.booked = 0
        self.fare = fare

    def book_ticket(self, n=1):
        if self.booked + n > self.total_seats:
            return False
        self.booked += n
        return True

    def get_status(self):
        return self.total_seats - self.booked

    def get_fare(self):
        return self.fare


# Demo
train = Train('Rajdhani', total_seats=10, fare=500.0)
print('Available before booking:', train.get_status())
print('Booking 3 tickets:', train.book_ticket(3))
print('Available after booking:', train.get_status())
print('Fare:', train.get_fare())
