from Config import dataconfig
from Pages.basemethod import MyGenericMethods
from Pages.privacypolicy import *

class StepDefPrivacyPolicyPage(MyGenericMethods, LocatorPrivacyPolicyAndTermsofUsePage):

    def __init__(self, driver):
        super().__init__(driver)

    def check_menu_kebijakan_privasi_is_visible(self):
        self.is_visible(self.LOC_MENU_KEBIJAKAN_PRIVASI)
        self.back_to_previous_page()

    def check_text_menu_kebijakan_privasi_is_correct(self):
        KebijakanPrivasi = self.get_element_text(self.LOC_MENU_KEBIJAKAN_PRIVASI)
        assert KebijakanPrivasi == 'Kebijakan Privasi', "Text Menu Tidak Sesuai"

    def check_menu_syaratketentuanpenggunaan_is_visible(self):
        self.is_visible(self.LOC_MENU_SYARAT_KETENTUAN_PENGGUNAAN)
        self.back_to_previous_page()

    def check_text_menu_syaratketentuanpenggunaan_is_correct(self):
        SyaratKetentuanPenggunaan = self.get_element_text(self.LOC_MENU_SYARAT_KETENTUAN_PENGGUNAAN)
        assert SyaratKetentuanPenggunaan == 'Syarat dan Ketentuan Penggunaan', "Text Menu Tidak Sesuai"