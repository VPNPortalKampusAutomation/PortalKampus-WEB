from selenium.webdriver.common.by import By


class LocatorPrivacyPolicyAndTermsofUsePage:
    LOC_MENU_KEBIJAKAN_PRIVASI = (By.XPATH, "//div[contains(@class, 'joy-j7qwjs')]/p[text()='Kebijakan Privasi']")
    LOC_MENU_SYARAT_KETENTUAN_PENGGUNAAN = (By.XPATH, "//div[contains(@class, 'joy-j7qwjs')]/p[text()='Syarat dan Ketentuan Penggunaan']")