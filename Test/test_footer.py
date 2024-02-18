import pytest
from StepsDefinition.step_footer import StepDefFooter
from StepsDefinition.step_navbar import StepDefNavbarAllRole

@pytest.mark.usefixtures("setup_scope_class")
class TestFooterUi:

    def test_verify_theres_copyright(self):
        footer = StepDefFooter(self.driver)
        # this row will be place the step for login user
        footer.check_copyright_is_visible()

    def test_verify_copyright_text_is_correct(self):
        footer = StepDefFooter(self.driver)
        # this row will be place the step for login user
        footer.check_copyright_text_is_correct()

    def test_verify_theres_termsofuse(self):
        footer = StepDefFooter(self.driver)
        # this row will be place the step for login user
        footer.check_terms_of_use_is_visible()

    def test_verify_termsofuse_text_indo_is_correct(self):
        footer = StepDefFooter(self.driver)
        navbar = StepDefNavbarAllRole(self.driver)
        # this row will be place the step for login user
        navbar.change_language_to_indonesia()
        footer.check_terms_of_use_text_indo()

    def test_verify_termsofuse_text_english_is_correct(self):
        footer = StepDefFooter(self.driver)
        navbar = StepDefNavbarAllRole(self.driver)
        # this row will be place the step for login user
        navbar.change_language_to_english()
        footer.check_terms_of_use_text_english()

    def test_verify_theres_privacypolicy(self):
        footer = StepDefFooter(self.driver)
        # this row will be place the step for login user
        footer.check_privacy_policy_is_visible()

    def test_verify_privacypolicy_text_indo_is_correct(self):
        footer = StepDefFooter(self.driver)
        navbar = StepDefNavbarAllRole(self.driver)
        # this row will be place the step for login user
        navbar.change_language_to_indonesia()
        footer.check_privacy_policy_text_indo()

    def test_verify_privacypolicy_text_english_is_correct(self):
        footer = StepDefFooter(self.driver)
        navbar = StepDefNavbarAllRole(self.driver)
        # this row will be place the step for login user
        navbar.change_language_to_english()
        footer.check_privacy_policy_text_english()


@pytest.mark.usefixtures("setup_scope_function")
class TestFooterFunctionality:

    def test_click_termsofuse_text(self):
        footer = StepDefFooter(self.driver)
        footer.click_terms_of_use()
        # this row will be placing assertion at terms of use page

    def test_click_privacy_text(self):
        footer = StepDefFooter(self.driver)
        footer.click_privacy_policy()
        # this row will be placing assertion at terms of use page


