# Sumary
- **[Introduction](#introduction)**
- **[Initial declarations and imports](#initial-declarations-and-imports)**
- **[Class Register](#register)**


# Introduction
This module has been divided into classes for each interface function.
> The explanation of the functions will be objective or detailed according to the complexity.

# Initial declarations and imports
Initially the program imports: 
- template that is responsible for organizing the client's classes and functions 
- CRUD_DATA responsible for some operations with data 
- QtWidgets that helps in some operations that are not contained in the main interface file.

After the imports, the client class is initialized.
```python
from utils import template
from utils import CRUD_data as cd
from PyQt5 import QtWidgets
c = template.Client()
```
The most used function in the program is declared, responsible for setting or "changing" the current page.
```python
def switch_page(stacked, page):
        stacked.setCurrentWidget(page)
```

# Register
This module is responsible for customer registration.
- **[Initial declaration of variables](#initial-declaration-of-variables)**
- **[Clean data](#clean-data)**
- **[Get data page 1](#get-data-page-1)**
- **[Finish Register](#finish-register)**
- **[RMCR INIT](#rmcr-init)**
- **[RMCR BUTTON](#rmcr-button)**
- **[RMCR NEXT PAGE](#rmcr-next-page)**
- **[RMCR PREVIOUS PAGE](#rmcr-previous-page)**
- **[RMCR FUNCTIONS](#rmcr-functions)**

## Initial declaration of variables
```python
class Register():
    def __init__(self):
        data = None
```

## Clean data
Responsible for resetting all filled fields
```python
def clean_data(self, w):
```
## Get data page 1
Responsible for getting the values of all fields filled in and storing them
```python
def get_data_pg1(self, w):
```
## Finish Register
Responsible for obtaining the values of all fields filled in, storing them and sending them to the "create customer" function, finalizing the registration
```python
def finish_register(self, w):
```
## RMCR INIT
Home page settings
```python
def rmcr_init(self, w, init):
```
First, it is directed to the initial registration page, the button **next** are visible again and the fonts and respective texts also return to their initial positions.
```python
switch_page(w.rm_stackedWidget,w.rmcr)
        w.rmcr_btn_b.setVisible(True)
        w.rmcr_btn_n.setVisible(True)
        w.rmcr_lb_ed.setText("ENTER THE DATA")
        w.rmcr_lb_ed.setStyleSheet("color:#f6f6e9;\nfont: 28pt \"Fira Sans\";\n")
        w.rmcr_lb_rs.setText("REGISTER SYSTEM")
```
Whenever the function is called, the fields will be reset and directed to the home page

```python
self.clean_data(w)
        if (init == 0):
            switch_page(w.rmcr_cb_stackedWidget,w.rmcr_cb_1)
            init = 1
```

## RMCR BUTTON 
Page buttons settings (BACK AND NEXT)
```python
def rmcr_btn(self, w):
```
## RMCR NEXT PAGE
Settings whenever the **Next page** button is pressed
```python
def rmcr_next_step(self, w, current):
```
Switch to the **Second page**, collect the data from the first, change the sources and make the button **back** visible
```python
if (current == 0):
```
Switch to the **Third page**, collect the data from the second, complete the registration, change the sources and hide the buttons
```python
elif (current == 1):
```
## RMCR PREVIOUS PAGE
Settings whenever the **Previous page** button is pressed
```python
 def rmcr_back_step(self, w, current):
```
Switch to the **First page**, change the sources and hide **back** button
```python
if (current == 0):
```
## RMCR FUNCTIONS
Responsible for initializing the button "capture" process
```python
def rmcr_Functions(self, w):
```
