from seleniumpagefactory import PageFactory

class SkillgunStudentDashboard(PageFactory):
    def __init__(self,driver):
        self.driver = driver
    locators={
        'newplacement':('id','ContentPlaceHolder1_ahrefnewdrive'),
        'interschedules':('id','ContentPlaceHolder1_ahrefInterview'),
    }
    def click_newplacement(self):
        self.newplacement.click()
    def click_interschedules(self):
        self.interschedules.click()


