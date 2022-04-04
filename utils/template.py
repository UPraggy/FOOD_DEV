import utils.CRUD_data as cd
import os

class Order:
    def create(self,file_path,  input_data):
        try:
            cd.insert_data(file_path, 'ORDER', input_data)
            return "Sucessfull"
        except:
            return "Error"
            
    def select(self, field_src, file_path, input_data):
        try:
            input_data = cd.select_data(file_path, 'ORDER', field_src, input_data)
            return input_data
        except:
            return "Error"
    def view(self, file_path):
        try:
            input_data = cd.view_data(file_path, 'ORDER')
            return input_data
        except:
            return "Error"
    def update(self, data, file_path,  field_src, input_data, update_data):
        try:
            cd.update_data(data, file_path, field_src, input_data, update_data)
            return "Sucessfull"
        except:
            return "Error"
    def delete(self, data, file_path, input_data):
        try:
            cd.delete_data(data, file_path, input_data)
            return "Sucessfull"
        except:
            return "Error"

class Client:

    def src_path(self):
        address_file = os.getcwd()
        address_file = address_file.split(r'utils')[0]
        address_file = address_file.replace('\\','/')
        try:
            address_file = address_file.replace('/FOOD_DEV/','')
            address_file = address_file.replace('/FOOD_DEV','')
            address_file = f'{address_file}/FOOD_DEV/CLIENT/'
        except:
            address_file = f'{address_file}/FOOD_DEV/CLIENT/'
        file = 'CLIENT.xlsx'
        file = (f'{address_file}{file}')
        return file  
    
    def create(self, input_data):
        try:
            cd.insert_data(self.src_path(), 'CLIENT', input_data)
            return "Sucessfull"
        except:
            return "Error"
            
    def select(self, field_src, input_data):
        try:
            input_data = cd.select_data(self.src_path(), 'CLIENT', field_src, input_data)
            return input_data
        except:
            return "Error"
    def view(self):
        try:
            print(self.src_path())
            input_data = cd.view_data(self.src_path(), 'CLIENT')
            return input_data
        except:
            return "Error"
    def update(self, data,  field_src, input_data, update_data):
        try:
            cd.update_data(data, self.src_path(), field_src, input_data, update_data)
            return "Sucessfull"
        except:
            return "Error"
    def delete(self, data, input_data):
        try:
            cd.delete_data(data, self.src_path(), input_data)
            return "Sucessfull"
        except:
            return "Error"

class Product:
        
    def src_path(self):
        address_file = os.getcwd()
        address_file = address_file.split(r'utils')[0]
        address_file = address_file.replace('\\','/')
        try:
            address_file = address_file.replace('/FOOD_DEV/','')
            address_file = address_file.replace('/FOOD_DEV','')
            address_file = f'{address_file}/FOOD_DEV/PRODUCTS/'
        except:
            address_file = f'{address_file}/FOOD_DEV/PRODUCTS/'
        file = 'PRODUCTS.xlsx'
        file = (f'{address_file}{file}')
        return file
    
    def create(self, input_data):
        try:
            cd.insert_data(self.src_path(), 'PRODUCT', input_data)
            return "Sucessfull"
        except:
            return "Error"
            
    def select(self, field_src, input_data):
        try:
            input_data = cd.select_data(self.src_path(), 'PRODUCT', field_src, input_data)
            return input_data
        except:
            return "Error"
    def view(self):
        try:
            input_data = cd.view_data(self.src_path(), 'PRODUCT')
            return input_data
        except:
            return "Error"
    def update(self, data,  field_src, input_data, update_data):
        try:
            cd.update_data(data, self.src_path(), field_src, input_data, update_data)
            return "Sucessfull"
        except:
            return "Error"
    def delete(self, data, input_data):
        try:
            cd.delete_data(data, self.src_path(), input_data)
            return "Sucessfull"
        except:
            return "Error"


