from Config import dataconfig
from Pages.basemethod import MyGenericMethods
from Pages.loc_dashboard_page import *
from Pages.loc_privacy_and_terms_page import *

class StepDefAllRole(MyGenericMethods, LocatorMainContentAdminUniversity):
    pass

class StepDefContentAdmUniv(StepDefAllRole):
    pass

class StepDefContentAdmFaculty(StepDefAllRole):
    pass

class StepDefContentAdmMajor(StepDefAllRole):
    pass

class StepDefContentLecturer(StepDefAllRole):
    pass

class StepDefContentStudent(StepDefAllRole):
    pass












