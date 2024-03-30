from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_BUTTON = (By.CSS_SELECTOR, ".user-block .btn.small")
    USER_NAME = (By.CSS_SELECTOR, ".name")
    MY_TOURNAMENTS_BUTTON = (By.CSS_SELECTOR, ".user-block .popover .name")


class LoginPageLocators:
    EMAIL_FIELD = (By.ID, "input-email")
    PASSWORD_FIELD = (By.ID, "input-password")
    LOGIN_BUTTON = (By.ID, "btn-login")


class OrganizerPageLocators:
    # Creating new tournament
    CREATE_TOURNAMENT_BUTTON = (By.ID, "btn-create-tournament")
    TEST_TOURNAMENT_INPUT = (By.ID, "input-tournament-test-true")
    TITLE_FIELD = (By.ID, "input-tournament-title")
    COUNTRY_FIELD = (By.CSS_SELECTOR, "#vs1__combobox > .vs__selected-options > input")
    CITY_FIELD = (By.CSS_SELECTOR, "#vs2__combobox > div.vs__selected-options > input")
    DESCRIPTION_FIELD = (By.ID, "input-tournament-description")
    SAVE_BUTTON = (By.ID, "btn-tournament-save")
    # Open tournament
    TOURNAMENT_BANNER = (By.CSS_SELECTOR, "#app > div > div:nth-child(2) > div"
                                          "> div:nth-child(6) > div > div > div:nth-child(3) > button")


class TournamentPageLocators:
    # Creating new nomination
    NOMINATIONS_TAB = (By.ID, "tournament-menu-nominations")
    CREATE_NOMINATION_BUTTON = (By.ID, "btn-nomination-add")
    NOMINATION_TITLE_FIELD = (By.ID, "input-nomination-title")
    WEAPON_SELECT = (By.ID, "input-nomination-weapon")
    SAVE_NOMINATION_BUTTON = (By.ID, "btn-nomination-save")
    # Opening nomination
    NOMINATION_LINK = (By.XPATH, "//button[@id='btn-nomination-add']/following-sibling::div[1]//div//a")
    # Creating new stage
    STAGES_TAB = (By.ID, "nomination-menu-stages")
    ADD_STAGE_BUTTON = (By.ID, "btn-stage-add")
    TYPE_RADIO_LIST = (By.XPATH, "//div[@class='stages'//div//div//div[@class='radio-blocks']")
    TO_THE_FINALS_TRUE = (By.ID, "input-stage-tillFinals-true")
    TO_THE_FINALS_FALSE = (By.ID, "input-stage-tillFinals-false")
    FIGHT_TIME_FIELD = (By.ID, "input-stage-fightTime")
    GOES_NEXT_STAGE_FIELD = (By.ID, "input-stage-outputCount-num")
    PLAYOFF_SIZE_4 = (By.ID, "input-stage-playoffSize-4")
    PLAYOFF_SIZE_8 = (By.ID, "input-stage-playoffSize-8")
    PLAYOFF_SIZE_16 = (By.ID, "input-stage-playoffSize-16")
    PLAYOFF_SIZE_32 = (By.ID, "input-stage-playoffSize-32")
    PLAYOFF_SIZE_64 = (By.ID, "input-stage-playoffSize-64")
    SWISS_EMPTY_FIGHT_RESULT_WIN = (By.ID, "input-stage-byeMode-win")
    SWISS_EMPTY_FIGHT_RESULT_DRAW = (By.ID, "input-stage-byeMode-draw")
    HITS_INITIAL_HP = (By.ID, "input-stage-swiss-hits-initial")
    HITS_LIMIT_HP = (By.ID, "input-stage-swiss-hits-fight-limit")
    SAVE_STAGE_BUTTON = (By.ID, "btn-stage-editing-save")
    # Adding participants
    PARTICIPANTS_TAB = (By.ID, "nomination-menu-participants")
    PARTICIPANTS_NUMBER_SELECT = (By.ID, "input-requests-test-enroll-number")
    ENROLL_TEST_PARTICIPANTS_BUTTON = (By.ID, "btn-requests-test-enroll")
    FULL_APPROVE_BUTTON = (By.ID, "input-requests-test-full-approve")
    # Creating new pool
    ADD_POOL_BUTTON = (By.ID, "btn-stage-0-add-pool")
    # Adding random participants to pool
    SEED_RANDOM_PARTICIPANTS_BUTTON = (By.ID, "btn-stage-0-seed")
    # Creating new ring
    RINGS_TAB = (By.ID, "tournament-menu-areas")
    ADD_RING_BUTTON = (By.ID, "btn-area-add")
    RING_TITLE_FIELD = (By.CSS_SELECTOR, "input")
    SAVE_RING_BUTTON = (By.ID, "btn-area-save")
