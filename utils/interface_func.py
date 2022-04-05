from utils.INTERFACE_FUNCIONALITIES import rmc, rmp
class Interface():
    def __init__(self):
        current_page = None
    def loading_funcs_client(self, w):
        rmcr = rmc.Register()
        rmcv = rmc.View()
        rmcu = rmc.Update()
        rmcd = rmc.Delete()
        self.switch_page(w.lm_stackedWidget,w.lmc)
        #CLIENT MENU BUTTONS
        w.lmc_btn_r.clicked.connect(lambda: rmcr.rmcr_init(w, 0))
        w.lmc_btn_v.clicked.connect(lambda: rmcv.rmcv_init(w))
        w.lmc_btn_u.clicked.connect(lambda: rmcu.rmcu_init(w, 0))
        w.lmc_btn_d.clicked.connect(lambda: rmcd.rmcd_init(w, 0))
        w.lmc_btn_m.clicked.connect(lambda: self.switch_main(w))
        rmcr.rmcr_Functions(w)#REGISTER
        rmcv.rmcv_Functions(w) # VIEW
        rmcu.rmcu_Functions(w) # UPDATE
        rmcd.rmcd_Functions(w) # DELETE

    def loading_funcs_product(self, w):
        rmpr = rmp.Register()
        rmpv = rmp.View()
        rmpu = rmp.Update()
        rmpd = rmp.Delete()
        self.switch_page(w.lm_stackedWidget,w.lmp)
        #PRODUCT MENU BUTTONS
        w.lmp_btn_r.clicked.connect(lambda: rmpr.rmpr_init(w, 0))
        w.lmp_btn_s.clicked.connect(lambda: rmpv.rmpv_init(w, 0))
        w.lmp_btn_u.clicked.connect(lambda: rmpu.rmpu_init(w, 0))
        w.lmp_btn_d.clicked.connect(lambda: rmpd.rmpd_init(w, 0))
        w.lmp_btn_m.clicked.connect(lambda: self.switch_main(w))
        rmpr.rmpr_Functions(w)#REGISTER
        rmpv.rmpv_Functions(w) # VIEW
        rmpu.rmpu_Functions(w) # UPDATE
        rmpd.rmpd_Functions(w) # DELETE

    def loading_funcs_main(self, loading_funcs = ' ', w = ' '):
        if (loading_funcs == 'c'):
            self.loading_funcs_client(w)
        elif (loading_funcs == 'p'):
            self.loading_funcs_product(w)

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
        w.lmm_btn_o.clicked.connect(lambda: self.switch_page(w.lm_stackedWidget,w.lmp))
        w.lmm_btn_p.clicked.connect(lambda: self.loading_funcs_main('p', w))
    #BACK
        w.lmo_btn_m.clicked.connect(lambda: self.switch_page(w.lm_stackedWidget,w.lmm))
        w.lmp_btn_m.clicked.connect(lambda: self.switch_page(w.lm_stackedWidget,w.lmm))

