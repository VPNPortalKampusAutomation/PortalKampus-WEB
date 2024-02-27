from selenium.webdriver.common.by import By


class LocatorLogin:
    LOC_UNIV_LOGO = (By.XPATH, '//img[@alt="logo of University"]')
    LOC_WELCOME_TEXT = (By.XPATH, '//h4[@class="MuiTypography-root MuiTypography-h4 joy-u0z7n0"]')
    LOC_USERNAME_FIELD = (By.XPATH, '//input[@id=":r0:"]')
    LOC_PASSWORD_FIELD = (By.XPATH, '//input[@id=":r1:"]')
    LOC_LOGIN_BUTTON = (By.XPATH, '//div[@class="MuiStack-root joy-wgvb8x"]/button[3]')