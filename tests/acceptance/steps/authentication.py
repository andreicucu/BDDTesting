# from selenium import webdriver
# from behave import *
# from tests.acceptance.locators.login_page import LoginPageLocators
# from tests.acceptance.locators.cm import CMLocators
# from tests.testData import loginData as sdt
# import time
#
# # using regex from behave library for matching steps below
# use_step_matcher('re')
#
# @given('I am presented with the login page')
# def step_impl(context):
#     chromePath = 'C:/Users/andrei.cucu/PycharmProjects/udemy/BDD/chromedriver.exe'
#     context.driver = webdriver.Chrome(chromePath)
#     context.driver.maximize_window()
#     context.driver.implicitly_wait(30)
#     context.driver.get(sdt['url'])
#     assert context.driver.title == 'Softdial Login'
#
#
# @when('I click fill the tenant, username, password and hit enter')
# def step_impl(context):
#     """
#     using locators package (dependent on Selenium By class to pass the tuples
#     * for unpacking the tuple for find_element method
#
#     """
#     context.driver.find_element(*LoginPageLocators.TENANT).send_keys(sdt['tenant'])
#     context.driver.find_element(*LoginPageLocators.USERNAME).send_keys(sdt['user'])
#     context.driver.find_element(*LoginPageLocators.PASSWORD).send_keys(sdt['pwd'])
#     context.driver.find_element(*LoginPageLocators.LANGUAGE).click()
#     context.driver.find_element(*LoginPageLocators.LANGUAGEOPTION).click()
#     context.driver.find_element(*LoginPageLocators.LOGINBTN).click()
#     time.sleep(5)
#
# @then('I am presented with the Sytel options')
# def step_imp(context):
#     """
#     i am presented with authentication options
#     and select campaign Manager
#     """
#     assert context.driver.title == 'Softdial Startpage 10.6.807'
#     context.driver.find_element(*CMLocators.CMBTN).click()