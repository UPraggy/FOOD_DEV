import pandas as pd
import  time_order as tOrder

def verify_type(file_path):
    if (file_path[3] == True):
        file_path = tOrder.current_file_src()
    else:
        month = file_path[0]
        year = file_path[1]
        file_path = tOrder.file_src(month,year)
    return file_path

def search_data(data, field_src):
    input_data = input("Input: ")
    try:
       input_data = int(input_data)
    except ValueError:
        input_data = str(input_data)
    input_data = data.loc[data[field_src] == input_data]
    return input_data

def insert_data(file_path, type_data):
    if(type_data == 'ORDER'):
        file_path = verify_type(file_path)       
    data = pd.read_excel(f'{file_path}')
    cols = data.columns
    nw_data = [x for x in range(len(cols))]
    print("Insert the dataset")
    for x in range(len(cols)):
        nw_data[x] = input(f'Insert {cols[x]}: ')
    nw_data = [tuple(nw_data)]
    nw_data = pd.DataFrame(nw_data, columns = cols)
    data = [data, nw_data]
    data = pd.concat(data)
    data = data.set_index(f'{cols[0]}')
    data.to_excel(f'{file_path}')

def select_data(file_path, type_data, field_src):
    if(type_data == 'ORDER'):
        file_path = verify_type(file_path)
        
    data = pd.read_excel(f'{file_path}')
    input_data = search_data(data, field_src)
    if(len(input_data) == 0):
        print("ERROR: Invalid Input")
    else:
        print("List of records: \n")
        print(input_data)

def update_data(file_path, type_data, field_src):
    if(type_data == 'ORDER'):
        file_path = verify_type(file_path)
        
    data = pd.read_excel(f'{file_path}')
    cols = data.columns
    input_data = search_data(data, field_src)
    if(len(input_data) == 0):
        print("ERROR: Invalid Input")
    else:
        if (len(input_data.index) > 1):
            print("There is more than one record with the parameter passed \nSelect the record to be updated:")
            print(input_data)
            input_data = int(input("Input: "))
        else:
            input_data = input_data.index
        update_col = field_src
        update_data = input("Enter the new data: ")
        new_df = pd.DataFrame({update_col : update_data}, index=[input_data[0]])
        data.update(new_df)
        data = data.set_index(f'{cols[0]}')
        data.to_excel(f'{file_path}')


def delete_data(file_path, type_data, field_src):
    if(type_data == 'ORDER'):
        file_path = verify_type(file_path)
        
    data = pd.read_excel(f'{file_path}')
    cols = data.columns
    input_data = search_data(data, field_src)
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
        data = data.set_index(f'{cols[0]}')
        data.to_excel(f'{file_path}')

