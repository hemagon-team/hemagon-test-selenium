from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
from .locators import TournamentPageLocators


class TournamentPage(BasePage):
    def should_be_tournament_title(self, title):
        tournament_title = WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located(TournamentPageLocators.TOURNAMENT_TITLE)
        )
        actual_tournament_title = tournament_title.text
        # This construction doesn't work if there's more than one tournament
        # WHOLE LOGIC SHOULD BE REWROTE
        assert actual_tournament_title == title, f"Tournament title is {actual_tournament_title}, should be {title}"

    def create_nomination(self, title, weapon_id, fight_time, last_round_time):
        # Switch tab to Nominations
        nominations_tab = WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located(TournamentPageLocators.NOMINATIONS_TAB)
        )
        nominations_tab.click()
        # Create nomination
        create_nominations_button = WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located(TournamentPageLocators.CREATE_NOMINATION_BUTTON)
        )
        create_nominations_button.click()
        # Enter a title of the nomination
        nomination_title_field = WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located(TournamentPageLocators.NOMINATION_TITLE_FIELD)
        )
        nomination_title_field.send_keys(title)
        # Choose a weapon
        weapon_select = Select(self.browser.find_element(*TournamentPageLocators.WEAPON_SELECT))
        weapon_select.select_by_index(weapon_id)
        # ADD RADIO BUTTONS HANDLING
        # Set fight time
        fight_time_input = self.browser.find_element(*TournamentPageLocators.FIGHT_TIME_INPUT)
        fight_time_input.send_keys(fight_time)
        # Set last round time
        last_round_time_input = self.browser.find_element(*TournamentPageLocators.LAST_ROUND_TIME_INPUT)
        last_round_time_input.send_keys(last_round_time)
        # Save nomination
        save_nomination_button = self.browser.find_element(*TournamentPageLocators.SAVE_NOMINATION_BUTTON)
        save_nomination_button.click()

    def open_nomination(self):
        # Switch tab to Nominations
        nominations_tab = WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located(TournamentPageLocators.NOMINATIONS_TAB)
        )
        nominations_tab.click()
        # Open nomination
        nomination_link = WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located(TournamentPageLocators.NOMINATION_LINK)
        )
        nomination_link.click()

    def open_stages_tab(self):
        # stages_tab = self.browser.find_element(*TournamentPageLocators.STAGES_TAB)
        stages_tab = WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located(TournamentPageLocators.STAGES_TAB)
        )
        stages_tab.click()

    def create_stage(self, type_id, to_the_finals, fight_time, go_next_stage,
                     playoff_size=None, swiss_empty_win=None, hits_initial_hp=None, hits_limit_hp=None):
        self.open_nomination()
        self.open_stages_tab()
        # Create stage
        # add_stage_button = self.browser.find_element(*TournamentPageLocators.ADD_STAGE_BUTTON)
        add_stage_button = WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located(TournamentPageLocators.ADD_STAGE_BUTTON)
        )
        add_stage_button.click()
        # Choose type4 / 8 / 16 / 32 / 64
        # Choose type4 / 8 / 16 / 32 / 64
        # ADD RADIO BUTTONS HANDLING
        # Choose option: to the finals or not
        if to_the_finals:
            to_the_finals_input = self.browser.find_element(*TournamentPageLocators.TO_THE_FINALS_TRUE)
        else:
            to_the_finals_input = self.browser.find_element(*TournamentPageLocators.TO_THE_FINALS_FALSE)
        to_the_finals_input.click()
        # Set fight time
        fight_time_field = self.browser.find_element(*TournamentPageLocators.FIGHT_TIME_FIELD)
        fight_time_field.send_keys(fight_time)
        # Only for not finals: choose how many participants go to next stage
        if not to_the_finals:
            goes_next_stage_field = self.b
        # ADD RADIO BUTTONS HANDLING
        # Choose option: to the finals or not
        if to_the_finals:
            to_the_finals_input = self.browser.find_element(*TournamentPageLocators.TO_THE_FINALS_TRUE)
        else:
            to_the_finals_input = self.browser.find_element(*TournamentPageLocators.TO_THE_FINALS_FALSE)
        to_the_finals_input.click()
        # Set fight time
        fight_time_field = self.browser.find_element(*TournamentPageLocators.FIGHT_TIME_FIELD)
        fight_time_field.send_keys(fight_time)
        # Only for not finals: choose how many participants go to next stage
        if not to_the_finals:
            goes_next_stage_field = self.browser.find_element(*TournamentPageLocators.GOES_NEXT_STAGE_FIELD)
            goes_next_stage_field.send_keys(go_next_stage)
        # Only for pools: unlimited pool option
        # ADD SLIDER HANDLING
        # Only for playoff: choose playoff size (4 / 8 / 16 / 32 / 64)
        if playoff_size == 4:
            playoff_size_input = self.browser.find_element(*TournamentPageLocators.PLAYOFF_SIZE_4)
        elif playoff_size == 8:
            playoff_size_input = self.browser.find_element(*TournamentPageLocators.PLAYOFF_SIZE_8)
        elif playoff_size == 16:
            playoff_size_input = self.browser.find_element(*TournamentPageLocators.PLAYOFF_SIZE_16)
        elif playoff_size == 32:
            playoff_size_input = self.browser.find_element(*TournamentPageLocators.PLAYOFF_SIZE_32)
        elif playoff_size == 64:
            playoff_size_input = self.browser.find_element(*TournamentPageLocators.PLAYOFF_SIZE_64)
        else:
            raise Exception("No such option: playoff size can only be 4 / 8 / 16 / 32 / 64")
        playoff_size_input.click()
        # Only for Swiss system and Swiss system with hits: choose how to handle an empty fight
        if swiss_empty_win:
            swiss_empty_input = self.browser.find_element(*TournamentPageLocators.SWISS_EMPTY_FIGHT_RESULT_WIN)
        else:
            swiss_empty_input = self.browser.find_element(*TournamentPageLocators.SWISS_EMPTY_FIGHT_RESULT_DRAW)
        swiss_empty_input.click()
        # Only for Swiss system with hits: set initial value and limit of HP
        hits_initial_input = self.browser.find_element(*TournamentPageLocators.HITS_INITIAL_HP)
        hits_initial_input.send_keys(hits_initial_hp)
        hits_limit_input = self.browser.find_element(*TournamentPageLocators.HITS_LIMIT_HP)
        hits_limit_input.send_keys(hits_limit_hp)
        # Save stage
        save_stage_button = self.browser.find_element(*TournamentPageLocators.SAVE_STAGE_BUTTON)
        save_stage_button.click()

    def add_participants(self, number):
        self.open_nomination()
        # Open tab Participants
        participants_tab = self.browser.find_element(*TournamentPageLocators.PARTICIPANTS_TAB)
        participants_tab.click()
        # Choose number of test participants
        number_select = Select(self.browser.find_element(*TournamentPageLocators.PARTICIPANTS_NUMBER_SELECT))
        number_select.select_by_value(number)
        # Enroll test participants
        enroll_test_participants = self.browser.find_element(*TournamentPageLocators.ENROLL_TEST_PARTICIPANTS_BUTTON)
        enroll_test_participants.click()
        # Full approve all participants
        full_approve_button = self.browser.find_element(*TournamentPageLocators.FULL_APPROVE_BUTTON)
        full_approve_button.click()

    def create_pool(self):
        self.open_nomination()
        self.open_stages_tab()
        # Create pool
        add_pool_button = self.browser.find_element(*TournamentPageLocators.ADD_POOL_BUTTON)
        add_pool_button.click()

    def add_participants_to_pool(self):
        self.open_nomination()
        self.open_stages_tab()
        # Seed random participants
        seed_random_participants = self.browser.find_element(*TournamentPageLocators.SEED_RANDOM_PARTICIPANTS_BUTTON)
        seed_random_participants.click()

    def add_ring(self, title):
        # Switch to tab Rings
        rings_tab = self.browser.find_element(*TournamentPageLocators.RINGS_TAB)
        rings_tab.click()
        # Create ring
        add_ring_button = self.browser.find_element(*TournamentPageLocators.ADD_RING_BUTTON)
        add_ring_button.click()
        # Set ring title
        ring_title_field = self.browser.find_element(*TournamentPageLocators.RING_TITLE_FIELD)
        ring_title_field.send_keys(title)
        # Save ring
        save_ring_button = self.browser.find_element(*TournamentPageLocators.SAVE_RING_BUTTON)
        save_ring_button.click()
