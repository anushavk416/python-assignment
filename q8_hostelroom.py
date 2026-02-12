import logging

logging.basicConfig(
    filename = "hostel.log",
    level = logging.INFO,
    format = "%(asctime)s - %(levelname)s - %(message)s"
)

class HostelRoom:
    college_name = "BVRITH"
    addr = "Kondapur"
    rent_per_day = 100
    base_rent = 1000

    def __init__(self, room_no, sname, days):
        self.room_no = room_no
        self.sname = sname
        self.allocated = False
        self.days = days

    def allocate_room(self):
        if not self.allocated:
            self.allocated = True
        else:
            logging.error("Room already allocated.")

    def vacate_room(self):
        if self.allocated:
            self.allocated = False
        else:
            logging.error("Room not allocated.")

    def calculate_monthly_fee(self):
        return HostelRoom.rent_per_day * self.days // 30

    @classmethod
    def update_rent_per_day(cls, new_rent):
        cls.rent_per_day = new_rent
        logging.info("updated room rent: %s", cls.rent_per_day)
        

s1 = HostelRoom(102, "Anusha", 134)
s1.vacate_room()
s1.allocate_room()
logging.info("monthly fee: %s", s1.calculate_monthly_fee())

HostelRoom.update_rent_per_day(200)
