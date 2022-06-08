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
- **[Search_data - RMC](#search_data---rmc)**
- **[Insert_tree_data - RMC](#insert_tree_data---rmc)**
- **[Rmc_Register](#rmc_register)**
- **[Rmc_View](#rmc_view)**
- **[Rmc_Update](#rmc_update)**
- **[Rmc_Delete](#rmc_delete)**


## Search_data - RMC
Responsible by fetch data by a string insert in search field and insert into QTreeWidget, formating the field Address:
```python
def search_data(self, self2, src_field_data, tree):
```
## Insert_tree_data - RMC
Responsible by insert the data in QTreeWidget, formating the field Address:
```python
def insert_tree_data(self, data, tree):
```
## Rmc_Register
- **[Data_tratament_error - RMCR](#data_tratament_error---rmcr)**
- **[Clean_data - RMCR](#clean_data---rmcr)**
- **[Get_data_pg1 - RMCR](#get_data_pg1---rmcr)**
- **[Finish_register - RMCR](#finish_register---rmcr)**
- **[Rmcr_init](#rmcr_init)**
- **[Rmcr_btn](#rmcr_btn)**
- **[Rmcr_next_step](#rmcr_next_step)**
- **[Rmcr_back_step](#rmcr_back_step)**
- **[Rmcr_Functions](#rmcr_Functions)**


### Data_tratament_error - RMCR
Responsible by notify the client case insert the data of incorrect form
```python
def data_tratament_error(self, step, w):
```

### Clean_data - RMCR
Responsible by cleaning fields
```python
def clean_data(self, w):
```

### Get_data_pg1 - RMCR
Responsible by  get data in the fields of first page
```python
def get_data_pg1(self, w):
```
### Finish_register - RMCR
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
Responsible by  initialize TreeWidget, get data and set the main page
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
- **[Clean_data - RMCU](#clean_data---rmcu)**
- **[Get_data_... - RMCU](#get_data_---rmcu)**
- **[Rmcu_init](#rmcu_init)**
- **[Rmcu_btn](#rmcu_btn)**
- **[Rmcu_next_step](#rmcu_next_step)**
- **[Rmcu_back_step](#rmcu_back_step)**
- **[Rmcu_Functions](#rmcu_Functions)**



### Clean_data - RMCU
Responsible by cleaning fields
```python
def clean_data(self, w):
```

### Get_data_... - RMCU
```get_data_generic, get_data_card and get_data_add```<br>
Responsible by  get data in the fields and update data:
```python
def get_data_...(self, w):
```
### Rmcu_init
Responsible by  initialize TreeWidget and fields and set the main page
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

## Rmc_Delete
- **[Delete_data - RMCD](#delete_data---rmcd)**
- **[Init_Tree_widget - RMCD](#init_tree_widget---rmcd)**
- **[Rmcd_init](#rmcd_init)**
- **[Rmcd_btn](#rmcd_btn)**
- **[Rmcd_next_step](#rmcd_next_step)**
- **[Rmcd_Functions](#rmcd_Functions)**



### Delete_data - RMCD
Responsible by delete data
```python
def delete_data(self):
```
### Init_Tree_widget - RMCD
Responsible by fill the TreeWidget and change some fonts:
```python
def init_Tree_widget(self, w):
```
### Rmcd_init
Responsible by  initialize TreeWidget and set the main page
```python
def rmcd_init(self, w, init):
```
### Rmcd_btn
Responsible by  initialize buttons
```python
def rmcd_btn(self, w):
```
### Rmcd_next_step
Responsible for changing fonts, pages and getting data, according to the current page, when the **NEXT** button is pressed:
```python
def rmcd_next_step(self, w, current):
```
### Rmcd_Functions
Responsible for calling button function
```python
def rmcd_Functions(self, w):
```




# CLASSES FOR PRODUCT - RMP_FUNCTIONS
- **[Search_data - RMP](#search_data---rmp)**
- **[Insert_tree_data - RMP](#insert_tree_data---rmp)**
- **[Rmp_Register](#rmp_register)**
- **[Rmp_View](#rmp_view)**
- **[Rmp_Update](#rmp_update)**
- **[Rmp_Delete](#rmp_delete)**


## Search_data - RMP
Responsible by fetch data by a string insert in search field and insert into QTreeWidget, formating the field Address:
```python
def search_data(self, src_field_data, tree, data):
```
## Insert_tree_data - RMP
Responsible by insert the data in QTreeWidget, formating the field Address:
```python
def insert_tree_data(self, data, tree):
```
## Rmp_Register
- **[Data_tratament_error - RMPR](#data_tratament_error---rmpr)**
- **[Clean_data - RMPR](#clean_data---rmpr)**
- **[Get_data - RMPR](#get_data---rmpr)**
- **[Rmpr_init](#rmpr_init)**
- **[Rmpr_btn](#rmpr_btn)**
- **[Rmpr_next_step](#rmpr_next_step)**
- **[Rmpr_Functions](#rmpr_Functions)**


### Data_tratament_error - RMPR
Responsible by notify the client case insert the data of incorrect form
```python
def data_tratament_error(self, w):
```

### Clean_data - RMPR
Responsible by cleaning fields
```python
def clean_data(self, w):
```

### Get_data - RMPR
Responsible by get data in the fields and finish register
```python
def get_data(self, w): 
```

### Rmpr_init
Responsible by  initialize fields and set the main page
```python
def rmpr_init(self, w, init):
```
### Rmpr_btn
Responsible by  initialize buttons
```python
def rmpr_btn(self, w):
```
### Rmpr_next_step
Responsible for changing fonts, pages and getting data, according to the current page, when the **NEXT** button is pressed:
```python
def rmpr_next_step(self, w):
```
### Rmpr_Functions
Responsible for calling button function
```python
def rmpr_Functions(self, w):
```



## Rmp_View
- **[Rmpv_init](#rmpv_init)**
- **[Rmpv_btn](#rmpv_btn)**
- **[Animated_graphic - RMPV](#animated_graphic---rmpv)**
- **[Place_graphic - RMPV](#place_graphic---rmpv)**
- **[Rmpv_back_step](#rmpv_btn)**
- **[Rmpv_next_step](#rmpv_btn)**
- **[Rmpv_Functions](#rmpv_Functions)**

### Rmpv_init
Responsible by  initialize TreeWidget, get data and set the main page
```python
def rmpv_init(self, w, init):
```
### Rmpv_btn
Responsible by  initialize buttons
```python
def rmpv_btn(self, w):
```
### Animated_graphic - RMPV
Responsible for creating an animated graph, using the matplotlib library
```python
def animated_graphic(self, x , y, grapich_Title):
```
### Place_graphic - RMPV
Responsible for generate and place an graph in png, using the matplotlib library
```python
def place_graphic(self, frame,  x , y, grapich_Title):
```
### Rmpv_next_step
Responsible for changing fonts, pages and getting data, according to the current page, when the **NEXT** button is pressed:
```python
def rmpv_next_step(self, w, current):
```
### Rmpv_back_step
Responsible for changing fonts, pages and getting data, according to the current page, when the **BACK** button is pressed
```python
def rmpv_back_step(self, w):
```
### Rmpv_Functions
Responsible for calling button function
```python
def rmpv_Functions(self, w):
```

## Rmp_Update
- **[Clean_data](#clean_data)**
- **[Get_data_generic](#get_data_generic)**
- **[Rmpu_init](#rmpu_init)**
- **[Rmpu_btn](#rmpu_btn)**
- **[Rmpu_next_step](#rmpu_next_step)**
- **[Rmpu_back_step](#rmpu_back_step)**
- **[Rmpu_Functions](#rmpu_Functions)**



### Clean_data
Responsible by cleaning fields
```python
def clean_data(self, w):
```

### Get_data_generic
Responsible by get data in the fields and update data:
```python
def get_data_generic(self, w, field):
```
### Rmpu_init
Responsible by  initialize TreeWidget and fields and set the main page
```python
def rmpu_init(self, w, init):
```
### Rmpu_btn
Responsible by  initialize buttons
```python
def rmpu_btn(self, w):
```
### Rmpu_next_step
Responsible for changing fonts, pages and getting data, according to the current page, when the **NEXT** button is pressed:
```python
def rmpu_next_step(self, w, current, widget):
```
### Rmpu_back_step
Responsible for changing fonts, pages and getting data, according to the current page, when the **BACK** button is pressed
```python
def rmpu_back_step(self, w, current):
```
### Rmpu_Functions
Responsible for calling button function
```python
def rmpu_Functions(self, w):
```

## Rmp_Delete
- **[Delete_data - RMPD](#delete_data---rmpd)**
- **[Init_Tree_widget - RMPD](#init_tree_widget---rmpd)**
- **[Rmpd_init](#rmpd_init)**
- **[Rmpd_btn](#rmpd_btn)**
- **[Rmpd_next_step](#rmpd_next_step)**
- **[Rmpd_Functions](#rmpd_Functions)**



### Delete_data - RMPD
Responsible by delete data
```python
def delete_data(self):
```
### Init_Tree_widget - RMPD
Responsible by fill the TreeWidget and change some fonts:
```python
def init_Tree_widget(self, w):
```
### Rmpd_init
Responsible by  initialize TreeWidget and set the main page
```python
def rmpd_init(self, w, init):
```
### Rmpd_btn
Responsible by  initialize buttons
```python
def rmpd_btn(self, w):
```
### Rmpd_next_step
Responsible for changing fonts, pages and getting data, according to the current page, when the **NEXT** button is pressed:
```python
def rmpd_next_step(self, w, current):
```
### Rmpd_Functions
Responsible for calling button function
```python
def rmpd_Functions(self, w):
```


# CLASSES FOR ORDER - RMO_FUNCTIONS AND SUBCLASSES
- **[Search_data - RMO](#search_data---rmo)**
- **[Insert_tree_data - RMO](#insert_tree_data---rmo)**
- **[Switch_data - RMO](#switch_data---rmo)**      
- **[Rmo_add_win](#rmo_add_win)**
- **[Rmo add and remove](#rmo-add-and-remove)**
- **[Rmo add_qt and remove_qt](#rmo-add_qt-and-remove_qt)**
- **[Tree_update_data - RMO](#tree_update_data---rmo)**
- **[Rmo_Register](#rmo_register)**
- **[Rmo_View](#rmo_view)**
- **[Rmo_Update](#rmo_update)**
- **[Rmo_Delete](#rmo_delete)**


## Search_data - RMO
Responsible by fetch data by a string insert in search field and insert into QTreeWidget, formating the field Address:
```python
def search_data(self, self2, src_field_data, tree):
```
## Insert_tree_data - RMO
Responsible by insert the data in QTreeWidget, formating the field Address:
```python
def insert_tree_data(self, data, tree):
```
## Switch_data - RMO
Responsible for formatting and fetching orders according to a period of time:
```python
def switch_data(self, self2, w, date, operation = None, tree = None): 
```
### Data_tratament_error - RMO
Responsible by notify the client case insert the data of incorrect form:
```python
def data_tratament_error(self, self2, page, w, data, tree_reg = None, stack_reg = None, page_reg = None):
```
### Rmo_add_win
Responsible by show the products windown:
```python
def rmo_add_win(self,w):
```
### Rmo add and remove
Responsible by add or remove the selected product in the TreeWidget:
```python
def rmo_add(self, self2, w, tree_products, total_value_lb, operation = None):
```
### Rmo add_qt and remove_qt
Responsible by add or remove a quantity of the selected product in the TreeWidget:
```python
def rmo_add_qt(self, self2, w):
```
### Tree_update_data - RMO
Responsible for updating the QTreeWidget, the function exists because of a bug with the data:
```python
def tree_update_data(self):
```

## Rmo_Register
- **[Data_tratament_error_rmor](#data_tratament_error_rmor)**
- **[Clean_data - RMOR](#clean_data---rmor)**
- **[Set_cad_default](#set_cad_default)**
- **[Get_data_... - RMOR](#get_data_...---rmor)**
- **[Radio_toggle - RMOR](#radio_toggle---rmor)**
- **[Set_conf_form - RMOR](#set_conf_form---rmor)**
- **[Finish_reg - RMOR](#finish_reg---rmor)**
- **[Rmor_init](#rmor_init)**
- **[Rmor_btn](#rmor_btn)**
- **[Rmor_next_step](#rmor_next_step)**
- **[Rmor_back_step](#rmor_back_step)**
- **[Rmor_Functions](#rmor_Functions)**


### Data_tratament_error_rmor
Responsible by notify the client case insert the data of incorrect form
```python
def data_tratament_error_rmor(self, page, w, data):
```

### Clean_data - RMOR
Responsible by cleaning fields
```python
def clean_data(self, w):
```

### Get_data_... - RMOR
```get_data_client, get_data_card and get_data_add```<br>
Responsible by get data in the fields:
```python
def get_data_...(self, w):
```
### Radio_toggle - RMOR
Responsible for getting option from "radio buttons":
```python
def radio_toggle(self, w):
```
### Set_conf_form - RMOR
Responsible for requesting confirmation from the client about the data entered:
```python
def set_conf_form(self, w):
```
### Finish_register - RMOR
Responsible by get data in the fields of second page and finish register
```python
def finish_reg(self):
```
### Rmor_init
Responsible by  initialize fields and set the main page
```python
def rmor_init(self, w, init):
```
### Rmor_btn
Responsible by  initialize buttons
```python
def rmor_btn(self, w):
```
### Rmor_next_step
Responsible for changing fonts, pages and getting data, according to the current page, when the **NEXT** button is pressed:
```python
def rmor_next_step(self, w, current):
```
### Rmor_back_step
Responsible for changing fonts, pages and getting data, according to the current page, when the **BACK** button is pressed
```python
def rmor_back_step(self, w):
```
### Rmor_Functions
Responsible for calling button function
```python
def rmor_Functions(self, w):
```



## Rmo_View
- **[Pg_date](#pg_date)**
- **[Get_date](#get_date)**
- **[Animated_graphic - RMOV](#animated_graphic---rmov)**
- **[Place_graphic - RMOV](#place_graphic---rmov)**
- **[Date_tratament - RMOV](#date_tratament---rmov)**
- **[Rmov_init](#rmov_init)**
- **[Rmov_btn](#rmov_btn)** 
- **[Rmov_back_step](#rmov_btn)**
- **[Rmov_next_step](#rmov_btn)**
- **[Rmov_Functions](#rmov_Functions)**


### Pg_date
Responsible by switch page to select date:
```python
def pg_date(self, w, page):
```
### Get_date
Responsible by get selected date:
```python
def get_date(self, w, page):
```
### Animated_graphic - RMOV
Responsible for creating an animated graph, using the matplotlib library
```python
def animated_graphic(self, x , y, grapich_Title):
```
### Place_graphic - RMOV
Responsible for generate and place an graph in png, using the matplotlib library
```python
def place_graphic(self, frame,  x , y, grapich_Title):
```
### Data_tratament - ROMOV
Responsible for getting the updated data. Obs.: this function exists because of an interface bug that takes old data:
```python
def date_tratament(self, month = None):
```
### Rmov_init   
Responsible by  initialize TreeWidget, get data and set the main page
```python
def rmpv_init(self, w, init):
```
### Rmov_btn
Responsible by  initialize buttons
```python
def rmov_btn(self, w):
```
### Rmov_next_step
Responsible for changing fonts, pages and getting data, according to the current page, when the **NEXT** button is pressed:
```python
def rmov_next_step(self, w, btn):
```
### Rmou_back_step
Responsible for changing fonts, pages and getting data, according to the current page, when the **BACK** button is pressed
```python
def rmov_back_step(self, w):
```
### Rmov_Functions
Responsible for calling button function
```python
def rmov_Functions(self, w):
```

## Rmo_Update
- **[Clean_data - RMCU](#clean_data---rmou)**
- **[Get_data - RMCU](#get_data---rmou)**
- **[Radio_toggle - RMOU](#radio_toggle---rmou)**
- **[Rmou_init](#rmou_init)**
- **[Rmou_btn](#rmou_btn)**
- **[Rmou_next_step](#rmou_next_step)**
- **[Rmou_back_step](#rmou_back_step)**
- **[Rmou_Functions](#rmou_Functions)**



### Clean_data - RMOU
Responsible by cleaning fields
```python
def clean_data(self, w):
```

### Get_data - RMOU
Responsible by  get data in the fields and update data:
```python
def get_data(self, w, field):
```
### Radio_toggle - RMOU
Responsible for getting option from "radio buttons":
```python
def radio_toggle(self, w):
```
### Rmou_init
Responsible by  initialize TreeWidget and fields and set the main page
```python
def rmou_init(self, w, init):
```
### Rmou_btn
Responsible by  initialize buttons
```python
def rmou_btn(self, w):
```
### Rmou_next_step
Responsible for changing fonts, pages and getting data, according to the current page, when the **NEXT** button is pressed:
```python
def rmou_next_step(self, w, current, widget):
```
### Rmou_back_step
Responsible for changing fonts, pages and getting data, according to the current page, when the **BACK** button is pressed
```python
def rmou_back_step(self, w, current):
```
### Rmou_Functions
Responsible for calling button function
```python
def rmou_Functions(self, w):
```

## Rmo_Delete
- **[Delete_data - RMOD](#delete_data---rmod)**
- **[Init_Tree_widget - RMOD](#init_tree_widget---rmod)**
- **[Rmod_init](#rmod_init)**
- **[Rmod_btn](#rmod_btn)**
- **[Rmod_next_step](#rmod_next_step)**
- **[Rmod_Functions](#rmod_Functions)**



### Delete_data - RMOD
Responsible by delete data
```python
def delete_data(self):
```
### Init_Tree_widget - RMOD
Responsible by fill the TreeWidget and change some fonts:
```python
def init_Tree_widget(self, w):
```
### Rmod_init
Responsible by  initialize TreeWidget and set the main page
```python
def rmod_init(self, w, init):
```
### Rmod_btn
Responsible by  initialize buttons
```python
def rmod_btn(self, w):
```
### Rmod_next_step
Responsible for changing fonts, pages and getting data, according to the current page, when the **NEXT** button is pressed:
```python
def rmod_next_step(self, w, current):
```
### Rmod_Functions
Responsible for calling button function
```python
def rmod_Functions(self, w):
```













**THIS PROGRAM WAS MADE BY**:<br>
**Rafael Moreira Ramos de Rezende** 

 [![image](https://user-images.githubusercontent.com/100146657/159492505-d6134d9b-7d19-43ee-9e30-72be719d69f4.png)](https://www.linkedin.com/in/rafael-moreira-ramos-de-rezende-16420b21b/)

