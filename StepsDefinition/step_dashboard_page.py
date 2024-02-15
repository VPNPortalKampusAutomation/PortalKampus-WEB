from Config import dataconfig
from Pages.basemethod import MyGenericMethods
from Pages.loc_dashboard_page import *
from Pages.loc_privacy_and_terms_page import *

class StepDefNavbar(MyGenericMethods, LocatorNavbar):
    pass

class StepDefSidebar(MyGenericMethods, LocatorSidebar):
    pass

class StepDefContentAdmUniv(MyGenericMethods, LocatorMainContentAdminUniversity):
    pass

class StepDefContentAdmFaculty(MyGenericMethods, LocatorMainContentAdminFaculty):
    pass

class StepDefContentAdmMajor(MyGenericMethods, LocatorMainContentAdminMajor):
    pass

class StepDefContentLecturer(MyGenericMethods, LocatorMainContentLecturer):
    pass

class StepDefContentStudent(MyGenericMethods, LocatorMainContentStudent):
    pass

class StepDefFooter(MyGenericMethods, LocatorFooter, LocatorPrivacyPolicyAndTermsofUse):

    def __init__(self, driver):
        super().__init__(driver)

    def check_terms_of_use_on_footer_indo(self):
        self.is_visible(self.LOC_TERMOFUSE_TXT)
        assert self.LOC_TERMOFUSE_TXT == "Syarat Ketentuan Penggunaan"

    def check_terms_of_use_on_footer_english(self):
        self.is_visible(self.LOC_TERMOFUSE_TXT)
        assert self.LOC_TERMOFUSE_TXT == "Terms of Use"

    def click_terms_of_use_on_footer(self):
        self.click_to(self.LOC_TERMOFUSE_TXT)

    def check_privacy_policy_on_footer_indo(self):
        self.is_visible(self.LOC_PRIVACYPOLCY_TXT)
        assert self.LOC_PRIVACYPOLCY_TXT == "Kebijakan Privasi"

    def check_privacy_policy_on_footer_english(self):
        self.is_visible(self.LOC_PRIVACYPOLCY_TXT)
        assert self.LOC_PRIVACYPOLCY_TXT == "Privacy Policy"

    def click_privacy_policy_on_footer(self):
        self.click_to(self.LOC_PRIVACYPOLCY_TXT)












