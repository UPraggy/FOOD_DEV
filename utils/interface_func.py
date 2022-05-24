from utils.INTERFACE_FUNCIONALITIES import rm
from PyQt5 import QtCore
from numpy import isin
class Interface():
    def __init__(self):
        current_page = None
        self.init_zoom = -1
        self.const_aux_zoom = 0.4
        self.control_zoom = 1
        self.current_op = None
        self.initial_run = [x for x in range(1, 13)]

    def loading_funcs_client(self, w):
        self.switch_page(w.lm_stackedWidget,w.lmc)
        #CLIENT MENU BUTTONS
        w.lmc_btn_r.clicked.connect(lambda: self.load_rm(w, 'rmcr'))
        w.lmc_btn_v.clicked.connect(lambda: self.load_rm(w, 'rmcv'))
        w.lmc_btn_u.clicked.connect(lambda: self.load_rm(w, 'rmcu'))
        w.lmc_btn_d.clicked.connect(lambda: self.load_rm(w, 'rmcd'))
        w.lmc_btn_m.clicked.connect(lambda: self.switch_main(w))
        

    def loading_funcs_product(self, w):
        self.switch_page(w.lm_stackedWidget,w.lmp)
        #PRODUCT MENU BUTTONS
        w.lmp_btn_r.clicked.connect(lambda: self.load_rm(w, 'rmpr'))
        w.lmp_btn_s.clicked.connect(lambda: self.load_rm(w, 'rmpv'))
        w.lmp_btn_u.clicked.connect(lambda: self.load_rm(w, 'rmpu'))
        w.lmp_btn_d.clicked.connect(lambda: self.load_rm(w, 'rmpd'))
        w.lmp_btn_m.clicked.connect(lambda: self.switch_main(w))


    def loading_funcs_order(self, w):
        self.switch_page(w.lm_stackedWidget,w.lmo)
        #PRODUCT MENU BUTTONS
        w.lmo_btn_do.clicked.connect(lambda: self.load_rm(w, 'rmor'))
        w.lmo_btn_v.clicked.connect(lambda: self.load_rm(w, 'rmov'))
        w.lmo_btn_u.clicked.connect(lambda: self.load_rm(w, 'rmou'))
        w.lmo_btn_d.clicked.connect(lambda: self.load_rm(w, 'rmod'))
        w.lmo_btn_m.clicked.connect(lambda: self.switch_main(w))

    def load_rm(self, w, operation):
        if (operation[:3] == 'rmc'):
            if (operation == 'rmcr'):
                self.current_op = rm.Rmc_Register()
                self.current_op.rmcr_init(w, 0)
                if (isin(1, self.initial_run)):
                    self.initial_run[0] = None
                    self.current_op.rmcr_Functions(w) 
            elif (operation == 'rmcv'):
                self.current_op = rm.Rmc_View()
                self.current_op.rmcv_init(w) 
                if (isin(2, self.initial_run)):
                    self.initial_run[1] = None
                    self.current_op.rmcv_Functions(w) 
            elif (operation == 'rmcu'):
                self.current_op = rm.Rmc_Update()
                self.current_op.rmcu_init(w, 0)
                if (isin(3, self.initial_run)):
                    self.initial_run[2] = None
                    self.current_op.rmcu_Functions(w) # UPDATE
            elif (operation == 'rmcd'):
                self.current_op = rm.Rmc_Delete()
                self.current_op.rmcd_init(w, 0) 
                if (isin(4, self.initial_run)):
                    self.initial_run[3] = None
                    self.current_op.rmcd_Functions(w) 


        elif (operation[:3] == 'rmp'):
            if (operation == 'rmpr'):
                self.current_op = rm.Rmp_Register()
                self.current_op.rmpr_init(w, 0)
                if (isin(5, self.initial_run)):
                    self.initial_run[4] = None  
                    self.current_op.rmpr_Functions(w)
            elif (operation == 'rmpv'):
                self.current_op = rm.Rmp_View()
                self.current_op.rmpv_init(w, 0)
                if (isin(6, self.initial_run)): 
                    self.initial_run[5] = None 
                    self.current_op.rmpv_Functions(w) 
            elif (operation == 'rmpu'):
                self.current_op = rm.Rmp_Update()
                self.current_op.rmpu_init(w, 0)
                if (isin(7, self.initial_run)):
                    self.initial_run[6] = None  
                    self.current_op.rmpu_Functions(w) 
            elif (operation == 'rmpd'):
                self.current_op = rm.Rmp_Delete()
                self.current_op.rmpd_init(w, 0) 
                if (isin(8, self.initial_run)):
                    self.initial_run[7] = None 
                    self.current_op.rmpd_Functions(w) 

        elif (operation[:3] == 'rmo'):
            if (operation == 'rmor'):
                self.current_op = rm.Rmo_Register()
                self.current_op.rmor_init(w, 0)  
                if (isin(9, self.initial_run)):
                    self.initial_run[8] = None
                    self.current_op.rmor_Functions(w)
            elif (operation == 'rmov'):
                self.current_op = rm.Rmo_View()
                self.current_op.rmov_init(w, 0) 
                if (isin(10, self.initial_run)): 
                    self.initial_run[9] = None
                    self.current_op.rmov_Functions(w) 
            elif (operation == 'rmou'):
                self.current_op = rm.Rmo_Update()
                self.current_op.rmou_init(w, 0)
                if (isin(11, self.initial_run)): 
                    self.initial_run[10] = None 
                    self.current_op.rmou_Functions(w) 
            elif (operation == 'rmod'):
                self.current_op = rm.Rmo_Delete()
                self.current_op.rmod_init(w, 0)
                if (isin(12, self.initial_run)): 
                   self.initial_run[11] = None 
                   self.current_op.rmod_Functions(w)
        
    def setzoom(self):
        if (self.control_zoom == 1):
            if (self.init_zoom == 1):
                self.const_aux_zoom = self.const_aux_zoom - 0.2
            elif (self.init_zoom == 2):
                self.const_aux_zoom = self.const_aux_zoom - 0.06
            elif (self.init_zoom == 3):
                self.const_aux_zoom = self.const_aux_zoom - 0.04
            elif (self.init_zoom == 4):
                self.const_aux_zoom = self.const_aux_zoom - 0.02
            elif (self.init_zoom == 5 or self.init_zoom == 6):
                self.const_aux_zoom = self.const_aux_zoom - 0.01
            elif (self.init_zoom > 6 and self.init_zoom < 12):
                self.const_aux_zoom = self.const_aux_zoom - 0.005
            elif (self.init_zoom > 12):
                self.const_aux_zoom = self.const_aux_zoom - 0.000019
            self.control_zoom = 0

    def zoom_scale(self, w, type_zoom):
        if (type_zoom == 'm'):
            zoom = w.rma_f1_web.zoomFactor() + self.const_aux_zoom 
        else:
            zoom = w.rma_f1_web.zoomFactor() - self.const_aux_zoom
        w.rma_f1_web.setZoomFactor(zoom)
        
    def loading_funcs_about(self, w):
        self.switch_page(w.rm_stackedWidget,w.rma)
        url = 'https://upraggy.github.io/FOOD_DEV/'
        w.rma_f1_web.setZoomFactor(0.85)
        w.rma_f1_web.load(QtCore.QUrl(url))
        self.control_zoom = 1
        self.init_zoom += 1
        self.setzoom()
        #ABOUT MAIN BUTTON
        w.rma_f1_fb_btn_b.clicked.connect(lambda:  w.rma_f1_web.back())
        w.rma_f1_fb_btn_m.clicked.connect(lambda: w.rma_f1_web.load(QtCore.QUrl(url)))
        w.rma_f1_fb_btn_zl.clicked.connect(lambda: self.zoom_scale(w, 'l'))
        w.rma_f1_fb_btn_zm.clicked.connect(lambda: self.zoom_scale(w, 'm'))
        

    def loading_funcs_main(self, loading_funcs = ' ', w = ' '):
        if (loading_funcs == 'c'):
            self.loading_funcs_client(w)
        elif (loading_funcs == 'p'):
            self.loading_funcs_product(w)
        elif (loading_funcs == 'o'):
            self.loading_funcs_order(w)
        elif (loading_funcs == 'a'):
            self.loading_funcs_about(w)

    def switch_page(self, stacked, page):
        stacked.setCurrentWidget(page)

    def switch_main(self, w):
        self.switch_page(w.lm_stackedWidget,w.lmm)
        self.switch_page(w.rm_stackedWidget,w.rmm)
        
    def functionalties(self, w):
        #INITIALIZATE
        init = 1
        if (init == 1):
            self.switch_page(w.lm_stackedWidget,w.lmm)
            self.switch_page(w.rm_stackedWidget,w.rmm)
            init = 0
        #LATERAL MENU OPTONS
        #MAIN MENU
        w.lmm_btn_c.clicked.connect(lambda: self.loading_funcs_main('c', w))
        w.lmm_btn_o.clicked.connect(lambda: self.loading_funcs_main('o', w))
        w.lmm_btn_p.clicked.connect(lambda: self.loading_funcs_main('p', w))
        w.lmm_btn_about.clicked.connect(lambda: self.loading_funcs_main('a', w))
    #BACK
        w.lmo_btn_m.clicked.connect(lambda: self.switch_page(w.lm_stackedWidget,w.lmm))
        w.lmp_btn_m.clicked.connect(lambda: self.switch_page(w.lm_stackedWidget,w.lmm))

