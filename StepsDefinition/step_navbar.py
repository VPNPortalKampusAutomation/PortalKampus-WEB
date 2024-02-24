from Config import dataconfig
from Pages.basemethod import MyGenericMethods
from Pages.dashboard import LocatorNavbar

class StepDefNavbarAllRole(MyGenericMethods, LocatorNavbar):

    def __init__(self, driver):
        super().__init__(driver)

    def click_dropdown_language(self):
        self.click_to(self.LOC_DROPDOWN_LANGUAGE)

    def change_language_to_english(self):
        self.click_to(self.LOC_DROPDOWN_LANGUAGE)
        self.click_to(self.LOC_SELECT_EN)

    def change_language_to_indonesia(self):
        self.click_to(self.LOC_DROPDOWN_LANGUAGE)
        self.click_to(self.LOC_SELECT_IN)


'''-------------------------------------------------------------------------------------------'''

class StepDefNavbarAdminOrLecturer(StepDefNavbarAllRole):

    pass

'''-------------------------------------------------------------------------------------------'''

class StepDefNavbarStudent(StepDefNavbarAllRole):

    pass












