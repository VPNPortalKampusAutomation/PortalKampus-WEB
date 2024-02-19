from Config import dataconfig
from Pages.basemethod import MyGenericMethods
from Pages.loc_dashboard_page import LocatorNavbar

class StepDefNavbarAllRole(MyGenericMethods, LocatorNavbar):

    def __init__(self, driver):
        super().__init__(driver)

    def click_dropdown_language(self):
        self.click_to(self.LOC_DROPDOWN_LANGUANGE)

    def change_language_to_english(self):
        self.click_to(self.LOC_DROPDOWN_LANGUANGE)
        self.click_to(self.LOC_ENGLISH_SELECT)

    def change_language_to_indonesia(self):
        self.click_to(self.LOC_DROPDOWN_LANGUANGE)
        self.click_to(self.LOC_INDONESIA_SELECT)


'''-------------------------------------------------------------------------------------------'''

class StepDefNavbarAdminOrLecturer(StepDefNavbarAllRole):

    pass

'''-------------------------------------------------------------------------------------------'''

class StepDefNavbarStudent(StepDefNavbarAllRole):

    pass












