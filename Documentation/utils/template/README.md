# Sumary
- **[Introduction](#introduction)**
- **[Initial declarations and imports](#initial-declarations-and-imports)**
- **[Create_DF](#create_df)**
- **[Operations Path](#operations-path)**
- **[Classes](#classes)**



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


# Create_DF
This module is responsible for creating the files in excel, according to the standard of columns defined by class in the **typeclass** variable, naming the file according to **name_file**, saving in the address **address_file**
```python
def create_DF(type_class, address_file, name_file):
```

# Operations Path
This module is responsible for checking and searching the path where the program is, after that it checks if the folders where the excel files exist, if they don't exist, it creates and calls the **create_DF** function

```python
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

  ...
  
try:
    mkdir(f'{address_file_p}')
    mkdir(f'{address_file_p}/GRAPHICS')
    create_DF('Product', address_file_p, 'PRODUCTS.xlsx')
except:
    pass
```


# Classes
This Chapter summarizes the functions of the classes: Order, Client, Products

### Src Path
This function aims to capture the file address in excel, with differences in the Order class where it will be checked if the file refers to the current month or not and will call the respective Crud functions for directories and files.

### Create
Responsible for entering the data in the excel file, receiving the filled data as a parameter.

### View
Responsible for fetching data from an excel file.

### Update
Responsible for updating the data of a given column, receiving the data from the file, directory, the column to be updated, the row to be updated, and the new data.

### Delete
Responsible for Deleting a line, when receiving it as a parameter.






**THIS PROGRAM WAS MADE BY**:<br>
**Rafael Moreira Ramos de Rezende** 

 [![image](https://user-images.githubusercontent.com/100146657/159492505-d6134d9b-7d19-43ee-9e30-72be719d69f4.png)](https://www.linkedin.com/in/rafael-moreira-ramos-de-rezende-16420b21b/)