from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_BUTTON = (By.CSS_SELECTOR, ".user-block .btn.small")
    # User popover
    USER_NAME = (By.CLASS_NAME, "name")
    USER_POPOVER = (By.CSS_SELECTOR, ".user-block .popover")
    PROFILE_BUTTON = (By.CSS_SELECTOR, "div:nth-of-type(2) ul li:nth-of-type(1) a")
    MY_TOURNAMENTS_BUTTON = (By.CSS_SELECTOR, "div:nth-of-type(2) ul li:nth-of-type(4) a")
    CLOSE_COOKIES_BUTTON = (By.CLASS_NAME, "cookies-alert__button")
    # Footer
    CONTACT_LINK_FOOTER = (By.CSS_SELECTOR, ".links > a:nth-of-type(1)")
    ABOUT_LINK_FOOTER = (By.CSS_SELECTOR, ".links > a:nth-of-type(2)")
    # About tab
    ABOUT_PRICES = (By.CLASS_NAME, "price-options")
    # Contact tab
    CONTACT_ICON = (By.CLASS_NAME, "fa-facebook")
    # Terms and privacy policy
    TERMS_LINK = (By.CSS_SELECTOR, ".terms > a")
    # NEED TO CHANGE FOR SOME LOCATOR WITHOUT TEXT
    TERMS_TITLE = (By.XPATH, "//h1[text()=' Terms and Privacy Policy ']")


class MainPageLocators:
    # Tabs
    TOURNAMENTS_TAB = (By.CSS_SELECTOR, ".menu-main > li:nth-of-type(1) > a")
    RATING_TAB = (By.CSS_SELECTOR, ".menu-main > li:nth-of-type(2) > a")
    """FIGHTERS_TAB = (By.CSS_SELECTOR, ".menu-main > li:nth-of-type(3) > a")
    CLUBS_TAB = (By.CSS_SELECTOR, ".menu-main > li:nth-of-type(4) > a")"""
    ACHIEVEMENTS_TAB = (By.CSS_SELECTOR, ".menu-main > li:nth-of-type(3) > a")
    ABOUT_TAB = (By.CSS_SELECTOR, ".menu-main > li:nth-of-type(4) > a")
    CONTACT_TAB = (By.CSS_SELECTOR, ".menu-main > li:nth-of-type(5) > a")
    INSTANT_FIGHT_TAB = (By.CSS_SELECTOR, ".menu-main > li:nth-of-type(6) > a")
    # Tournament tab
    TOURNAMENT_STATUS_TITLE = (By.CLASS_NAME, "tournaments-status-title")
    # Rating tab
    RATING_SELECTOR = (By.CLASS_NAME, "weapon-type-selector")
    RATING_WEAPON_TABS = (By.CSS_SELECTOR, ".weapon-type-selector > button")
    RATING_WEAPON_TITLE = (By.CSS_SELECTOR, ".weapon-block > div:nth-of-type(1) > div:nth-of-type(1).weapon-title")
    RATING_OPEN_LIST_OVERALL_BUTTON = (By.CSS_SELECTOR, ".weapon-block > div > div > a")
    RATING_OPEN_LIST_BUTTON = (By.CSS_SELECTOR, ".weapon-block > div > a")
    RATING_LIST_INPUT = (By.CSS_SELECTOR, "div > input")
    RATING_LIST_TITLE = (By.CSS_SELECTOR, "div > h1")
    RATING_LIST_TABLE = (By.CSS_SELECTOR, "table > tbody > tr")
    RATING_ABOUT_LINK = (By.CSS_SELECTOR, ".description > div:nth-of-type(1) > a")
    RATING_IMPORT_LINK = (By.CSS_SELECTOR, ".description > div:nth-of-type(2) > span")
    # How we calculate rating
    RATING_ABOUT_TITLE = (By.XPATH, "//h1[text()=' About rating ']")
    # Import tournament
    RATING_IMPORT_BUTTON = (By.CSS_SELECTOR, ".collapse-block > .collapse-block-body > .wrapper > label > .btn")
    # Fighter tab
    FIGHTERS_TITLE = (By.XPATH, "//h1[text()='Fighters']")
    # Clubs tab
    CLUBS_TITLE = (By.XPATH, "//h1[text()='Clubs']")
    # Achievements tab
    ACHIEVEMENTS_TITLE = (By.XPATH, "//h1[text()='Achievements']")
    # Instant fight tab
    INSTANT_FIGHT_RUN_TIME_BUTTON = (By.CSS_SELECTOR, ".space-button > button")
    INSTANT_FIGHT_CLOSE = (By.CSS_SELECTOR, ".bottom > button")


class LoginPageLocators:
    EMAIL_FIELD = (By.ID, "input-email")
    PASSWORD_FIELD = (By.ID, "input-password")
    LOGIN_BUTTON = (By.ID, "btn-login")


class ProfilePageLocators:
    USER_NAME = (By.CLASS_NAME, "user-view__title")
    USER_CLUB = (By.CSS_SELECTOR, ".user-view__club > a")
    FIGHTERS_HEADER = (By.CSS_SELECTOR, ".breadcrumbs > a")


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
    REMOVE_TOURNAMENT_BUTTON = (By.CSS_SELECTOR, ".organizer-tournament div > div > div:nth-child(2) > button")


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
    TYPE_RADIO_POOLS = (By.CSS_SELECTOR, ".stage.temp > div:nth-of-type(1) > .radio-blocks > label:nth-of-type(1)")
    TYPE_RADIO_PLAYOFF = (By.CSS_SELECTOR, ".stage.temp > div:nth-of-type(1) > .radio-blocks > label:nth-of-type(2)")
    TYPE_RADIO_SWISS = (By.CSS_SELECTOR, ".stage.temp > div:nth-of-type(1) > .radio-blocks > label:nth-of-type(3)")
    TYPE_RADIO_SWISS_HITS = (By.CSS_SELECTOR, ".stage.temp > div:nth-of-type(1) > .radio-blocks > label:nth-of-type(4)")
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
    # PARTICIPANTS_NUMBER_SELECT = (By.ID, "input-requests-test-enroll-number")
    PARTICIPANTS_NUMBER_INPUT = (By.ID, "input-requests-test-enroll-number-alt")
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
    REMOVE_POOL_BUTTON = (By.CSS_SELECTOR, ".pool > div:nth-of-type(2) > button:nth-of-type(2)")
    # Deleting playoff
    REMOVE_PLAYOFF_BUTTON = (By.CSS_SELECTOR, ".eliminations > div > div > .pool > div > button:nth-of-type(1)")
    REMOVE_ROUND_BUTTON = (By.CSS_SELECTOR, ".round > div > div > button")
    # Adding all participants to swiss system
    ENROLL_ALL_TO_SWISS = (By.CSS_SELECTOR, ".pool > button")
    # Pairs and rings for swiss system
    ALLOCATE_RINGS_BUTTON = (By.CSS_SELECTOR, ".pool > div:nth-of-type(3) > button:nth-of-type(1)")
    CHANGE_PAIRS_BUTTON = (By.CSS_SELECTOR, ".pool > div:nth-of-type(3) > button:nth-of-type(2)")
    DRAG_ZONES = (By.CLASS_NAME, "drag-zone")
    DRAG_ITEMS = (By.CLASS_NAME, "drag-item")
    ADD_UNALLOCATED_TO_RING = (By.CSS_SELECTOR, ".areas > div:nth-of-type(2) > button")
    CLOSE_SWISS_SETTINGS_BUTTON = (By.CSS_SELECTOR, 'button.round')
    # Deleting stage
    REMOVE_POOLS_STAGE_BUTTON = (By.CSS_SELECTOR, ".stage-content > div:nth-of-type(1) > button:nth-of-type(1)")
    # REMOVE_PLAYOFF_STAGE_BUTTON = (By.CSS_SELECTOR, "div.stage-content:nth-of-type(2) > div > button")
    REMOVE_PLAYOFF_STAGE_BUTTON = (By.ID, "btn-stage-1-remove")
    NO_STAGES_TITLE = (By.CLASS_NAME, "empty-state")
    # Deleting nomination
    REMOVE_NOMINATION_BUTTON = (By.CSS_SELECTOR, ".organizer-tournament-nomination > div > div >"
                                                 "div:nth-of-type(4) > button")
    # Deleting ring
    ANY_RING_LINE = (By.CSS_SELECTOR, ".grid > table > tbody > tr")
    REMOVE_RING_BUTTON = (By.CLASS_NAME, "svg-inline--fa.fa-xmark")


class FightPageLocators:
    HTML = (By.TAG_NAME, 'html')
    SCORE_LEFT = (By.CSS_SELECTOR, 'div.sides > div:nth-child(1) > div.scores')
    SCORE_RIGHT = (By.CSS_SELECTOR, 'div.sides > div:nth-child(2) > div.scores')
    ADD_LEFT_BUTTON = (By.CSS_SELECTOR, 'div.scores-buttons-left > div:nth-child(1) > button')
    ADD_RIGHT_BUTTON = (By.CSS_SELECTOR, 'div.scores-buttons-right > div:nth-child(1) > button')
    MINUS_LEFT_BUTTON = (By.CSS_SELECTOR, 'div.scores-buttons-left > div:nth-child(2) > button')
    MINUS_RIGHT_BUTTON = (By.CSS_SELECTOR, 'div.scores-buttons-right > div:nth-child(2) > button')
    ADD_5SECONDS_BUTTON = (By.CSS_SELECTOR, 'div.bottom > button:nth-child(3)')
    TECHNICAL_DEFEAT_BUTTON = (By.CSS_SELECTOR, 'div.bottom > button:nth-child(4)')
    FINISH_BUTTON = (By.CSS_SELECTOR, 'div.bottom > button:nth-child(5)')
    CLOSE_BUTTON = (By.CSS_SELECTOR, 'div.bottom > button:nth-child(6)')


class StagePageLocators:
    POOLS_NUMBER = (By.CSS_SELECTOR, 'div.pool')
    NEXT_STAGE_BUTTON = (By.ID, 'btn-stage-0-build-next-stage')
    NEXT_PLAYOFF_STAGE_BUTTON = (By.ID, 'btn-stage-1-build-next-round-playoff')
    LEFT_BRANCH_RUN_BUTTON = (By.ID, 'btn-stage-1-side-0-build-next-playoff-round')
    RIGHT_BRANCH_RUN_BUTTON = (By.ID, 'btn-stage-1-side-1-build-next-playoff-round')
    FINALS_RUN_BUTTON = (By.ID, 'btn-stage-1-side-0-run-playoff-round')
    RECOMMEND_SWISS_ROUNDS_NUMBER = (By.ID, 'stage-0-swiss-recommended-rounds')
    BUILD_NEXT_SWISS_ROUND = (By.ID, 'btn-stage-0-build-next-round-swiss')
    SWISS_RUN_POOL_BUTTON = (By.CSS_SELECTOR, "#btn-stage-0-pool-0-run[class='small active']")
    LEFT_RUN_BUTTON = (By.CSS_SELECTOR, '#btn-stage-1-side-0-run-playoff-round.active')
    RIGHT_RUN_BUTTON = (By.CSS_SELECTOR, '#btn-stage-1-side-1-run-playoff-round.active')



class PoolPageLocators:
    FIGHT_ROW = (By.CSS_SELECTOR, 'div.pool > div.row')
    FIGHT_BUTTON = (By.CSS_SELECTOR, 'button.small.active')
    CLOSE_POOL_BUTTON = (By.CSS_SELECTOR, 'button.round')
    SEED_RANDOM_RESULTS_BUTTON = (By.CSS_SELECTOR, ".pool > div:nth-of-type(3) > button")
    SUCCESS_NOTIFICATION = (By.CLASS_NAME, "notification-content")
    RUN_FIGHT_BUTTON_ACTIVE = (By.CSS_SELECTOR, ".row > div:nth-of-type(3) > div > button.active")


class SwissPoolPageLocators:
    FIGHT_ROW = (By.CSS_SELECTOR, 'div.pool > div.row > div:nth-child(4) > div:nth-child(1) > button')
    CLOSE_POOL_BUTTON = (By.CSS_SELECTOR, 'button.round')

    # def asd!!!!!!!!!!!!! (pool):
    #     return (By.ID, 'btn-stage-0-pool-' + str(pool) +'-run')
