from selenium import webdriver
from behave import *
from tests.acceptance.locators.login_page import LoginPageLocators
from tests.acceptance.locators.cm import CMLocators
from tests.testData import loginData as sdt
import time
from tests.testData import campaignData as cmdt
from tests.testData import tabNumber as tno


print(CMLocators.TABS[0], CMLocators.TABS[1].format(tno[4]))

# using regex from behave library for matching steps below
use_step_matcher('re')

@given('I am presented with the login page')
def step_impl(context):
    chromePath = 'C:/Users/andrei.cucu/PycharmProjects/udemy/BDD/chromedriver.exe'
    context.driver = webdriver.Chrome(chromePath)
    context.driver.maximize_window()
    context.driver.implicitly_wait(30)
    context.driver.get(sdt['url'])
    assert context.driver.title == 'Softdial Login'


@given('I click fill the tenant, username, password and hit enter')
def step_impl(context):
    """
    using locators package (dependent on Selenium By class to pass the tuples
    * for unpacking the tuple for find_element method

    """
    context.driver.find_element(*LoginPageLocators.TENANT).send_keys(sdt['tenant'])
    context.driver.find_element(*LoginPageLocators.USERNAME).send_keys(sdt['user'])
    context.driver.find_element(*LoginPageLocators.PASSWORD).send_keys(sdt['pwd'])
    context.driver.find_element(*LoginPageLocators.LANGUAGE).click()
    context.driver.find_element(*LoginPageLocators.LANGUAGEOPTION).click()
    context.driver.find_element(*LoginPageLocators.LOGINBTN).click()
    time.sleep(3)

@given('I am presented with the Sytel options')
def step_imp(context):
    """
    i am presented with authentication options
    and select campaign Manager
    """
    assert context.driver.title == 'Softdial Startpage 10.6.807'
    context.driver.find_element(*CMLocators.CMBTN).click()


@given('User is in the campaign manager web application')
def step_impl(context):
    assert context.driver.title == 'Campaign Manager 10.6.807 on 208.64.5.164'

@when('New button is pressed')
def step_impl(context):
    context.driver.find_element(*CMLocators.NEWBTN).click()

@when('Campaign name is filled')
def step_impl(context):
    context.driver.find_element(*CMLocators.CAMPNAME).send_keys(cmdt['cname'])
    # sends click to campaign type tuple's second value after passing 0 into the radio btn value

@when('Campaign type is selected')
def step_impl(context):
    context.driver.find_element(CMLocators.CAMPTYPE[0], CMLocators.CAMPTYPE[1].format(0)).click()
    # navigate to third tab (id 2)
    context.driver.find_element(CMLocators.TABS[0], CMLocators.TABS[1].format(tno[2])).click()
    context.driver.find_element(*CMLocators.CTLayer).send_keys(cmdt['tellayer'])

@when('Database Input is given')
def step_impl(context):
    # navigate to fifth tab (id 4)
    context.driver.find_element(CMLocators.TABS[0], CMLocators.TABS[1].format(tno[5])).click()
    context.driver.find_element(*CMLocators.DSN).click()
    context.driver.find_element(*CMLocators.DSNOPT).click()
    context.driver.find_element(*CMLocators.DSNUSER).send_keys(cmdt['dsnuser'])
    context.driver.find_element(*CMLocators.DSNPWD).send_keys(cmdt['dsnpass'])
    context.driver.find_element(*CMLocators.DSNVERIFY).click()


@when('Database Fields are selected')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element(*CMLocators.TABLE).click()
    context.driver.find_element(*CMLocators.TABLEOPT).click()
    context.driver.find_element(*CMLocators.PHONECOL).click()
    context.driver.find_element(*CMLocators.PHONEOPT).click()
    context.driver.find_element(*CMLocators.UNIQCOL).click()
    context.driver.find_element(*CMLocators.UNIQCOLOPT).click()

@when('Ok button is pressed')
def step_impl(context):
    context.driver.find_element(*CMLocators.OKBTN).click()


@then('Campaign should be visible')
def step_impl(context):
    pass