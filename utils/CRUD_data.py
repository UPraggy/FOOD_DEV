import pandas as pd

def insert_data(file_path_origin, file_path_destination):
    data = pd.read_excel(f'{file_path_origin}')
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
    data.to_excel(f'{file_path_destination}')

def select_data(file_path_origin, field_src):
    data = pd.read_excel(f'{file_path_origin}')
    input_data = input("Input: ")
    try:
       int(input_data)
    except ValueError:
        str(input_data)
    input_data = data.loc[data[field_src] == input_data]
    if(len(input_data) == 0):
        print("ERROR: Invalid Input")
    else:
        print("List of records: \n")
        print(input_data)

def update_data(file_path_origin, file_path_destination, field_src):
    data = pd.read_excel(f'{file_path_origin}')
    cols = data.columns
    input_data = input("Input: ")
    try:
       int(input_data)
    except ValueError:
        str(input_data)
    input_data = data.loc[data[field_src] == input_data]
    if(len(input_data) == 0):
        print("ERROR: Invalid Input")
    elif (len(input_data.index) > 1):
        print("There is more than one record with the parameter passed \nSelect the record to be updated:")
        print(input_data)
        input_data = int(input("Input: "))
    else:
        input_data = input_data.index
    update_col = input("Choose the field to update: ")
    update_data = input("Enter the new data: ")
    new_df = pd.DataFrame({update_col : update_data}, index=[input_data[0]])
    data.update(new_df)
    data = data.set_index(f'{cols[0]}')
    data.to_excel(f'{file_path_destination}')


def delete_data(file_path_origin, file_path_destination, field_src):
    data = pd.read_excel(f'{file_path_origin}')
    cols = data.columns
    input_data = input("Input: ")
    try:
       int(input_data)
    except ValueError:
        str(input_data)
    input_data = data.loc[data[field_src] == input_data]
    if(len(input_data) == 0):
        print("ERROR: Invalid Input")
    elif (len(input_data.index) > 1):
        print("There is more than one record with the parameter passed \nSelect the record to be deleted:")
        print(input_data)
        record = int(input("Input: "))
        data = data.drop([record])
    else:
        input_data = input_data.index
        data = data.drop([input_data[0]])
    data = data.set_index(f'{cols[0]}')
    data.to_excel(f'{file_path_destination}')
    
update_data('0_PROJETOS_PORTIFOLIO/TESTE.xlsx','0_PROJETOS_PORTIFOLIO/TESTE2.xlsx','Client')

