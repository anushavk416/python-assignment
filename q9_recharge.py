import logging

logging.basicConfig(
    filename="recharge.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class Recharge:
    plans = {300: 28, 400: 56, 599: 84}

    def __init__(self, mobile_no: str, name: str) -> None:
        """
        Docstring for __init__
        
        :param self: object of class Recharge
        :param mobile_no: Mobile no of user
        :type mobile_no: str
        :param name: Name of user
        :type name: str
        """
        self.mobile_no = mobile_no
        self.name = name
        self.balance = 0
        self.validity_days = 0

    def do_recharge(self, plan_amount: int) -> None:
        """
        Docstring for do_recharge
        
        :param self: object of class Recharge
        :param plan_amount: Amount of plan opted by user
        :type plan_amount: int
        """
        if plan_amount in Recharge.plans:
            self.balance = plan_amount
            self.validity_days = Recharge.plans[plan_amount]

            logging.info("Recharge successful for amount %s", plan_amount)

        else:
            logging.error("Invalid plan amount selected!")

    def check_validity(self) -> None:
        """
        Docstring for check_validity
        
        :param self: object of class Recharge
        """
        if self.validity_days == 0:
            logging.error("Recharge expired.")

        elif self.validity_days < 2:
            logging.warning("Recharge soon, validity almost over.")
        logging.info("Validity days remaining: %s", self.validity_days)

    def show_balance(self) -> int:
        """
        Docstring for show_balance
        
        :param self: object of class Recharge
        :return: Description
        :rtype: int
        """
        return self.balance

    @classmethod
    def add_new_plan(cls, price: int, validity: int) -> None:
        """
        Docstring for add_new_plan
        :param cls: Recharge
        :param price: New plan price
        :type price: int
        :param validity: New plan validity
        :type validity: int
        """
        cls.plans[price] = validity
        logging.info("New plan added: %s amount for %s days", price, validity)
        
        
r1 = Recharge("1234412312", "Anusha")

r1.do_recharge(300)
logging.info("Balance: %s", r1.show_balance())

r1.check_validity()
Recharge.add_new_plan(799, 120)