from seleniumpagefactory import PageFactory

class SkillgunNewPlacementPage(PageFactory):
    def __init__(self,driver):
        self.driver=driver
    locators= {
        'gohome':('xpath','//*[@id="content"]/div[1]/div[1]/div/div/div/div/div[2]/fieldset/div[2]/div/a')
    }

    def click_gohome(self):
        self.gohome.click()


