import pandas as pd
import  utils.time_order as tOrder


def data_processing(input_data):
    try:
       input_data = int(input_data)
    except ValueError:
        input_data = str(input_data)
    return input_data
    
def verify_type(file_path):
    if (file_path[3] == True):
        file_path = tOrder.current_file_src()
    else:
        month = file_path[0]
        year = file_path[1]
        file_path = tOrder.file_src(month,year)
    return file_path

def view_data(file_path, type_data):
    if(type_data == 'ORDER'):
        file_path = verify_type(file_path)
    data = pd.read_excel(f'{file_path}')
    if(len(data) == 0):
        return("ERROR: Invalid Input")
    else:
        return data
        
def search_data(data, field_src, input_data):
    input_data = data_processing(input_data)
    input_data = data.loc[data[field_src] == input_data]
    return input_data

def insert_data(file_path, type_data, input_data):
    if(type_data == 'ORDER'):
        file_path = verify_type(file_path)
    data = pd.read_excel(f'{file_path}')
    cols = data.columns
    nw_data = [x for x in range(len(cols))]
    for x in range(len(cols)):
        input_data[x] = data_processing(input_data[x])
        nw_data[x] = input_data[x]
    nw_data = [tuple(nw_data)]
    nw_data = pd.DataFrame(nw_data, columns = cols)
    data = [data, nw_data]
    data = pd.concat(data)
    data = data.set_index(f'{cols[0]}')
    data.to_excel(f'{file_path}')

def select_data(file_path, type_data, field_src, input_data):
    if(type_data == 'ORDER'):
        file_path = verify_type(file_path)
        
    data = pd.read_excel(f'{file_path}')
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
            new_df = pd.DataFrame({update_col : update_data}, index=[input_data[0]])
        except:
            new_df = pd.DataFrame({update_col : update_data}, index=[input_data])
            
        data.update(new_df)
        data = data.set_index(f'{cols[0]}')
        data.to_excel(f'{file_path}')


def delete_data(data, file_path, input_data):
    cols = data.columns
    input_data = input_data.index
    data = data.drop([input_data[0]])   
    data = data.set_index(f'{cols[0]}')
    data.to_excel(f'{file_path}')

