from selenium.webdriver.common.by import By

class LocatorMainContent:
    # LOC_TEACHER_WELCOME_TITLE = (By.XPATH, '//div[@class="pageHeading"]/p/em')
    # LOC_MODAL_INPUT_EMAIL = (By.XPATH, '//div[@class="modal-content email-change-modal"]')
    pass

class LocatorSidebar:
    pass

class LocatorNavbar:
    pass

class LocatorFooter:
    LOC_COPYRIGHT_TXT = (By.XPATH, '//div[@class="MuiStack-root joy-13011bp"]/span')
    LOC_TERMOFUSE_TXT = (By.XPATH, "//a[text()='Terms Of Use' or text()='Syarat Ketentuan Penggunaan']")
    LOC_PRIVACYPOLCY_TXT = (By.XPATH, "//a[text()='Kebijakan Privasi' or text()='Privacy Policy']")
    pass
