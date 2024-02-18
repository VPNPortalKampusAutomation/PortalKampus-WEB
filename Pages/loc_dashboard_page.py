from selenium.webdriver.common.by import By


class LocatorNavbar:
    LOC_DROPDOWN_LANGUANGE = (By.XPATH, "/html[1]/body[1]/nav[1]/div[1]/div[2]/button[1]/*[name()='svg'][1]")
    LOC_ENGLISH_SELECT= (By.XPATH, "//p[@class='MuiTypography-root MuiTypography-body-sm joy-1bdd33t']")
    LOC_INDONESIA_SELECT = (By.XPATH, "//li[@id=':rn:']//div[@class='MuiStack-root joy-1ryzfwd']")

class LocatorMainContentAdminUniversity:
    pass

class LocatorMainContentAdminFaculty:
    pass

class LocatorMainContentAdminMajor:
    pass

class LocatorMainContentLecturer:
    pass

class LocatorMainContentStudent:
    pass

class LocatorSidebar:
    pass

class LocatorFooter:
    LOC_COPYRIGHT_TXT = (By.XPATH, '//div[@class="MuiStack-root joy-13011bp"]/span')
    LOC_TERMOFUSE_TXT = (By.XPATH, "//a[text()='Terms of Use' or text()='Syarat Ketentuan Penggunaan']")
    LOC_PRIVACYPOLCY_TXT = (By.XPATH, "//a[text()='Kebijakan Privasi' or text()='Privacy Policy']")
