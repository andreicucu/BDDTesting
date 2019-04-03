from selenium.webdriver.common.by import By
from tests.testData import tabNumber as tno

class CMLocators:
    CMBTN = (By.XPATH,"//*[@id='CampaignManager']")
    NEWBTN = (By.XPATH,"//button[contains(text(),'New')]")
    # tab navigation - MUST pass tab text value with format
    TABS = (By.XPATH,"//span[contains(text(),'{}')]")
    CAMPNAME = (By.XPATH,"//input[@name='CampaignName']")
    # {Predictive=0, Progressive=1, Preview=2, Manual Outbound=3, Inbound=4, Inbound On-Hook=5}
    CAMPTYPE = (By.XPATH,"//input[@value='{}']")
    CTLayer = (By.XPATH,"//input[@name='CTLayerID']")
    DSN = (By.XPATH,"//input[@name='DSN']")
    # selects the BetterWRX DSN from the dropdown
    DSNOPT = (By.XPATH,"//div[contains(text(), 'BetterWRX') and contains(@class,'x-combo-list-item')]")
    DSNUSER = (By.NAME,'DBUser')
    DSNPWD = (By.NAME,'DBPassword')
    DSNVERIFY = (By.XPATH,"//button[contains(text(), 'Verify database connection')]")
    TABLE = (By.ID,'sd-cm-ed-dbin-colTable')
    TABLEOPT = (By.XPATH,"//div[contains(@class,'x-combo-list-item') and text()='Test']")
    PHONECOL = (By.ID,'sd-cm-ed-dbin-colTel')
    # xpath for selecting option from Phone dropdown, query is:
    # find the visible dropdown grandchild containing PHONE_NUME text and list_item class
    PHONEOPT = (By.XPATH,"//div[@class='x-layer x-combo-list ' and contains(@style,'visibility: visible')]/"
                         "child::div[@class='x-combo-list-inner']/"
                         "child::div[contains(@class,'x-combo-list-item') and text()='Phone']")
    CLICOL = (By.ID,'sd-cm-ed-dbin-colCLI')
    UNIQCOL = (By.ID,'sd-cm-ed-dbin-colKey')
    # same as Phone only new we pass ACCOUNT as UNIQUE column
    UNIQCOLOPT = (By.XPATH,"//div[@class='x-layer x-combo-list ' and contains(@style,'visibility: visible')]/child::div[@class='x-combo-list-inner']/child::div[contains(@class,'x-combo-list-item') and text()='ID']")
    OKBTN = (By.XPATH,"//table[@id='sd-cm-ed-btnOk']/tbody/tr[2]/td[2]/em/button[contains(text(),'OK')]")



# for t in tabNumber:
#     print(CMLocators.TABS[1].format(t))