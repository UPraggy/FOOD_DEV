import CRUD_data as cd 
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

        def create(file_path_origin, file_path_destination):
            cd.insert_data(file_path_origin, file_path_destination)

        def select(file_path_origin, field_src):
            cd.select_data(file_path_origin, field_src)

        def update(file_path_origin, file_path_destination, field_src):
            cd.update_data(file_path_origin, file_path_destination, field_src)

        def delete(file_path_origin, file_path_destination, field_src):
            cd.delete_data(file_path_origin, file_path_destination, field_src)

class Client:
    def __init__(self, name, address, phone_number, payment, email):
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.payment = payment
        self.email = email

    def create(file_path_origin, file_path_destination):
        cd.insert_data(file_path_origin, file_path_destination)
            
    def select(file_path_origin, field_src):
        cd.select_data(file_path_origin, field_src)

    def update(file_path_origin, file_path_destination, field_src):
        cd.update_data(file_path_origin, file_path_destination, field_src)

    def delete(file_path_origin, file_path_destination, field_src):
        cd.delete_data(file_path_origin, file_path_destination, field_src)
        
class Chat:
    def __init__(self, name_employee, name_client, order_number):
        self.name_employee = name_employee
        self.name_client = name_client
        self.order_number = order_number
