from Config import dataconfig
from Pages.basemethod import MyGenericMethods
from Pages.loc_dashboard_page import LocatorNavbar
from Pages.loc_profile_setting import LocatorNavbarProfile
from Pages.loc_profile_setting import LocatorSettingProfile

class StepDefNavbarAllRole(MyGenericMethods, LocatorNavbar, LocatorNavbarProfile, LocatorSettingProfile):
    def __init__(self, driver):
        super().__init__(driver)

    def Type_Name(self):
        self.find_element(LocatorSettingProfile.LOC_USERNAME_FIELD)
        self.clear_field(LocatorSettingProfile.LOC_USERNAME_FIELD)
        self.sendkeys_to(LocatorSettingProfile.LOC_USERNAME_FIELD, "Rania")

        
