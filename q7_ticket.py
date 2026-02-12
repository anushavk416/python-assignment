import logging

logging.basicConfig(
    filename = "ticket.log",
    level = logging.INFO,
    format = "%(asctime)s - %(levelname)s - %(message)s"
)

class Ticket:
    base_fare = 100
    fare_per_km  = 50

    def __init__(self, pname, distance):
        self.pname = pname
        self.distance = distance
        self.booked = False

    def book_ticket(self):
        self.booked = True
        logging.info("Ticket booked.")

    def cancel_ticket(self):
        if self.booked:
            self.booked = False
            logging.info("Ticket cancelled.")
        else:
            logging.warning("Ticket not booked.")

    def calculate_fare(self):
        return Ticket.base_fare + Ticket.fare_per_km * self.distance

    @classmethod
    def update_base_fare(cls, new_fare):
        cls.base_fare = new_fare
        logging.info("New base fare: %s", cls.base_fare)
        
p1 = Ticket("anusha", 500)
p1.cancel_ticket()
p1.book_ticket()

logging.info("fare for travel: %s", p1.calculate_fare())
Ticket.update_base_fare(80)
