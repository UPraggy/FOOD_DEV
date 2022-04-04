from datetime import datetime
import datetime as dtime
import pandas as pd
import os

def file_src(month, year):
    file = f'ORDER_{month}_{year}.xlsx'
    address_file = os. getcwd()
    try:
        address_file = address_file.split(r'utils')[0]
        address_file = address_file.replace('\\','/')
        os.mkdir(f'{address_file}ORDERS/{year}')
        address_file = f'{address_file}ORDERS/{year}/'
    except FileExistsError:
        address_file = f'{address_file}ORDERS/{year}/'
    try:
        pd.read_excel(f'{address_file}{file}')
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
    model = pd.read_excel(f'{address_file}utils/Model/MODEL_ORDER.xlsx')
    cols = model.columns
    model = model.set_index(f'{cols[0]}')
    model.to_excel(f'{address_file}ORDERS/{year}/{file}')
    file = (f'{address_file}ORDERS/{year}/{file}')
    return file

