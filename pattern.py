class Order:
    def __init__(self, number_order, client, address, status, products, delivery_fee, value, payment_form):
        self.number_order = number_order
        self.client = client
        self.adress = address
        self.status = status
        self.products = products
        self.value = value
        self.payment_form = payment_form
        self.delivery_fee = delivery_fee
class Client:
    def __init__(self, name, address, phone_number, payment, email):
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.payment = payment
        self.email = email

class Chat:
    def __init__(self, name_employee, name_client, order_number):
        self.name_employee = name_employee
        self.name_client = name_client
        self.order_number = order_number
