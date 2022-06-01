# Sumary
- **[Introduction](#introduction)**
- **[Initial declarations and imports](#initial-declarations-and-imports)**
- **[Switch_page](#switch_page)**
- **[CLASSES FOR CLIENT - RMC_FUNCTIONS](#classes-for-client---rmc-functions)**
- **[CLASSES FOR PRODUCT - RMP_FUNCTIONS](#classes-for-product---rmp-functions)**
- **[CLASSES FOR ORDER - RMO_FUNCTIONS](#classes-for-order---rmo-functions)**



# Introduction
This module has been divided into classes for each function and class.
> The explanation will be objective or detailed according to the complexity.

# Initial declarations and imports
Initially the program imports:
- template to call operations on classes
- QTreeWidgetItem for operations on TreeWidgets (data table)
- date time operations with dates
- rule operations with dates only more specific
- matplotlib.pyplot operations with graphs
- Pandas for operations with dataframe and excel files

After that, the classes are initialized.

```python
from utils import template
from PyQt5.QtWidgets import QTreeWidgetItem
import datetime as dtime 
from dateutil import rrule
import matplotlib.pyplot as plt
from pandas import concat as pd_concat

c = template.Client()
p = template.Product()
o = template.Order()
```



# Switch_page
Responsible for changing pages
```python
def switch_page(stacked, page):
```

# CLASSES FOR CLIENT - RMC_FUNCTIONS
- **[search_data](#search_data)**
- **[insert_tree_data](#insert_tree_data)**
- **[Rmc_Register](#rmc_register)**
- **[Rmc_View](#rmc_view)**
- **[Rmc_Update](#rmc_update)**
- **[Rmc_Delete](#rmc_delete)**








 
**THIS PROGRAM WAS MADE BY**:<br>
**Rafael Moreira Ramos de Rezende** 

 [![image](https://user-images.githubusercontent.com/100146657/159492505-d6134d9b-7d19-43ee-9e30-72be719d69f4.png)](https://www.linkedin.com/in/rafael-moreira-ramos-de-rezende-16420b21b/)

