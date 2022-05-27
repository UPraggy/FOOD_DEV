import utils.CRUD_data as cd
from pandas import DataFrame, read_excel
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
    try:
        d = read_excel(f'{address_file}/{name_file}')
    except:
        d.to_excel(f'{address_file}/{name_file}')
temp = 0
temp2 = 0
address_file = ''
temp = sys.path[0]
temp2 = temp.find(r'AppData')
if (temp2 == -1):
    address_file = temp
else:
    temp = getcwd() 
    temp2 = temp.find(r'AppData')
    if (temp2 == -1):
        address_file = temp
    else:
        temp = realpath(__file__) 
        temp2 = temp.split(r'AppData')
        if (temp2 == -1):
            address_file = temp
        else:
            pass

address_file = address_file.replace('\\','/')
address_file = f'{address_file}/Main_Aux_files'
address_file_c = f'{address_file}/Clients'
address_file_o = f'{address_file}/ORDERS'
address_file_p = f'{address_file}/Products'



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
    mkdir(f'{address_file_o}/GRAPHICS')
    mkdir(f'{address_file_o}/Model')
    create_DF('Order', f'{address_file_o}/Model', 'MODEL_ORDER.xlsx')
except:
    pass
try:
    mkdir(f'{address_file_p}')
    mkdir(f'{address_file_p}/GRAPHICS')
    create_DF('Product', address_file_p, 'PRODUCTS.xlsx')
except:
    pass

#print(f"""\n
 #           _______________CURRENT PATH TEMPLATE_______________
  #                       {address_file}
   #         ______________________________\n
    #    """)  



class Order:
    def src_path(self, current, month = None, year = None):
        if (current == True):
            file_path = cd.current_file_src(address_file_o)
        else:
            file_path = cd.file_src(address_file_o, month,year)
        return file_path

    def create(self, input_data):
        try:
            path = self.src_path(True)
            cd.insert_data(path, input_data)
            return "Sucessfull"
        except:
            return "Error"
    def view(self, current = True, month = None, year = None):
            path = self.src_path(current, month, year)
            input_data = cd.view_data(path)
            return input_data
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
        file = 'CLIENTS.xlsx'
        file = (f'{address_file_c}/{file}')
        
        return file  
    
    def create(self, input_data):
        try:
            cd.insert_data(self.src_path(), input_data)
            return "Sucessfull"
        except:
            return "Error"
    def view(self):
            input_data = cd.view_data(self.src_path())
            return input_data
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
        file = 'PRODUCTS.xlsx'
        file = (f'{address_file_p}/{file}')
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
