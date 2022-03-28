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

    def create(file_path, input_data):,
        try:
            cd.insert_data(file_path, 'ORDER', input_data)
            return "Sucessfull"
        except:
            return "Error"
            
    def select(file_path, field_src, input_data):
        try:
            input_data = cd.select_data(file_path, 'ORDER', field_src, input_data)
            return input_data
        except:
            return "Error"

    def update(file_path, field_src, input_data, update_data):
        try:
            input_data = select(file_path, field_src, input_data)
            cd.update_data(file_path, type_data, field_src, input_data, update_data)
            return "Sucessfull"
        except:
            return "Error"
    def delete(file_path, field_src, input_data):
        try:
        input_data = select(file_path, field_src, input_data)
        cd.delete_data(file_path, 'ORDER', field_src, input_data)
            return "Sucessfull"
        except:
            return "Error"

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
    
    def create(input_data):,
        try:
            cd.insert_data(Client.src_path(), 'CLIENT', input_data)
            return "Sucessfull"
        except:
            return "Error"
            
    def select(field_src, input_data):
        try:
            input_data = cd.select_data(Client.src_path(), 'CLIENT', field_src, input_data)
            return input_data
        except:
            return "Error"
        
    def update(field_src, input_data):
        try:
            cd.update_data(Client.src_path(), 'CLIENT', field_src, input_data)
            return "Sucessfull"
        except:
            return "Error"
    def delete(field_src, input_data):
        try:
        cd.delete_data(Client.src_path(), 'CLIENT', field_src, input_data)
            return "Sucessfull"
        except:
            return "Error"

class Product:
    def __init__(self, id_product, product, unit, measure, value):
        self.id_product = id_product
        self.product = product
        self.unit = unit
        self.measure = measure
        self.value = value
        
    def src_path():
        address_file = os.getcwd()
        address_file = address_file.split(r'utils')[0]
        address_file = address_file.replace('\\','/')
        address_file = f'{address_file}PRODUCTS/'
        file = 'PRODUCTS.xlsx'
        file = (f'{address_file}{file}')
        return file
    
    def create(input_data):,
        try:
            cd.insert_data(Product.src_path(), 'PRODUCTS', input_data)
            return "Sucessfull"
        except:
            return "Error"
            
    def select(field_src, input_data):
        try:
            input_data = cd.select_data(Product.src_path(), 'PRODUCTS', field_src, input_data)
            return input_data
        except:
            return "Error"
        
    def update(field_src, input_data):
        try:
            cd.update_data(Product.src_path(), 'PRODUCTS', field_src, input_data)
            return "Sucessfull"
        except:
            return "Error"
    def delete(field_src, input_data):
        try:
        cd.delete_data(Product.src_path(), 'PRODUCTS', field_src, input_data)
            return "Sucessfull"
        except:
            return "Error"
