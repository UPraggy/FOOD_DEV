from utils import template
from PyQt5 import QtWidgets
p = template.Product()
def switch_page(stacked, page):
        stacked.setCurrentWidget(page)

def search_data(src_field_data, tree, data):
            filtered_data = data['PRODUCT']
            filtered_data = data.loc[filtered_data.str.contains(f'^{src_field_data}', case = False)] #search data for respective field
            data_total = filtered_data.values.tolist()
            tree.clear()
            for x in data_total:
                processed_data = [ '' if str(y) == 'nan' else str(y) for y in x]
                QtWidgets.QTreeWidgetItem(tree, processed_data)

def insert_tree_data(data, tree):
        data_total = data.values.tolist()
        for x in data_total:
            processed_data = [ '' if str(y) == 'nan' else str(y) for y in x]
            QtWidgets.QTreeWidgetItem(tree, processed_data)

class Register():
    def __init__(self):
        data = None
        
    def clean_data(self, w):
        w.rmpr_cb_f1_id.setText("")
        w.rmpr_cb_f1_n.setText("")
        w.rmpr_cb_f2_desc.setText("")
        w.rmpr_cb_f3_u.setText("")
        w.rmpr_cb_f3_um.setText("")
        w.rmpr_cb_f4_v.setText("")

    def get_data(self, w):
        self.data = [w.rmpr_cb_f1_id.text(),
                     w.rmpr_cb_f1_n.text(),
                     w.rmpr_cb_f2_desc.text(),
                     w.rmpr_cb_f3_u.text(),
                     w.rmpr_cb_f3_um.text(),
                     w.rmpr_cb_f4_v.text()]
        p.create(self.data)
        
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
            switch_page(w.rmpr_cb_stackedWidget,w.rmpr_sc)
            self.get_data(w)
            w.rmpr_btn_n.setVisible(False)
            w.rmpr_lb_rs.setText("")
            w.rmpr_lb_ed.setText("REGISTER SYSTEM")
            w.rmpr_lb_ed.setStyleSheet("font: 60pt \"Voga \";  \ncolor:#f6f6e9;")
            

    #INIT FUNCTIONS
    def rmpr_Functions(self, w):
            self.rmpr_btn(w)

class View():
    def __init__(self):
        data = None
        slct_data = None

    def rmpv_btn(self, w):
        # SEARCH
        w.rmpv_slct_btn.clicked.connect(lambda: search_data(w.rmpv_slct_srp.text(), w.rmpv_f_tree, self.data))

    def rmpv_init(self, w):
        switch_page(w.rm_stackedWidget,w.rmpv)
        w.rmpv_f_tree.clear()
        self.data = p.view()
        insert_tree_data(self.data, w.rmpv_f_tree)
    #INIT FUNCTIONS
    def rmpv_Functions(self, w):
            self.rmpv_btn(w)

class Update():
    def __init__(self):
        data = None
        slct_data = None
        slct_data1 = None
        current_Widget = None
        
    def clean_data(self, w):
        w.rmpu_gen_f1_lb.setText("")

            
    def get_data_generic(self, w, field):
        data_up = w.rmpu_gen_f1_lb.text()
        p.update(self.data, field, self.slct_data, data_up)
        
        
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
        w.rmpu_f2_btn_u.clicked.connect(lambda: self.rmpu_next_step(w, w.rmpu_stackedWidget.currentIndex(),'UNIT'))
        w.rmpu_f2_btn_um.clicked.connect(lambda: self.rmpu_next_step(w, w.rmpu_stackedWidget.currentIndex(),'measure'))
        w.rmpu_f2_btn_v.clicked.connect(lambda: self.rmpu_next_step(w, w.rmpu_stackedWidget.currentIndex(),'VALUE'))
        # SEARCH
        w.rmpu_slct_btn.clicked.connect(lambda: search_data(w.rmpu_slct_src.text(), w.rmpu_f2_tree, self.data))
        
    def rmpu_next_step(self, w, current, widget):
        if (current == 0):
            switch_page(w.rmpu_stackedWidget,w.rmpu_slct)
            w.rmpu_btn_n.setVisible(True)
            w.rmpu_btn_b.setVisible(True)
            self.current_Widget = widget
            self.data = p.view()
            insert_tree_data(self.data, w.rmpu_f2_tree)
                
            w.rmpu_lb_ed.setText("SELECT REGISTER")
            w.rmpu_lb_us.setText("UPDATE SYSTEM")
            w.rmpu_lb_ed.setStyleSheet("color:#f6f6e9;\nfont: 28pt \"Fira Sans\";\n")
        
        if (current == 1):
            self.slct_data = w.rmpu_f2_tree.currentItem().text(0)
            self.slct_data = self.data.loc[self.data['ID'] == int(self.slct_data)]
            self.slct_data1 = w.rmpu_f2_tree.currentItem().text(1)
            self.slct_data = self.slct_data.loc[self.slct_data['PRODUCT'] == self.slct_data1]
            
            switch_page(w.rmpu_stackedWidget,w.rmpu_gen)
            w.rmpu_gen_f1_lb.setPlaceholderText(self.current_Widget)

            w.rmpu_lb_ed.setText("INSERT THE DATA")
            w.rmpu_lb_us.setText("UPDATE SYSTEM")
            w.rmpu_lb_ed.setStyleSheet("color:#f6f6e9;\nfont: 28pt \"Fira Sans\";\n")

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


class Delete():
    def __init__(self):
        data = None
        slct_data = None
        current_Widget = None
            
    def delete_data(self):
        print(p.delete(self.data, self.slct_data))
    #DELETE CLIENT FUNCTIONS

    def init_Tree_widget(self, w):
            w.rmpd_btn_n.setVisible(True)
            self.data = p.view()
            insert_tree_data(self.data, w.rmpd_f_tree)
            w.rmpd_lb_so.setText("SELECT REGISTER")
            w.rmpd_lb_ds.setText("DELETE SYSTEM")
            w.rmpd_lb_so.setStyleSheet("color:#f6f6e9;\nfont: 28pt \"Fira Sans\";\n")
            
    def rmpd_init(self, w, init):
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
        w.rmpd_slct_btn.clicked.connect(lambda: search_data(w.rmpd_slct_srp.text(), w.rmpd_f_tree, self.data))
    
            
    def rmpd_next_step(self, w):
            self.slct_data = w.rmpd_f_tree.currentItem().text(1)
            self.slct_data = self.data.loc[self.data['CPF'] == int(self.slct_data)]
            switch_page(w.rmpd_stackedWidget,w.rmpd_sc)
            self.delete_data()
            w.rmpd_btn_n.setVisible(False)
            w.rmpd_lb_ds.setText("")
            w.rmpd_lb_so.setText("DELETE SYSTEM")
            w.rmpd_lb_so.setStyleSheet("font: 60pt \"Voga \";  \ncolor:#f6f6e9;")
            

    #INIT FUNCTIONS
    def rmpd_Functions(self, w):
            self.rmpd_btn(w)
