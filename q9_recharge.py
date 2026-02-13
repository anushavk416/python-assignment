import logging
logging.basicConfig(
    filename = "recharge.log",
    level = logging.INFO,
    format = "%(asctime)s - %(levelname)s - %(message)s"
)

class Recharge:
    plan_price = 300
    default_validity = 28

    def __init__(self, mobile_no, name):
        self.mobile_no = mobile_no
        self.name = name
        self.balance = 0
        self.validity_days = 0

    def do_recharge(self):
        self.balance = Recharge.plan_price
        self.validity_days = Recharge.default_validity
        logging.info("Recharge successful.")

    def check_validity(self):
        if(self.validity_days == 0):
            logging.error("Recharge expired.")
        elif(self.validity_days < 2):
            logging.warning("Required to recharge soon!")
        logging.info("Validity days: %s", self.validity_days)

    def show_balance(self):
        return self.balance

    @classmethod
    def update_recharge_plans(cls, new_price, new_validity):
        cls.plan_price = new_price
        cls.default_validity = new_validity
        logging.info("Recharge plan updated.")

r1 = Recharge("1234412312", "Anusha")

r1.do_recharge()
logging.info("Balance: %s", r1.show_balance())
r1.check_validity()
Recharge.update_recharge_plans(400, 56)