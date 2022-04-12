# Sumary
- **[Introduction](#introduction)**
- **[Initial declarations and imports](#initial-declarations-and-imports)**
- **[Class Register](#register)**
- **[Class View](#view)**
- **[Class Update](#update)**
- **[Class Delete](#delete)**


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
The most used function in the program is declared, responsible for setting or "changing" the current page.
```python
def switch_page(stacked, page):
        stacked.setCurrentWidget(page)
```
Filter the data and insert it into the respective TreeWidget
```python
def search_data(src_field_data, tree, data):
```
Insert all data into TreeWidget
```python
def insert_tree_data(data, tree):
```

# Register
This module is responsible for customer registration.
- **[Initial declaration of variables - RMPR](#initial-declaration-of-variables---rmpr)**
- **[Data tratament Error - RMPR](#data-tratament-error---rmpr)**
- **[Clean data - RMPR](#clean-data---rmpr)**
- **[Get data](#get-data)**
- **[RMPR INIT](#rmpr-init)**
- **[RMPR BUTTON](#rmpr-button)**
- **[RMPR NEXT PAGE](#rmpr-next-page)**
- **[RMPR PREVIOUS PAGE](#rmpr-previous-page)**
- **[RMPR FUNCTIONS](#rmpr-functions)**

## Initial declaration of variables - RMPR
```python
class Register():
    def __init__(self):
        data = None
```
## Data tratament Error - RMPR
Responsible for monitoring the fields, and verifying that they were duly filled in, if they are not an error window will be triggered to indicate the problem
```python
def data_tratament_error(self, w):
```
## Clean data - RMPR
Responsible for resetting all filled fields
```python
def clean_data(self, w):
```
## Get data 
Responsible for obtaining the values of all fields filled in, storing them and sending them to the "create product" function, finalizing the registration
```python
def get_data(self, w):
```
## RMPR INIT
Home page settings
```python
def rmcp_init(self, w, init):
```
First, it is directed to the initial registration page, the button **next** are visible again and the fonts and respective texts also return to their initial positions.
```python
switch_page(w.rm_stackedWidget,w.rmpr)
        w.rmpr_btn_n.setVisible(True)
        w.rmpr_lb_ed.setText("ENTER THE DATA")
        w.rmpr_lb_ed.setStyleSheet("color:#f6f6e9;\nfont: 28pt \"Fira Sans\";\n")
        w.rmpr_lb_rs.setText("REGISTER SYSTEM")
```
Whenever the function is called, the fields will be reset and directed to the home page

```python
self.clean_data(w)
        if (init == 0):
            switch_page(w.rmpr_cb_stackedWidget,w.rmpr_cb)
            init = 1
```

## RMPR BUTTON 
Page buttons settings (BACK AND NEXT)
```python
def rmpr_btn(self, w):
```
## RMPR NEXT PAGE
Settings whenever the **Next page** button is pressed, collect the data, complete the registration, change the sources and hide the buttons
```python
def rmpr_next_step(self, w, current):
```

## RMPR FUNCTIONS
Responsible for initializing the button "capture" process
```python
def rmpr_Functions(self, w):
```

# View
This module is responsible for customer registration.
- **[Initial declaration of variables](#initial-declaration-of-variables---rmpv)**
- **[RMPV BUTTON](#rmpv-button)**
- **[ANIMATED GRAPHIC](#animated-graphic)**
- **[PLACE GRAPHIC](#place-graphic)**
- **[View init - RMPV](#view-init-rmcv)**
- **[RMPV NEXT PAGE](#rmpv-next-page)**
- **[RMPV PREVIOUS PAGE](#rmpv-previous-page)**
- **[RMPV FUNCTIONS](#rmpv-functions)**

## Initial declaration of variables - RMPV
```python
class View():
    def __init__(self):
        data = None
        slct_data = None
```
## RMPV BUTTON
Back page button settings and those that generate static or animated graphics
```python
def rmpv_btn(self, w):
```
## ANIMATED GRAPHIC
Responsible for capturing selected field and generating the respective animated graph, opening an auxiliary window
```python
def animated_graphic(self, x , y, grapich_Title):
```
## PLACE GRAPHIC
Responsible for capturing selected field and generating the respective static graph
```python
def place_graphic(self, frame,  x , y, grapich_Title):
```
## View init - RMPV
Responsible for resetting the TreeWidget and populating it again
```python
def rmcv_init(self, w):
```
## RMPV BUTTON 
Page buttons settings (SEARCH)
```python
def rmcu_btn(self, w):
```
## RMPV FUNCTIONS
Responsible for initializing the button "capture" process
```python
def rmcv_Functions(self, w):
```

# Update
This module is responsible for customer registration.
- **[Initial declaration of variables - RMCU](#initial-declaration-of-variables---rmcu)**
- **[Clean data - RMCU](#clean-data---rmcu)**
- **[Get data generic](#get-data-generic)**
- **[Get data card](#get-data-card)**
- **[Get data address](#get-data-address)**
- **[RMCU INIT](#rmcu-init)**
- **[RMCU BUTTON](#rmcu-button)**
- **[RMCU NEXT PAGE](#rmcu-next-page)**
- **[RMCU PREVIOUS PAGE](#rmcu-previous-page)**
- **[RMCU FUNCTIONS](#rmcu-functions)**

## Initial declaration of variables - RMCU
```python
class Update():
    def __init__(self):
        data = None
        slct_data = None
        slct_data1 = None
        current_Widget = None
```

## Clean data - RMCU
Responsible for resetting all filled fields
```python
def clean_data(self, w):
```

## Get data generic
Responsible for obtaining the values of a single and/or generic field (Name, CPF, Telephone number and E-mail) filled in and storing it.
```python
def get_data_generic(self, w, field):
```
## Get data card
Responsible for getting the values of the filled-in address-related fields and storing it.
```python
def get_data_card(self, w):
```
## Get data address
Responsible for getting the values of the filled-in card-related fields and storing it
```python
def get_data_add(self, w):
```

## RMCU INIT
Home page settings
```python
def rmcu_init(self, w, init):
```
First, it is directed to the home page, the **next and back** buttons are hidden and the fonts and respective texts also return to their initial positions.
```python
switch_page(w.rm_stackedWidget,w.rmcu)
        w.rmcu_btn_b.setVisible(False)
        w.rmcu_btn_n.setVisible(False)
        w.rmcu_lb_ed.setText("SELECT A OPTION")
        w.rmcu_lb_ed.setStyleSheet("color:#f6f6e9;\nfont: 28pt \"Fira Sans\";\n")
        w.rmcu_lb_us.setText("UPDATE SYSTEM")
```
Whenever the function is called, the fields and TreeWidget will be reset and directed to the home page

```python
self.clean_data(w)
w.rmcu_f_tree.clear()
if (init == 0):
       switch_page(w.rmcu_stackedWidget,w.rmcu_op)
       init = 1
```

## RMCU BUTTON 
Page buttons settings (SEARCH, BACK, NEXT and RESPECTIVES UPDATE OPTIONS)
```python
def rmcu_btn(self, w):
```
## RMCU NEXT PAGE
Settings whenever the **Next page** button is pressed
```python
def rmcu_next_step(self, w, current):
```
Switch to **Second page**, change fonts and make **back and next** button visible
```python
if (current == 0):
```
Switch to the **Third page** (according to the option selected on the first page), collect the data of the selected record from the second, change the fonts and hide the buttons.
```python
elif (current == 1):
```
Before it checks if any records were selected for right after switching to the **Fourth page** and collects the information that was entered to update and change the fonts.
```python
elif (current == 2 or current == 3 or current == 4):
```
## RMCU PREVIOUS PAGE
Settings whenever the **Previous page** button is pressed
```python
def rmcu_back_step(self, w, current):
```
Switch to the **First page**, change the fonts, hide **back and next** button, an reset treeWidget
```python
if (current == 0):
```
Switch to the **Second page** and change the fonts
```python
else:
```
## RMCU FUNCTIONS
Responsible for initializing the button "capture" process
```python
def rmcu_Functions(self, w):
```
Switch to the **Third page** (according to the option selected on the first page), collect the data of the selected record from the second, change the fonts and hide the buttons.
```python
elif (current == 1):
```
Switch to **Fourth page** and collect the information that was entered to update, and change fonts.
```python
elif (current == 2 or current == 3 or current == 4):
```

# Delete
This module is responsible for customer registration.
- **[Initial declaration of variables - RMCD](#initial-declaration-of-variables---rmcd)**
- **[INIT TREE WIDGET](#init-tree-widget)**
- **[RMCD INIT](#rmcd-init)**
- **[RMCD BUTTON](#rmcd-button)**
- **[RMCD NEXT PAGE](#rmcd-next-page)**
- **[RMCD FUNCTIONS](#rmcd-functions)**

## Initial declaration of variables - RMCD
```python
class Delete():
    def __init__(self):
        data = None
        slct_data = None
        current_Widget = None
```

## INIT TREE WIDGET
Responsible for resetting the TreeWidget and populating it again, and after change fonts
```python
def init_Tree_widget(self, w):
```

## RMCU INIT
Home page settings
```python
def rmcd_init(self, w, init):
```
First, it is directed to the home page, hide **back** button, and the respective fonts return to their initial positions.
```python
switch_page(w.rm_stackedWidget,w.rmcd)
        w.rmcd_btn_n.setVisible(False)
        w.rmcd_lb_ds.setStyleSheet("color:#f6f6e9;\nfont: 28pt \"Fira Sans\";\n")
        w.rmcd_lb_so.setText("DELETE SYSTEM")
```
Whenever the function is called the TreeWidget will be reset and directed to the home page.
```python
w.rmcd_f_tree.clear()
        self.init_Tree_widget(w)
        if (init == 0):
            switch_page(w.rmcd_stackedWidget,w.rmcd_slct)
            init = 1
```

## RMCD BUTTON 
Page buttons settings (SEARCH and NEXT)
```python
def rmcd_btn(self, w):
```
## RMCD NEXT PAGE
Settings whenever the **Next Page** button is pressed, before it checks if any records have been selected for right after switching to change fonts and hide the button.
```python
def rmcu_next_step(self, w, current):
```

## RMCD FUNCTIONS
Responsible for initializing the button "capture" process
```python
def rmcd_Functions(self, w):
```

