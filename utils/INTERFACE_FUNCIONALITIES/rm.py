from utils import template
from PyQt5.QtWidgets import QTreeWidgetItem
import datetime as dtime 
from dateutil import rrule
import matplotlib.pyplot as plt
from pandas import concat as pd_concat

c = template.Client()
p = template.Product()
o = template.Order()



def switch_page(stacked, page):
        stacked.setCurrentWidget(page)

                                                ################################################
                                                ################################################
                                                ##########CLASSES FOR CLIENT OPERATIONS#########
                                                #####################BELLOW#####################
                                                ################################################

class RMC_FUNCTIONS():
    def search_data(self, self2, src_field_data, tree):
                self2.data = c.view()
                filtered_data = self2.data['Name']
                filtered_data = self2.data.loc[filtered_data.str.contains(f'^{src_field_data}', case = False)] #search data for respective field
                data_total = filtered_data.values.tolist()
                tree.clear()
                for x in data_total:
                    processed_data = [ '' if str(y) == 'nan' else str(y) for y in x]
                    processed_data[7] = f'{processed_data[7]}, ' \
                                    f'{processed_data[8]} - '\
                                    f'{processed_data[9]}, '\
                                    f'{processed_data[10]}/'\
                                    f'{processed_data[11]}' # Address Formating
                    QTreeWidgetItem(tree, processed_data)

    def insert_tree_data(self, data, tree):
            data_total = data.values.tolist()
            for x in data_total:
                processed_data = [ '' if str(y) == 'nan' else str(y) for y in x]
                processed_data[7] = f'{processed_data[7]}, ' \
                                    f'{processed_data[8]} - '\
                                    f'{processed_data[9]}, '\
                                    f'{processed_data[10]}/'\
                                    f'{processed_data[11]}' # Address Formating
                QTreeWidgetItem(tree, processed_data)

class Rmc_Register(RMC_FUNCTIONS):
    def __init__(self):
        super().__init__()
        data = None
    
    def data_tratament_error(self, step, w):
        if (step == 'pg1'):
            field = ['NAME', 'CPF', 'PHONE NUMBER', 'EMAIL']

            for x in range(0 , len(self.data)):
                    if (x >= 4 and x <= 6):
                        pass
                    else:
                        if (self.data[x] == ''):
                            w.alert.show()
                            if (x == 2):
                                w.alert.Alert_win_f1_lb.setStyleSheet("font: 18pt \"Voga \";\n color:#f6f6e9;")
                            else:
                                w.alert.Alert_win_f1_lb.setStyleSheet("font: 25pt \"Voga \";\n color:#f6f6e9;")
                            w.alert.Alert_win_f1_lb.setText(f'The "{field[x]}" field is empty! \nPlease enter some data')
                            w.hide()
                            return 'ERROR'  

            if (self.data[3].find("@") > 3):
                pass
            else:
                w.alert.show()
                w.alert.Alert_win_f1_lb.setText(f'Please enter a valid email!')
                w.hide()
                return 'ERROR'

            for x in self.data[0]:
                try:
                    int(x)
                    w.alert.show()
                    w.alert.Alert_win_f1_lb.setText(f'The "NAME" field, \n only accepts text as input')
                    w.alert.Alert_win_f1_lb.setStyleSheet("font: 25pt \"Voga \";\n color:#f6f6e9;")
                    w.hide()
                    return 'ERROR'
                except:
                    pass

            for x in self.data[1]:
                try:
                    int(x)
                    pass
                except:
                    w.alert.show()
                    w.alert.Alert_win_f1_lb.setText(f'The "CPF" field, only\naccepts numbers as input')
                    w.alert.Alert_win_f1_lb.setStyleSheet("font: 25pt \"Voga \";\n color:#f6f6e9;")
                    w.hide()
                    return 'ERROR'
        else:
            field = ['','','','','','','','ADDRESS','NUMBER', 'DISTRICT','CITY', 'STATE']
            for x in range(7 , len(self.data)):
                if (self.data[x] == ''):
                    w.alert.show()
                    w.alert.Alert_win_f1_lb.setStyleSheet("font: 21pt \"Voga \";\n color:#f6f6e9;")
                    w.alert.Alert_win_f1_lb.setText(f'The "{field[x]}" field is empty! \nPlease enter some data')
                    w.hide()
                    return 'ERROR'
                else:
                    pass
        return 'SUCCESS'

    def clean_data(self, w):
        w.rmcr_cb_1_f1_name.setText("")
        w.rmcr_cb_1_f2_cpf.setText("")
        w.rmcr_cb_1_f2_phone.setText("")
        w.rmcr_cb_1_f3_email.setText("")
        w.rmcr_cb_1_f4_card.setText("")
        w.rmcr_cb_1_f5_cvv.setText("")
        w.rmcr_cb_1_f5_date.setText("")
        w.rmcr_cb_2_f1_add.setText("")
        w.rmcr_cb_2_f2_dist.setText("")
        w.rmcr_cb_2_f2_num.setText("")
        w.rmcr_cb_2_f3_cty.setText("")
        w.rmcr_cb_2_f3_stte.setText("")
    def get_data_pg1(self, w):
        self.data = [w.rmcr_cb_1_f1_name.text(),
                     w.rmcr_cb_1_f2_cpf.text(),
                     w.rmcr_cb_1_f2_phone.text(),
                     w.rmcr_cb_1_f3_email.text(),
                     w.rmcr_cb_1_f4_card.text(),
                     w.rmcr_cb_1_f5_cvv.text(),
                     w.rmcr_cb_1_f5_date.text()]
        return self.data_tratament_error('pg1', w)

    def finish_register(self, w):
        self.data.append(w.rmcr_cb_2_f1_add.text())
        self.data.append(w.rmcr_cb_2_f2_num.text())
        self.data.append(w.rmcr_cb_2_f2_dist.text())
        self.data.append(w.rmcr_cb_2_f3_cty.text())
        self.data.append(w.rmcr_cb_2_f3_stte.text())
        return self.data_tratament_error('pg2', w)

    #REGISTER CLIENT FUNCTIONS
    def rmcr_init(self, w, init):
        switch_page(w.rm_stackedWidget,w.rmcr)
        w.rmcr_btn_b.setVisible(False)
        w.rmcr_btn_n.setVisible(True)
        w.rmcr_lb_ed.setText("ENTER THE DATA")
        w.rmcr_lb_ed.setStyleSheet("color:#f6f6e9;\nfont: 28pt \"Fira Sans\";\n")
        w.rmcr_lb_rs.setText("REGISTER SYSTEM")
        self.clean_data(w)
        if (init == 0):
            switch_page(w.rmcr_cb_stackedWidget,w.rmcr_cb_1)
            init = 1
    def rmcr_btn(self, w):
        w.rmcr_btn_b.clicked.connect(lambda: self.rmcr_back_step(w))
        w.rmcr_btn_n.clicked.connect(lambda: self.rmcr_next_step(w, w.rmcr_cb_stackedWidget.currentIndex()))
        
    def rmcr_next_step(self, w, current):
        if (current == 0):
            get_success = self.get_data_pg1(w)
            if (get_success == 'SUCCESS'):
                w.rmcr_btn_b.setVisible(True)
                switch_page(w.rmcr_cb_stackedWidget,w.rmcr_cb_2)
                w.rmcr_lb_ed.setText("INSERT ADDRESS")
                w.rmcr_lb_rs.setText("REGISTER SYSTEM")
                w.rmcr_lb_ed.setStyleSheet("color:#f6f6e9;\nfont: 28pt \"Fira Sans\";\n")
            else:
                pass

        elif (current == 1 ):
            get_success = self.finish_register(w)
            if (get_success == "SUCCESS"):
                switch_page(w.rmcr_cb_stackedWidget,w.rmcr_cb_3)
                print(c.create(self.data))
                w.rmcr_btn_b.setVisible(False)
                w.rmcr_btn_n.setVisible(False)
                w.rmcr_lb_rs.setText("")
                w.rmcr_lb_ed.setText("REGISTER SYSTEM")
                w.rmcr_lb_ed.setStyleSheet("font: 60pt \"Voga \";  \ncolor:#f6f6e9;")
            else:
                self.data = self.data[0:7]
                pass

    def rmcr_back_step(self, w):
            switch_page(w.rmcr_cb_stackedWidget,w.rmcr_cb_1)
            w.rmcr_btn_b.setVisible(False)
            w.rmcr_lb_ed.setText("ENTER THE DATA")
            w.rmcr_lb_rs.setText("REGISTER SYSTEM")
            w.rmcr_lb_ed.setStyleSheet("color:#f6f6e9;\nfont: 28pt \"Fira Sans\";\n")
            

    #INIT FUNCTIONS
    def rmcr_Functions(self, w):
            self.rmcr_btn(w)

class Rmc_View(RMC_FUNCTIONS):
    def __init__(self):
        super().__init__()
        self.data = None
        self.slct_data = None

    def rmcv_btn(self, w):
        # SEARCH
        w.rmcv_slct_btn.clicked.connect(lambda: self.search_data(self, w.rmcv_slct_src.text(), w.rmcv_f_tree))

    def rmcv_init(self, w):
        self.data = c.view()
        try:
                if (self.data == "Error"):
                        w.alert.show()
                        w.alert.Alert_win_f1_lb.setStyleSheet("font: 28pt \"Voga \";\n color:#f6f6e9;")
                        w.alert.Alert_win_f1_lb.setText(f'No data to Show')
                        w.hide()
                if (self.data == "ERROR: Invalid Input"):
                        w.alert.show()
                        w.alert.Alert_win_f1_lb.setStyleSheet("font: 28pt \"Voga \";\n color:#f6f6e9;")
                        w.alert.Alert_win_f1_lb.setText(f'No data to Show')
                        w.hide()
        except:
            switch_page(w.rm_stackedWidget,w.rmcv)
            w.rmcv_f_tree.clear()
            self.insert_tree_data(self.data, w.rmcv_f_tree)
    #INIT FUNCTIONS
    def rmcv_Functions(self, w):
            self.rmcv_btn(w)

class Rmc_Update(RMC_FUNCTIONS):
    def __init__(self):
        super().__init__()
        self.data = None
        self.slct_data = None
        self.slct_data1 = None
        self.current_Widget = None
        self.tool_tip = None
        
    def clean_data(self, w):
        w.rmcu_gen_f1_lb.setText("")
        w.rmcu_card_f1_card.setText("")
        w.rmcu_card_f2_cvv.setText("")
        w.rmcu_card_f2_date.setText("")
        w.rmcu_add_f1_add.setText("")
        w.rmcu_add_f2_dist.setText("")
        w.rmcu_add_f2_num.setText("")
        w.rmcu_add_f3_cty.setText("")
        w.rmcu_add_f3_stte.setText("")
            
    def get_data_generic(self, w, field):
        data_up = w.rmcu_gen_f1_lb.text()  
        print(c.update(self.data, field, self.slct_data, data_up))

                     
    def get_data_card(self, w):
        data_up = [w.rmcu_card_f1_card.text(),
                     w.rmcu_card_f2_cvv.text(),
                     w.rmcu_card_f2_date.text()]
        field = ["Card Number", "CVV", "Expiration Date"]
        y = 0
        for x in data_up:
                print(c.update(self.data, field[y], self.slct_data, x))
                y += 1


    def get_data_add(self, w):
        data_up = [w.rmcu_add_f1_add.text(),
                     w.rmcu_add_f2_num.text(),
                     w.rmcu_add_f2_dist.text(),
                     w.rmcu_add_f3_cty.text(),
                     w.rmcu_add_f3_stte.text()]
        field = ["Address", "Number", "District", "City", "State"]
        y = 0
        for x in data_up:
                print(c.update(self.data, field[y], self.slct_data, x))
                y += 1

        
    #UPDATE CLIENT FUNCTIONS
    def rmcu_init(self, w, init):
        switch_page(w.rm_stackedWidget,w.rmcu)
        w.rmcu_btn_b.setVisible(False)
        w.rmcu_btn_n.setVisible(False)
        w.rmcu_lb_ed.setText("SELECT A OPTION")
        w.rmcu_lb_ed.setStyleSheet("color:#f6f6e9;\nfont: 28pt \"Fira Sans\";\n")
        w.rmcu_lb_us.setText("UPDATE SYSTEM")
        self.clean_data(w)
        w.rmcu_f_tree.clear()
        if (init == 0):
            switch_page(w.rmcu_stackedWidget,w.rmcu_op)
            init = 1


    def rmcu_btn(self, w):
            w.rmcu_btn_b.clicked.connect(lambda: self.rmcu_back_step(w, w.rmcu_stackedWidget.currentIndex()))
            w.rmcu_btn_n.clicked.connect(lambda: self.rmcu_next_step(w, w.rmcu_stackedWidget.currentIndex(),''))
            # OPTION SELECTED
            w.rmcu_f1_btn_n.clicked.connect(lambda: self.rmcu_next_step(w, w.rmcu_stackedWidget.currentIndex(),'Name'))
            w.rmcu_f1_btn_cpf.clicked.connect(lambda: self.rmcu_next_step(w, w.rmcu_stackedWidget.currentIndex(),'CPF'))
            w.rmcu_f1_btn_pn.clicked.connect(lambda: self.rmcu_next_step(w, w.rmcu_stackedWidget.currentIndex(),'Phone Number'))
            w.rmcu_f2_btn_add.clicked.connect(lambda: self.rmcu_next_step(w, w.rmcu_stackedWidget.currentIndex(),'Add'))
            w.rmcu_f2_btn_email.clicked.connect(lambda: self.rmcu_next_step(w, w.rmcu_stackedWidget.currentIndex(),'Email'))
            w.rmcu_f2_btn_pay.clicked.connect(lambda: self.rmcu_next_step(w, w.rmcu_stackedWidget.currentIndex(),'Pay'))
            # SEARCH
            w.rmcu_slct_btn.clicked.connect(lambda: self.search_data(self, w.rmcu_slct_src.text(), w.rmcu_f_tree))

    def rmcu_next_step(self, w, current, widget):
        if (current == 0):
            self.data = c.view()
            try:
                    if (self.data == "ERROR: Invalid Input"):
                        w.alert.show()
                        w.alert.Alert_win_f1_lb.setStyleSheet("font: 28pt \"Voga \";\n color:#f6f6e9;")
                        w.alert.Alert_win_f1_lb.setText(f'No data to Update')
                        w.hide()
                    if (self.data == "Error"):
                            w.alert.show()
                            w.alert.Alert_win_f1_lb.setStyleSheet("font: 28pt \"Voga \";\n color:#f6f6e9;")
                            w.alert.Alert_win_f1_lb.setText(f'No data to Update')
                            w.hide()

            except:
                switch_page(w.rmcu_stackedWidget,w.rmcu_slct)
                w.rmcu_btn_n.setVisible(True)
                w.rmcu_btn_b.setVisible(True)
                self.current_Widget = widget
                self.insert_tree_data(self.data, w.rmcu_f_tree)
                w.rmcu_lb_ed.setText("SELECT REGISTER")
                w.rmcu_lb_us.setText("UPDATE SYSTEM")
                w.rmcu_lb_ed.setStyleSheet("color:#f6f6e9;\nfont: 28pt \"Fira Sans\";\n")
        
        if (current == 1):
            if (w.rmcu_f_tree.currentItem() != None):
                self.slct_data = w.rmcu_f_tree.currentItem().text(0)
                self.slct_data = self.data.loc[self.data['Name'] == self.slct_data]
                self.slct_data1 = w.rmcu_f_tree.currentItem().text(1)
                self.slct_data = self.slct_data.loc[self.slct_data['CPF'] == int(self.slct_data1)]
                if (self.current_Widget == 'Add'):
                    switch_page(w.rmcu_stackedWidget,w.rmcu_add)
                elif (self.current_Widget == 'Pay'):
                    switch_page(w.rmcu_stackedWidget,w.rmcu_card)
                    
                else:
                    switch_page(w.rmcu_stackedWidget,w.rmcu_gen)
                    if (self.current_Widget == 'Name'):
                        self.tool_tip = 'FULL NAME'
                    elif (self.current_Widget == 'CPF'):
                        self.tool_tip = 'CPF'
                    elif (self.current_Widget == 'Phone Number'):
                        self.tool_tip = '(DDD) YOUR-NUMBER'
                    elif (self.current_Widget == 'Email'):
                        self.tool_tip = 'Example: email@email.com'

                    w.rmcu_gen_f1_lb.setToolTip(self.tool_tip)
                    w.rmcu_gen_f1_lb.setPlaceholderText(self.current_Widget)

                w.rmcu_lb_ed.setText("INSERT THE DATA")
                w.rmcu_lb_us.setText("UPDATE SYSTEM")
                w.rmcu_lb_ed.setStyleSheet("color:#f6f6e9;\nfont: 28pt \"Fira Sans\";\n") 
            else:
                w.alert.show()
                w.alert.Alert_win_f1_lb.setStyleSheet("font: 30pt \"Voga \";\n color:#f6f6e9;")
                w.alert.Alert_win_f1_lb.setText(f'Please select a \nrecord to proceed')
                w.hide()

        elif (current == 2 or current == 3 or current == 4):
            if (current == 2):
                    self.get_data_generic(w, self.current_Widget)
            elif (current == 3):
                    self.get_data_add(w)
            elif (current == 4):
                    self.get_data_card(w)
            switch_page(w.rmcu_stackedWidget,w.rmcu_sc)
            w.rmcu_btn_b.setVisible(False)
            w.rmcu_btn_n.setVisible(False)
            w.rmcu_lb_us.setText("")
            w.rmcu_lb_ed.setText("UPDATE SYSTEM")
            w.rmcu_lb_ed.setStyleSheet("font: 60pt \"Voga \";  \ncolor:#f6f6e9;")


    def rmcu_back_step(self, w, current):
        if (current == 1 ):
            w.rmcu_f_tree.clear()
            switch_page(w.rmcu_stackedWidget,w.rmcu_op)
            w.rmcu_btn_n.setVisible(False)
            w.rmcu_btn_b.setVisible(False)
            w.rmcu_lb_ed.setText("SELECT A OPTION")
            w.rmcu_lb_us.setText("UPDATE SYSTEM")
            w.rmcu_lb_ed.setStyleSheet("color:#f6f6e9;\nfont: 28pt \"Fira Sans\";\n")
        else:
            switch_page(w.rmcu_stackedWidget,w.rmcu_slct)
            w.rmcu_lb_ed.setText("SELECT REGISTER")
            w.rmcu_lb_us.setText("UPDATE SYSTEM")
            w.rmcu_lb_ed.setStyleSheet("color:#f6f6e9;\nfont: 28pt \"Fira Sans\";\n")

            

    #INIT FUNCTIONS
    def rmcu_Functions(self, w):
            self.rmcu_btn(w)


class Rmc_Delete(RMC_FUNCTIONS):
    def __init__(self):
        super().__init__()
        data = None
        slct_data = None
        current_Widget = None
            
    def delete_data(self):
        print(c.delete(self.data, self.slct_data))
        self.__init__()
    #DELETE CLIENT FUNCTIONS

    def init_Tree_widget(self, w):
            w.rmcd_btn_n.setVisible(True)
            self.insert_tree_data(self.data, w.rmcd_f_tree)
            w.rmcd_lb_so.setText("SELECT REGISTER")
            w.rmcd_lb_ds.setText("DELETE SYSTEM")
            w.rmcd_lb_so.setStyleSheet("color:#f6f6e9;\nfont: 28pt \"Fira Sans\";\n")
            
    def rmcd_init(self, w, init):
        self.data = c.view()
        try:
                if (self.data == "ERROR: Invalid Input"):
                        w.alert.show()
                        w.alert.Alert_win_f1_lb.setStyleSheet("font: 28pt \"Voga \";\n color:#f6f6e9;")
                        w.alert.Alert_win_f1_lb.setText(f'No data to Delete')
                        w.hide()
                if (self.data == "Error"):
                            w.alert.show()
                            w.alert.Alert_win_f1_lb.setStyleSheet("font: 28pt \"Voga \";\n color:#f6f6e9;")
                            w.alert.Alert_win_f1_lb.setText(f'No data to Delete')
                            w.hide()
        except:
            switch_page(w.rm_stackedWidget,w.rmcd)
            w.rmcd_btn_n.setVisible(False)
            w.rmcd_lb_ds.setStyleSheet("color:#f6f6e9;\nfont: 28pt \"Fira Sans\";\n")
            w.rmcd_lb_so.setText("DELETE SYSTEM")
            w.rmcd_f_tree.clear()
            self.init_Tree_widget(w)
            if (init == 0):
                switch_page(w.rmcd_stackedWidget,w.rmcd_slct)
                init = 1

    def rmcd_btn(self, w):
        w.rmcd_btn_n.clicked.connect(lambda: self.rmcd_next_step(w))
        # SEARCH
        w.rmcd_slct_btn.clicked.connect(lambda: self.search_data(self, w.rmcd_slct_src.text(), w.rmcd_f_tree))
    
            
    def rmcd_next_step(self, w):
            if (w.rmcd_f_tree.currentItem() != None):
                    self.data = c.view()
                    self.slct_data = w.rmcd_f_tree.currentItem().text(0)
                    self.slct_data = self.data.loc[self.data['Name'] == self.slct_data]
                    self.slct_data1 = w.rmcd_f_tree.currentItem().text(1)
                    self.slct_data = self.slct_data.loc[self.slct_data['CPF'] == int(self.slct_data1)]
                    switch_page(w.rmcd_stackedWidget,w.rmcd_sc)
                    self.delete_data()
                    w.rmcd_btn_n.setVisible(False)
                    w.rmcd_lb_ds.setText("")
                    w.rmcd_lb_so.setText("DELETE SYSTEM")
                    w.rmcd_lb_so.setStyleSheet("font: 60pt \"Voga \";  \ncolor:#f6f6e9;")
            else:
                w.alert.show()
                w.alert.Alert_win_f1_lb.setStyleSheet("font: 30pt \"Voga \";\n color:#f6f6e9;")
                w.alert.Alert_win_f1_lb.setText(f'Please select a \nrecord to proceed')
                w.hide()

    #INIT FUNCTIONS
    def rmcd_Functions(self, w):
            self.rmcd_btn(w)





                                ################################################
                                ################################################
                                #########CLASSES FOR PRODUCTS OPERATIONS########
                                #####################BELLOW#####################
                                ################################################





class RMP_FUNCTIONS():
    def search_data(self, src_field_data, tree, data):
                filtered_data = data['PRODUCT']
                filtered_data = data.loc[filtered_data.str.contains(f'^{src_field_data}', case = False)] #search data for respective field
                data_total = filtered_data.values.tolist()
                tree.clear()
                for x in data_total:
                    processed_data = [ '' if str(y) == 'nan' or str(y) == 'NaN' else str(y) for y in x]
                    QTreeWidgetItem(tree, processed_data)

    def insert_tree_data(self, data, tree):
            data_total = data.values.tolist()
            for x in data_total:
                processed_data = [ '' if str(y) == 'nan' or str(y) == 'NaN' else str(y) for y in x]
                QTreeWidgetItem(tree, processed_data)

class Rmp_Register(RMP_FUNCTIONS):
    def __init__(self):
        super().__init__()
        data = None
        
    def data_tratament_error(self, w):
            field = ['ID', 'PRODUCT NAME', 'DESCRIPTION', 'UNIT MEASURE', 'VALUE']

            for x in range(0 , len(self.data)):   
                if (self.data[x] == ''):
                    w.alert.show()
                    if (x == 1):
                        w.alert.Alert_win_f1_lb.setStyleSheet("font: 21pt \"Voga \";\n color:#f6f6e9;")
                    else:
                        w.alert.Alert_win_f1_lb.setStyleSheet("font: 24pt \"Voga \";\n color:#f6f6e9;")
                    w.alert.Alert_win_f1_lb.setText(f'The "{field[x]}" field is empty! \nPlease enter some data')
                    w.hide()
                    return 'ERROR'

            for x in self.data[0]:
                try:
                    int(x)
                    pass
                except:
                    w.alert.show()
                    w.alert.Alert_win_f1_lb.setText(f'The "ID" field, only\naccepts numbers as input')
                    w.alert.Alert_win_f1_lb.setStyleSheet("font: 25pt \"Voga \";\n color:#f6f6e9;")
                    w.hide()
                    return 'ERROR'

            for x in self.data[1]:
                try:
                    int(x)
                    w.alert.show()
                    w.alert.Alert_win_f1_lb.setText(f'The "PRODUCT NAME" field,\nonly accepts text as input')
                    w.alert.Alert_win_f1_lb.setStyleSheet("font: 25pt \"Voga \";\n color:#f6f6e9;")
                    w.hide()
                    return 'ERROR'
                except:
                    pass
            for x in self.data[3]:
                try:
                    int(x)
                    w.alert.show()
                    w.alert.Alert_win_f1_lb.setText(f'The "UNIT MEASURE" field,\n only accepts units as input \nEx: KG, UNIT, L')
                    w.alert.Alert_win_f1_lb.setStyleSheet("font: 27pt \"Voga \";\n color:#f6f6e9;")
                    w.hide()
                    return 'ERROR'
                except:
                    pass
            return 'SUCCESS'
                
    def clean_data(self, w):
        w.rmpr_cb_f1_id.setText("")
        w.rmpr_cb_f1_n.setText("")
        w.rmpr_cb_f2_desc.setText("")
        w.rmpr_cb_f3_um.setText("")
        w.rmpr_cb_f4_v.setText("")

    def get_data(self, w):
        self.data = [w.rmpr_cb_f1_id.text(),
                     w.rmpr_cb_f1_n.text(),
                     w.rmpr_cb_f2_desc.text(),
                     w.rmpr_cb_f3_um.text(),
                     w.rmpr_cb_f4_v.text(), 0,0, 0, 0]
        #print(f"DATA PRODUCTS GET {self.data}")
        return self.data_tratament_error(w)

           
        
    #REGISTER CLIENT FUNCTIONS
    def rmpr_init(self, w, init):
        switch_page(w.rm_stackedWidget,w.rmpr)
        w.rmpr_btn_n.setVisible(True)
        w.rmpr_lb_ed.setText("ENTER THE DATA")
        w.rmpr_lb_ed.setStyleSheet("color:#f6f6e9;\nfont: 28pt \"Fira Sans\";\n")
        w.rmpr_lb_rs.setText("REGISTER SYSTEM")
        self.clean_data(w)
        if (init == 0):
            switch_page(w.rmpr_cb_stackedWidget,w.rmpr_cb)
            init = 1
    def rmpr_btn(self, w):
        w.rmpr_btn_n.clicked.connect(lambda: self.rmpr_next_step(w))
        
    def rmpr_next_step(self, w):
            get_success = self.get_data(w)
            if (get_success == 'SUCCESS'):
                    print(p.create(self.data))
                    switch_page(w.rmpr_cb_stackedWidget,w.rmpr_sc)
                    w.rmpr_btn_n.setVisible(False)
                    w.rmpr_lb_rs.setText("")
                    w.rmpr_lb_ed.setText("REGISTER SYSTEM")
                    w.rmpr_lb_ed.setStyleSheet("font: 60pt \"Voga \";  \ncolor:#f6f6e9;")
            else:
                    pass
            

    #INIT FUNCTIONS
    def rmpr_Functions(self, w):
            self.rmpr_btn(w)

class Rmp_View(RMP_FUNCTIONS):
    def __init__(self):
        super().__init__()
        data = None
        slct_data = None

    def rmpv_btn(self, w):
        #BACK
        w.rmpv_btn_b.clicked.connect(lambda: self.rmpv_back_step(w))
        # SEARCH
        w.rmpv_slct_btn.clicked.connect(lambda: self.search_data(w.rmpv_slct_src.text(), w.rmpv_f2_tree, self.data))
        #OPTION
        w.rmpv_op_f1_btn_reg.clicked.connect(lambda: self.rmpv_next_step(w, 'REG'))
        w.rmpv_op_f1_btn_stock.clicked.connect(lambda: self.rmpv_next_step(w, 'STK'))
        w.rmpv_op_f2_btn_sells.clicked.connect(lambda: self.rmpv_next_step(w, 'SELL'))
        w.rmpv_op_f2_btn_price.clicked.connect(lambda: self.rmpv_next_step(w, 'PRICE'))
        #ANIMATED
        w.rmpv_stk_f1_btn_ani.clicked.connect(lambda: self.animated_graphic("PRODUCT","STOCK", "STOCK GRAPHIC"))
        w.rmpv_sells_f1_btn_ani.clicked.connect(lambda: self.animated_graphic("PRODUCT","SELLS", "SELLS GRAPHIC"))
        w.rmpv_price_f1_btn_ani.clicked.connect(lambda: self.animated_graphic("PRODUCT","VALUE", "PRICE GRAPHIC"))
        
    def animated_graphic(self, x , y, grapich_Title):
        x = self.data[x].values.tolist()
        y = self.data[y].values.tolist()
        x = [temp.replace(' ', '\n') if len(temp) > 7 else temp for temp in x]
        plt.title(grapich_Title)
        plt.bar(x, y)
        plt.show()
        
    def place_graphic(self, frame,  x , y, grapich_Title):
        x = self.data[x].values.tolist()
        y = self.data[y].values.tolist()
        x = [temp.replace(' ', '\n') if len(temp) > 10 else temp for temp in x]
        plt.title(grapich_Title)
        plt.barh(x, y)
        file = p.src_path()
        file = file.replace('PRODUCTS.xlsx','GRAPHICS')
        file = f'{file}/{grapich_Title}.png'
        plt.savefig(file)
        plt.close()
        style = f'border-image: url({file}) 0 0 0 0 stretch stretch;\nborder-radius: 5px;\n'
        frame.setStyleSheet(style)
   
        
    def rmpv_init(self, w, init):
        self.data = p.view()
        w.rmpv_lb_p.setText("PRODUCTS")
        w.rmpv_lb_p.setStyleSheet("color:rgb(0,0,0);\nfont: 80pt \"Voga \";")
        w.rmpv_btn_b.setVisible(False)
        try:
                if (self.data == "ERROR: Invalid Input"):
                        w.alert.show()
                        w.alert.Alert_win_f1_lb.setStyleSheet("font: 28pt \"Voga \";\n color:#f6f6e9;")
                        w.alert.Alert_win_f1_lb.setText(f'No data to Show')
                        w.hide()
                if (self.data == "Error"):
                            w.alert.show()
                            w.alert.Alert_win_f1_lb.setStyleSheet("font: 28pt \"Voga \";\n color:#f6f6e9;")
                            w.alert.Alert_win_f1_lb.setText(f'No data to Show')
                            w.hide()
        except:
            switch_page(w.rm_stackedWidget,w.rmpv)
                
            if (init == 0):
                switch_page(w.rmpv_stackedWidget,w.rmpv_op)
                init = 1
    def rmpv_back_step(self, w):
            switch_page(w.rmpv_stackedWidget,w.rmpv_op)
            w.rmpv_btn_b.setVisible(False)
            w.rmpv_lb_p.setText("PRODUCTS")
            w.rmpv_lb_p.setStyleSheet("color:rgb(0,0,0);\nfont: 80pt \"Voga \";")
            
    def rmpv_next_step(self, w, btn):
            print(f'DATA {self.data}')
            w.rmpv_lb_p.setText("GRAPHIC")
            w.rmpv_lb_p.setStyleSheet("color:#f6f6e9;\nfont: 60pt \"Voga \";")
            w.rmpv_btn_b.setVisible(True)
            self.data = p.view()
            if (btn == 'STK'):
                switch_page(w.rmpv_stackedWidget,w.rmpv_stock)
                self.place_graphic(w.rmpv_stk_f2_img, "PRODUCT","STOCK", "STOCK GRAPHIC")
            elif (btn == 'SELL'):
                switch_page(w.rmpv_stackedWidget,w.rmpv_sells)
                self.place_graphic(w.rmpv_sells_f2_img, "PRODUCT","SELLS", "SELLS GRAPHIC")
            elif (btn == 'PRICE'):
                switch_page(w.rmpv_stackedWidget,w.rmpv_price)
                self.place_graphic(w.rmpv_price_f2_img, "PRODUCT","VALUE", "PRICE GRAPHIC")
            else:
                w.rmpv_f2_tree.clear()
                switch_page(w.rmpv_stackedWidget,w.rmpv_src)
                self.insert_tree_data(self.data, w.rmpv_f2_tree)
                w.rmpv_lb_p.setText("PRODUCTS")
                w.rmpv_lb_p.setStyleSheet("color:rgb(0,0,0);\nfont: 80pt \"Voga \";")
    

            
    #INIT FUNCTIONS
    def rmpv_Functions(self, w):
            self.rmpv_btn(w)

class Rmp_Update(RMP_FUNCTIONS):
    def __init__(self):
        super().__init__()
        data = None
        slct_data = None
        slct_data1 = None
        current_Widget = None
        tool_tip = None
        
    def clean_data(self, w):
        w.rmpu_gen_f1_lb.setText("")

            
    def get_data_generic(self, w, field):
        data_up = w.rmpu_gen_f1_lb.text()
        print(p.update(self.data, field, self.slct_data, data_up))
        
        
    #UPDATE CLIENT FUNCTIONS
    def rmpu_init(self, w, init):
        switch_page(w.rm_stackedWidget,w.rmpu)
        w.rmpu_btn_b.setVisible(False)
        w.rmpu_btn_n.setVisible(False)
        w.rmpu_lb_ed.setText("SELECT A OPTION")
        w.rmpu_lb_ed.setStyleSheet("color:#f6f6e9;\nfont: 28pt \"Fira Sans\";\n")
        w.rmpu_lb_us.setText("UPDATE SYSTEM")
        self.clean_data(w)
        w.rmpu_f2_tree.clear()
        if (init == 0):
            switch_page(w.rmpu_stackedWidget,w.rmpu_op)
            init = 1
    def rmpu_btn(self, w):
        w.rmpu_btn_b.clicked.connect(lambda: self.rmpu_back_step(w, w.rmpu_stackedWidget.currentIndex()))
        w.rmpu_btn_n.clicked.connect(lambda: self.rmpu_next_step(w, w.rmpu_stackedWidget.currentIndex(),''))
        # OPTION SELECTED
        w.rmpu_f1_btn_id.clicked.connect(lambda: self.rmpu_next_step(w, w.rmpu_stackedWidget.currentIndex(),'ID'))
        w.rmpu_f1_btn_n.clicked.connect(lambda: self.rmpu_next_step(w, w.rmpu_stackedWidget.currentIndex(),'PRODUCT'))
        w.rmpu_f1_btn_desc.clicked.connect(lambda: self.rmpu_next_step(w, w.rmpu_stackedWidget.currentIndex(),'DESCRIPTION'))
        w.rmpu_f2_btn_um.clicked.connect(lambda: self.rmpu_next_step(w, w.rmpu_stackedWidget.currentIndex(),'measure'))
        w.rmpu_f2_btn_v.clicked.connect(lambda: self.rmpu_next_step(w, w.rmpu_stackedWidget.currentIndex(),'VALUE'))
        w.rmpu_f3_btn_stk.clicked.connect(lambda: self.rmpu_next_step(w, w.rmpu_stackedWidget.currentIndex(),'STOCK'))
        # SEARCH
        w.rmpu_slct_btn.clicked.connect(lambda: self.search_data(w.rmpu_slct_src.text(), w.rmpu_f2_tree, self.data))
        
    def rmpu_next_step(self, w, current, widget):
        if (current == 0):
            self.data = p.view()
            try:
                    if (self.data == "ERROR: Invalid Input"):
                        w.alert.show()
                        w.alert.Alert_win_f1_lb.setStyleSheet("font: 28pt \"Voga \";\n color:#f6f6e9;")
                        w.alert.Alert_win_f1_lb.setText(f'No data to Update')
                        w.hide()
                    if (self.data == "Error"):
                            w.alert.show()
                            w.alert.Alert_win_f1_lb.setStyleSheet("font: 28pt \"Voga \";\n color:#f6f6e9;")
                            w.alert.Alert_win_f1_lb.setText(f'No data to Update')
                            w.hide()
            except:
                switch_page(w.rmpu_stackedWidget,w.rmpu_slct)
                w.rmpu_btn_n.setVisible(True)
                w.rmpu_btn_b.setVisible(True)
                self.current_Widget = widget
                self.insert_tree_data(self.data, w.rmpu_f2_tree)   
                w.rmpu_lb_ed.setText("SELECT REGISTER")
                w.rmpu_lb_us.setText("UPDATE SYSTEM")
                w.rmpu_lb_ed.setStyleSheet("color:#f6f6e9;\nfont: 28pt \"Fira Sans\";\n")
        
        if (current == 1):
            if (w.rmpu_f2_tree.currentItem() != None):
                    self.slct_data = w.rmpu_f2_tree.currentItem().text(0)
                    self.slct_data = self.data.loc[self.data['ID'] == int(self.slct_data)]
                    self.slct_data1 = w.rmpu_f2_tree.currentItem().text(1)
                    self.slct_data = self.slct_data.loc[self.slct_data['PRODUCT'] == self.slct_data1]  
                    switch_page(w.rmpu_stackedWidget,w.rmpu_gen)
                    w.rmpu_gen_f1_lb.setPlaceholderText(self.current_Widget)
                    if (self.current_Widget == 'ID'):
                        self.tool_tip = 'PRODUCT ID'
                    elif (self.current_Widget == 'PRODUCT'):
                        self.tool_tip = 'PRODUCT NAME'
                    elif (self.current_Widget == 'DESCRIPTION'):
                        self.tool_tip = 'PRODUCT DESCRIPTION'
                    elif (self.current_Widget == 'measure'):
                        self.tool_tip = 'EX: KG, UNIT, L'
                    elif (self.current_Widget == 'VALUE'):
                        self.tool_tip = 'PRODUCT VALUE PER UNIT'
                    elif (self.current_Widget == 'STOCK'):
                        self.tool_tip = 'STOCK OF PRODUCTS'

                    w.rmpu_gen_f1_lb.setToolTip(self.tool_tip)
                    w.rmpu_lb_ed.setText("INSERT THE DATA")
                    w.rmpu_lb_us.setText("UPDATE SYSTEM")
                    w.rmpu_lb_ed.setStyleSheet("color:#f6f6e9;\nfont: 28pt \"Fira Sans\";\n")
            else:
                    w.alert.show()
                    w.alert.Alert_win_f1_lb.setStyleSheet("font: 30pt \"Voga \";\n color:#f6f6e9;")
                    w.alert.Alert_win_f1_lb.setText(f'Please select a \nrecord to proceed')
                    w.hide() 

        elif (current == 2):
            self.get_data_generic(w, self.current_Widget)
            switch_page(w.rmpu_stackedWidget,w.rmpu_sc)
            w.rmpu_btn_b.setVisible(False)
            w.rmpu_btn_n.setVisible(False)
            w.rmpu_lb_us.setText("")
            w.rmpu_lb_ed.setText("UPDATE SYSTEM")
            w.rmpu_lb_ed.setStyleSheet("font: 60pt \"Voga \";  \ncolor:#f6f6e9;")

    def rmpu_back_step(self, w, current):
        if (current == 1 ):
            w.rmpu_f2_tree.clear()
            switch_page(w.rmpu_stackedWidget,w.rmpu_op)
            w.rmpu_btn_n.setVisible(False)
            w.rmpu_btn_b.setVisible(False)
            w.rmpu_lb_ed.setText("SELECT A OPTION")
            w.rmpu_lb_us.setText("UPDATE SYSTEM")
            w.rmpu_lb_ed.setStyleSheet("color:#f6f6e9;\nfont: 28pt \"Fira Sans\";\n")
        else:
            switch_page(w.rmpu_stackedWidget,w.rmpu_slct)
            w.rmpu_lb_ed.setText("SELECT REGISTER")
            w.rmpu_lb_us.setText("UPDATE SYSTEM")
            w.rmpu_lb_ed.setStyleSheet("color:#f6f6e9;\nfont: 28pt \"Fira Sans\";\n")
            

    #INIT FUNCTIONS
    def rmpu_Functions(self, w):
            self.rmpu_btn(w)


class Rmp_Delete(RMP_FUNCTIONS):
    def __init__(self):
        super().__init__()
        data = None
        slct_data = None
        slct_data1 = None
        current_Widget = None
            
    def delete_data(self):
        print(p.delete(self.data, self.slct_data))
    #DELETE CLIENT FUNCTIONS

    def init_Tree_widget(self, w):
            w.rmpd_btn_n.setVisible(True)
            self.insert_tree_data(self.data, w.rmpd_f_tree)
            w.rmpd_lb_so.setText("SELECT REGISTER")
            w.rmpd_lb_ds.setText("DELETE SYSTEM")
            w.rmpd_lb_so.setStyleSheet("color:#f6f6e9;\nfont: 28pt \"Fira Sans\";\n")
            
    def rmpd_init(self, w, init):
        self.data = p.view()
        try:
                if (self.data == "ERROR: Invalid Input"):
                        w.alert.show()
                        w.alert.Alert_win_f1_lb.setStyleSheet("font: 28pt \"Voga \";\n color:#f6f6e9;")
                        w.alert.Alert_win_f1_lb.setText(f'No data to Delete')
                        w.hide()
                if (self.data == "Error"):
                            w.alert.show()
                            w.alert.Alert_win_f1_lb.setStyleSheet("font: 28pt \"Voga \";\n color:#f6f6e9;")
                            w.alert.Alert_win_f1_lb.setText(f'No data to Delete')
                            w.hide()
        except:
            switch_page(w.rm_stackedWidget,w.rmpd)
            w.rmpd_btn_n.setVisible(False)
            w.rmpd_lb_ds.setStyleSheet("color:#f6f6e9;\nfont: 28pt \"Fira Sans\";\n")
            w.rmpd_lb_so.setText("DELETE SYSTEM")
            w.rmpd_f_tree.clear()
            self.init_Tree_widget(w)
            if (init == 0):
                switch_page(w.rmpd_stackedWidget,w.rmpd_slct)
                init = 1

    def rmpd_btn(self, w):
        w.rmpd_btn_n.clicked.connect(lambda: self.rmpd_next_step(w))
        # SEARCH
        w.rmpd_slct_btn.clicked.connect(lambda: self.search_data(w.rmpd_slct_src.text(), w.rmpd_f_tree, self.data))
    
            
    def rmpd_next_step(self, w):
            if (w.rmpd_f_tree.currentItem() != None):
                    self.data = p.view()
                    self.slct_data = w.rmpd_f_tree.currentItem().text(0)
                    self.slct_data = self.data.loc[self.data['ID'] == int(self.slct_data)]
                    self.slct_data1 = w.rmpd_f_tree.currentItem().text(1)
                    self.slct_data = self.slct_data.loc[self.slct_data['PRODUCT'] == self.slct_data1]
                    switch_page(w.rmpd_stackedWidget,w.rmpd_sc)
                    self.delete_data()
                    w.rmpd_btn_n.setVisible(False)
                    w.rmpd_lb_ds.setText("")
                    w.rmpd_lb_so.setText("DELETE SYSTEM")
                    w.rmpd_lb_so.setStyleSheet("font: 60pt \"Voga \";  \ncolor:#f6f6e9;")
            else:
                    w.alert.show()
                    w.alert.Alert_win_f1_lb.setStyleSheet("font: 30pt \"Voga \";\n color:#f6f6e9;")
                    w.alert.Alert_win_f1_lb.setText(f'Please select a \nrecord to proceed')
                    w.hide()   

    #INIT FUNCTIONS
    def rmpd_Functions(self, w):
            self.rmpd_btn(w)







                                ################################################
                                ################################################
                                ##########CLASSES FOR ORDER OPERATIONS##########
                                #####################BELLOW#####################
                                ################################################







class RMO_FUNCTIONS():
    def search_data(self, src_field_data, tree, data, field_src, type_data = None, more_field = None):
                try:
                        f = data
                        data = pd_concat(f)
                except:
                    pass
                filtered_data = data[field_src]
                temp = data.loc[filtered_data.str.contains(f'^{src_field_data}', case = False)] #search data for respective field
                temp2 = ''
                for x in range(0, 2):
                                #print(f"filtered_data {temp}")
                                if (str(temp)[0:15] != 'Empty DataFrame'):
                                        pass
                                else:
                                    temp2 = data[more_field[x]]
                                    temp2 = data.loc[temp2.astype(str).str.contains(f'^{src_field_data}', case = False)]
                                    if(x == 1 and str(temp2)[0:15] == 'Empty DataFrame'):
                                        filtered_data = data
                                        break
                                    if (str(temp2)[0:15] != 'Empty DataFrame'):
                                            filtered_data = temp2
                                            break
                                if(x == 1 and (str(temp2)[0:15] == 'Empty DataFrame' or str(temp)[0:15] != 'Empty DataFrame')):
                                    filtered_data = temp
                                #print(f"OLA {filtered_data}")  
                data_total = filtered_data.values.tolist()
                tree.clear()
                if (type_data == 'Order'):
                        temp_cont = [0,8,1,2,3,4,5,7]
                        for x in data_total:
                            processed_data = [ '' if str(y) == 'nan' or str(y) == 'NaN' else str(y) for y in x]
                            temp = [processed_data[x] for x in temp_cont]
                            if (processed_data[6] == "MONEY"):
                                temp[7] = "MONEY" 
                            QTreeWidgetItem(tree, temp)
                else:
                    for x in data_total:
                        processed_data = [ '' if str(y) == 'nan' or str(y) == 'NaN' else str(y) for y in x]
                        if (type_data == 'Client'):
                            processed_data[7] = f'{processed_data[7]}, ' \
                                            f'{processed_data[8]} - '\
                                            f'{processed_data[9]}, '\
                                            f'{processed_data[10]}/'\
                                            f'{processed_data[11]}' # Address Formating
                        QTreeWidgetItem(tree, processed_data)
    
    def insert_tree_data(self, data, tree, type_data = None, start = None, end = None):
            try:
                    data_total = []
                    for j in data:
                            data_total += j.values.tolist()
                            
                    if (len(str(start.day)) == 1):
                            if (len(str(start.month)) == 1):
                                    start1 = f'{start.year}-0{start.month}-0{start.day}'
                            else:
                                    start1 = f'{start.year}-{start.month}-0{start.day}'
                    elif (len(str(start.month)) == 1):
                            start1 = f'{start.year}-0{start.month}-{start.day}'
                    else:
                            start1 = f'{start.year}-{start.month}-{start.day}'
                    if (len(str(end.day)) == 1):
                            if (len(str(end.month)) == 1):
                                    end1 = f'{end.year}-0{end.month}-0{end.day}'
                            else:
                                    end1 = f'{end.year}-{end.month}-0{end.day}'
                                    pass
                    elif (len(str(end.month)) == 1):
                            end1 = f'{end.year}-0{end.month}-{end.day}'
                    else:
                            end1 = f'{end.year}-{end.month}-{end.day}'
                    delete_data = []
                    temp = 0
                    for x in range(0, len(data_total)):
                            temp = data_total[x][8].split("-")
                            
                            if ((int(temp[2]) > end.day and int(temp[1]) == end.month) or (int(temp[2]) < start.day and int(temp[1]) == start.month)):
                                if (temp == 1):
                                       delete_data == x 
                                else:
                                        delete_data.append(x)
                    for x in range(0, len(delete_data)):
                           del data_total[(delete_data[x]-x)]
                            
            except:
                    data_total = data.values.tolist()
               
            if (type_data == 'Order'):
                        temp_cont = [0,8,1,2,3,4,5,7]
                        for x in data_total:
                            processed_data = [ '' if str(y) == 'nan' or str(y) == 'NaN' else str(y) for y in x]
                            temp = [processed_data[x] for x in temp_cont]
                            if (processed_data[6] == "MONEY"):
                                temp[7] = "MONEY"
                            QTreeWidgetItem(tree, temp)
                                    
            else:
                for x in data_total:
                    processed_data = [ '' if str(y) == 'nan' or str(y) == 'NaN' else str(y) for y in x]
                    if (type_data == 'Client'):
                        processed_data[7] = f'{processed_data[7]}, ' \
                                            f'{processed_data[8]} - '\
                                            f'{processed_data[9]}, '\
                                            f'{processed_data[10]}/'\
                                            f'{processed_data[11]}' # Address Formating
                    QTreeWidgetItem(tree, processed_data)
    
    

    def switch_data(self, self2, w, date, operation = None, tree = None): 
                    self2.data = []
                    start_date = dtime.datetime(date[0][0],date[0][1],1)
                    start_date = dtime.datetime(date[0][0],date[0][1],1)
            
                    try:
                            end_date= dtime.datetime(date[1][0],date[1][1],28)
                            end_date= dtime.datetime(date[1][0],date[1][1],29)
                            end_date= dtime.datetime(date[1][0],date[1][1],30)
                            end_date= dtime.datetime(date[1][0],date[1][1],31)#date[1][2])
                    except:
                            pass
                
                    #print (f'START DATE {start_date}  END DATE {end_date}') #DEBUG    
                    for dt in rrule.rrule(rrule.MONTHLY, dtstart=start_date, until=end_date):
                        month = f'{dtime.datetime.strftime(dt, "%B")}'
                        #print (f'MONTH {month}') #DEBUG
                        temp = o.view(False, month, int(dt.year))
                        try:
                                if (temp == "ERROR: Invalid Input"):
                                        pass
                                elif (temp == "Error"):
                                        pass
                        except:
                                self2.data.append(temp)
                    if (operation == 'GRAPH'):
                            self2.place_graphic(w.rmov_f3_img, "number_order","value", "ORDERS GRAPHIC")
                    else:
                            start_date = dtime.datetime(date[0][0],date[0][1],date[0][2])
                            if (date[1][2] > 28):
                                try:
                                    end_date= dtime.datetime(date[1][0],date[1][1],28)
                                    end_date= dtime.datetime(date[1][0],date[1][1],29)
                                    end_date= dtime.datetime(date[1][0],date[1][1],30)
                                    end_date= dtime.datetime(date[1][0],date[1][1],31)#date[1][2])
                                except:
                                    pass
                            else:
                                    end_date = dtime.datetime(date[1][0],date[1][1],date[1][2])
                            self.insert_tree_data(self.data, tree, 'Order', start_date, end_date) 
    

    def data_tratament_error(self, self2, page, w, data, tree_reg = None, stack_reg = None, page_reg = None):
                field = ['START', 'END']
                w.alert.Alert_win_f1_lb.setStyleSheet("font: 24pt \"Voga \";\n color:#f6f6e9;")
                temp = [[],[]]
                for x in range(0 , len(data)):   
                    if (data[x] == ''):
                        w.alert.show()
                        w.alert.Alert_win_f1_lb.setText(f'The "{field[x]}" field is empty! \nPlease enter some data')
                        w.hide()
                        return print("ERROR INVALID ENTER")
                    else:
                        w.alert.Alert_win_f1_lb.setStyleSheet("font: 20pt \"Voga \";\n color:#f6f6e9;")
                        w.alert.Alert_win_f1_lb.setText(f'The input data in "{field[x]}"\n field is invalid! \nPlease enter a valid data')
                        try:
                            temp[x] = [int(data[x].split("/")[y]) for y in range(0, 3)]
                            if (len(str(temp[x][0])) != 4 or (len(str(temp[x][1]))!= 2 and len(str(temp[x][1]))!= 1) or (len(str(temp[x][2])) != 2 and len(str(temp[x][2])) != 1)):
                                w.alert.show()
                                w.hide()
                                return print("ERROR INVALID ENTER")
                            elif (int(temp[x][1]) > 12 or int(temp[x][2]) > 31):
                                w.alert.show()
                                w.hide()
                                return print("ERROR INVALID INTERVAL")
                        except:
                            w.alert.show()
                            w.hide()
                            return print("ERROR INVALID ENTER")
                if (page == 'GRAPH'):
                    switch_page(w.rmov_gph_stackedWidget,w.rmov_gph_f1) #GRAPH
                    data = temp
                    self2.switch_data(self2, w, data, 'GRAPH')
                else:
                    switch_page(stack_reg, page_reg) #REG
                    data = temp
                    self2.switch_data(self2, w, data, 'REG', tree_reg)
    
    def rmo_add_win(self,w):
        w.rmor_slc_p.show()
        w.alert.Alert_win_f1_lb.setStyleSheet("font: 24pt \"Voga \";\n color:#f6f6e9;")
    
    def rmo_add(self, self2, w, tree_products, total_value_lb):
            get_error = 0
            item = w.rmor_slc_p.rmor_slct_p_f3_tree.currentItem()
            if (self2.prod_qt[self2.curr_prod_qt] < 1):
                    w.alert.show()
                    w.alert.Alert_win_f1_lb.setText(f'Please add at least one\n unit of the chosen product!')
                    get_error = 1
                    w.hide()
            else:
               for x in range(0 , len(self2.data_products)):
                    if (item.text(1) == self2.data_products[x][0]):
                        w.alert.show()
                        w.alert.Alert_win_f1_lb.setText(f'Please dont select\n the same item!')
                        get_error = 1
                        w.hide()
                    else:
                        pass
            if (get_error == 0):
                temp = []
                value_prod = self2.prod_qt[self2.curr_prod_qt] * float(item.text(4)) #PRODUCT VALUE PER QUANTITY
                value_prod = round(value_prod, 2)
                temp.append(item.text(1)) 
                temp.append(str(self2.prod_qt[self2.curr_prod_qt]))
                temp.append(str(value_prod))
                QTreeWidgetItem(tree_products, temp) #INSERT NAME PROD, QUANTITY, VALUE
                self2.data_products.append(temp)
                self2.prod_qt.append(0) 
                self2.curr_prod_qt +=  1
                self2.total_value += value_prod
                total_value_lb.setText(f'TOTAL VALUE: {self2.total_value}')
                self2.prod_qt[self2.curr_prod_qt] = 0
                w.rmor_slc_p.rmor_slct_p_f4_lb.setText(str(self2.prod_qt[self2.curr_prod_qt]))
    
            w.rmor_slc_p.hide()
    
    def rmo_remove_qt(self, self2, w):
            if (self2.prod_qt[self2.curr_prod_qt] > 0):
                self2.prod_qt[self2.curr_prod_qt] = self2.prod_qt[self2.curr_prod_qt] - 1
                w.rmor_slc_p.rmor_slct_p_f4_lb.setText(str(self2.prod_qt[self2.curr_prod_qt]))  
    
    def rmo_add_qt(self, self2, w):
            self2.prod_qt[self2.curr_prod_qt] = self2.prod_qt[self2.curr_prod_qt] + 1
            w.rmor_slc_p.rmor_slct_p_f4_lb.setText(str(self2.prod_qt[self2.curr_prod_qt]))   
    
    def rmo_remove(self, self2, w, total_value_lb):
            tree = w.rmor_slct_p_f2_tree
            item = tree.currentItem()
            if (item != None):
                tree.takeTopLevelItem(tree.indexOfTopLevelItem(item))
                self2.total_value -= float(item.text(2))
                self2.total_value = round(self2.total_value, 2)
                total_value_lb.setText(f'TOTAL: {self2.total_value}')
                if (len(self2.data_products) > 0):
                    x = 0
                    for y in range(0, len(self2.data_products)):
                        if (self2.data_products[x][0] == item.text(0)):
                            x = y
                    self2.data_products.pop(x)
                    self2.curr_prod_qt = self2.curr_prod_qt - 1
            else:
                w.alert.show()
                w.alert.Alert_win_f1_lb.setStyleSheet("font: 30pt \"Voga \";\n color:#f6f6e9;")
                w.alert.Alert_win_f1_lb.setText(f'Please select a \nproduct to proceed')
                w.hide() 


    def tree_update_data(self):
          self.data = o.view() #TO RESOLVE BUGS OF MEMORY








                    
class Rmo_Register(RMO_FUNCTIONS):
    def __init__(self):
        super().__init__()
        self.data = [[],[]]
        self.data_order = [[],[],[],[],[],[],[],[],[]]
        self.data_products = []
        self.prod_qt = [0]
        self.curr_prod_qt = 0
        self.add_format = ''
        self.total_value = 0
        self.op_pay = 'CARD'

    def data_tratament_error_rmor(self, page, w, data):
            if (page == 'pgAdd'):
                field = ['ADDRESS', 'NUMBER', 'DISTRICT', 'CITY', 'STATE']
            else:
                field = ['CARD NUMBER', 'EXPIRATION DATE', 'CVV']
            for x in range(0 , len(data)):   
                if (data[x] == ''):
                    w.alert.show()
                    if (field[x] == 'CARD NUMBER'):
                        w.alert.Alert_win_f1_lb.setStyleSheet("font: 18pt \"Voga \";\n color:#f6f6e9;")
                        w.alert.Alert_win_f1_lb.setText(f'The "{field[x]}" field is empty! \nPlease enter some data')
                    elif (field[x] == 'EXPIRATION DATE'):
                        w.alert.Alert_win_f1_lb.setStyleSheet("font: 21pt \"Voga \";\n color:#f6f6e9;")
                        w.alert.Alert_win_f1_lb.setText(f'The "{field[x]}" field\nis empty! \nPlease enter some data')
                    else:
                        w.alert.Alert_win_f1_lb.setStyleSheet("font: 24pt \"Voga \";\n color:#f6f6e9;")
                        w.alert.Alert_win_f1_lb.setText(f'The "{field[x]}" field is empty! \nPlease enter some data')
                    w.hide()
                    return 'ERROR'
            return 'SUCCESS'

    def clean_data(self, w):
        w.rmor_slct_a_f1_add.setText("")
        w.rmor_slct_a_f2_num.setText("")
        w.rmor_slct_a_f2_dist.setText("")
        w.rmor_slct_a_f3_cty.setText("")
        w.rmor_slct_a_f3_stte.setText("")
        w.rmor_slct_pay_f_f1_card.setText("")
        w.rmor_slct_pay_f_f2_ex.setText("")
        w.rmor_slct_pay_f_f2_cvv.setText("")

    def set_cad_default(self, w):
        w.rmor_slct_pay_f_f1_card.setText(w.rmor_slct_c_f2_tree.currentItem().text(4))
        w.rmor_slct_pay_f_f2_ex.setText(w.rmor_slct_c_f2_tree.currentItem().text(5))
        w.rmor_slct_pay_f_f2_cvv.setText(w.rmor_slct_c_f2_tree.currentItem().text(6))
        address = w.rmor_slct_c_f2_tree.currentItem().text(7)
        address = address.split(", ")
        w.rmor_slct_a_f1_add.setText(address[0])
        w.rmor_slct_a_f2_num.setText((address[1]).split(" - ")[0])
        w.rmor_slct_a_f2_dist.setText((address[1]).split(" - ")[1])
        w.rmor_slct_a_f3_cty.setText((address[2]).split("/")[0])
        w.rmor_slct_a_f3_stte.setText((address[2]).split("/")[1])

    def get_data_client(self, w):
        slct_data = [w.rmor_slct_c_f2_tree.currentItem().text(0)]
        slct_data.append(w.rmor_slct_c_f2_tree.currentItem().text(1))
        self.data_order[1] = slct_data
        self.set_cad_default(w)
                     
    def get_data_add(self, w):
        slct_data = [w.rmor_slct_a_f1_add.text(),
                     w.rmor_slct_a_f2_num.text(),
                     w.rmor_slct_a_f2_dist.text(),
                     w.rmor_slct_a_f3_cty.text(),
                     w.rmor_slct_a_f3_stte.text()]
        return [self.data_tratament_error_rmor('pgAdd', w, slct_data), slct_data]

    def get_data_card(self, w):
        if (self.op_pay == 'MONEY'):
            slct_data = ['MONEY']
            return ['SUCCESS', slct_data]
        else:
            slct_data = [w.rmor_slct_pay_f_f1_card.text(),
                        w.rmor_slct_pay_f_f2_ex.text(),
                        w.rmor_slct_pay_f_f2_cvv.text()]
            return [self.data_tratament_error_rmor('pgCard', w, slct_data), slct_data]
    
    #RADIO BUTTON
    def radio_toggle(self, w):
        radioButton = w.sender()
        if radioButton.isChecked():
            if (radioButton.op == 'MONEY'):
                self.op_pay = 'MONEY'
                switch_page(w.rmor_slct_pay_stackedWidget, w.rmor_slct_pay_pg2)
                w.rmor_slct_pay_pg2_f_v.setText(f'TOTAL: {self.total_value}')
            else:
                self.op_pay = 'CARD'
                switch_page(w.rmor_slct_pay_stackedWidget, w.rmor_slct_pay_pg1)

    def set_conf_form(self, w):
        for x in self.data_products:
                processed_data = [str(y) for y in x]
                QTreeWidgetItem(w.rmor_conf_f3_tree, processed_data)

        self.add_format = f'{self.data_order[2][0]}, ' \
                                f'{self.data_order[2][1]} - '\
                                f'{self.data_order[2][2]}, '\
                                f'{self.data_order[2][3]}/'\
                                f'{self.data_order[2][4]}'
        w.rmor_conf_f1_c.setText(f'CLIENT: {self.data_order[1][0]}')
        if (self.op_pay == 'MONEY'):
            w.rmor_conf_f1_p.setText(f'PAYMENT: MONEY')
        else:
            w.rmor_conf_f1_p.setText(f'PAYMENT: {self.data_order[7][0]}')
        w.rmor_conf_f2_add_2.setText(f'ADDRESS: {self.add_format}')
        w.rmor_conf_f4_v.setText(f'TOTAL: {self.total_value}')
        

    def finish_reg(self):
        # DATA TRATAMENTS
        temp = f'{self.data_order[1][0]} cpf: {self.data_order[1][1]}' #Name and cpf
        self.data_order[1] = temp
        self.data_order[2] = self.add_format
        temp = ''
        for x in range(0, len(self.data_order[4])):
                if (x == 0):
                        temp = f'{temp}Product: {self.data_order[4][x][0]}/{self.data_order[4][x][1]}/{self.data_order[4][x][2]}'
                else:
                    temp = f'{temp} \nProduct: {self.data_order[4][x][0]}/{self.data_order[4][x][1]}/{self.data_order[4][x][2]}'

        self.data_order[4] = temp
        if (self.op_pay == "CARD"): 
                self.data_order[7] = f'Card: {self.data_order[7][0]}'
        else:
                self.data_order[7] = ''
        order = o.view(True)
        date = dtime.date.today()
        month = date.month
        if (len(str(month)) == 1):
                month = f'0{month}'
        else:
                month = f'{month}'

        try:
                temp = order.iat[-1,0]
                self.data_order[0] = int(temp) + 1 # NUMBER ORDER
                self.data_order[0] = str(self.data_order[0])
        except:
                self.data_order[0] = f'{date.year}{month}000001' # NUMBER ORDER
        self.data_order[3] = 'received' # STATUS
        self.data_order[5] = str(self.total_value) # TOTAL VALUE
        
        self.data_order[8] = str(date) # ACTUAL DATE
        print(f'{o.create(self.data_order)}')
        self.__init__()
         

    #REGISTER ORDER FUNCTIONS
    def rmor_init(self, w, init):
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
        try:
                if (self.data[0] == "ERROR: Invalid Input"):
                        pass
                if (self.data[0] == "Error"):
                        pass
        except:
            self.insert_tree_data(self.data[0], w.rmor_slct_c_f2_tree, 'Client')
        w.rmor_slct_p_f1_tv.setText(f'TOTAL VALUE: 0')
        self.clean_data(w)
        if (init == 0):
            switch_page(w.rmor_stackedWidget,w.rmor_slct_c)
            init = 1
            
    def rmor_btn(self, w):
        w.rmor_btn_n.clicked.connect(lambda: self.rmor_next_step(w, w.rmor_stackedWidget.currentIndex()))
        w.rmor_btn_b.clicked.connect(lambda: self.rmor_back_step(w, w.rmor_stackedWidget.currentIndex()))
        # BUTTON TREE PRODUCT
        w.rmor_btn_r.clicked.connect(lambda: self.rmo_remove(self, w, w.rmor_slct_p_f1_tv))
        w.rmor_btn_a.clicked.connect(lambda: self.rmo_add_win(w))
        # SEARCH
        w.rmor_slct_c_f1_btn.clicked.connect(lambda: self.search_data(w.rmor_slct_c_f1_src.text(), w.rmor_slct_c_f2_tree, self.data[0], 'Name', 'Client'))
        w.rmor_slc_p.rmor_slct_p_f5_btn.clicked.connect(lambda: self.search_data(w.rmor_slc_p.rmor_slct_p_f5_src.text(), w.rmor_slc_p.rmor_slct_p_f3_tree, self.data[1], 'PRODUCT', 'Product'))  
        #BUTTON POP-UP
        w.rmor_slc_p.rmor_slct_p_f4_btn_add.clicked.connect(lambda: self.rmo_add(self, w, w.rmor_slct_p_f2_tree, w.rmor_slct_p_f1_tv))
        w.rmor_slc_p.rmor_slct_p_f4_btn_l.clicked.connect(lambda: self.rmo_remove_qt(self, w))
        w.rmor_slc_p.rmor_slct_p_f4_btn_m.clicked.connect(lambda: self.rmo_add_qt(self, w))
        # RADIO BUTTONS PAYMENT
        w.rmor_slct_pay_f1_rbc.op = 'CARD'
        w.rmor_slct_pay_f1_rbm.op = 'MONEY'
        w.rmor_slct_pay_f1_rbc.toggled.connect(lambda: self.radio_toggle(w))
        w.rmor_slct_pay_f1_rbm.toggled.connect(lambda: self.radio_toggle(w))
        
    def rmor_next_step(self, w, current):
        
            if (current == 0):
                if (w.rmor_slct_c_f2_tree.currentItem() != None):
                    self.get_data_client(w)
                    w.rmor_btn_b.setVisible(True)
                    w.rmor_Spacer_btts.setVisible(True)
                    switch_page(w.rmor_stackedWidget,w.rmor_slct_a)
                    w.rmor_lb_ed.setText("INSERT ADDRESS")
                else:
                    w.alert.show()
                    w.alert.Alert_win_f1_lb.setStyleSheet("font: 30pt \"Voga \";\n color:#f6f6e9;")
                    w.alert.Alert_win_f1_lb.setText(f'Please select a \nrecord to proceed')
                    w.hide() 

            elif (current == 1 ):
                    get_sucess = self.get_data_add(w)
                    if (get_sucess[0] == 'SUCCESS'):
                        self.data_order[2] = get_sucess[1]
                        w.rmor_btn_a.setVisible(True)
                        w.rmor_btn_r.setVisible(True)
                        w.rmor_Spacer_btts.setVisible(False)
                        w.rmor_slct_p_f2_tree.clear()
                        w.rmor_slc_p.rmor_slct_p_f3_tree.clear()
                        self.total_value = 0
                        w.rmor_slct_p_f1_tv.setText(f'TOTAL: {self.total_value}')
                        self.data[1] = p.view()
                        try:
                                if (self.data[1] == "ERROR: Invalid Input"):
                                    pass
                                if (self.data[1] == "Error"):
                                    pass
                        except:
                            self.insert_tree_data(self.data[1], w.rmor_slc_p.rmor_slct_p_f3_tree, 'Product')
                        switch_page(w.rmor_stackedWidget,w.rmor_slct_p)
                        w.rmor_lb_ed.setText("SELECT THE PRODUCTS")
                    else:
                        pass
                

            elif (current == 2 ):
                if (self.data_products != []):
                    self.data_order[4]  = self.data_products
                    w.rmor_btn_a.setVisible(False)
                    w.rmor_btn_r.setVisible(False)
                    w.rmor_Spacer_btts.setVisible(True)
                    switch_page(w.rmor_stackedWidget,w.rmor_slct_pay)
                    switch_page(w.rmor_slct_pay_stackedWidget,w.rmor_slct_pay_pg1)
                    w.rmor_lb_ed.setText("ENTER THE DATA")
                    w.rmor_slct_pay_f_f3_v.setText(f'TOTAL: {self.total_value}')

                else:
                    w.alert.show()
                    w.alert.Alert_win_f1_lb.setStyleSheet("font: 30pt \"Voga \";\n color:#f6f6e9;")
                    w.alert.Alert_win_f1_lb.setText(f'Please include a \nproduct to proceed')
                    w.hide() 

            elif (current == 3 ):
                get_sucess = self.get_data_card(w)
                if (get_sucess[0] == 'SUCCESS'):
                    self.data_order[6]  = self.op_pay
                    if (self.op_pay == 'MONEY'):
                        self.data_order[7] = ''
                    else:
                        self.data_order[7] = get_sucess[1]
                    #w.rmor_btn_a.setVisible(False)
                    #w.rmor_btn_r.setVisible(False)
                    switch_page(w.rmor_stackedWidget,w.rmor_conf)
                    w.rmor_lb_ed.setText("CONFIRM THE ORDER")
                    w.rmor_conf_f3_tree.clear()
                    self.set_conf_form(w)
                else:
                    pass
                
            elif (current == 4 ):
                switch_page(w.rmor_stackedWidget,w.rmor_suc)
                self.finish_reg()
                w.rmor_btn_b.setVisible(False)
                w.rmor_btn_n.setVisible(False)
                w.rmor_lb_rs.setText("")
                w.rmor_lb_ed.setText("REGISTER SYSTEM")
                w.rmor_lb_ed.setStyleSheet("font: 60pt \"Voga \";  \ncolor:#f6f6e9;")


    def rmor_back_step(self, w, current):
            if (current == 1 ):
                switch_page(w.rmor_stackedWidget,w.rmor_slct_c)
                w.rmor_btn_b.setVisible(False)
                w.rmor_lb_ed.setText("SELECT THE CLIENT")
                w.rmor_lb_ed.setStyleSheet("color:#f6f6e9;\nfont: 28pt \"Fira Sans\";\n")
                w.rmor_lb_rs.setText("REGISTER SYSTEM")

            elif (current == 2 ):
                w.rmor_btn_a.setVisible(False)
                w.rmor_btn_r.setVisible(False)
                w.rmor_Spacer_btts.setVisible(True)
                switch_page(w.rmor_stackedWidget,w.rmor_slct_a)
                w.rmor_slc_p.rmor_slct_p_f3_tree.clear()
                self.data_products = []
                w.rmor_lb_ed.setText("INSERT ADDRESS")
                

            elif (current == 3 ):
                switch_page(w.rmor_stackedWidget,w.rmor_slct_p)
                w.rmor_btn_a.setVisible(True)
                w.rmor_btn_r.setVisible(True)
                w.rmor_Spacer_btts.setVisible(False)
                w.rmor_lb_ed.setText("SELECT THE PRODUCTS")

            elif (current == 4 ):
                switch_page(w.rmor_stackedWidget,w.rmor_slct_pay)
                w.rmor_lb_ed.setText("ENTER THE DATA")
                
                                       

    #INIT FUNCTIONS
    def rmor_Functions(self, w):
            self.rmor_btn(w)


class Rmo_View(RMO_FUNCTIONS):
    def __init__(self):
        super().__init__()
        data = []
        slct_data = None

    def pg_date(self, w, page):
        if (page == 'GRAPH'):
            switch_page(w.rmov_gph_stackedWidget,w.rmov_gph_f2)
        else:
            switch_page(w.rmov_reg_stackedWidget,w.rmov_reg_f3)

    def get_date(self, w, page):
        if (page == 'GRAPH'):
            slct_data = [w.rmov_gph_f2_start.text(),
                             w.rmov_gph_f2_end.text()]
            return self.data_tratament_error(self, 'GRAPH', w, slct_data)
                
        else:
            slct_data = [w.rmov_reg_f3_start.text(),
                         w.rmov_reg_f3_end.text()]
            w.rmov_reg_f2_tree.clear()
            self.data = o.view()
            return self.data_tratament_error(self, 'REG', w, slct_data, w.rmov_reg_f2_tree, w.rmov_reg_stackedWidget,w.rmov_reg_f1_2)

    def animated_graphic(self, x , y, grapich_Title):
        try:
                test = self.data[1]
                tx = []
                ty = []
                for j in self.data:
                        try:
                                tx += j[x].values.tolist()
                                ty += j[y].values.tolist()
                        except TypeError:
                                pass
                test = 1
        except:
                test = 0
                tx = self.data[x].values.tolist()
                ty = self.data[y].values.tolist()
        for j in range(0, len(ty)):
                ty[j] = float(ty[j])
                tx[j] = str(tx[j])
                if (test == 1 and len(self.data) > 5):
                        tx[j] = tx[j][0:6]
        plt.xlabel('ORDER')
        plt.ylabel('VALUE')
        plt.title(grapich_Title)
        plt.barh(tx, ty)
        plt.show()
        
    def place_graphic(self, frame,  x , y, grapich_Title):
        try:
                test = self.data[1]
                tx = []
                ty = []
                for j in self.data:
                        try:
                                tx += j[x].values.tolist()
                                ty += j[y].values.tolist()
                        except TypeError:
                                pass
                test = 1
        except:
                test = 0
                tx = self.data[x].values.tolist()
                ty = self.data[y].values.tolist()
        for j in range(0, len(ty)):
                ty[j] = float(ty[j])
                tx[j] = str(tx[j])
                if (test == 1 and len(self.data) > 5):
                        tx[j] = tx[j][0:6]

        len_tx = len(tx)
        if (len_tx > 25):
                tempx = []
                tempy = []
                sum_ty = 0
                temp_date = f'{tx[0][:6]}'
                for x in range(0, len_tx):
                    temp = f'{tx[x][:6]}'
                    if (temp != temp_date):
                        tempx += [temp_date]
                        tempy += [round(sum_ty,2)]
                        temp_date = f'{tx[x][:6]}'
                        sum_ty = 0  
                    sum_ty += ty[x]
                    
                tempx += [temp_date]
                tempy += [sum_ty]
                tx = tempx
                ty = tempy
                        
        plt.xlabel('VALUE')
        plt.ylabel('ORDER')
        plt.title(grapich_Title)
        plt.barh(tx, ty)
        file = p.src_path()
        file = file.replace('PRODUCTS/PRODUCTS.xlsx','ORDERS/GRAPHICS')
        style = f'border-image: url({file}/temp.png) 0 0 0 0 stretch stretch;\nborder-radius: 5px;\n'
        frame.setStyleSheet(style)
        file = f'{file}/{grapich_Title}.png'
        plt.savefig(file)
        plt.close()
        style = f'border-image: url({file}) 0 0 0 0 stretch stretch;\nborder-radius: 5px;\n'
        frame.setStyleSheet(style)
    
    def date_tratament(self, month = None):
        if (month == None):
            self.data = o.view()
        else:
            pass

    def rmov_btn(self, w):
        #BACK
        w.rmov_btn_b.clicked.connect(lambda: self.rmov_back_step(w))
        # SEARCH
        w.rmov_reg_f1_btn.clicked.connect(lambda: self.search_data(w.rmov_reg_f1_src.text(), w.rmov_reg_f2_tree, self.data, 'client', 'Order', ['date', 'number_order']))
        #OPTION
        w.rmov_op_reg.clicked.connect(lambda: self.rmov_next_step(w, 'REG'))
        w.rmov_op_graph.clicked.connect(lambda: self.rmov_next_step(w, 'GRAPH'))
        #ANIMATED
        w.rmov_gph_f1_ani.clicked.connect(lambda: self.animated_graphic("number_order","value", "ORDERS GRAPHIC"))
        #DATE
        w.rmov_reg_f1_date.clicked.connect(lambda: self.pg_date(w, 'REG'))
        w.rmov_gph_f1_date.clicked.connect(lambda: self.pg_date(w, 'GRAPH'))
        w.rmov_reg_f3_btn.clicked.connect(lambda: self.get_date(w, 'REG'))
        w.rmov_gph_f2_btn.clicked.connect(lambda: self.get_date(w, 'GRAPH'))
    
    def rmov_init(self, w, init):
        w.rmov_btn_b.setVisible(False)
        switch_page(w.rm_stackedWidget,w.rmov)
        self.date_tratament() #DEFAULT CURRENT DATA
        if (init == 0):
            switch_page(w.rmov_stackedWidget,w.rmov_op)
            init = 1
        

    def rmov_next_step(self, w, btn):
            w.rmov_btn_b.setVisible(True)
            if (btn == 'GRAPH'):
                try:
                        if (self.data == "Error"):
                            w.alert.show()
                            w.alert.Alert_win_f1_lb.setStyleSheet("font: 28pt \"Voga \";\n color:#f6f6e9;")
                            w.alert.Alert_win_f1_lb.setText(f'No data to Show')
                            w.hide()
                        if (self.data == "ERROR: Invalid Input"):
                                w.alert.show()
                                w.alert.Alert_win_f1_lb.setStyleSheet("font: 28pt \"Voga \";\n color:#f6f6e9;")
                                w.alert.Alert_win_f1_lb.setText(f'No data to Show')
                                w.hide()
                except:
                    switch_page(w.rmov_stackedWidget,w.rmov_gph)
                    switch_page(w.rmov_gph_stackedWidget,w.rmov_gph_f1)
                    self.place_graphic(w.rmov_f3_img, "number_order","value", "ORDERS GRAPHIC")
            else:
                try:
                        if (self.data == "Error"):
                            w.alert.show()
                            w.alert.Alert_win_f1_lb.setStyleSheet("font: 28pt \"Voga \";\n color:#f6f6e9;")
                            w.alert.Alert_win_f1_lb.setText(f'No data to Show')
                            w.hide()
                        if (self.data == "ERROR: Invalid Input"):
                                w.alert.show()
                                w.alert.Alert_win_f1_lb.setStyleSheet("font: 28pt \"Voga \";\n color:#f6f6e9;")
                                w.alert.Alert_win_f1_lb.setText(f'No data to Show')
                                w.hide()
                except:
                    try:
                        data_total = []
                        for j in self.data:
                                data_total += j.values.tolist()
                    except:
                        self.data = o.view(True)
                    w.rmov_reg_f2_tree.clear()
                    switch_page(w.rmov_stackedWidget,w.rmov_reg)
                    switch_page(w.rmov_reg_stackedWidget,w.rmov_reg_f1_2)
                    self.insert_tree_data(self.data, w.rmov_reg_f2_tree, 'Order')

    def rmov_back_step(self, w):
            switch_page(w.rmov_stackedWidget,w.rmov_op)
            w.rmov_btn_b.setVisible(False)

    #INIT FUNCTIONS
    def rmov_Functions(self, w):
            self.rmov_btn(w)


class Rmo_Update(RMO_FUNCTIONS):
    def __init__(self):
        super().__init__()
        self.data = None
        self.slct_data = None
        self.slct_data1 = None
        self.current_Widget = None
        self.tool_tip = None
        self.data_products = []
        self.data_p = None
        self.prod_qt = [0]
        self.curr_prod_qt = 0
        self.total_value = 0
        self.op_pay = 'CARD'
        
    def clean_data(self, w): #FINALIZADO
        w.rmou_add_f1_add.setText("")
        w.rmou_add_f2_num.setText("")
        w.rmou_add_f2_dist.setText("")
        w.rmou_add_f3_cty.setText("")
        w.rmou_add_f3_stte.setText("")
        w.rmou_gen_f1_lb.setText("")
        w.rmou_slct_pay_f_f1_card.setText("")
        w.rmou_slct_pay_f_f2_cvv.setText("")
        w.rmou_slct_pay_f_f2_ex.setText("")
        w.rmou_p_slct_tree.clear()
        w.rmou_slct_f2_tree.clear()
        w.rmou_c_slct_f2_tree.clear()
            
    def get_data(self, w, field): 
        if (field == "status"):
                data_up = w.rmou_gen_f1_lb.text()  
                print(o.update(self.data, field, self.slct_data, data_up))
        elif (field == "Products"):
                temp = ''
                
                for x in range(0, len(self.data_products)):
                        if (x == 0):
                            temp = f'{temp}Product: {self.data_products[x][0]}/{self.data_products[x][1]}/{self.data_products[x][2]}'
                        else:
                            temp = f'{temp} \nProduct: {self.data_products[x][0]}/{self.data_products[x][1]}/{self.data_products[x][2]}'

                self.data_products = temp
                print(o.update(self.data, "products/qnt/value", self.slct_data, self.data_products))
                print(o.update(self.data, "value", self.slct_data, self.total_value))
        elif (field == "client"):
                data_up = ['','']
                data_up[0] = w.rmou_c_slct_f2_tree.currentItem().text(0)
                data_up[1] = w.rmou_c_slct_f2_tree.currentItem().text(1)
                data_up = f'{data_up[0]} cpf: {data_up[1]}' #Name and cpf
                print(o.update(self.data, field, self.slct_data, data_up))
        elif (field == "Pay"):            
                if (self.op_pay == 'MONEY'):
                        data_up = ''
                else:
                        data_up = f'Number: {w.rmou_slct_pay_f_f1_card.text()}'
                            # w.rmou_slct_pay_f_f2_cvv.text(),
                             #w.rmou_slct_pay_f_f2_ex.text()]
                print(o.update(self.data, "payment_form", self.slct_data, self.op_pay))
                print(o.update(self.data, "card_number", self.slct_data, data_up))
        elif (field == "address"):  
                data_up = f'{w.rmou_add_f1_add.text()}, ' \
                                f'{w.rmou_add_f2_num.text()} - '\
                                f'{w.rmou_add_f2_dist.text()}, '\
                                f'{w.rmou_add_f3_cty.text()}/'\
                                f'{w.rmou_add_f3_stte.text()}'
                print(o.update(self.data, field, self.slct_data, data_up))
        self.__init__()
        self.rmou_init(w, 1)

    #RADIO BUTTON
    def radio_toggle(self, w):
        radioButton = w.sender()
        if radioButton.isChecked():
            if (radioButton.op == 'MONEY'):
                self.op_pay = 'MONEY'
                switch_page(w.rmou_slct_pay_stackedWidget, w.rmou_slct_pay_pg2)
            else:
                self.op_pay = 'CARD'
                switch_page(w.rmou_slct_pay_stackedWidget, w.rmou_slct_pay_pg1)

    #UPDATE ORDER FUNCTIONS
    def rmou_init(self, w, init):
        self.data = o.view()
        try:
                if (self.data == "Error"):
                        pass
                if (self.data == "ERROR: Invalid Input"):
                       pass
        except:
            self.clean_data(w)
            self.insert_tree_data(self.data, w.rmou_slct_f2_tree, 'Order')
        switch_page(w.rm_stackedWidget,w.rmou)
        w.rmou_btn_n.setVisible(True)
        w.rmou_btn_b.setVisible(False)
        w.rmou_btn_a.setVisible(False)
        w.rmou_btn_r.setVisible(False)
        w.rmou_lb_ed.setText("SELECT A REGISTER")
        w.rmou_lb_ed.setStyleSheet("color:#f6f6e9;\nfont: 28pt \"Fira Sans\";\n")
        w.rmou_lb_us.setText("UPDATE SYSTEM")
            
        if (init == 0):
            switch_page(w.rmou_stackedWidget,w.rmou_slct)
            init = 1
        self.tree_update_data()
        
            
    def rmou_btn(self, w):
        # FINALIZADO BOTAO
        w.rmou_btn_b.clicked.connect(lambda: self.rmou_back_step(w, w.rmou_stackedWidget.currentIndex()))
        w.rmou_btn_n.clicked.connect(lambda: self.rmou_next_step(w, w.rmou_stackedWidget.currentIndex(),''))
        # OPTION SELECTED - FINALIZADO BOTAO
        w.rmou_f1_btn_c.clicked.connect(lambda: self.rmou_next_step(w, w.rmou_stackedWidget.currentIndex(),'Client'))
        w.rmou_f1_btn_add.clicked.connect(lambda: self.rmou_next_step(w, w.rmou_stackedWidget.currentIndex(),'Add'))
        w.rmou_f1_btn_pd.clicked.connect(lambda: self.rmou_next_step(w, w.rmou_stackedWidget.currentIndex(),'Products'))
        w.rmou_f2_btn_status.clicked.connect(lambda: self.rmou_next_step(w, w.rmou_stackedWidget.currentIndex(),'Status'))
        w.rmou_f2_btn_pay.clicked.connect(lambda: self.rmou_next_step(w, w.rmou_stackedWidget.currentIndex(),'Pay'))
        # BUTTON TREE PRODUCT - FINALIZADO BOTAO
        w.rmou_btn_r.clicked.connect(lambda: self.rmo_remove(self, w, w.rmou_slct_pay_f_v))
        w.rmou_btn_a.clicked.connect(lambda: self.rmo_add_win(w))
        # SEARCH BOTAO
        w.rmor_slc_p.rmor_slct_p_f5_btn.clicked.connect(lambda: self.search_data(w.rmor_slc_p.rmor_slct_p_f5_src.text(), w.rmor_slc_p.rmor_slct_p_f3_tree, self.data_p, 'PRODUCT', 'Product'))  
        w.rmou_date_f1_btn.clicked.connect(lambda: self.search_data(w.rmou_date_f1_src.text(), w.rmou_slct_f2_tree, self.data, 'client', 'Order', ['date', 'number_order']))
        #BUTTON POP-UP - FINALIZADO BOTAO
        w.rmor_slc_p.rmor_slct_p_f4_btn_add.clicked.connect(lambda: self.rmo_add(self, w, w.rmou_p_slct_tree, w.rmou_slct_p_f1_tv))
        w.rmor_slc_p.rmor_slct_p_f4_btn_l.clicked.connect(lambda: self.rmo_remove_qt(self, w))
        w.rmor_slc_p.rmor_slct_p_f4_btn_m.clicked.connect(lambda: self.rmo_add_qt(self, w))
        # RADIO BUTTONS PAYMENT - FINALIZADO BOTAO
        w.rmou_slct_pay_f1_rbc.op = 'CARD'
        w.rmou_slct_pay_f1_rbm.op = 'MONEY'
        w.rmou_slct_pay_f1_rbc.toggled.connect(lambda: self.radio_toggle(w))
        w.rmou_slct_pay_f1_rbm.toggled.connect(lambda: self.radio_toggle(w))


    def rmou_next_step(self, w, current, widget):
        if (current == 0):
                if (w.rmou_slct_f2_tree.currentItem() != None):
                        w.rmou_btn_b.setVisible(True)
                        w.rmou_btn_n.setVisible(False)
                        switch_page(w.rmou_stackedWidget,w.rmou_op)
                        self.slct_data = w.rmou_slct_f2_tree.currentItem().text(0)
                        self.slct_data = self.data.loc[self.data['number_order'] == int(self.slct_data)]
                        self.slct_data1 = w.rmou_slct_f2_tree.currentItem().text(2)
                        self.slct_data = self.slct_data.loc[self.slct_data['client'] == self.slct_data1]
                else:
                        w.alert.show()
                        w.alert.Alert_win_f1_lb.setStyleSheet("font: 30pt \"Voga \";\n color:#f6f6e9;")
                        w.alert.Alert_win_f1_lb.setText(f'Please select a \nrecord to proceed')
                        w.hide()    
                
        elif (current == 1):
                self.current_Widget = widget
                w.rmou_btn_n.setVisible(True)
                if (self.current_Widget == 'Client'):
                    switch_page(w.rmou_stackedWidget,w.rmou_c)
                    w.rmou_c_slct_f2_tree.clear()
                    client_v = c.view()
                    try:
                            if (client_v == "ERROR: Invalid Input"):
                                pass
                            if (client_v == "Error"):
                                pass
                    except:
                        self.insert_tree_data(client_v, w.rmou_c_slct_f2_tree)
                elif (self.current_Widget == 'Add'):
                    switch_page(w.rmou_stackedWidget,w.rmou_add)
                elif (self.current_Widget == 'Products'):
                    switch_page(w.rmou_stackedWidget,w.rmou_p)
                    w.rmor_slc_p.rmor_slct_p_f3_tree.clear()
                    w.rmou_slct_p_f1_tv.setText(f'TOTAL VALUE: 0')
                    self.data_p = p.view()
                    try:
                            if (self.data_p == "ERROR: Invalid Input"):
                                pass
                            if (self.data_p == "Error"):
                                pass
                    except:
                        self.insert_tree_data(self.data_p, w.rmor_slc_p.rmor_slct_p_f3_tree, 'Product')
                    w.rmou_btn_a.setVisible(True)
                    w.rmou_btn_r.setVisible(True)
                elif (self.current_Widget == 'Status'):
                    switch_page(w.rmou_stackedWidget,w.rmou_gen)
                    w.rmou_gen_f1_lb.setToolTip("received, preparing, on the way or delivered") #TOOL TIP
                    
                elif (self.current_Widget == 'Pay'):
                    self.op_pay = 'CARD'
                    switch_page(w.rmou_stackedWidget,w.rmou_card)

        elif (current >= 2 or current <=6 ):
                print("NEXT")
                switch_page(w.rmou_stackedWidget,w.rmou_suc)
                if (self.current_Widget == 'Client'): #OK
                        self.get_data(w, 'client')
                elif (self.current_Widget == 'Add'): #OK
                        self.get_data(w, 'address')
                elif (self.current_Widget == 'Products'):
                        w.rmou_btn_a.setVisible(False)
                        w.rmou_btn_r.setVisible(False)
                        self.get_data(w, 'Products')
                elif (self.current_Widget == 'Status'): #OK
                        self.get_data(w, 'status')
                elif (self.current_Widget == 'Pay'): #OK
                        self.get_data(w, 'Pay')
                w.rmou_btn_n.setVisible(False)
                w.rmou_btn_b.setVisible(False)

    def rmou_back_step(self, w, current):
        if (current == 1):
            switch_page(w.rmou_stackedWidget,w.rmou_slct)
            w.rmou_btn_n.setVisible(True)
        elif (current >= 2 or current <=6 ):
            w.rmou_btn_b.setVisible(True)
            w.rmou_btn_n.setVisible(False)
            w.rmou_btn_a.setVisible(False)
            w.rmou_btn_r.setVisible(False)
            switch_page(w.rmou_stackedWidget,w.rmou_op)
    #INIT FUNCTIONS
    def rmou_Functions(self, w):
            self.rmou_btn(w)


class Rmo_Delete(RMO_FUNCTIONS):
    def __init__(self):
        data = None
        slct_data = None
        current_Widget = None
            
    def delete_data(self, w):
        print(o.delete(self.data, self.slct_data))
        self.__init__()
        self.rmod_init(w, 1)
    #DELETE CLIENT FUNCTIONS

    def init_Tree_widget(self, w):
            w.rmod_btn_n.setVisible(True)
            self.tree_update_data()
            self.insert_tree_data(self.data, w.rmod_reg_f2_tree, 'Order')
            w.rmod_lb_so.setText("SELECT REGISTER")
            w.rmod_lb_ds.setText("DELETE SYSTEM")
            w.rmod_lb_so.setStyleSheet("color:#f6f6e9;\nfont: 28pt \"Fira Sans\";\n")
          
    def rmod_init(self, w, init):
        self.data = o.view()
        try:
                if (self.data == "Error"):
                            w.alert.show()
                            w.alert.Alert_win_f1_lb.setStyleSheet("font: 28pt \"Voga \";\n color:#f6f6e9;")
                            w.alert.Alert_win_f1_lb.setText(f'No data to Delete')
                            w.hide()
                if (self.data == "ERROR: Invalid Input"):
                        w.alert.show()
                        w.alert.Alert_win_f1_lb.setStyleSheet("font: 28pt \"Voga \";\n color:#f6f6e9;")
                        w.alert.Alert_win_f1_lb.setText(f'No data to Delete')
                        w.hide()
        except:
            switch_page(w.rm_stackedWidget,w.rmod)
            w.rmod_btn_n.setVisible(False)
            w.rmod_lb_ds.setStyleSheet("color:#f6f6e9;\nfont: 28pt \"Fira Sans\";\n")
            w.rmod_lb_so.setText("DELETE SYSTEM")
            w.rmod_reg_f2_tree.clear()
            self.init_Tree_widget(w)
            if (init == 0):
                switch_page(w.rmod_stackedWidget,w.rmod_slct)
                init = 1

    def rmod_btn(self, w):
        w.rmod_btn_n.clicked.connect(lambda: self.rmod_next_step(w))
        # SEARCH
        w.rmod_reg_f1_btn.clicked.connect(lambda: self.search_data(w.rmod_reg_f1_src.text(), w.rmod_reg_f2_tree, self.data, 'client', 'Order', ['date', 'number_order']))
    
            
    def rmod_next_step(self, w):
            if (w.rmod_reg_f2_tree.currentItem() != None):
                    self.slct_data = w.rmod_reg_f2_tree.currentItem().text(0)
                    self.slct_data = self.data.loc[self.data['number_order'] == int(self.slct_data)]
                    self.slct_data1 = w.rmod_reg_f2_tree.currentItem().text(2)
                    print(f"DATA SOLICITADA {self.slct_data1}")
                    self.slct_data = self.slct_data.loc[self.slct_data['client'] == self.slct_data1]
                    switch_page(w.rmod_stackedWidget,w.rmod_suc)
                    print(f"DATA SOLICITADA {self.slct_data}")
                    self.delete_data(w)
                    w.rmod_btn_n.setVisible(False)
                    w.rmod_lb_ds.setText("")
                    w.rmod_lb_so.setText("DELETE SYSTEM")
                    w.rmod_lb_so.setStyleSheet("font: 60pt \"Voga \";  \ncolor:#f6f6e9;")
            else:
                w.alert.show()
                w.alert.Alert_win_f1_lb.setStyleSheet("font: 30pt \"Voga \";\n color:#f6f6e9;")
                w.alert.Alert_win_f1_lb.setText(f'Please select a \nrecord to proceed')
                w.hide()

    #INIT FUNCTIONS
    def rmod_Functions(self, w):
            self.rmod_btn(w)
