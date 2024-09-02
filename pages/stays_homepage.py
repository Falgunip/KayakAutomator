import time

from selenium.webdriver.common.by import By

from utilities.utilities import WebDriverUtils
from base.base_driver import BaseDriver

class StaysHomepage(BaseDriver):
    def __init__(self,driver, WebDriverUtils =WebDriverUtils):
        super().__init__(driver)
        self.utils = WebDriverUtils(driver)

    # Locators:
    OPEN_STAYS_PAGE_LINK = "//a[@aria-label='Search for hotels ']"
    SEARCH_VALUE_FIELD = "//input[@placeholder='Enter a city, hotel, airport or landmark']"
    SELECT_LOCATION_FROM_AUTOSUGGESTION_DROPDOWN = "//div[@class='c2u5p c2u5p-mod-spacing-base']//ul//li"
    CALENDAR_VISIBILITY = "//div[@class='sGVi sGVi-dropdown-content']"
    NEXT_MONTH_ARROW_BUTTON = '//div[@aria-label="Next Month"]'
    MONTH_YEAR_DISPLAY = "//table[@class='or3C or3C-wrapper']//caption"
    ALL_DATES = "//tbody//tr[@class='or3C-week or3C-grid']//td//div[@class='vn3g-button']"
    VERIFY_ROOM_GUESTS_POPUP = "//div[@class='KIGt-counter']"
    ROOMS_INCREMENT_LOCATOR_BUTTON = "//div[@class='T_3c']//button[@aria-disabled='false']"
    ROOMS_INPUT_LOCATOR = "//input[@class='T_3c-input']"
    ADULTS_INCREMENT_LOCATOR_BUTTON = "//div[@class='KIGt-counter']//div[2]//div[@class='T_3c']//button[2]"
    ADULTS_INPUT_LOCATOR = "//span[text()='Adults']/following::input[@aria-label='Adults' and @class='T_3c-input']"
    CHILDREN_INCREMENT_LOCATOR_BUTTON = "//div[@class='KIGt-counter']//div[3]//following::button[@aria-disabled = 'false']"
    CHILDREN_INPUT_LOCATOR = "//input[@aria-label='Children']"
    AGE_OF_CHILD_POPUP = "//div[@class='KIGt-childrenAges']"
    GET_AGE_OF_CHILD_DROPDOWN = "//div[@role='combobox']"
    GET_AGE_OF_CHILD_DROPDOWN_OPTIONS = "//ul[@role='listbox']//li"
    SELECTED_AGE_VALUE = "//span[@class='Uczr-select-title Uczr-mod-alignment-left']"
    SEARCH_BUTTON = "//button[@aria-label='Search']//div[@class='RxNS-button-content']"

    def opens_stayspage_link(self):
        """
        Click on stays link
        :return:
        """
        return self.utils.click_element(By.XPATH, self.OPEN_STAYS_PAGE_LINK)

    def get_searchvalue_field(self):
        """
        Get element of Search value field
        :return:
        """
        return self.utils.wait_for_visibility_of_element(By.XPATH, self.SEARCH_VALUE_FIELD)

    def enter_searchvalue(self, location_partial):
        """
        Enter search value in search field
        :param value: The value to enter in the search field.
        :return: The entered value in the search field.
        """
        self.get_searchvalue_field().click()
        self.get_searchvalue_field().send_keys(location_partial)
        return self.get_searchvalue_field()


    def select_location_from_autosuggestion(self, location):
        """
        Select value from auto suggestion
        :param desired_value:
        :return:
        """
        return self.utils.select_value_from_auto_suggestion(By.XPATH,self.SELECT_LOCATION_FROM_AUTOSUGGESTION_DROPDOWN, location)

    def verify_selectedvalue(self):
       """
       Verify selected value
       :return:
       """
       return self.utils.wait_for_visibility_of_element(By.XPATH,self.SEARCH_VALUE_FIELD)

    def verify_calendar_visibility(self):
        """
        Verify calendar visibility
        :return:
        """
        return self.utils.wait_for_visibility_of_element(By.XPATH,self.CALENDAR_VISIBILITY)

    def get_next_month_arrow_element(self):
        """
        Get next arrow element
        :return:
        """
        return self.utils.wait_for_visibility_of_element(By.XPATH, self.NEXT_MONTH_ARROW_BUTTON)

    def navigate_to_month(self,target_month_year):
        """
         Navigate to the specified month by clicking on the next arrow and waiting for the month to change.
        :param target_month_year: The target month and year to navigate to.
        :return: True if the month and year are successfully changed, False otherwise.
        """
        while True:
            month_year_display = self.utils.wait_for_visibility_of_element(By.XPATH, self.MONTH_YEAR_DISPLAY)
            current_month_year = month_year_display.text

            if target_month_year in current_month_year:
                break
            else:
                self.get_next_month_arrow_element().click()
                time.sleep(1)
        return current_month_year

    def select_check_in_and_check_out(self, check_in, check_out):
        """
        Select planned start and end dates on the calendar
        :param planned_startdate:
        :param planned_enddate:
        :return: start and end date
        """
        all_dates = self.utils.wait_for_visibility_of_elements(By.XPATH,self.ALL_DATES)
        start_date,end_date = None,None
        for date_element in all_dates:
            date = date_element.get_attribute("aria-label")
            if check_in in date:
                start_date = date
                date_element.click()
                time.sleep(1)  # Ensure date selection is complete
                break

        for date_element in all_dates:
            date = date_element.get_attribute("aria-label")
            if check_out in date:
                end_date = date
                date_element.click()
                break

        return start_date, end_date

    def verify_room_guests_popup(self):
        """
        Verify room - guests popup is displayed
        :return:
        """
        return self.utils.wait_for_visibility_of_element(By.XPATH,self.VERIFY_ROOM_GUESTS_POPUP)

    def select_rooms(self, rooms):
        """
        Select desired number of rooms in the room - guests popup
        :param desired_rooms:
        return: current value of rooms
        """
        value = self.utils.increment_value(
            increment_button_locator = self.ROOMS_INCREMENT_LOCATOR_BUTTON,
            input_locator = self.ROOMS_INPUT_LOCATOR ,
            targeted_value = rooms
        )
        return value


    def select_adults(self, adults):
        """
        Select desired number of adults in the room - guests popup
        :param targeted_adults:
        :return:  current value of adults
        """
        value = self.utils.increment_value(
            increment_button_locator = self.ADULTS_INCREMENT_LOCATOR_BUTTON,
            input_locator = self.ADULTS_INPUT_LOCATOR,
            targeted_value=adults
        )
        return value

    def select_children(self, children):
        """
        Select desired number of children in the room - guests popup
        :param targeted_children:
        :return:
        """
        value = self.utils.increment_value(
            increment_button_locator =self.CHILDREN_INCREMENT_LOCATOR_BUTTON,
            input_locator = self.CHILDREN_INPUT_LOCATOR,
            targeted_value=children
        )
        return value

    def verify_age_of_child_option_popup(self):
        """
        Verify age of child option is displayed
        :return:
        """
        return self.utils.wait_for_visibility_of_element(By.XPATH, self.AGE_OF_CHILD_POPUP)

    def get_age_of_child_dropdown(self):
        """
        Click on age of child dropdown
        :return:
        """
        return self.utils.click_element(By.XPATH, self.GET_AGE_OF_CHILD_DROPDOWN )

    def select_age_of_child(self, age_of_child):
        """
        Select desired age of child in age of child dropdown
        :param desired_age:
        :return:
        """
        # list = self.utils.wait_for_visibility_of_element(By.XPATH, "//ul[@role='listbox']")
        dropdown_options = self.utils.wait_for_visibility_of_elements(By.XPATH, self.GET_AGE_OF_CHILD_DROPDOWN_OPTIONS)
        for option in dropdown_options:
            if option.text ==  age_of_child:
                option.click()
                break
        time.sleep(1)
        selected_age = self.utils.wait_for_visibility_of_element(By.XPATH, self.SELECTED_AGE_VALUE )
        return selected_age

    def click_search_button(self):
        """
        Click on search button
        :return:
        """
        return self.utils.click_element(By.XPATH,self.SEARCH_BUTTON )

    def search_hotels(self, location_partial, location, target_month_year, check_in, check_out, rooms, adults, children,  age_of_child):
        self.enter_searchvalue(location_partial)
        self.select_location_from_autosuggestion(location)
        self.verify_selectedvalue()
        self.verify_calendar_visibility()
        self.navigate_to_month(target_month_year)
        self.select_check_in_and_check_out(check_in, check_out)
        self.verify_room_guests_popup()
        self.select_rooms(rooms)
        self.select_adults(adults)
        self.select_children(children)
        self.verify_age_of_child_option_popup()
        self.get_age_of_child_dropdown()
        self.select_age_of_child(age_of_child)
        self.click_search_button()


