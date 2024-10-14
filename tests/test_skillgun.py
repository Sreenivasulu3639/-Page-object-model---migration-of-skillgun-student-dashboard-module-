from selenium import webdriver
import time

from src.pages.SkillgunNewPlacementPage import SkillgunNewPlacementPage
from src.pages.skillgunStudentDashboard import SkillgunStudentDashboard
from src.pages.skillgunloginpage import SkillgunLoginpage

driver = webdriver.Chrome()

def test_login():
    driver.get('http://skillgun.com')
    time.sleep(5)
    l = SkillgunLoginpage(driver)
    l.enter_mobile('6302483639')
    time.sleep(5)#wait for number validation
    l.enter_email('sreenivasulupinnepalli@gmail.com')
    l.enter_pw('Sreenu@8242')
    l.click_cb()
    time.sleep(10)#we can enter captcha
    l.click_login()
    time.sleep(5)#wait for next page to load
    assert 'Home' in driver.current_url

def test_new_placement():
    dashboard = SkillgunStudentDashboard(driver)
    dashboard.click_newplacement()
    time.sleep(5)
    assert 'NewPlacementDrive' in driver.current_url

def test_go_home_newplacements():
    placements = SkillgunNewPlacementPage(driver)
    placements.click_gohome()
    time.sleep(5)
    assert'Home' in driver.current_url

def test_inter_schedules():
    dashboard =SkillgunStudentDashboard(driver)
    dashboard.click_interschedules()
    time.sleep(5)
    assert'Interviews' in driver.current_url