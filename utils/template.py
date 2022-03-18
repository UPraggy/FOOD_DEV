import CRUD_data as cd
import os

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

        def create(file_path):
            cd.insert_data(file_path, 'ORDER')

        def select(file_path, field_src):
            cd.select_data(file_path, 'ORDER', field_src)

        def update(file_path, field_src):
            cd.update_data(file_path, 'ORDER', field_src)

        def delete(file_path, field_src):
            cd.delete_data(file_path, 'ORDER', field_src)

class Client:
    def __init__(self, name, address, phone_number, payment, email):
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.payment = payment
        self.email = email
        
    def src_path():
        address_file = os.getcwd()
        address_file = address_file.split(r'utils')[0]
        address_file = address_file.replace('\\','/')
        address_file = f'{address_file}CLIENT/'
        file = 'CLIENT.xlsx'
        file = (f'{address_file}{file}')
        return file  
    
    def create():
        cd.insert_data(Client.src_path(), 'CLIENT')
            
    def select(field_src):
        cd.select_data(Client.src_path(), 'CLIENT', field_src)

    def update(field_src):
        cd.update_data(Client.src_path(), 'CLIENT', field_src)

    def delete(field_src):
        cd.delete_data(Client.src_path(), 'CLIENT', field_src)

