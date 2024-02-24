from Config import dataconfig
from Pages.basemethod import MyGenericMethods
from Pages.dashboard import *
from Pages.privacypolicy import *

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












