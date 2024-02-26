from Config import dataconfig
from Pages.basemethod import MyGenericMethods
from Pages.dashboard import LocatorNavbar
from Pages.loc_profile_setting import LocatorSettingProfile
from Pages.loc_profile_setting import LocatorLogin

class StepDefNavbarAllRole(MyGenericMethods, LocatorNavbar, LocatorSettingProfile, LocatorLogin):
    def __init__(self, driver):
        super().__init__(driver)

    def Type_Name(self):
        self.find_element(LocatorSettingProfile.LOC_USERNAME_FIELD)
        self.clear_field(LocatorSettingProfile.LOC_USERNAME_FIELD)
        self.sendkeys_to(LocatorSettingProfile.LOC_USERNAME_FIELD, "Rania")
    def Type_Email_Login(self):
        self.sendkeys_to(self.LocatorLogin.LOC_USERNAME, "yuyun.alsahri@gmail.com")
    def Type_Pass_Login(self):
        self.sendkeys_to(self.LOC_PASSWORD, "studentnoprofile2")
    def Click_button_Login(self):
        self.click_to(self.LOC_BUTTON_LOGIN)

