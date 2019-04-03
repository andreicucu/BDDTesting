from selenium.webdriver.common.by import By


class LoginPageLocators:
    TENANT = (By.ID,'sd-login-tnt')
    USERNAME = (By.ID,'sd-login-usr')
    PASSWORD = (By.ID,'sd-login-pwd')
    LANGUAGE = (By.ID,'sd-login-lang')
    LANGUAGEOPTION = (By.XPATH,"//div[contains(text(),'English')]")
    LOGINBTN = (By.XPATH,'//button[contains(text(),"Login")]')