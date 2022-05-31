# Sumary
- **[Introduction](#introduction)**
- **[Initial declarations and imports](#initial-declarations-and-imports)**
- **[Class Register](#register)**



# Introduction
This module has been divided into classes for each interface function.
> The explanation of the functions will be objective or detailed according to the complexity.

# Initial declarations and imports
Initially the program imports: 
- template that is responsible for organizing the product's classes and functions 
- CRUD_DATA responsible for some operations with data 
- QtWidgets that helps in some operations that are not contained in the main interface file.
- Matplotlib is responsible for generating graphs (x,y)

After the imports, the product class is initialized.
```python
from utils import template
from PyQt5 import QtWidgets
import matplotlib.pyplot as plt
p = template.Product()
```


# Register
This module is responsible for customer registration.
- **[RMPR INIT](#rmpr-init)**


## Initial declaration of variables - RMPR
```python
class Register():
    def __init__(self):
        data = None
```

## RMPR FUNCTIONS
Responsible for initializing the button "capture" process
```python
def rmpr_Functions(self, w):
```




**THIS PROGRAM WAS MADE BY**:<br>
**Rafael Moreira Ramos de Rezende** 

 [![image](https://user-images.githubusercontent.com/100146657/159492505-d6134d9b-7d19-43ee-9e30-72be719d69f4.png)](https://www.linkedin.com/in/rafael-moreira-ramos-de-rezende-16420b21b/)
