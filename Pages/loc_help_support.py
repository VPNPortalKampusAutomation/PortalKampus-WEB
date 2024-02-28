
from selenium.webdriver.common.by import By

class LocatorCategory:
    LOC_TITTLE_CATEGORY = (By.XPATH, '(//p[normalize-space()="Profile"])[1]')
    LOC_ICON_CATEGORY = (By.XPATH, '(//div[@class="HelpCenter_boxIcon__86dv2"])[2]')
    LOC_CARD_CATEGORY = (By.XPATH, '(//button[@class="MuiButtonBase-root MuiCardActionArea-root joy-fmtgi3"])[1]')
    LOC_SEARCH_BAR = (By.XPATH, '(//input[@placeholder="Search help center" or @placeholder="Cari pusat bantuan"])[1]')

class LocatorFAQ:
    LOC_TOPIC_LIST = (By.XPATH, '//p[@class="MuiTypography-root MuiTypography-title-sm joy-1goy8p5"]')
    LOC_TITTLE_TOPIC = (By.XPATH, '//p[@class="MuiTypography-root MuiTypography-title-lg joy-llt9fo"]')
    LOC_FAQ_EMPTY = (By.XPATH, '//div[@class="HelpCenter_categoryEmptyWrapper__sVmIg"]')
    LOC_VIDEO_TAB = (By.XPATH, '//button[@id=":r8:"]')
    LOC_FAQ_TAB = (By.XPATH, '//button[@id=":r7:"]')
