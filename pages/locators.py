from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_BUTTON = (By.CSS_SELECTOR, ".user-block .btn.small")
    USER_NAME = (By.CLASS_NAME, "name")
    MY_TOURNAMENTS_BUTTON = (By.CSS_SELECTOR, ".user-block .popover li:nth-child(4) a")
    CLOSE_COOKIES_BUTTON = (By.CLASS_NAME, "cookies-alert__button")


class LoginPageLocators:
    EMAIL_FIELD = (By.ID, "input-email")
    PASSWORD_FIELD = (By.ID, "input-password")
    LOGIN_BUTTON = (By.ID, "btn-login")


class OrganizerPageLocators:
    # Creating new tournament
    CREATE_TOURNAMENT_BUTTON = (By.ID, "btn-create-tournament")
    TEST_TOURNAMENT_INPUT = (By.ID, "input-tournament-test-true")
    TITLE_FIELD = (By.ID, "input-tournament-title")
    START_DATE_PICKER = (By.CSS_SELECTOR, ".advanced-datepicker:nth-of-type(1)")
    END_DATE_PICKER = (By.CSS_SELECTOR, ".advanced-datepicker:nth-of-type(2)")
    COUNTRY_FIELD = (By.CSS_SELECTOR, "#vs1__combobox > .vs__selected-options > input")
    CITY_FIELD = (By.CSS_SELECTOR, "#vs2__combobox > div.vs__selected-options > input")
    DESCRIPTION_FIELD = (By.ID, "input-tournament-description")
    SAVE_BUTTON = (By.ID, "btn-tournament-save")
    # Open tournament
    TOURNAMENT_BANNERS = (By.CSS_SELECTOR, ".tournaments > div > a > .title")
    TOURNAMENT_OVERVIEW_TAB = (By.ID, "tournament-menu-overview")
    # Delete tournament
    REMOVE_TOURNAMENT_BUTTON = (By.CSS_SELECTOR, "#app > div > div:nth-child(2) > div > div:nth-child(6) >"
                                                 "div > div > div:nth-child(3) > button")


class TournamentPageLocators:
    # Verifying tournament name
    TOURNAMENT_TITLE = (By.CSS_SELECTOR, "#app > div > div > div > h1")
    # Creating new nomination
    NOMINATIONS_TAB = (By.ID, "tournament-menu-nominations")
    CREATE_NOMINATION_BUTTON = (By.ID, "btn-nomination-add")
    NOMINATION_TITLE_FIELD = (By.ID, "input-nomination-title")
    WEAPON_SELECT = (By.ID, "input-nomination-weapon")
    FIGHT_TIME_INPUT = (By.ID, "input-nomination-time-fight")
    LAST_ROUND_TIME_INPUT = (By.ID, "input-nomination-time-last-round")
    SAVE_NOMINATION_BUTTON = (By.ID, "btn-nomination-save")
    # Opening nomination
    NOMINATION_LINK = (By.XPATH, "//button[@id='btn-nomination-add']/following-sibling::div[1]//div//a")
    # Creating new stage
    STAGES_TAB = (By.ID, "nomination-menu-stages")
    ADD_STAGE_BUTTON = (By.ID, "btn-stage-add")
    TYPE_RADIO_POOLS = (By.CSS_SELECTOR, "#app > div > div:nth-child(2) > div > div:nth-child(6) > div > div >"
                        "div:nth-child(3) > div > div > div > div:nth-child(2) > div > label:nth-child(1)")
    TYPE_RADIO_PLAYOFF = (By.CSS_SELECTOR, "#app > div > div:nth-child(2) > div > div:nth-child(6) > div > div >"
                          "div:nth-child(3) > div > div > div > div:nth-child(2) > div > label:nth-child(2)")
    TYPE_RADIO_SWISS = (By.CSS_SELECTOR, "#app > div > div:nth-child(2) > div > div:nth-child(6) > div > div >"
                        "div:nth-child(3) > div > div > div > div:nth-child(2) > div > label:nth-child(3)")
    TYPE_RADIO_SWISS_HITS = (By.CSS_SELECTOR, "#app > div > div:nth-child(2) > div > div:nth-child(6) > div > div >"
                             "div:nth-child(3) > div > div > div > div:nth-child(2) > div > label:nth-child(4)")
    TO_THE_FINALS_TRUE = (By.ID, "input-stage-tillFinals-true")
    TO_THE_FINALS_FALSE = (By.ID, "input-stage-tillFinals-false")
    FIGHT_TIME_FIELD = (By.ID, "input-stage-fightTime")
    GOES_NEXT_STAGE_FIELD = (By.ID, "input-stage-outputCount-num")
    PLAYOFF_SIZE_4 = (By.ID, "input-stage-playoffSize-4")
    PLAYOFF_SIZE_8 = (By.ID, "input-stage-playoffSize-8")
    PLAYOFF_SIZE_16 = (By.ID, "input-stage-playoffSize-16")
    PLAYOFF_SIZE_32 = (By.ID, "input-stage-playoffSize-32")
    PLAYOFF_SIZE_64 = (By.ID, "input-stage-playoffSize-64")
    PLAYOFF_FINALS_MODE_1 = (By.ID, "input-stage-finalsMode-bo1")
    PLAYOFF_FINALS_MODE_3 = (By.ID, "input-stage-finalsMode-bo3")
    PLAYOFF_THIRD_PLACE_TRUE = (By.ID, "input-stage-fightForThirdPlace-true")
    PLAYOFF_THIRD_PLACE_FALSE = (By.ID, "input-stage-fightForThirdPlace-false")
    SWISS_EMPTY_FIGHT_RESULT_WIN = (By.ID, "input-stage-byeMode-win")
    SWISS_EMPTY_FIGHT_RESULT_DRAW = (By.ID, "input-stage-byeMode-draw")
    SWISS_EMPTY_WIN_POINTS = (By.ID, "input-stage-byeMode-win-points")
    HITS_INITIAL_HP = (By.ID, "input-stage-swiss-hits-initial")
    HITS_LIMIT_HP = (By.ID, "input-stage-swiss-hits-fight-limit")
    SAVE_STAGE_BUTTON = (By.ID, "btn-stage-editing-save")
    # Adding participants
    PARTICIPANTS_TAB = (By.ID, "nomination-menu-participants")
    PARTICIPANTS_NUMBER_SELECT = (By.ID, "input-requests-test-enroll-number")
    ENROLL_TEST_PARTICIPANTS_BUTTON = (By.ID, "btn-requests-test-enroll")
    PARTICIPANT_LINE = (By.CLASS_NAME, "user-tooltip-provider")
    FULL_APPROVE_BUTTON = (By.ID, "input-requests-test-full-approve")
    ACCEPTED_NUMBER = (By.ID, "requests-stats-accepted")
    # Creating new ring
    RINGS_TAB = (By.ID, "tournament-menu-areas")
    ADD_RING_BUTTON = (By.ID, "btn-area-add")
    RING_TITLE_FIELD = (By.CSS_SELECTOR, "input")
    SAVE_RING_BUTTON = (By.ID, "btn-area-save")
    # Creating new pool
    ADD_POOL_BUTTON = (By.CSS_SELECTOR, ".stage-content > div:nth-of-type(5) > button:nth-of-type(1)")
    SET_RING_INPUT = (By.CSS_SELECTOR, "#vs1__combobox > div > input")
    # Adding random participants to pool
    SEED_RANDOM_PARTICIPANTS_BUTTON = (By.CSS_SELECTOR, ".stage-content > div:nth-of-type(5) > button:nth-of-type(2)")
    # Deleting pool
    REMOVE_POOL_BUTTON = (By.CSS_SELECTOR, ".pool > div:nth-of-type(2) > button:nth-of-type(3)")
    # Adding all participants to swiss system
    ENROLL_ALL_TO_SWISS = (By.CSS_SELECTOR, ".pool > button")
    # Pairs and rings for swiss system
    ALLOCATE_RINGS_BUTTON = (By.CSS_SELECTOR, ".pool > div:nth-of-type(3) > button:nth-of-type(1)")
    CHANGE_PAIRS_BUTTON = (By.CSS_SELECTOR, ".pool > div:nth-of-type(3) > button:nth-of-type(2)")
    DRAG_ZONES = (By.CLASS_NAME, "drag-zone")
    DRAG_ITEMS = (By.CLASS_NAME, "drag-item")
    ADD_UNALLOCATED_TO_RING = (By.CSS_SELECTOR, ".areas > div:nth-of-type(2) > button")
    # Deleting stage
    REMOVE_STAGE_BUTTON = (By.CSS_SELECTOR, ".stage-content > div:nth-of-type(1) > button")
    NO_STAGES_TITLE = (By.CLASS_NAME, "empty-state")
    # Deleting nomination
    REMOVE_NOMINATION_BUTTON = (By.CSS_SELECTOR, "#app > div > div:nth-child(2) > div > div:nth-child(6) > div"
                                                 "> div > div:nth-child(3) > div > div > div:nth-child(4) > button")
    # Deleting ring
    ANY_RING_LINE = (By.CSS_SELECTOR, ".grid > table > tbody > tr")
    REMOVE_RING_BUTTON = (By.CLASS_NAME, "svg-inline--fa.fa-xmark")
