import pytest
from StepsDefinition.step_footer import StepDefFooter

@pytest.mark.usefixtures("setup_scope_function")
class TestFooter:

    def __init__(self):
        self.footer = StepDefFooter(self.driver)

    def test_verify_theres_copyright(self):
        # this row will be place the step for login user
        self.footer.check_copyright_is_visible()

    def test_verify_copyright_text_is_correct(self):
        # this row will be place the step for login user
        self.footer.check_copyright_text_is_correct()

    def test_verify_theres_termsofuse(self):
        # this row will be place the step for login user
        self.footer.check_terms_of_use_is_visible()

    def test_verify_termsofuse_text_indo_is_correct(self):
        # this row will be place the step for login user
        self.footer.check_terms_of_use_text_indo()

    def test_verify_termsofuse_text_english_is_correct(self):
        # this row will be place the step for login user
        # this row will be place step for change language in navbar
        self.footer.check_terms_of_use_text_english()





