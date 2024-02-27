from selenium.webdriver.common.by import By


class LocatorNavbar:
    LOC_DROPDOWN_LANGUAGE = (By.XPATH, "//button[contains(@class, 'joy-10m9115')]")
    LOC_SELECT_IN = (By.XPATH, "//p[text()='ID']")
    LOC_SELECT_EN = (By.XPATH, "//p[text()='EN']")
    LOC_SELECTED_LANGUAGE_ID = (By.XPATH, "//button[contains(@class, 'joy-10m9115')]/img[contains(@srcset, 'indonesia_flag')]")  # assert contains : indonesia_flag | english_flag
    LOC_SELECTED_LANGUAGE_EN = (By.XPATH, "//button[contains(@class, 'joy-10m9115')]/img[contains(@srcset, 'english_flag')]")
    LOC_PROFILE_NAME = (By.XPATH, "//div[contains(@class, 'joy-1319j58')]/p")
    LOC_ROLE_NAME_OR_NIM = (By.XPATH, "//div[contains(@class, 'joy-1319j58')]/span")
    LOC_DROPDOWN_NAVBAR_PROFILE = (By.XPATH, "//button[contains(@class, 'joy-1bev472')]/div")
    LOC_SETTING_PROFILE = (By.XPATH, "//ul[@id=':r1:']/li[1]/div/p")
    LOC_HELPCENTER = (By.XPATH, "//ul[@id=':r1:']/li[2]/div/p")
    LOC_LOGOUT = (By.XPATH, "//ul[@id=':r1:']/li[3]/div/p")

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
