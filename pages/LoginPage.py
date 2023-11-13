from selenium.webdriver.common.by import By

class LoginPageLocators:
    LOGIN_BUTTON = (By.XPATH,'//*[@data-l="t,sign_in"]')
    QR_BUTTON = (By.XPATH,'//*[@data-l="t,get_qr"]')
    VK_ICON = (By.XPATH,'//*[@data-l="t,vkc"]')
    MAILRU_ICON = (By.XPATH,'//*[@data-l="t,mailru"]')
    GOOGLE_ICON = (By.XPATH,'//*[@data-l="t,google"]')
    APPLE_ICON = (By.XPATH, '//*[@data-l="t,apple"]')
    HEADER_LOGIN = (By.XPATH,'//*[@data-l="t,login_tab"]')
    HEADER_QR = (By.XPATH,'//*[@data-l="t,qr_tab"]')
    DATA_LINE = (By.XPATH,'//*[@id="field_email"]')
    PASSWORD_LINE = (By.XPATH,'//*[@name="st.password"]')
    SUPPORT_LINE = (By.XPATH,'//*[@data-l="t,restore"]')
    REGISTRATION_BUTTON = (By.XPATH,'//*[@class="button-pro __sec mb-3x"]')
