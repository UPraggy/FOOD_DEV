from utils import template
from PyQt5 import QtWidgets
import matplotlib.pyplot as plt

p = template.Product()
def switch_page(stacked, page):
        stacked.setCurrentWidget(page)

def search_data(src_field_data, tree, data):
            filtered_data = data['PRODUCT']
            filtered_data = data.loc[filtered_data.str.contains(f'^{src_field_data}', case = False)] #search data for respective field
            data_total = filtered_data.values.tolist()
            tree.clear()
            for x in data_total:
                processed_data = [ '' if str(y) == 'nan' or str(y) == 'NaN' else str(y) for y in x]
                QtWidgets.QTreeWidgetItem(tree, processed_data)

def insert_tree_data(data, tree):
        data_total = data.values.tolist()
        for x in data_total:
            processed_data = [ '' if str(y) == 'nan' or str(y) == 'NaN' else str(y) for y in x]
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
                     w.rmpr_cb_f4_v.text(), 0,0, 0, 0]
        print(p.create(self.data))
        
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
        #BACK
        w.rmpv_btn_b.clicked.connect(lambda: self.rmpv_back_step(w))
        # SEARCH
        w.rmpv_slct_btn.clicked.connect(lambda: search_data(w.rmpv_slct_src.text(), w.rmpv_f2_tree, self.data))
        #OPTION
        w.rmpv_op_f1_btn_reg.clicked.connect(lambda: self.rmpv_next_step(w, 'REG'))
        w.rmpv_op_f1_btn_stock.clicked.connect(lambda: self.rmpv_next_step(w, 'STK'))
        w.rmpv_op_f2_btn_sells.clicked.connect(lambda: self.rmpv_next_step(w, 'SELL'))
        w.rmpv_op_f2_btn_price.clicked.connect(lambda: self.rmpv_next_step(w, 'PRICE'))
        #ANIMATED
        w.rmpv_stk_f1_btn_ani.clicked.connect(lambda: self.animated_graphic("PRODUCT","STOCK", "STOCK GRAPHIC"))
        w.rmpv_sells_f1_btn_ani.clicked.connect(lambda: self.animated_graphic("PRODUCT","SELLS", "SELLS GRAPHIC"))
        w.rmpv_price_f1_btn_ani.clicked.connect(lambda: self.animated_graphic("PRODUCT","PRICE", "PRICE GRAPHIC"))
        
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
        w.rmpv_lb_p.setText("PRODUCTS")
        w.rmpv_lb_p.setStyleSheet("color:rgb(0,0,0);\nfont: 80pt \"Voga \";")
        w.rmpv_btn_b.setVisible(False)
        switch_page(w.rm_stackedWidget,w.rmpv)
        self.data = p.view()
        if (init == 0):
            switch_page(w.rmpv_stackedWidget,w.rmpv_op)
            init = 1
    def rmpv_back_step(self, w):
            switch_page(w.rmpv_stackedWidget,w.rmpv_op)
            w.rmpv_btn_b.setVisible(False)
            w.rmpv_lb_p.setText("PRODUCTS")
            w.rmpv_lb_p.setStyleSheet("color:rgb(0,0,0);\nfont: 80pt \"Voga \";")
            
    def rmpv_next_step(self, w, btn):
            w.rmpv_lb_p.setText("GRAPHIC")
            w.rmpv_lb_p.setStyleSheet("color:#f6f6e9;\nfont: 60pt \"Voga \";")
            self.data = p.view()
            w.rmpv_btn_b.setVisible(True)
            if (btn == 'STK'):
                switch_page(w.rmpv_stackedWidget,w.rmpv_stock)
                self.place_graphic(w.rmpv_stk_f2_img, "PRODUCT","STOCK", "STOCK GRAPHIC")
            elif (btn == 'SELL'):
                switch_page(w.rmpv_stackedWidget,w.rmpv_sells)
                self.place_graphic(w.rmpv_sells_f2_img, "PRODUCT","SELLS", "SELLS GRAPHIC")
            elif (btn == 'PRICE'):
                switch_page(w.rmpv_stackedWidget,w.rmpv_price)
                self.place_graphic(w.rmpv_price_f2_img, "PRODUCT","PRICE", "PRICE GRAPHIC")
            else:
                w.rmpv_f2_tree.clear()
                switch_page(w.rmpv_stackedWidget,w.rmpv_src)
                insert_tree_data(self.data, w.rmpv_f2_tree)
                w.rmpv_lb_p.setText("PRODUCTS")
                w.rmpv_lb_p.setStyleSheet("color:rgb(0,0,0);\nfont: 80pt \"Voga \";")
    

            
    #INIT FUNCTIONS
    def rmpv_Functions(self, w):
            self.rmpv_btn(w)

class Update():
    def __init__(self):
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
        w.rmpu_f2_btn_u.clicked.connect(lambda: self.rmpu_next_step(w, w.rmpu_stackedWidget.currentIndex(),'UNIT'))
        w.rmpu_f2_btn_um.clicked.connect(lambda: self.rmpu_next_step(w, w.rmpu_stackedWidget.currentIndex(),'measure'))
        w.rmpu_f2_btn_v.clicked.connect(lambda: self.rmpu_next_step(w, w.rmpu_stackedWidget.currentIndex(),'VALUE'))
        w.rmpu_f3_btn_stk.clicked.connect(lambda: self.rmpu_next_step(w, w.rmpu_stackedWidget.currentIndex(),'STOCK'))
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
            if (self.current_Widget == 'ID'):
                self.tool_tip = 'PRODUCT ID'
            elif (self.current_Widget == 'PRODUCT'):
                self.tool_tip = 'PRODUCT NAME'
            elif (self.current_Widget == 'DESCRIPTION'):
                self.tool_tip = 'PRODUCT DESCRIPTION'
            elif (self.current_Widget == 'UNIT'):
                self.tool_tip = 'Quantity'
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
        slct_data1 = None
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
        w.rmpd_slct_btn.clicked.connect(lambda: search_data(w.rmpd_slct_src.text(), w.rmpd_f_tree, self.data))
    
            
    def rmpd_next_step(self, w):
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
            

    #INIT FUNCTIONS
    def rmpd_Functions(self, w):
            self.rmpd_btn(w)
