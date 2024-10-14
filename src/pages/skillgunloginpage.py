from seleniumpagefactory import PageFactory


class SkillgunLoginpage(PageFactory):
    def __init__(self,driver):
        self.driver=driver
    locators ={
        'mobile':('id','ContentPlaceHolder1_tbPhoneNumber'),
        'email' :('id','ContentPlaceHolder1_tbEmail'),
        'pw':('id','ContentPlaceHolder1_tbPassword'),
        'cb':('id','ckbkPolicyAgreement'),
        'login':('id','ContentPlaceHolder1_btnLogin'),

    }
    def enter_mobile(self,mobileno):
        self.mobile.send_keys(mobileno),
    def enter_email(self,emailid):
        self.email.send_keys(emailid)
    def enter_pw(self,password):
        self.pw.send_keys(password)
    def click_cb(self):
        self.cb.click()
    def click_login(self):
        self.login.click()