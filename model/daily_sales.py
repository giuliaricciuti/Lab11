from dataclasses import dataclass
from datetime import datetime


@dataclass
class DailySale:
    Retailer_code: int
    Product_number: int
    Date: datetime

    def __hash__(self):
        return hash((self.Retailer_code, self.Product_number, self.Date))

    def __eq__(self, other):
        return self.Retailer_code == other.Retailer_code and self.Product_number == other.Product_number and self.Date == other.Date

    def __str__(self):
        return f'{self.Product_number}-{self.Retailer_code}'

