from selenium.webdriver.common.by import By


class LocatorNavbar:
    pass

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
