from enum import Enum

class OrderStatus(Enum):
    CREATED = 'CREATED'
    PAYED = 'PAYED'
    COMPLETED = 'COMPLETED'
    CACELLED = 'CANCELED'

choices = [ (tag, tag.value)  for tag in OrderStatus ]