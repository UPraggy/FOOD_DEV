# Sumary
- **[Introduction](#introduction)**
- **[Initial declarations and imports](#initial-declarations-and-imports)**
- **[TIME FUNCTIONS FOR ORDER](#time-functions-for-order)**
- **[CRUD FUNCTIONS](#crud-functions)**



# Introduction
This module has been divided into classes for each function and class.
> The explanation will be objective or detailed according to the complexity.

# Initial declarations and imports
Initially the program imports:
- CRUD_DATA responsible for some operations with data
- Pandas for operations with dataframe and excel files
- "sys" and "os" for some directory operations

```python
import utils.CRUD_data as cd
from pandas import DataFrame, read_excel
import sys
from os import getcwd
from os import mkdir
from os.path import realpath 
```


# TIME FUNCTIONS FOR ORDER
This module is responsible for checking if there is (file_src) the directory and excel of a certain period (month and year) if it does not exist it creates it (create_file), there is also a check for the current month (current_file_src)
```python
def file_src(address_file, month, year):

def current_file_src(address_file):

def create_file(address_file, month, year):
```

# CRUD FUNCTIONS
Module responsible for inserting data, searching, updating and deleting

## Data_processing
Responsible for converting the search or input data, so that the error does not occur when looking for the data in the dataframe (excel)
```python
def data_processing(input_data):
```

## View_data
Responsible for fetching excel data
```python
def view_data(file_path):
```

## Search_data
Responsible for fetching row or rows of excel data
```python
def search_data(data, field_src, input_data):
```

## Insert_data
Responsible for inserting a new row in excel
```python
def insert_data(file_path, input_data):
```

## Insert_data
Responsible for inserting a new row in excel
```python
def insert_data(file_path, input_data):
```

## Update_data
Responsible for updating a row in excel
```python
def update_data(data, file_path, field_up, input_data, update_data):
```

## Delete_data
Responsible for deleting a row in excel
```python
def delete_data(data, file_path, input_data):
```

 
**THIS PROGRAM WAS MADE BY**:<br>
**Rafael Moreira Ramos de Rezende** 

 [![image](https://user-images.githubusercontent.com/100146657/159492505-d6134d9b-7d19-43ee-9e30-72be719d69f4.png)](https://www.linkedin.com/in/rafael-moreira-ramos-de-rezende-16420b21b/)
