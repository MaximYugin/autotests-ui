from playwright.sync_api import Page, expect

from components.authentication.registration_form_component import RegistrationFormComponent
from elements.button import Button
from elements.text import Text
from pages.base_page import BasePage


class RegistrationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.registration_form = RegistrationFormComponent(page)

        self.registration_button = Button(page, 'registration-page-registration-button', 'Registration')
        self.dashboard_title = Text(page, 'dashboard-toolbar-title-text', 'Dashboard')

    def click_registration_button(self):
        self.registration_button.click()

    def check_visible_dashboard_title(self):
        self.dashboard_title.check_visible()
