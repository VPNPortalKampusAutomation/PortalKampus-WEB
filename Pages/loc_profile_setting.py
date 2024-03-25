from selenium.webdriver.common.by import By


class LocatorSettingProfile:
    LOC_PICTURE_UPLOADER = (By.XPATH, '//div[@class="MuiBox-root joy-lu7srx"]')
    LOC_MESSAGE_PROFPIC = (By.XPATH, '//div[@class="MuiGrid-root MuiGrid-direction-xs-row joy-lzsbcd"]')
    LOC_USERNAME_FIELD = (By.XPATH, '//input[@id=":r6:"]')
    LOC_GENERAL_TAB = (By.XPATH, 'id=":r3:"')
    LOC_SELECT_NATIONALITY = (By.XPATH, '//button[@id=":r2s:"]')
    LOC_NIK_FIELD = (By.XPATH, 'id=":r2u:"')
    LOC_MOTHER_NAME = (By.XPATH, '(//div[contains(@class,"MuiInput-root MuiInput-variantOutlined")])[5]')
    LOC_ADDRESS_KTP = (By.XPATH, '(//div[contains(@class,"MuiTextarea-root MuiTextarea-variantOutlined")])[1]')
    LOC_CURRENT_ADDRESS = (By.XPATH, '(//div[contains(@class,"MuiTextarea-root MuiTextarea-variantOutlined")])[2]')
    LOC_PHONE_NUMBER = (By.XPATH, '(//div[contains(@class,"MuiInput-root MuiInput-variantOutlined")])[6]')
    LOC_EMAIL_ADDRESS = (By.XPATH, '(//div[contains(@class,"MuiInput-root MuiInput-variantOutlined")])[7]')
    LOC_CHECKBOX = (By.XPATH, '//input[@id=":r2g:"]')

class DropdownReligion:
    LOC_SELECT_RELIGION = (By.XPATH, '//button[@id=":r2v:"]')
    LOC_DROPDOWN_ISLAM = (By.XPATH, '//li[@id=":r1g:"]')
    LOC_DROPDOWN_PROTESTAN = (By.XPATH, 'id=":r1h:"')
    LOC_DROPDOWN_KATOLIK = (By.XPATH, '//li[@id=":r1i:"]')
    LOC_DROPDOWN_BUDHA = (By.XPATH, '//li[@id=":r1j:"]')
    LOC_DROPDOWN_HINDU = (By.XPATH, '//li[@id=":r1k:"]')

class DropdownBloodType:
     LOC_DROPDOWN_BLOODTYPE = (By.XPATH, '(//div[contains(@class,"MuiSelect-root MuiSelect-variantOutlined")])[3]')
     LOC_BLOODTYPE_APLUS = (By.XPATH, '//li[@id=":r1l:"]')



