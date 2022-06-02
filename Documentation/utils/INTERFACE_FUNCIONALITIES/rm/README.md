# Sumary
- **[Introduction](#introduction)**
- **[Initial declarations and imports](#initial-declarations-and-imports)**
- **[Switch_page](#switch_page)**
- **[CLASSES FOR CLIENT - RMC_FUNCTIONS AND SUBCLASSES](#classes-for-client---rmc-functions-and-subclasses)**
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

# CLASSES FOR CLIENT - RMC_FUNCTIONS AND SUBCLASSES
- **[Search_data](#search_data)**
- **[Insert_tree_data](#insert_tree_data)**
- **[Rmc_Register](#rmc_register)**
- **[Rmc_View](#rmc_view)**
- **[Rmc_Update](#rmc_update)**
- **[Rmc_Delete](#rmc_delete)**


## Search_data
Responsible by fetch data by a string insert in search field and insert into QTreeWidget, formating the field Address:
```python
def search_data(self, self2, src_field_data, tree):
```
## Insert_tree_data
Responsible by insert the data in QTreeWidget, formating the field Address:
```python
def insert_tree_data(self, data, tree):
```
## Rmc_Register
- **[Data_tratament_error](#data_tratament_error)**
- **[Clean_data](#clean_data)**
- **[Get_data_pg1](#get_data_pg1)**
- **[Finish_register](#finish_register)**
- **[Rmcr_init](#rmcr_init)**
- **[Rmcr_btn](#rmcr_btn)**
- **[Rmcr_next_step](#rmcr_next_step)**
- **[Rmcr_back_step](#rmcr_back_step)**
- **[Rmcr_Functions](#rmcr_Functions)**


### Data_tratament_error
Responsible by notify the client case insert the data of incorrect form
```python
def data_tratament_error(self, step, w):
```

### Clean_data
Responsible by cleaning fields
```python
def clean_data(self, w):
```

### Get_data_pg1
Responsible by  get data in the fields of first page
```python
def get_data_pg1(self, w):
```
### Finish_register
Responsible by  get data in the fields of second page and finish register
```python
def finish_register(self, w):
```
### Rmcr_init
Responsible by  initialize fields and set the main page
```python
def rmcr_init(self, w, init):
```
### Rmcr_btn
Responsible by  initialize buttons
```python
def rmcr_btn(self, w):
```
### Rmcr_next_step
Responsible for changing fonts, pages and getting data, according to the current page, when the **NEXT** button is pressed:
```python
def rmcr_next_step(self, w, current):
```
### Rmcr_back_step
Responsible for changing fonts, pages and getting data, according to the current page, when the **BACK** button is pressed
```python
def rmcr_back_step(self, w):
```
### Rmcr_Functions
Responsible for calling button function
```python
def rmcr_Functions(self, w):
```



## Rmc_View
- **[Rmcv_init](#rmcv_init)**
- **[Rmcv_btn](#rmcv_btn)**
- **[Rmcv_Functions](#rmcv_Functions)**

### Rmcv_init
Responsible by  initialize fields, get data, fill the TreeWidget and set the main page
```python
def rmcv_init(self, w, init):
```
### Rmcv_btn
Responsible by  initialize buttons
```python
def rmcv_btn(self, w):
```
### Rmcv_Functions
Responsible for calling button function
```python
def rmcv_Functions(self, w):
```

## Rmc_Update
- **[Clean_data](#clean_data)**
- **[Get_data_...](#get_data_)**
- **[Rmcu_init](#rmcu_init)**
- **[Rmcu_btn](#rmcu_btn)**
- **[Rmcu_next_step](#rmcu_next_step)**
- **[Rmcu_back_step](#rmcu_back_step)**
- **[Rmcu_Functions](#rmcu_Functions)**



### Clean_data
Responsible by cleaning fields
```python
def clean_data(self, w):
```

### Get_data_...
```get_data_generic, get_data_card and get_data_add```<br>
Responsible by  get data in the fields and update data:
```python
def get_data_...(self, w):
```
### Rmcu_init
Responsible by  initialize fields and set the main page
```python
def rmcu_init(self, w, init):
```
### Rmcu_btn
Responsible by  initialize buttons
```python
def rmcu_btn(self, w):
```
### Rmcu_next_step
Responsible for changing fonts, pages and getting data, according to the current page, when the **NEXT** button is pressed:
```python
def rmcu_next_step(self, w, current):
```
### Rmcu_back_step
Responsible for changing fonts, pages and getting data, according to the current page, when the **BACK** button is pressed
```python
def rmcu_back_step(self, w):
```
### Rmcu_Functions
Responsible for calling button function
```python
def rmcu_Functions(self, w):
```

















**THIS PROGRAM WAS MADE BY**:<br>
**Rafael Moreira Ramos de Rezende** 

 [![image](https://user-images.githubusercontent.com/100146657/159492505-d6134d9b-7d19-43ee-9e30-72be719d69f4.png)](https://www.linkedin.com/in/rafael-moreira-ramos-de-rezende-16420b21b/)

