import logging

logging.basicConfig(
    filename = "movie.log",
    level = logging.INFO,
    format = "%(asctime)s - %(levelname)s - %(message)s"
)

class MovieTicket:
    ticket_price = 200
    theatre = "PVR"

    def __init__(self, movie_name, date):
        self.movie_name = movie_name
        self.date = date
        self.seats = 0

    def book_seats(self, seats):
        self.seats = self.seats + seats
        logging.info("Booked %s seats.", seats)

    def cancel_all_booking(self):
        if self.seats>0:
            self.seats = 0
            logging.info("Cancelled all seats.")
        else:
            logging.warning("Seat not booked.")

    def calculate_ticket_price(self):
        return MovieTicket.ticket_price * self.seats

    @classmethod
    def update_ticket_price(cls, new_price):
        cls.ticket_price = new_price
        logging.info("New ticket price: %s", cls.ticket_price)

p1 = MovieTicket("Coco", "10-02-2020")
p1.book_seats(5)
logging.info("Total ticket price: %s", p1.calculate_ticket_price())
p1.cancel_all_booking()
MovieTicket.update_ticket_price(380)