# from behave import *
# from tests.acceptance.locators.cm import CMLocators
# from selenium import webdriver
# from tests.testData import campaignData as cmdt
# from tests.testData import tabNumber as tno
# import time
#
# use_step_matcher('re')
#
# @given('User is in the campaign manager web application')
# def step_impl(context):
#     assert context.driver.title == 'Campaign Manager 10.6.807 on 208.64.5.164'
#     time.sleep(5)
#
# @when('New button is pressed')
# def step_impl(context):
#     time.sleep(5)
#     context.driver.find_element(*CMLocators.CMBTN)
#     context.driver.find_element(*CMLocators.NEWBTN)
#
# @when('Campaign name is filled')
# def step_impl(context):
#     context.driver.find_element(*CMLocators.CAMPNAME).send_keys(cmdt['cname'])
#     # sends click to campaign type tuple's second value after passing 0 into the radio btn value
#
# @when('Campaign type is selected')
# def step_impl(context):
#     context.driver.find_element(*CMLocators.CAMPTYPE[1].format(0)).click()
#     # navigate to third tab (id 2)
#     context.driver.find_element(*CMLocators.TABS[1].format(tno[2])).click()
#     context.driver.find_element(*CMLocators.CTLayer).send_keys(cmdt['tellayer'])
#
# @when('Database Input is given')
# def step_impl(context):
#     # navigate to fifth tab (id 4)
#     context.driver.find_element(*CMLocators.TABS[1].format(tno[4])).click()
#     context.driver.find_element(*CMLocators.DSN).click()
#     time.sleep(5)
#     context.driver.find_element(*CMLocators.DSNOPT).click()
#     context.driver.find_element(*CMLocators.DSNUSER).send_keys(cmdt['dsnuser'])
#     context.driver.find_element(*CMLocators.DSNPWD).send_keys(cmdt['dsnpass'])
#     context.driver.find_element(*CMLocators.DSNVERIFY).click()
#
#
# @when('Database Fields are selected')
# def step_impl(context):
#     time.sleep(5)
#     context.driver.find_element(*CMLocators.TABLE).click()
#     context.driver.find_element(*CMLocators.TABLEOPT).click()
#     context.driver.find_element(*CMLocators.PHONECOL).click()
#     context.driver.find_element(*CMLocators.PHONEOPT).click()
#     context.driver.find_element(*CMLocators.UNIQCOL).click()
#     context.driver.find_element(*CMLocators.UNIQCOLOPT).click()
#
# @when('Ok button is pressed')
# def step_impl(context):
#     context.driver.find_element(*CMLocators.OKBTN).click()
#
#
# @then('Campaign should be visible')
# def step_impl(context):
#     pass
#
# # @then('Campaign can be started')
# # def step_impl(context):
# #     pass