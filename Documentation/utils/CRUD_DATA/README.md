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



**THIS PROGRAM WAS MADE BY**:<br>
**Rafael Moreira Ramos de Rezende** 

 [![image](https://user-images.githubusercontent.com/100146657/159492505-d6134d9b-7d19-43ee-9e30-72be719d69f4.png)](https://www.linkedin.com/in/rafael-moreira-ramos-de-rezende-16420b21b/)
