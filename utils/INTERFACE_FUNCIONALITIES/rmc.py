from utils import template
from PyQt5 import QtWidgets
c = template.Client()
def switch_page(stacked, page):
        stacked.setCurrentWidget(page)

def search_data(src_field_data, tree, data):
            filtered_data = data['Name']
            filtered_data = data.loc[filtered_data.str.contains(f'^{src_field_data}', case = False)] #search data for respective field
            data_total = filtered_data.values.tolist()
            tree.clear()
            for x in data_total:
                processed_data = [ '' if str(y) == 'nan' else str(y) for y in x]
                processed_data[7] = f'{processed_data[7]}, ' \
                                f'{processed_data[8]} - '\
                                f'{processed_data[9]}, '\
                                f'{processed_data[10]}/'\
                                f'{processed_data[11]}' # Address Formating
                QtWidgets.QTreeWidgetItem(tree, processed_data)

def insert_tree_data(data, tree):
        data_total = data.values.tolist()
        for x in data_total:
            processed_data = [ '' if str(y) == 'nan' else str(y) for y in x]
            processed_data[7] = f'{processed_data[7]}, ' \
                                f'{processed_data[8]} - '\
                                f'{processed_data[9]}, '\
                                f'{processed_data[10]}/'\
                                f'{processed_data[11]}' # Address Formating
            QtWidgets.QTreeWidgetItem(tree, processed_data)

class Register():
    def __init__(self):
        data = None
        
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
    def finish_register(self, w):
        self.data.append(w.rmcr_cb_2_f1_add.text())
        self.data.append(w.rmcr_cb_2_f2_dist.text())
        self.data.append(w.rmcr_cb_2_f2_num.text())
        self.data.append(w.rmcr_cb_2_f3_cty.text())
        self.data.append(w.rmcr_cb_2_f3_stte.text())
        c.create(self.data)
        
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
        w.rmcr_btn_b.clicked.connect(lambda: self.rmcr_back_step(w, w.rmcr_cb_stackedWidget.currentIndex()))
        w.rmcr_btn_n.clicked.connect(lambda: self.rmcr_next_step(w, w.rmcr_cb_stackedWidget.currentIndex()))
        
    def rmcr_next_step(self, w, current):
        if (current == 0):
            self.get_data_pg1(w)
            w.rmcr_btn_b.setVisible(True)
            switch_page(w.rmcr_cb_stackedWidget,w.rmcr_cb_2)
            w.rmcr_lb_ed.setText("INSERT ADDRESS")
            w.rmcr_lb_rs.setText("REGISTER SYSTEM")
            w.rmcr_lb_ed.setStyleSheet("color:#f6f6e9;\nfont: 28pt \"Fira Sans\";\n")

        elif (current == 1 ):
            switch_page(w.rmcr_cb_stackedWidget,w.rmcr_cb_3)
            self.finish_register(w)
            w.rmcr_btn_b.setVisible(False)
            w.rmcr_btn_n.setVisible(False)
            w.rmcr_lb_rs.setText("")
            w.rmcr_lb_ed.setText("REGISTER SYSTEM")
            w.rmcr_lb_ed.setStyleSheet("font: 60pt \"Voga \";  \ncolor:#f6f6e9;")

    def rmcr_back_step(self, w, current):
        if (current == 1 ):
            switch_page(w.rmcr_cb_stackedWidget,w.rmcr_cb_1)
            w.rmcr_btn_b.setVisible(False)
            w.rmcr_lb_ed.setText("ENTER THE DATA")
            w.rmcr_lb_rs.setText("REGISTER SYSTEM")
            w.rmcr_lb_ed.setStyleSheet("color:#f6f6e9;\nfont: 28pt \"Fira Sans\";\n")
            

    #INIT FUNCTIONS
    def rmcr_Functions(self, w):
            self.rmcr_btn(w)

class View():
    def __init__(self):
        data = None
        slct_data = None

    def rmcv_btn(self, w):
        # SEARCH
        w.rmcv_slct_btn.clicked.connect(lambda: search_data(w.rmcv_slct_src.text(), w.rmcv_f_tree, self.data))

    def rmcv_init(self, w):
        switch_page(w.rm_stackedWidget,w.rmcv)
        w.rmcv_f_tree.clear()
        self.data = c.view()
        print("SELF DATA")
        print(self.data)
        insert_tree_data(self.data, w.rmcv_f_tree)
    #INIT FUNCTIONS
    def rmcv_Functions(self, w):
            self.rmcv_btn(w)

class Update():
    def __init__(self):
        data = None
        slct_data = None
        slct_data1 = None
        current_Widget = None
        
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
        c.update(self.data, field, self.slct_data, data_up)
                     
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
                c.update(self.data, field[y], self.slct_data, x)
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
        w.rmcu_slct_btn.clicked.connect(lambda: search_data(w.rmcu_slct_src.text(), w.rmcu_f_tree, self.data))
        
    def rmcu_next_step(self, w, current, widget):
        if (current == 0):
            switch_page(w.rmcu_stackedWidget,w.rmcu_slct)
            w.rmcu_btn_n.setVisible(True)
            w.rmcu_btn_b.setVisible(True)
            self.current_Widget = widget
            self.data = c.view()
            insert_tree_data(self.data, w.rmcu_f_tree)
                
            w.rmcu_lb_ed.setText("SELECT REGISTER")
            w.rmcu_lb_us.setText("UPDATE SYSTEM")
            w.rmcu_lb_ed.setStyleSheet("color:#f6f6e9;\nfont: 28pt \"Fira Sans\";\n")
        
        if (current == 1):
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
                w.rmcu_gen_f1_lb.setPlaceholderText(self.current_Widget)

            w.rmcu_lb_ed.setText("INSERT THE DATA")
            w.rmcu_lb_us.setText("UPDATE SYSTEM")
            w.rmcu_lb_ed.setStyleSheet("color:#f6f6e9;\nfont: 28pt \"Fira Sans\";\n")

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


class Delete():
    def __init__(self):
        data = None
        slct_data = None
        current_Widget = None
            
    def delete_data(self):
        print(c.delete(self.data, self.slct_data))
    #DELETE CLIENT FUNCTIONS

    def init_Tree_widget(self, w):
            w.rmcd_btn_n.setVisible(True)
            self.data = c.view()
            insert_tree_data(self.data, w.rmcd_f_tree)
            w.rmcd_lb_so.setText("SELECT REGISTER")
            w.rmcd_lb_ds.setText("DELETE SYSTEM")
            w.rmcd_lb_so.setStyleSheet("color:#f6f6e9;\nfont: 28pt \"Fira Sans\";\n")
            
    def rmcd_init(self, w, init):
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
        w.rmcd_slct_btn.clicked.connect(lambda: search_data(w.rmcd_slct_src.text(), w.rmcd_f_tree, self.data))
    
            
    def rmcd_next_step(self, w):
            self.slct_data = w.rmcu_f_tree.currentItem().text(0)
            self.slct_data = self.data.loc[self.data['Name'] == self.slct_data]
            self.slct_data1 = w.rmcu_f_tree.currentItem().text(1)
            self.slct_data = self.slct_data.loc[self.slct_data['CPF'] == int(self.slct_data1)]
            switch_page(w.rmcd_stackedWidget,w.rmcd_sc)
            self.delete_data()
            w.rmcd_btn_n.setVisible(False)
            w.rmcd_lb_ds.setText("")
            w.rmcd_lb_so.setText("DELETE SYSTEM")
            w.rmcd_lb_so.setStyleSheet("font: 60pt \"Voga \";  \ncolor:#f6f6e9;")
            

    #INIT FUNCTIONS
    def rmcd_Functions(self, w):
            self.rmcd_btn(w)
