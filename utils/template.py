import utils.CRUD_data as cd
from pandas import DataFrame
import sys
from os import getcwd
from os import mkdir
from os.path import realpath 

def create_DF(type_class, address_file, name_file):
    if (type_class == 'Order'):
        d = ['number_order', 'client', 'address', 'status', 'products/qnt/value', 'value', 'payment_form', 'card_number', 'date']
    elif (type_class == 'Client'):
        d = ['Name', 'CPF', 'Phone Number', 'Email', 'Card Number', 'CVV', 'Expiration Date', 'Address', 'Number', 'District', 'City', 'State']
    elif (type_class == 'Product'):
        d = ['ID', 'PRODUCT', 'DESCRIPTION', 'measure', 'VALUE', 'STOCK', 'SELLS', 'PRICE']
        
    d = DataFrame(columns=d)
    cols = d.columns
    d = d.set_index(f'{cols[0]}')
    d.to_excel(f'{address_file}/{name_file}')

temp = 0
temp2 = 0
address_file = ''
try:
    temp = sys.path[0]
    temp2 = temp.split(r'AppData')
except:
    address_file = temp
    
try:
    temp = getcwd() 
    temp2 = temp.split(r'AppData')
except:
    address_file = temp 

try:
    temp = realpath(__file__) 
    temp2 = temp.split(r'AppData')
except:
    address_file = temp 

address_file = address_file.replace('\\','/')
address_file = f'{address_file}/Main_Aux_files'
address_file_c = f'{address_file}/Clients'
address_file_o = f'{address_file}/ORDERS'
address_file_p = f'{address_file}/Products'

print(f'AUX PATH {address_file}')
try:
    mkdir(f'{address_file}')   
except:
    pass  
try:
    mkdir(f'{address_file_c}')
    create_DF('Client', address_file_c, 'CLIENTS.xlsx')
except:
    pass     
try:
    mkdir(f'{address_file_o}')
    mkdir(f'{address_file_o}/Model')
    create_DF('Order', address_file_o, 'MODEL_ORDER.xlsx')
except:
    pass  
try:
    mkdir(f'{address_file_p}')
    create_DF('Product', address_file_p, 'PRODUCTS.xlsx')
except:
    pass  



class Order:
    def src_path(self, current, month = None, year = None):
        if (current == True):
            file_path = cd.current_file_src()
        else:
            file_path = cd.file_src(month,year)
        return file_path

    def create(self, input_data):
        try:
            path = self.src_path(True)
            cd.insert_data(path, input_data)
            return "Sucessfull"
        except:
            return "Error"
    def view(self, current = True, month = None, year = None):
        try:
            path = self.src_path(current, month, year)
            print(f'ORDER PATH {path}')
            input_data = cd.view_data(path)
            return input_data
        except:
            return "Error"
    def update(self, data,  field_src, input_data, update_data):
        try:
            path = self.src_path(True)
            cd.update_data(data, path, field_src, input_data, update_data)
            return "Sucessfull"
        except:
            return "Error"
    def delete(self, data, input_data):
        try:
            path = self.src_path(True)
            cd.delete_data(data, path, input_data)
            return "Sucessfull"
        except:
            return "Error"


class Client:

    def src_path(self):
        address_file = sys.path[0]
        address_file = address_file.replace('\\','/')
        address_file = f'{address_file}/Main_Aux_files/Clients/'
        file = 'CLIENTS.xlsx'
        file = (f'{address_file}{file}')
        
        return file  
    
    def create(self, input_data):
        try:
            cd.insert_data(self.src_path(), input_data)
            return "Sucessfull"
        except:
            return "Error"
    def view(self):
        try:
            input_data = cd.view_data(self.src_path())
            print(f'CLIET PATH {self.src_path()}')
            print(f'CLIENT DATA {input_data}')
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
        address_file = sys.path[0]
        address_file = address_file.split(r'utils')[0]
        address_file = address_file.replace('\\','/')
        address_file = f'{address_file}/Main_Aux_files/Products/'
        file = 'PRODUCTS.xlsx'
        file = (f'{address_file}{file}')
        return file
    
    def create(self, input_data):
        try:
            cd.insert_data(self.src_path(), input_data)
            return "Sucessfull"
        except:
            return "Error"
    def view(self):
        try:
            input_data = cd.view_data(self.src_path())
            print(f'PROD PATH {self.src_path()}')
            print(f'PROD DATA {input_data}')
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
