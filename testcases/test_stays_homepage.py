import time

import pytest
from pages.stays_homepage import StaysHomepage

@pytest.mark.usefixtures("setup")
class TestStaysHomepage:
    """Tests for the Stays homepage."""

    def test_search_hotels(self):
        """Test the title of the Stays homepage."""
        driver = self.driver

        objstays = StaysHomepage(driver)
         # Stays page will open
        objstays.opens_stayspage_link()

        # Verify the title of the page
        expected_title = 'Places to Stay: Find Accommodation Deals & Discounts - KAYAK'
        assert driver.title == expected_title
        print("Title verified successfully!")

        objstays.search_hotels(
            location_partial="New",
            location='New Orleans',
            target_month_year='February 2025',
            check_in = 'February 1, 2025',
            check_out='March 15, 2025',
            rooms='2',
            adults='4',
            children='1',
            age_of_child='2')

        # Verify the correct keyword is entered or not
        # enter_keyword = objstays.enterSearchValue("New")
        # entered_value = enter_keyword.get_attribute('value')
        # assert entered_value == "New"
        #
        # # Verify the user selects a preferred location or not
        # time.sleep(10)
        # selected_value = objstays.selectValueFromAutosuggestion('New Orleans')
        # verify_selected_value = objstays.verifySelectedValue()
        # assert 'New Orleans' in verify_selected_value.get_attribute('value')
        # print("Desired value selected successfully from auto-suggestions")
        #
        # # Verify the calendar is visible or not
        # calendar_visibility = objstays.verifyCalendarVisibility()
        # assert calendar_visibility.is_displayed()
        #
        # # Verify the user navigates to the targeted month or not
        # navigate_to_target_month = objstays.navigateToMonth('February 2025')
        # assert 'February 2025'  == navigate_to_target_month
        # print("User successfully navigates to the targeted month")
        #
        # # Verify the user selects a planned dates or not
        # select_planned_dates = objstays.selectStartdateAndEnddate('February 1, 2025', 'March 15, 2025')
        # assert 'February 1, 2025' in select_planned_dates[0]
        # assert 'March 15, 2025' in select_planned_dates[1]
        # print("Planned dates are selected")
        #
        # # Verify room and guests popup is displayed or not
        # verify_room_guests_popup = objstays.verifyRoomGuestsPopup()
        # assert verify_room_guests_popup.is_displayed()
        #
        # # Verify the user selects a preferred number of rooms or not
        # targeted_rooms = objstays.selectRooms('2')
        # assert targeted_rooms == '2'
        # print("Use has selected preferred rooms")
        #
        # # Verify the user selects a preferred number of adults or not
        # targeted_adults = objstays.selectAdults('4')
        # assert targeted_adults == '4'
        # print('Use has selected preferred adults')
        #
        # # Verify the user selects a preferred number of children or not
        # targeted_children = objstays.selectChildren('1')
        # assert targeted_children == '1'
        # print('Use has selected preferred children')
        #
        # # Verify Age of Child option is visible or not
        # age_of_child_option = objstays.verifyAgeOfChildOptionPopup()
        # assert age_of_child_option.is_displayed()
        #
        # objstays.getAgeOfChildDropdown()
        #
        # # Verify user has selected preferred child age or not
        # age_of_child = objstays.selectAgeOfChild('2')
        # assert age_of_child.text == '2'
        # print("Use has selected preferred children's age")
        #
        # objstays.clickSearchButton()
        # time.sleep(10)




