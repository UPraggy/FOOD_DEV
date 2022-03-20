# Summary
- **[Objective](#objective)**
- **[Entries](#entries)**
- **[List Functions](#list-functions)**
- **[Functions](#functions)**

# Objective
- The objective of this module is to perform the basic operations of adding, selecting, updating and deleting. The other functions aim to simplify and improve performance and visualization, trying to avoid repeating lines. This section has been split so that it does not have recursion.

# List Functions
- **[Insert Data](#insert-data)**
- **[Select Data](#select--data)**
- **[Update Data](#update-data)**
- **[Delete Data](#delete--data)**
- **[Verify Type](#verify-type)**
- **[Search Data](#search-data)**   

# Entries
These are the inputs used according to each function.

   ### **Type Data** 
   > Input variable that checks what type of file
   that you want to access "CLIENT" or "ORDER". Its function is to help the File_path.
   ### **File Path**
   > Input variable that receives the folder address.
    where the file is located, varying according to the Type_data. When the
    Type_data assumes "ORDER" it receives the address of the Verify_type function where the
    set of operations around directories and files. When it assumes "CLIENT"
    it doesn't need to go through the conditional structure as it already has a directory
    default, which was received.
    Obs.: When assuming the value "ORDER" the variable also has other parameters of which
    are used in the Verify_type function, the description about these entries will be in the
    Verify_Type function description.
   ### **Field Src** 
   > Input variable that receives the name of the column you want to change.
    
# Functions

## Insert Data
The structure has as entries the file_path which varies according to
the type_data which is the other input, its purpose is to insert data in the selected file.<br>
- **Entries:**<br>
   - **[Type_data](#type-data)**

   - **[File_path](#file-path)**
  
```python
def insert_data(file_path, type_data):
```

- **Operation**:
  - After setting the value of File_path, the open operation is performed
    the excel file through Pandas and storage in the Data variable
```python
def insert_data(file_path, type_data):
    if(type_data == 'ORDER'):
        file_path = verify_type(file_path)       
    data = pd.read_excel(f'{file_path}')
```
  - stored the columns in the Cols variable
```python
    cols = data.columns
```
  - Creation of an Nw_data vector that will receive the input data
    it was created to the exact size according to the columns.
```python
    nw_data = [x for x in range(len(cols))]
```
  - After creating the vector and inputting data the vector is converted
    in a tuple which is the only way to create a Data_frame
    as seen soon after
```python
    print("Insert the dataset")
    for x in range(len(cols)):
        nw_data[x] = input(f'Insert {cols[x]}: ')
    nw_data = [tuple(nw_data)]
    nw_data = pd.DataFrame(nw_data, columns = cols)
```
  - The Data variable receives as a vector it and the new dataframe for logo
    then join the data with the concatenate function into a single DataFrame
```python
    data = [data, nw_data]
    data = pd.concat(data)
```
  - Finally, the index is set for the first column of data so that
  the first column of the new DataFrame does not display the column index values
  as 0,1,2... and yes as the first column, after that the saving is done
   of the data file with all changes in excel format.
```python
    data = data.set_index(f'{cols[0]}')
    data.to_excel(f'{file_path}')
```
   

## Select  Data
The structure has as entries the file_path that varies according to
the type_data which is the other input and the Field_src, its purpose is to select data in the
selected file.<br>
- **Entries:**<br>
   - **[Type_data](#type-data)**

  - **[File_path](#file-path)**
   
  - **[Field_src](#field-src)**

```python
    def select_data(file_path, type_data, field_src):
```
- **Operation**:
  - After setting the value of File_path, the open operation is performed
    the excel file through Pandas and storage in the Data variable
```python
    if(type_data == 'ORDER'):
        file_path = verify_type(file_path)
    data = pd.read_excel(f'{file_path}')
```
  - The Search_data function is executed where the data to be searched is entered
   and returns the line the data is on, the description about these entries and the function
   will be in the description of the Search_data function.
```python
    input_data = search_data(data, field_src)
```

  - Checks through the conditional structure if any data was recovered.After the data is retrieved, the data list with the same value is printed
```python
    if(len(input_data) == 0):
        print("ERROR: Invalid Input")
    else:
        print("List of records: \n")
        print(input_data)
```



## Update Data
The structure has as entries the file_path that varies according to
the type_data which is the other input and the Field_src, its purpose is to update data in the
selected file.<br>
- **Entries:**<br>
   - **[Type_data](#type-data)**

  - **[File_path](#file-path)**
    
  - **[Field_src](#field-src)**

- **Operation**:
  - After setting the value of File_path, the open operation is performed
    the excel file through Pandas and storage in the Data variable
    
  - stored the columns in the Cols variable
```python
    cols = data.columns
```
    
  - The Search_data function is executed where the data to be searched is entered
   and returns the line the data is on, the description about these entries and the function
   will be in the description of the Search_data function.
   
  - Checks through the conditional structure if any data was recovered and then
    after checking if there is more than one data retrieved.
    
  - If there is more than one data, you will be asked to select which data to
    be updated.
    
  - The Update_data variable receives as the updated value and is directed
   a new dataframe with the index of the current data to be immediately
   modified in the dataframe containing all the data.
    
  - Finally, the index is set for the first column of data so that
   the first column of the new DataFrame does not display the column index values
   as 0,1,2... and yes as the first column, after that the saving is done
   of the data file with all changes in excel format.
   
   
   
## Delete  Data
The structure has as entries the file_path that varies according to
the type_data which is the other input and the Field_src, its purpose is to delete data in the
selected file.<br>
- **Entries:**<br>
   - **[Type_data](#type-data)**

  - **[File_path](#file-path)**
    
  - **[Field_src](#field-src)**

- **Operation**:
  - After setting the value of File_path, the open operation is performed
    the excel file through Pandas and storage in the Data variable
    
  - stored the columns in the Cols variable
```python
    cols = data.columns
```
    
  - The Search_data function is executed where the data to be searched is entered
   and returns the line the data is on, the description about these entries and the function
   will be in the description of the Search_data function.
   
  - Checks through the conditional structure if any data was recovered and then
    after checking if there is more than one data retrieved.
    
  - If there is more than one data, you will be asked to select which data to
    be deleted.
    
  - The Data variable receives a new dataframe without the deleted data that was deleted.

  - Finally, the index is set for the first column of data so that
   the first column of the new DataFrame does not display the column index values
   as 0,1,2... and yes as the first column, after that the saving is done
   of the data file with all changes in excel format.
   
   
   > END OF PAGE
   

