import time
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from .base_page import BasePage
from .locators import TournamentPageLocators


class TournamentPage(BasePage):
    def should_be_tournament_title(self, title):
        tournament_title = self.find_element_wait(TournamentPageLocators.TOURNAMENT_TITLE)
        actual_tournament_title = tournament_title.text
        # This construction doesn't work if there's more than one tournament
        # WHOLE LOGIC SHOULD BE REWRITTEN
        assert actual_tournament_title == title, f"Tournament title is {actual_tournament_title}, should be {title}"

    def create_nomination(self, title, weapon_id, fight_time, last_round_time):
        # Switch tab to Nominations
        self.click_button(TournamentPageLocators.NOMINATIONS_TAB)

        # Create nomination
        self.click_button(TournamentPageLocators.CREATE_NOMINATION_BUTTON)

        # Enter a title of the nomination
        self.fill_input(TournamentPageLocators.NOMINATION_TITLE_FIELD, title)

        # Choose a weapon
        self.fill_select_by_index(TournamentPageLocators.WEAPON_SELECT, weapon_id)

        # ADD RADIO BUTTONS HANDLING

        # Set fight time
        self.fill_input(TournamentPageLocators.FIGHT_TIME_INPUT, fight_time)

        # Set last round time
        self.fill_input(TournamentPageLocators.LAST_ROUND_TIME_INPUT, last_round_time)

        # Save nomination
        self.click_button(TournamentPageLocators.SAVE_NOMINATION_BUTTON)

        time.sleep(1)

    def open_nomination(self):
        # Switch tab to Nominations
        self.click_button(TournamentPageLocators.NOMINATIONS_TAB)

        # Open nomination
        self.click_button(TournamentPageLocators.NOMINATION_LINK)

    def open_stages_tab(self):
        self.click_button(TournamentPageLocators.STAGES_TAB)

    def open_rings_tab(self):
        self.click_button(TournamentPageLocators.RINGS_TAB)

    def create_stage(self, type_id=1, to_the_finals=False, fight_time=120, go_next_stage=8,
                     playoff_finals_mode=None, playoff_third_place=None,
                     swiss_empty_win=None, swiss_win_points=None, hits_initial_hp=None, hits_limit_hp=None):
        self.open_nomination()
        self.open_stages_tab()

        # Create stage
        self.click_button(TournamentPageLocators.ADD_STAGE_BUTTON)

        # Choose type: pools, playoff, swiss system or swiss system with hits
        if type_id == 1:
            self.click_button(TournamentPageLocators.TYPE_RADIO_POOLS)
        elif type_id == 2:
            self.click_button(TournamentPageLocators.TYPE_RADIO_PLAYOFF)
        elif type_id == 3:
            self.click_button(TournamentPageLocators.TYPE_RADIO_SWISS)
        elif type_id == 4:
            self.click_button(TournamentPageLocators.TYPE_RADIO_SWISS_HITS)
        else:
            raise Exception("No such option: type id can only be 1 / 2 / 3 / 4")

        # Choose option: to the finals or not
        if to_the_finals:
            self.click_button(TournamentPageLocators.TO_THE_FINALS_TRUE)
        else:
            self.click_button(TournamentPageLocators.TO_THE_FINALS_FALSE)

        # Set fight time
        self.fill_input(TournamentPageLocators.FIGHT_TIME_FIELD, fight_time)

        # Only for not finals: choose how many participants go to next stage
        if not to_the_finals:
            self.fill_input(TournamentPageLocators.GOES_NEXT_STAGE_FIELD, go_next_stage)

        # Only for pools: unlimited pool option
        # ADD SLIDER HANDLING

        if type_id == 2 and to_the_finals:
            # Choose finals mode: best of 1 or best of 3
            if playoff_finals_mode == 1:
                self.click_button(TournamentPageLocators.PLAYOFF_FINALS_MODE_1)
            elif playoff_finals_mode == 3:
                self.click_button(TournamentPageLocators.PLAYOFF_FINALS_MODE_3)
            else:
                raise Exception("No such option: finals mode can be best of 1 or best of 3")
            # Choose if there will be a fight for the 3rd place
            if playoff_third_place:
                self.click_button(TournamentPageLocators.PLAYOFF_THIRD_PLACE_TRUE)
            else:
                self.click_button(TournamentPageLocators.PLAYOFF_THIRD_PLACE_FALSE)

        # Only for Swiss system and Swiss system with hits: choose how to handle an empty fight
        if type_id == 3 or type_id == 4:
            if swiss_empty_win:
                self.click_button(TournamentPageLocators.SWISS_EMPTY_FIGHT_RESULT_WIN)
                self.fill_input(TournamentPageLocators.SWISS_EMPTY_WIN_POINTS, swiss_win_points)
            else:
                self.click_button(TournamentPageLocators.SWISS_EMPTY_FIGHT_RESULT_DRAW)

        # Only for Swiss system with hits: set initial value and limit of HP
        if type_id == 4:
            self.fill_input(TournamentPageLocators.HITS_INITIAL_HP, hits_initial_hp)
            self.fill_input(TournamentPageLocators.HITS_LIMIT_HP, hits_limit_hp)

        # Save stage
        self.click_button(TournamentPageLocators.SAVE_STAGE_BUTTON)

        if type_id == 3 or type_id == 4:
            self.wait_for_element(TournamentPageLocators.ENROLL_ALL_TO_SWISS)

    def add_participants(self, number):
        self.open_nomination()

        # Open tab Participants
        self.click_button(TournamentPageLocators.PARTICIPANTS_TAB)

        # Choose number of test participants
        self.fill_input(TournamentPageLocators.PARTICIPANTS_NUMBER_INPUT, number)

        # Enroll test participants
        self.click_button(TournamentPageLocators.ENROLL_TEST_PARTICIPANTS_BUTTON)

        # Wait until test participants are added
        self.wait_for_element(TournamentPageLocators.PARTICIPANT_LINE)

        # Full approve all participants
        self.click_button(TournamentPageLocators.FULL_APPROVE_BUTTON)
        self.confirm_alert()

        # Wait until all test participants are approved
        WebDriverWait(self.browser, 10).until(
            EC.text_to_be_present_in_element(TournamentPageLocators.ACCEPTED_NUMBER, number)
        )

    def create_ring(self, title):
        # Switch to tab Rings
        self.open_rings_tab()

        # Create ring
        self.click_button(TournamentPageLocators.ADD_RING_BUTTON)

        # Set ring title
        self.fill_input(TournamentPageLocators.RING_TITLE_FIELD, title)

        # Save ring
        self.click_button(TournamentPageLocators.SAVE_RING_BUTTON)

    def create_pools(self, number):
        self.open_nomination()
        self.open_stages_tab()
        # Create pools
        for i in range(number):
            add_pool_button = WebDriverWait(self.browser, 5, poll_frequency=0.5).until(
                EC.element_to_be_clickable(TournamentPageLocators.ADD_POOL_BUTTON)
            )
            try:
                add_pool_button.click()
            except ElementClickInterceptedException:
                time.sleep(3)
                add_pool_button.click()
            time.sleep(0.2)

    def add_participants_to_pool(self):
        """self.open_nomination()
        self.open_stages_tab()"""
        # Seed random participants
        self.click_button(TournamentPageLocators.SEED_RANDOM_PARTICIPANTS_BUTTON)

    def set_ring_for_pool(self):
        """self.open_nomination()
        self.open_stages_tab()"""
        # Set ring
        self.fill_input(TournamentPageLocators.RING_TITLE_FIELD, "Ring" + Keys.ENTER)

    def delete_pools(self, number):
        """self.open_nomination()
        self.open_stages_tab()"""
        for i in range(number):
            self.click_button(TournamentPageLocators.REMOVE_POOL_BUTTON)
            self.confirm_alert()
            time.sleep(0.3)
        self.wait_for_element(TournamentPageLocators.REMOVE_POOLS_STAGE_BUTTON)

    def create_playoff(self, fight_time, finals_mode, third_place):
        """self.open_nomination()
        self.open_stages_tab()"""
        self.create_stage(type_id=2, to_the_finals=True, fight_time=fight_time,
                          playoff_finals_mode=finals_mode, playoff_third_place=third_place)

    def delete_playoff_stages(self, number):
        """self.open_nomination()
        self.open_stages_tab()"""
        fights_number = 2 ** math.ceil(math.log2(number))
        print("calculated fights number:", fights_number)
        fights = self.find_multiple_elements_wait(TournamentPageLocators.REMOVE_PLAYOFF_BUTTON)
        print("real fights number:", len(fights))
        for i in range(fights_number):
            self.click_button(TournamentPageLocators.REMOVE_PLAYOFF_BUTTON)
            self.confirm_alert()
            time.sleep(0.3)
        self.wait_for_element(TournamentPageLocators.REMOVE_PLAYOFF_STAGE_BUTTON)

    def delete_playoff(self):
        """self.open_nomination()
        self.open_stages_tab()"""
        self.click_button(TournamentPageLocators.REMOVE_PLAYOFF_STAGE_BUTTON)
        self.confirm_alert()

    def add_participants_to_swiss(self):
        """self.open_nomination()
        self.open_stages_tab()"""
        # Enroll all participants
        self.click_button(TournamentPageLocators.ENROLL_ALL_TO_SWISS)

    def set_ring_for_pairs(self):
        """self.open_nomination()
        self.open_stages_tab()"""
        # ONLY WORKS WITH ONE RING, FIX NEEDED
        self.click_button(TournamentPageLocators.ALLOCATE_RINGS_BUTTON)
        self.click_button(TournamentPageLocators.ADD_UNALLOCATED_TO_RING)
        self.click_button(TournamentPageLocators.CLOSE_SWISS_SETTINGS_BUTTON)

    def change_pairs(self):
        """self.open_nomination()
        self.open_stages_tab()"""
        self.click_button(TournamentPageLocators.CHANGE_PAIRS_BUTTON)
        drag_zones = self.find_multiple_elements_wait(TournamentPageLocators.DRAG_ZONES)
        drag_items = self.find_multiple_elements_wait(TournamentPageLocators.DRAG_ITEMS)
        actions = ActionChains(self.browser)
        # DOESN'T WORK, ONLY HIGHLIGHT TEXT FOR SOME REASON, FIX NEEDED
        actions.drag_and_drop(drag_items[0], drag_zones[1]).perform()
        self.click_button(TournamentPageLocators.CLOSE_SWISS_SETTINGS_BUTTON)

    def delete_pools_stage(self):
        """self.open_nomination()
        self.open_stages_tab()"""
        self.click_button(TournamentPageLocators.REMOVE_POOLS_STAGE_BUTTON)
        self.confirm_alert()
        self.wait_for_element(TournamentPageLocators.NO_STAGES_TITLE)

    def delete_nomination(self):
        self.open_nomination()
        self.click_button(TournamentPageLocators.REMOVE_NOMINATION_BUTTON)
        self.confirm_alert()
        self.wait_for_element(TournamentPageLocators.NO_STAGES_TITLE)

    def delete_ring(self):
        self.open_rings_tab()
        # Wait until page is switched to rings
        self.wait_for_element(TournamentPageLocators.ANY_RING_LINE)
        # Delete ring
        self.click_button(TournamentPageLocators.REMOVE_RING_BUTTON)
        self.confirm_alert()
