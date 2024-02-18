import pytest
from StepsDefinition.step_footer import StepDefFooter
from StepsDefinition.step_navbar import StepDefNavbarAllRole

@pytest.mark.usefixtures("setup_scope_function")
class TestFooter:

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





