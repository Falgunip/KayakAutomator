import time

from selenium.webdriver.common.by import By

from utilities.utilities import WebDriverUtils
from base.base_driver import BaseDriver

class StaysHomepage(BaseDriver):
    def __init__(self,driver, WebDriverUtils =WebDriverUtils):
        super().__init__(driver)
        self.utils = WebDriverUtils(driver)

    def open_stayspage(self):
        """
        Click on stays link
        :return:
        """
        return self.utils.click_element(By.XPATH, "//a[@aria-label='Search for hotels ']")

    def enter_value(self,value):
        """
        Enter value in search bar
        :param value: value
        :return:
        """
        entered_value = self.utils.wait_for_visibility_of_element(By.XPATH, "//input[@placeholder='Enter a city, hotel, airport or landmark']")
        entered_value.send_keys(value)
        return entered_value

    def select_value_from_autosuggestion(self, desired_value):
        """
        Select value from auto suggestion
        :param desired_value:
        :return:
        """
        return self.utils.select_value_from_auto_suggestion(By.XPATH,"//div[@class='c2u5p c2u5p-mod-spacing-base']//ul//li", desired_value)

    def verify_selected_value(self):
       """
       Verify selected value
       :return:
       """
       return self.utils.wait_for_visibility_of_element(By.XPATH,"//input[@placeholder ='Enter a city, hotel, airport or landmark']")

    def calendar_visibility(self):
        """
        Verify calendar visibility
        :return:
        """
        return self.utils.wait_for_visibility_of_element(By.XPATH,"//div[@class='sGVi sGVi-dropdown-content']")

    def navigate_to_month(self,target_month_year):
        """
         Navigate to the specified month by clicking on the next arrow and waiting for the month to change.
        :param target_month_year: The target month and year to navigate to.
        :return: True if the month and year are successfully changed, False otherwise.
        """
        next_arrow = self.utils.wait_for_visibility_of_element(By.XPATH, '//div[@aria-label="Next Month"]')
        while True:
            month_year_display = self.utils.wait_for_visibility_of_element(By.XPATH, "//table[@class='or3C or3C-wrapper']//caption")
            current_month_year = month_year_display.text

            if target_month_year in current_month_year:
                break
            else:
                next_arrow.click()
                time.sleep(1)
        return current_month_year

    def select_startdate_and_enddate(self, planned_startdate, planned_enddate):
        """
        Select planned start and end dates on the calendar
        :param planned_startdate:
        :param planned_enddate:
        :return: start and end date
        """
        all_dates = self.utils.wait_for_visibility_of_elements(By.XPATH,"//tbody//tr[@class='or3C-week or3C-grid']//td//div[@class='vn3g-button']")
        start_date, end_date = None,None
        for date_element in all_dates:
            date = date_element.get_attribute("aria-label")
            if planned_startdate in date:
                start_date = date
                date_element.click()
                time.sleep(1)  # Ensure date selection is complete
                break

        for date_element in all_dates:
            date = date_element.get_attribute("aria-label")
            if planned_enddate in date:
                end_date = date
                date_element.click()
                break

        return start_date, end_date

    def verify_room_guests_popup(self):
        """
        Verify room - guests popup is displayed
        :return:
        """
        return self.utils.wait_for_visibility_of_element(By.XPATH,"//div[@class='KIGt-counter']")

    def select_rooms(self, targeted_rooms):
        """
        Select desired number of rooms in the room - guests popup
        :param desired_rooms:
        return: current value of rooms
        """
        value = self.utils.increment_value(
            increment_button_locator = "//div[@class='T_3c']//button[@aria-disabled='false']",
            input_locator = "//input[@class='T_3c-input']",
            targeted_value = targeted_rooms
        )
        return value


    def select_adults(self, targeted_adults):
        """
        Select desired number of adults in the room - guests popup
        :param targeted_adults:
        :return:  current value of adults
        """
        value = self.utils.increment_value(
            increment_button_locator="//div[@class='KIGt-counter']//div[2]//div[@class='T_3c']//button[2]",
            input_locator="//span[text()='Adults']/following::input[@aria-label='Adults' and @class='T_3c-input']",
            targeted_value=targeted_adults
        )
        return value

    def select_children(self, targeted_children):
        """
        Select desired number of children in the room - guests popup
        :param targeted_children:
        :return:
        """
        value = self.utils.increment_value(
            increment_button_locator="//div[@class='KIGt-counter']//div[3]//following::button[@aria-disabled = 'false']",
            input_locator="//input[@aria-label='Children']",
            targeted_value=targeted_children
        )
        return value

    def verify_age_of_child_option(self):
        """
        Verify age of child option is displayed
        :return:
        """
        return self.utils.wait_for_visibility_of_element(By.XPATH, "//div[@class='KIGt-childrenAges']")

    def age_of_child_dropdown_click(self):
        """
        Click on age of child dropdown
        :return:
        """
        return self.utils.click_element(By.XPATH, "//div[@role='combobox']")

    def select_age_of_child(self, desired_age):
        """
        Select desired age of child in age of child dropdown
        :param desired_age:
        :return:
        """
        list = self.utils.wait_for_visibility_of_element(By.XPATH, "//ul[@role='listbox']")
        dropdown_options = self.utils.wait_for_visibility_of_elements(By.XPATH,"//ul[@role='listbox']//li")
        for option in dropdown_options:
            if option.text == desired_age:
                option.click()
                break
        time.sleep(1)
        selected_age = self.utils.wait_for_visibility_of_element(By.XPATH, "//span[@class='Uczr-select-title Uczr-mod-alignment-left']")
        return selected_age

    def click_search_button(self):
        """
        Click on search button
        :return:
        """
        return self.utils.click_element(By.XPATH, "//button[@aria-label='Search']//div[@class='RxNS-button-content']")


