# Sumary
- **[Introduction](#introduction)**
- **[Initial declarations and imports](#initial-declarations-and-imports)**
- **[loading_funcs_client, product, order](#loading_funcs_client-product-order)**
- **[load_rm](#load_rm)**
- **[setzoom](#setzoom)**
- **[zoom_scale](#zoom_scale)**
- **[loading_funcs_about](#loading_funcs_about)**
- **[loading_funcs_main](#loading_funcs_main)**
- **[switch_page](#switch_page)**   
- **[switch_main](#switch_main)** 
- **[functionalties](#functionalties)** 




# Introduction
This module has been divided into modules for each function.
> The explanation will be objective or detailed according to the complexity.

# Initial declarations and imports
Initially the program imports:
- rm responsible for operations with Orders, Customers and Products in the graphic interface, and data capture in the same
- QtCore responsible for website operations in the graphical interface


```python
from utils.INTERFACE_FUNCIONALITIES import rm
from PyQt5 import QtCore
from numpy import isin
```


# Create_DF
This module is responsible for creating the files in excel, according to the standard of columns defined by class in the **typeclass** variable, naming the file according to **name_file**, saving in the address **address_file**
```python
def create_DF(type_class, address_file, name_file):
```
# Loading_funcs_client, product, order
Module responsible for initializing the buttons of each Class in addition to changing the side menu (lm - left menu).

# Load_rm
According to the called operation (clicked button) it initializes the class and calls the initial function.
**Note:** the "initial run" check is used to initialize the buttons of each operation only once, the ```if``` is being called because of a bug when initializing the buttons more than once. buttons

# setzoom
Controls the variable responsible for zooming in the web page

# zoom_scale
Responsible for zooming on the web page

# loading_funcs_about
Responsible for web page settings


# loading_funcs_main
Responsible for loading the functions of each Class

# switch_page
Responsible for loading pages

# switch_main
Responsible for switching the page to the home menu

# Functionalties
Responsible for initializing the side menu buttons (lm - left menu)






**THIS PROGRAM WAS MADE BY**:<br>
**Rafael Moreira Ramos de Rezende** 

 [![image](https://user-images.githubusercontent.com/100146657/159492505-d6134d9b-7d19-43ee-9e30-72be719d69f4.png)](https://www.linkedin.com/in/rafael-moreira-ramos-de-rezende-16420b21b/)

