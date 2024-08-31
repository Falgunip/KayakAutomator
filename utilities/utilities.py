import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WebDriverUtils:
    def __init__(self,driver,wait_time = 10):
        self.driver = driver
        self.wait = WebDriverWait(driver,wait_time)

    def wait_for_visibility_of_element(self, locator_type, locator):
        """
        Wait for element to appear on the page
        :param locator_type: The type of locator (e.g., By.ID, By.CSS_SELECTOR)
        :param locator: The actual locator value (e.g., the id or xpath of the element)
        :return: The WebElement once it is visible.
        """
        return self.wait.until(EC.visibility_of_element_located((locator_type,locator)))

    def wait_for_visibility_of_elements(self, locator_type, locator):
        """
        Wait for elements to appear on the page
        :param locator_type: The type of locator (e.g., By.ID, By.CSS_SELECTOR)
        :param locator: The actual locator value (e.g., the id or xpath of the element)
        :return: A list of WebElements once they are visible.
        """
        return self.wait.until(EC.visibility_of_all_elements_located((locator_type,locator)))

    def click_element(self, locator_type, locator):
        """
        Click on element
        :param locator_type: The type of locator (e.g., By.ID, By.CSS_SELECTOR)
        :param locator: The actual locator value (e.g., the id or xpath of the element)
        :return: element once clicked
        """
        element = self.wait_for_visibility_of_element(locator_type, locator)
        if element.is_displayed():
            element.click()
        return element

    def select_value_from_auto_suggestion(self, locator_type, locator, desired_value):
        """
        Select value from auto suggestion dropdown.
        :param locator_type: The type of locator (e.g., By.ID, By.CSS_SELECTOR).
        :param locator: The actual locator value (e.g., the id or xpath of the dropdown).
        :param desired_value: The value to be selected from the dropdown.
        :return: The WebElement of the selected value or None if not found.
        """
        search_results = self.wait_for_visibility_of_elements(locator_type, locator)

        # Check if any results were found
        if not search_results:
            print(f"No elements found with locator {locator} of type {locator_type}")
            return None

        print(f"Found {len(search_results)} auto-suggestions.")

        # Iterate through the elements and select the desired one
        for value in search_results:
            if desired_value in value.text:
                value.click()
                return value

        print(f"Desired value '{desired_value}' not found in the auto-suggestions.")
        return None

    def increment_value(self, increment_button_locator, input_locator, targeted_value):
        """
        Increment value in a numeric input field until the desired value is reached.
        :param increment_button_locator: The locator of the increment button.
        :param input_locator: The locator of the input field.
        :param targeted_value: The value to which the input field should be incremented.
        :return: The final value in the input field.
        """
        increment_button = self.wait_for_visibility_of_element(By.XPATH, increment_button_locator)
        while True:
            input = self.wait_for_visibility_of_element(By.XPATH, input_locator)
            current_value = input.get_attribute('value')
            if current_value == targeted_value:
                break
            else:
                increment_button.click()
                time.sleep(1)
        return current_value