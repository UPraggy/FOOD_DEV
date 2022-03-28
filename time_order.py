from datetime import datetime
import datetime as dtime
import pandas as pd

def file_src(address_file, month, year, type_file):
    file = f'{type_file}_{month}_{year}.xlsx'
    print(f'{address_file}/{file}')
    try:
        file = pd.read_excel(f'{address_file}/{file}')
        return file
    except:
        create_file(address_file, month, year, type_file)

def current_file_src(address_file, type_file):
    date = dtime.date.today()
    date = [dtime.datetime.strftime(date, "%B"), date.year]
    file = f'{type_file}_{date[0]}_{date[1]}.xlsx'
    file = pd.read_excel(f'{address_file}/{file}')
    return file

    
def create_file(address_file, month, year, type_file):
    model = pd.read_excel('0_PROJETOS_PORTIFOLIO/FOOD_DEV/utils/Model/MODEL_ORDER.xlsx')
    file = f'{type_file}_{month}_{year}.xlsx'
    model.to_excel(f'{address_file}/{file}')
    return file


teste = current_file_src('0_PROJETOS_PORTIFOLIO/FOOD_DEV/2021', 'ORDER')
print(teste)

