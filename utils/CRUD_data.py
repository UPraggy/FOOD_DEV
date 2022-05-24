from pandas import read_excel as pd_read_excel
from pandas import DataFrame as pd_DataFrame
from pandas import concat as pd_concat
import datetime as dtime
import sys


################################################
################################################
##############TIME FUNCTIONS FOR ORDER##########
#####################BELLOW#####################
################################################
def file_src(month, year):
    file = f'ORDER_{month}_{year}.xlsx'
    address_file = sys.path[0]
    address_file = address_file.replace('\\','/')
    address_file = f'{address_file}/Main_Aux_files/ORDERS/{year}/'
    try:
        pd_read_excel(f'{address_file}{file}')
        file = (f'{address_file}{file}')
        return file  
    except:
        file = create_file(address_file,month, year)
        return file

def current_file_src():
    date = dtime.date.today()
    date = [dtime.datetime.strftime(date, "%B"), date.year]
    file = file_src(date[0], date[1])
    return file

    
def create_file(address_file, month, year):
    file = f'ORDER_{month}_{year}.xlsx'
    address_file = address_file.split(r'ORDERS')[0]
    model = pd_read_excel(f'{address_file}Model/MODEL_ORDER.xlsx')
    cols = model.columns
    model = model.set_index(f'{cols[0]}')
    model.to_excel(f'{address_file}ORDERS/{year}/{file}')
    file = (f'{address_file}ORDERS/{year}/{file}')
    return file

################################################
################################################
##################CRUD FUNCTIONS################
#####################BELLOW#####################
################################################

def data_processing(input_data):
    try:
       input_data = int(input_data)
    except ValueError:
        input_data = str(input_data)
    return input_data

def view_data(file_path):
    data = pd_read_excel(f'{file_path}')
    if(len(data) == 0):
        return("ERROR: Invalid Input")
    else:
        return data
        
def search_data(data, field_src, input_data):
    input_data = data_processing(input_data)
    input_data = data.loc[data[field_src] == input_data]
    return input_data

def insert_data(file_path, input_data):
    data = pd_read_excel(f'{file_path}')
    cols = data.columns
    nw_data = [x for x in range(len(cols))]
    for x in range(len(cols)):
        input_data[x] = data_processing(input_data[x])
        nw_data[x] = input_data[x]
    nw_data = [tuple(nw_data)]
    nw_data = pd_DataFrame(nw_data, columns = cols)
    data = [data, nw_data]
    data = pd_concat(data)
    data = data.set_index(f'{cols[0]}')
    data.to_excel(f'{file_path}')

def select_data(file_path, field_src, input_data):     
    data = pd_read_excel(f'{file_path}')
    input_data = data_processing(input_data)
    input_data = search_data(data, field_src,input_data)
    if(len(input_data) == 0):
        return("ERROR: Invalid Input")
    else:
        return input_data

def update_data(data, file_path, field_up, input_data, update_data):
        update_col = field_up
        cols = data.columns
        input_data = input_data.index
        try:
            new_df = pd_DataFrame({update_col : update_data}, index=[input_data[0]])
        except:
            new_df = pd_DataFrame({update_col : update_data}, index=[input_data])
        data.update(new_df)
        data = data.set_index(f'{cols[0]}')
        data.to_excel(f'{file_path}')


def delete_data(data, file_path, input_data):
    cols = data.columns
    input_data = input_data.index
    data = data.drop([input_data[0]])   
    data = data.set_index(f'{cols[0]}')
    data.to_excel(f'{file_path}')

