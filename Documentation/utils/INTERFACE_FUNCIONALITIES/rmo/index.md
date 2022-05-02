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
- **Template** that is responsible for organizing the product's classes and functions 
- **QtWidgets** that helps in some operations that are not contained in the main interface file.
- **Datetime** and dateutil that is responsible for operations with dates and time
- **Matplotlib** is responsible for generating graphs (x,y)
- **Pandas** is responsible for dataframe operations

After the imports, the product class is initialized.
```python
from utils import template
from PyQt5 import QtWidgets
import datetime as dtime
from dateutil import rrule
import matplotlib.pyplot as plt
import pandas as pd

c = template.Client()
p = template.Product()
o = template.Order()
```
The most used function in the program is declared, responsible for setting or "changing" the current page.
```python
def switch_page(stacked, page):
        stacked.setCurrentWidget(page)
```
Filter the data and insert them in the respective TreeWidget, inside it contains operations to search in more than one field, and order columns
```python
def search_data(src_field_data, tree, data):
```
Enter all data in QTreeWidget, and filter according to selected period
```python
def insert_tree_data(data, tree):
```

# Register
This module is responsible for customer registration.
- **[Initial declaration of variables - RMOR](#initial-declaration-of-variables---rmor)**
- **[Data tratament Error - RMOR](#data-tratament-error---rmor)**
- **[Clean data - RMOR](#clean-data---rmor)**
- **[Set cad default - RMOR](#set-cad-default---rmor)**
- **[Get data client](#get-data-client)**
- **[Get data address](#get-data-address)**
- **[Get data card](#get-data-card)**
- **[RMOR Add Win](#rmor-add-win)**
- **[RMOR Add](#rmor-add)**
- **[RMOR Remove](#rmor-remove)**
- **[RMOR Add qt](#rmor-add-qt)**
- **[RMOR Remove qt](#rmor-remove-qt)**
- **[RMOR radio toggle](#rmor-radio-toggle)**
- **[RMOR Set confirm](#rmor-set-confirm)**
- **[RMOR Finish Reg](#rmor-finish-reg)**
- **[RMOR INIT](#rmor-init)**
- **[RMOR BUTTON](#rmor-button)**
- **[RMOR NEXT PAGE](#rmor-next-page)**
- **[RMOR PREVIOUS PAGE](#rmor-previous-page)**
- **[RMOR FUNCTIONS](#rmor-functions)**

## Initial declaration of variables - RMOR
```python
class Register():
    def __init__(self):
        self.data = [[],[]]
        self.data_order = [[],[],[],[],[],[],[],[],[]]
        self.data_products = []
        self.prod_qt = [0]
        self.curr_prod_qt = 0
        self.add_format = ''
        self.total_value = 0
        self.op_pay = 'CARD'
```
## Data tratament Error - RMOR
Responsible for monitoring the fields, and verifying that they were duly filled in, if they are not an error window will be triggered to indicate the problem
```python
def data_tratament_error(self, w):
```
## Clean data - RMOR
Responsible for resetting all filled fields
```python
def clean_data(self, w):
```
## Set cad default - RMOR
Responsible for filling in the fields based on the client's pre-registration
```python
def clean_data(self, w):
```
## Get data client
Responsible for getting the values of all fields filled in and storing them
```python
def get_data_client(self, w):
```
## Get data address
Responsible for getting the values of all fields filled in and storing them
```python
def get_data_add(self, w):
```
## Get data card 
Responsible for getting the values of all fields filled in and storing them
```python
def get_data_card(self, w):
```
## RMOR Add Win
Responsible for opening the product selection screen
```python
def rmor_add_win(self, w):
```
## RMOR Add
Responsible for handling errors in product selection, it also calculates product value and adds it to the treewidget, in addition to updating the vector where all selected products will be stored
```python
def rmor_add(self, w):
```
## RMOR Remove
Responsible for removing the deleted product from the vector of selected products and removing it from the treewidget, in addition to calculating the new total value
```python
def rmor_add_win(self, w):
```
## RMOR Add qt
Responsible for updating by adding 1 unit quantity of the selected product
```python
def rmor_add_win(self, w):
```
## RMOR Remove qt
Responsible for updating by removing 1 unit quantity of the selected product
```python
def rmor_add_win(self, w):
```
## RMOR radio toggle
Responsible for capturing the payment method selected by the 'radio buttons'
```python
def radio_toggle(self, w):
```
## RMOR Set confirm
Responsible for the presentation of values and request for order confirmation
```python
def set_conf_form(self, w):
```
## RMOR Finish Reg
After confirming the order, this function is responsible for processing the data and registrations in addition to resetting the variables
```python
def finish_reg(self):
```
## RMOR INIT
Home page settings
```python
def rmor_init(self, w, init):
```
First, it is directed to the registration homepage, the **next** button and the spacer is visible again, the other hidden buttons and the fonts and respective texts also return to their initial positions, in addition to resetting the treeWidget.
```python
switch_page(w.rm_stackedWidget,w.rmor)
w.rmor_btn_n.setVisible(True)
w.rmor_Spacer_btts.setVisible(True)
w.rmor_btn_b.setVisible(False)
w.rmor_btn_a.setVisible(False)
w.rmor_btn_r.setVisible(False)
w.rmpr_lb_ed.setText("SELECT THE CLIENT")
w.rmpr_lb_ed.setStyleSheet("color:#f6f6e9;\nfont: 28pt \"Fira Sans\";\n")
w.rmpr_lb_rs.setText("REGISTER SYSTEM")
w.rmor_slct_c_f2_tree.clear()
self.data[0] = c.view()
insert_tree_data(self.data[0], w.rmor_slct_c_f2_tree, 'Client')
w.rmor_slct_p_f1_tv.setText(f'TOTAL VALUE: 0')
```
Whenever the function is called, the fields will be reset and directed to the home page

```python
self.clean_data(w)
if (init == 0):
    switch_page(w.rmor_stackedWidget,w.rmor_slct_c)
    init = 1
```

## RMOR BUTTON 
Page buttons settings (BACK, NEXT, TREE PRODUCT, SEARCH, POP-UP AND PAYMENT)
```python
def rmor_btn(self, w):
```
## RMOR NEXT PAGE
Settings whenever the **Next page** button is pressed
```python
def rmor_next_step(self, w, current):
```
Change to the **Second page**, collect the data from the first, change the fonts and make the **back** button visible and the button spacer also, if no record is selected on the previous page, it does not change anything and gives an error
```python
if (current == 0):
```
Switch to the **Third page**, collect the data from the second, change the fonts, hide the spacer and make the **Remove and Add** buttons visible, reset the treeWidgets, the total value and fill in the treeWidget products
```python
elif (current == 1):
```
Switch to the **Fourth page**, collect the data from the Third, change the fonts, hide the **Remove and Add** buttons and make the spacer visible
```python
elif (current == 2):
```
Switch to **Fifth page**, collect data from fourth, change sources
```python
elif (current == 3):
```
Switch to **Sixth page**, collect Farm data, complete registration, change fonts, hide buttons, reset treeWidgets
```python
elif (current == 4):
```
## RMOR PREVIOUS PAGE
Settings whenever the **Previous page** button is pressed<br>
Change to the previous page, change the fonts and hide the button or make it visible according to the page and reset some fields and variables if necessary
```python
def rmor_back_step(self, w, current):
```

## RMOR FUNCTIONS
Responsible for initializing the button "capture" process
```python
def rmor_Functions(self, w):
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
First, it is directed to the home page, the **back** button is hidden and the fonts and respective texts also return to their initial positions.
```python
def rmcv_init(self, w):
```
## RMPV NEXT PAGE
Settings whenever the **Next page** button is pressed, change the fonts and make the **back** button visible and **Next** hidden, after that it filters through the button (OPTION) that was pressed and chooses which type of registration or graph will present
```python
def rmpv_next_step(self, w, btn):
```

## RMPV PREVIOUS PAGE
Settings whenever the **Previous page** button is pressed, switch to the **First page**, change the fonts, hide **back** button, an reset treeWidget
```python
def rmpv_back_step(self, w, current):
```

## RMPV FUNCTIONS
Responsible for initializing the button "capture" process
```python
def rmcv_Functions(self, w):
```



























# Update
This module is responsible for customer registration.
- **[Initial declaration of variables - RMPU](#initial-declaration-of-variables---rmpu)**
- **[Clean data - RMPU](#clean-data---rmpu)**
- **[Get data generic](#get-data-generic)**
- **[RMPU INIT](#rmpu-init)**
- **[RMPU BUTTON](#rmpu-button)**
- **[RMPU NEXT PAGE](#rmpu-next-page)**
- **[RMPU PREVIOUS PAGE](#rmpu-previous-page)**
- **[RMPU FUNCTIONS](#rmpu-functions)**

## Initial declaration of variables - RMPU
```python
class Update():
    def __init__(self):
        data = None
        slct_data = None
        slct_data1 = None
        current_Widget = None
        tool_tip = None #pop up with tips on the fields filled in
```

## Clean data - RMPU
Responsible for resetting all filled fields
```python
def clean_data(self, w):
```

## Get data generic
Responsible for obtaining the values of a single and/or generic field filled in and storing it.
```python
def get_data_generic(self, w, field):
```

## RMPU INIT
Home page settings
```python
def rmcu_init(self, w, init):
```
First, it is directed to the home page, the **next and back** buttons are hidden and the fonts and respective texts also return to their initial positions.
```python
switch_page(w.rm_stackedWidget,w.rmpu)
        w.rmpu_btn_b.setVisible(False)
        w.rmpu_btn_n.setVisible(False)
        w.rmpu_lb_ed.setText("SELECT A OPTION")
        w.rmpu_lb_ed.setStyleSheet("color:#f6f6e9;\nfont: 28pt \"Fira Sans\";\n")
        w.rmpu_lb_us.setText("UPDATE SYSTEM")
```
Whenever the function is called, the fields and TreeWidget will be reset and directed to the home page

```python
self.clean_data(w)
w.rmpu_f2_tree.clear()
if (init == 0):
     switch_page(w.rmpu_stackedWidget,w.rmpu_op)
     init = 1
```

## RMPU BUTTON 
Page buttons settings (SEARCH, BACK, NEXT and RESPECTIVES UPDATE OPTIONS)
```python
def rmpu_btn(self, w):
```
## RMPU NEXT PAGE
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
elif (current == 2):
```
## RMPU PREVIOUS PAGE
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
## RMPU FUNCTIONS
Responsible for initializing the button "capture" process
```python
def rmcu_Functions(self, w):
```

# Delete
This module is responsible for customer registration.
- **[Initial declaration of variables - RMPD](#initial-declaration-of-variables---rmpd)**
- **[INIT TREE WIDGET](#init-tree-widget)**
- **[Delete data](#delete-data)**
- **[RMPD INIT](#rmpd-init)**
- **[RMPD BUTTON](#rmcd-button)**
- **[RMPD NEXT PAGE](#rmpd-next-page)**
- **[RMPD FUNCTIONS](#rmpd-functions)**

## Initial declaration of variables - RMPD
```python
class Delete():
    def __init__(self):
        data = None
        slct_data = None
        slct_data1 = None
        current_Widget = None
```

## INIT TREE WIDGET
Responsible for resetting the TreeWidget and populating it again, and after change fonts
```python
def init_Tree_widget(self, w):
```
## Delete data
Responsible for deleting the selected record
```python
def delete_data(self):
```
## RMPU INIT
Home page settings
```python
def rmpd_init(self, w, init):
```
First, it is directed to the home page, hide **next** button, and the respective fonts return to their initial positions.
```python
switch_page(w.rm_stackedWidget,w.rmpd)
        w.rmpd_btn_n.setVisible(False)
        w.rmpd_lb_ds.setStyleSheet("color:#f6f6e9;\nfont: 28pt \"Fira Sans\";\n")
        w.rmpd_lb_so.setText("DELETE SYSTEM")
```
Whenever the function is called the TreeWidget will be reset and directed to the home page.
```python
w.rmpd_f_tree.clear()
        self.init_Tree_widget(w)
        if (init == 0):
            switch_page(w.rmpd_stackedWidget,w.rmpd_slct)
            init = 1
```

## RMPD BUTTON 
Page buttons settings (SEARCH and NEXT)
```python
def rmpd_btn(self, w):
```
## RMPD NEXT PAGE
Settings whenever the **Next Page** button is pressed, before it checks if any records have been selected for right after switching to change fonts and hide the button.
```python
def rmpd_next_step(self, w):
```

## RMPD FUNCTIONS
Responsible for initializing the button "capture" process
```python
def rmpd_Functions(self, w):
```

