from Config import dataconfig
from Pages.basemethod import MyGenericMethods
from Pages.dashboard import LocatorNavbar
from Pages.loc_profile_setting import LocatorSettingProfile
from Pages.loc_profile_setting import LocatorLogin

class StepDefProfileSetting(MyGenericMethods, LocatorNavbar, LocatorSettingProfile, LocatorLogin):
    def __init__(self, driver):
        super().__init__(driver)

    def Type_Name(self):
        self.find_element(LocatorSettingProfile.LOC_USERNAME_FIELD)
        self.clear_field(LocatorSettingProfile.LOC_USERNAME_FIELD)
        self.sendkeys_to(LocatorSettingProfile.LOC_USERNAME_FIELD, "Rania")

    def User_Logout(self):
        self.click_to(LocatorNavbar.LOC_LOGOUT)

    def Assert_Success_Logout(self):
        self.User_Logout()
        self.find_element()"""nunggu locator dari khairun"""

