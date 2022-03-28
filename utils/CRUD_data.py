import pandas as pd
import  time_order as tOrder

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

def return_amount_register(file_path, type_data, field_src, input_data):
    if(type_data == 'ORDER'):
        file_path = verify_type(file_path)
        
    data = pd.read_excel(f'{file_path}')
    cols = data.columns
    input_data = data_processing(input_data)
    input_data = search_data(data, field_src, input_data)
    return input_data, cols, data
    
    if(len(input_data) == 0):
        return (file_path, type_data, field_src, input_data, 0, 0)
    else:
        if (len(input_data.index) > 1):
            return (file_path, type_data, field_src, input_data, 1)
        else:
            return input_data.index
        
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

def update_data(file_path, type_data, field_src, input_data, update_data):
        input_data, cols, data = return_amount_register(file_path, type_data, field_src, input_data)
        update_col = field_src
        update_data = input("Enter the new data: ")
        update_data = data_processing(update_data)
        try: 
            new_df = pd.DataFrame({update_col : update_data}, index=[input_data[0]])
        except:
            new_df = pd.DataFrame({update_col : update_data}, index=[input_data])
            
        data.update(new_df)
        data = data.set_index(f'{cols[0]}')
        data.to_excel(f'{file_path}')


def delete_data(file_path, type_data, field_src, input_data, verify):

    if(len(input_data) == 0):
        print("ERROR: Invalid Input")
    else:
        if (len(input_data.index) > 1):
            print("There is more than one record with the parameter passed \nSelect the record to be deleted:")
            print(input_data)
            record = int(input("Input: "))
            data = data.drop([record])
        else:
            input_data = input_data.index
            data = data.drop([input_data[0]])
            
        if (verify == 0):
            return ("ERROR: Invalid Input")
        elif (verify == 1):
            data = data.drop([record])
        else:
            data = data.drop([input_data[0]])
            
        data = data.set_index(f'{cols[0]}')
        data.to_excel(f'{file_path}')

