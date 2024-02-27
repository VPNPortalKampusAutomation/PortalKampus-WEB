from Pages.basemethod import MyGenericMethods
from Pages.login import LocatorLogin
from Config.dataconfig import TestData


class StepLogin(MyGenericMethods, LocatorLogin, TestData):

    def __init__(self, driver):
        super().__init__(driver)

    def student_login(self):
        self.sendkeys_to(self.LOC_USERNAME_FIELD, self.STUDENT_EMAIL)
        self.sendkeys_to(self.LOC_PASSWORD_FIELD, self.VALID_PASSWORD)
        self.click_to(self.LOC_LOGIN_BUTTON)

    def lecturer_login(self):
        self.sendkeys_to(self.LOC_USERNAME_FIELD, self.LECTURER_EMAIL)
        self.sendkeys_to(self.LOC_PASSWORD_FIELD, self.VALID_PASSWORD)
        self.click_to(self.LOC_LOGIN_BUTTON)

    def major_login(self):
        self.sendkeys_to(self.LOC_USERNAME_FIELD, self.ADMIN_MAJOR_EMAIL)
        self.sendkeys_to(self.LOC_PASSWORD_FIELD, self.VALID_PASSWORD)
        self.click_to(self.LOC_LOGIN_BUTTON)

    def faculty_login(self):
        self.sendkeys_to(self.LOC_USERNAME_FIELD, self.ADMIN_FACULTY_EMAIL)
        self.sendkeys_to(self.LOC_PASSWORD_FIELD, self.VALID_PASSWORD)
        self.click_to(self.LOC_LOGIN_BUTTON)

    def university_login(self):
        self.sendkeys_to(self.LOC_USERNAME_FIELD, self.ADMIN_UNIVERSITY_EMAIL)
        self.sendkeys_to(self.LOC_PASSWORD_FIELD, self.VALID_PASSWORD)
        self.click_to(self.LOC_LOGIN_BUTTON)