from selenium.webdriver.common.by import By


class BasePageLocators:
    MAIN_PAGE_BUTTON = (By.CSS_SELECTOR, ".app-title > a")
    MAIN_PAGE_TITLE = (By.CLASS_NAME, "tournaments-status-title")
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
    PASSWORD_RECOVERY = (By.CSS_SELECTOR, 'div.sub-link > a')
    ACCOUNT_REGISTRATION = (By.PARTIAL_LINK_TEXT, 'Register a new account')
    GET_CODE_BUTTON = (By.CSS_SELECTOR, 'form.form > button')
    PASSWORD_RECOVERY_EMAIL_FIELD = (By.CSS_SELECTOR, 'input#input-email')
    SEND_CODE_BUTTON = (By.CSS_SELECTOR, 'button.active')
    ENTER_NEW_PASSWORD = (By.CSS_SELECTOR, 'input#pass-new')
    CONFIRM_NEW_PASSWORD = (By.CSS_SELECTOR, 'input#pass-new-re')
    SAVE_PASSWORD_BUTTON = (By.CSS_SELECTOR, 'form > button')
    INCORRECT_CODE_ALERT = (By.XPATH, '//*[text()="Incorrect recovery code"]')


class ProfilePageLocators:
    USER_NAME = (By.CLASS_NAME, "user-view__title")
    USER_CLUB = (By.CSS_SELECTOR, ".user-view__club > a")
    SUMMARY_TAB = (By.ID, "users")
    USER_CLUB1 = (By.CSS_SELECTOR, "div.mb-24 div.text-center > a")
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
    REMOVE_TOURNAMENT_BUTTON = (By.ID, "btn-tournament-remove")


class TournamentPageLocators:
    # Verifying tournament name
    TOURNAMENT_TITLE = (By.CSS_SELECTOR, "#tournament-title")
    # Creating new nomination
    NOMINATIONS_TAB = (By.ID, "tournament-menu-nominations")
    CREATE_NOMINATION_BUTTON = (By.ID, "btn-nomination-add")
    NOMINATION_TITLE_FIELD = (By.ID, "input-nomination-title")
    WEAPON_SELECT = (By.ID, "input-nomination-weapon")
    FIGHT_TIME_INPUT = (By.ID, "input-nomination-time-fight")
    LAST_ROUND_TIME_INPUT = (By.ID, "input-nomination-time-last-round")
    SAVE_NOMINATION_BUTTON = (By.ID, "btn-nomination-save")
    # Tournament breadcrumbs menu
    BREADCRUMBS_TOURNAMENT_CATEGORIES = (By.ID, "tournament-breadcrumbs-categories")
    # Opening nomination
    NOMINATION_LINK = (By.CSS_SELECTOR, "#grid-nomination a")
    # Creating new stage
    STAGES_TAB = (By.ID, "nomination-menu-stages")
    ADD_STAGE_BUTTON = (By.ID, "btn-stage-add")
    TYPE_RADIO_POOLS = (By.ID, "input-stage-type-POOL")
    TYPE_RADIO_PLAYOFF = (By.ID, "input-stage-type-ELIMINATION")
    TYPE_RADIO_SWISS = (By.ID, "input-stage-type-SWISS")
    TYPE_RADIO_SWISS_HITS = (By.ID, "input-stage-type-SWISS_HITS")
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
    PARTICIPANTS_NUMBER_INPUT = (By.ID, "input-requests-test-enroll-number-alt")
    ENROLL_TEST_PARTICIPANTS_BUTTON = (By.ID, "btn-requests-test-enroll")
    PARTICIPANT_LINE = (By.CLASS_NAME, "user-tooltip-provider")
    FULL_APPROVE_BUTTON = (By.ID, "input-requests-test-full-approve")
    ACCEPTED_NUMBER = (By.ID, "requests-stats-accepted")
    # Handling participants
    APPLICATIONS_TAB = (By.ID, "tournament-menu-applications")
    PARTICIPANT_APPROVE_BUTTON = (By.CSS_SELECTOR, ".organizer-tournament > div > div > div > div:nth-of-type(2) > table > tbody >"
                                                   "tr > td > div:nth-of-type(1) > div:nth-of-type(2) > button:nth-of-type(1)")
    PARTICIPANT_BAN_BUTTON = (By.CSS_SELECTOR, ".organizer-tournament > div > div > div > div:nth-of-type(2) > table > tbody >"
                                               "tr > td > div:nth-of-type(1) > div:nth-of-type(2) > button:nth-of-type(2)")
    PARTICIPANT_WAITING_LIST_BUTTON = (By.CSS_SELECTOR, ".organizer-tournament > div > div > div > div:nth-of-type(2) > table > tbody >"
                                                        "tr > td > div:nth-of-type(1) > div:nth-of-type(2) > button:nth-of-type(3)")
    PARTICIPANT_PAID_BUTTON = (By.CSS_SELECTOR, ".organizer-tournament > div > div > div > div:nth-of-type(2) > table > tbody >"
                                                "tr > td > div:nth-of-type(1) > div:nth-of-type(3) > button:nth-of-type(1)")
    PARTICIPANT_PRESENT_BUTTON = (By.CSS_SELECTOR, ".organizer-tournament > div > div > div > div:nth-of-type(2) > table > tbody >"
                                                   "tr > td > div:nth-of-type(1) > div:nth-of-type(3) > button:nth-of-type(2)")
    PRESENT_NUMBER = (By.ID, "requests-stats-present")
    # Creating new ring
    RINGS_TAB = (By.ID, "tournament-menu-areas")
    ADD_RING_BUTTON = (By.ID, "btn-area-add")
    RING_TITLE_FIELD = (By.CSS_SELECTOR, ".organizer-tournament > div > div:nth-of-type(2) > div:nth-of-type(1) > input")
    SAVE_RING_BUTTON = (By.ID, "btn-area-save")
    # Creating new pool
    ADD_POOL_BUTTON = (By.ID, "btn-stage-0-add-pool")
#     ADD_POOL_BUTTON = (By.CSS_SELECTOR, ".stage-content > div:nth-of-type(5) > button:nth-of-type(1)")
    SET_RING_INPUT = (By.CSS_SELECTOR, "#vs1__combobox > div > input")
    # Adding random participants to pool
    SEED_RANDOM_PARTICIPANTS_BUTTON = (By.ID, "btn-stage-0-seed")
#     SEED_RANDOM_PARTICIPANTS_BUTTON = (By.CSS_SELECTOR, ".stage-content > div:nth-of-type(5) > button:nth-of-type(2)")
    # Setting ring for pool
    RING_FOR_POOL_FIELD = (By.CSS_SELECTOR, ".pool > div > div > div > div > div > input")
    # Deleting pool
    REMOVE_POOL_BUTTON = (By.CSS_SELECTOR, ".pool > div:nth-of-type(2) > button:nth-of-type(2)")
    # Deleting playoff
    REMOVE_PLAYOFF_BUTTON = (By.CSS_SELECTOR, ".eliminations > div > div > .pool > div > button:nth-of-type(1)")
    REMOVE_ROUND_BUTTON = (By.CSS_SELECTOR, ".round > div > div > button")
    # Adding all participants to swiss system
    ENROLL_ALL_TO_SWISS = (By.CSS_SELECTOR, ".pool > button")
    # Pairs and rings for swiss system
    ALLOCATE_RINGS_BUTTON = (By.CSS_SELECTOR, ".pool [data-test-class=btn-distribute-fights-to-areas]")
    CHANGE_PAIRS_BUTTON = (By.CSS_SELECTOR, ".pool [data-test-class=btn-change-fight-pairs]")
    DRAG_ZONES = (By.CLASS_NAME, "drag-zone")
    DRAG_ITEMS = (By.CLASS_NAME, "drag-item")
    ADD_UNALLOCATED_TO_RING = (By.CSS_SELECTOR, ".areas > div:nth-of-type(2) > button")
    CLOSE_SWISS_SETTINGS_BUTTON = (By.CSS_SELECTOR, 'button.round')
    # Deleting stage
    REMOVE_STAGE_BUTTON = (By.ID, "btn-stage-0-remove")
    NO_STAGES_TITLE = (By.CLASS_NAME, "empty-state")
    GRID_NO_ENTITIES = (By.CSS_SELECTOR, ".grid .no-data")
    # Deleting nomination
    REMOVE_NOMINATION_BUTTON = (By.ID, "btn-nomination-remove")
    # Deleting ring
    ANY_RING_LINE = (By.CSS_SELECTOR, ".grid > table > tbody > tr")
    REMOVE_RING_BUTTON = (By.CLASS_NAME, "svg-inline--fa.fa-xmark")
    # Changing status
    STATUS_DEVELOPMENT = (By.ID, "btn-set-status-DEVELOPING")
    STATUS_UPCOMING = (By.ID, "btn-set-status-UPCOMING")
    STATUS_REG_OPEN = (By.ID, "btn-set-status-REG_OPEN")
    STATUS_REG_CLOSED = (By.ID, "btn-set-status-REG_CLOSED")
    STATUS_ONGOING = (By.ID, "btn-set-status-ONGOING")
    STATUS_FINISHED = (By.ID, "btn-set-status-FINISHED")
    STATUS_DEVELOPMENT_ACTIVE = (By.CSS_SELECTOR, "#btn-set-status-DEVELOPING.active")
    STATUS_UPCOMING_ACTIVE = (By.CSS_SELECTOR, "#btn-set-status-UPCOMING.active")
    STATUS_REG_OPEN_ACTIVE = (By.CSS_SELECTOR, "#btn-set-status-REG_OPEN.active")
    STATUS_REG_CLOSED_ACTIVE = (By.CSS_SELECTOR, "#btn-set-status-REG_CLOSED.active")
    STATUS_ONGOING_ACTIVE = (By.CSS_SELECTOR, "#btn-set-status-ONGOING.active")
    STATUS_FINISHED_ACTIVE = (By.CSS_SELECTOR, "#btn-set-status-FINISHED.active")
    # Registration
    OVERVIEW_TAB = (By.ID, "tournament-menu-overview")
    REG_TAB = (By.ID, "tournament-menu-registration")
    ENABLE_HEMAGON_REG = (By.CSS_SELECTOR, "div.radio-inlines > label:nth-of-type(1) > input")
    ADD_FIRST_CATEGORY_TO_REG = (By.CSS_SELECTOR, ".organizer-tournament > div > div:nth-of-type(2) > div:nth-of-type(2) >"
                                            "div > .radio-blocks > label:nth-of-type(1) > input")
    ADD_SECOND_CATEGORY_TO_REG = (By.CSS_SELECTOR, ".organizer-tournament > div > div:nth-of-type(2) > div:nth-of-type(2) >"
                                            "div > .radio-blocks > label:nth-of-type(2) > input")
    SAVE_REG_BUTTON = (By.CSS_SELECTOR, "div.organizer-tournament > div > div:nth-of-type(3) > button")
    GO_TO_PUBLIC_PAGE_CATEGORY = (By.ID, "link-go-to-public-view-nomination")
    GO_TO_PUBLIC_PAGE_TOURNAMENT = (By.ID, "link-go-to-public-view-tournament")
    APPLY_BUTTON = (By.CSS_SELECTOR, ".application-actions > button")
    CATEGORY_RADIO = (By.CSS_SELECTOR, ".radio-blocks > label > input")
    CONFIRM_APPLICATION = (By.CSS_SELECTOR, ".container > div.form-container > div.flex > button")
    REG_SUCCESS = (By.CLASS_NAME, "registration-success")
    GO_TO_TOURNAMENT = (By.CSS_SELECTOR, ".registration-success > div > a")
    CHANGE_APPLICATION_BUTTON = (By.CSS_SELECTOR, ".application-actions > a:nth-of-type(1)")
    PUBLIC_NOMINATIONS = (By.CSS_SELECTOR, "div.nomination > a > div:nth-of-type(1)")
    PUBLIC_STAGES = (By.CSS_SELECTOR, "div.stage > h3")
    RETURN_TO_PUBLIC_NOMINATIONS = (By.CSS_SELECTOR, ".tournament-title > a")


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
    def POOL_START_BUTTON(pool):
        return (By.ID, 'btn-stage-0-pool-' + str(pool) +'-run')
    def STAGE_SHOW_BUTTON(stage):
        return (By.ID, 'btn-stage-' + str(stage) + '-toggle')
    def STAGE_SHOW_BUTTON_ARROW_DOWN(stage):
        return (By.CSS_SELECTOR, '#btn-stage-' + str(stage) + '-toggle > svg.fa-caret-down')
    NEXT_STAGE_BUTTON = (By.ID, 'btn-stage-0-build-next-stage')
    NEXT_PLAYOFF_STAGE_BUTTON = (By.ID, 'btn-stage-1-build-next-round-playoff')
    LEFT_BRANCH_RUN_BUTTON = (By.ID, 'btn-stage-1-side-0-build-next-playoff-round')
    RIGHT_BRANCH_RUN_BUTTON = (By.ID, 'btn-stage-1-side-1-build-next-playoff-round')
    LEFT_BRANCH_BUILD_BUTTON = (By.CSS_SELECTOR, '#btn-stage-1-side-0-build-next-playoff-round.small.active')
    RIGHT_BRANCH_BUILD_BUTTON = (By.CSS_SELECTOR, '#btn-stage-1-side-1-build-next-playoff-round.small.active')
    FINALS_RUN_BUTTON = (By.ID, 'btn-stage-1-side-0-run-playoff-round')
    RECOMMEND_SWISS_ROUNDS_NUMBER = (By.ID, 'stage-0-swiss-recommended-rounds')
    BUILD_NEXT_SWISS_ROUND = (By.ID, 'btn-stage-0-build-next-round-swiss')
    SWISS_RUN_POOL_BUTTON = (By.CSS_SELECTOR, "#btn-stage-0-pool-0-run[class='small active']")
    LEFT_RUN_BUTTON = (By.CSS_SELECTOR, '#btn-stage-1-side-0-run-playoff-round.active')
    RIGHT_RUN_BUTTON = (By.CSS_SELECTOR, '#btn-stage-1-side-1-run-playoff-round.active')


class PoolPageLocators:
    FIGHT_ROW = (By.CSS_SELECTOR, 'div.pool > div.row')
    FIGHT_BUTTON = (By.CSS_SELECTOR, 'div.row button.small.active')
#     CLOSE_POOL_BUTTON = (By.CSS_SELECTOR, 'button.round')
    CLOSE_POOL_BUTTON = (By.ID, 'tournament-breadcrumbs-category-stages')
    SEED_RANDOM_RESULTS_BUTTON = (By.CSS_SELECTOR, ".pool > div:nth-of-type(3) > button")
    SUCCESS_NOTIFICATION = (By.CLASS_NAME, "notification-content")
    RUN_FIGHT_BUTTON_ACTIVE = (By.CSS_SELECTOR, ".row > div:nth-of-type(3) > div > button.active")
    RUN_FIGHT_BUTTON_ACTIVE_SWISS = (By.CSS_SELECTOR, ".row > div:nth-of-type(4) > div > button.active")
    BYE_BUTTON = (By.CSS_SELECTOR, "#btn-pass-bye")


# class SwissPoolPageLocators:
#     FIGHT_ROW = (By.CSS_SELECTOR, 'div.pool > div.row > div:nth-child(4) > div:nth-child(1) > button')
#     CLOSE_POOL_BUTTON = (By.CSS_SELECTOR, 'button.round')

class PostalPageLocators:
    LOGIN_PAGE_BUTTON = (By.CSS_SELECTOR, 'button#signin')
    LOGIN_EMAIL = (By.CSS_SELECTOR, 'input#UserID')
    LOGIN_PASSWORD = (By.CSS_SELECTOR, 'input#Password')
    LOGIN_BUTTON = (By.CSS_SELECTOR, 'input.btn')
    LETTERS = (By.CSS_SELECTOR, '#nav-mail > div')
    LETTER_CHOISE = (By.CLASS_NAME, 'GCSDBRWBCU.GCSDBRWBEU.listUnread.trow')
    MESSAGE = (By.CLASS_NAME, "GCSDBRWBCRC.mail-html-content.not-dark")
    MESSAGES_LIST = (By.CSS_SELECTOR, 'div.listSubject')

class RegistrationPageLocators:
    FIRST_NAME = (By.CSS_SELECTOR, 'div.form > div:nth-child(1) > input')
    LAST_NAME = (By.CSS_SELECTOR, 'div.form > div:nth-child(2) > input')
    EMAIL = (By.CSS_SELECTOR, 'div.form > div:nth-child(3) > input')
    PASSWORD = (By.CSS_SELECTOR, 'div.form > div:nth-child(4) > input')
    PASSWORD_CONFIRMATION = (By.CSS_SELECTOR, 'div.form > div:nth-child(5) > input')
    ORGANIZER_YES = (By.CSS_SELECTOR, 'div.radio-inlines > label:nth-child(1) > input[type=radio]')
    ORGANIZER_NO = (By.CSS_SELECTOR, 'div.radio-inlines > label:nth-child(2) > input[type=radio]')
    CREATE_ACCOUNT_BUTTON = (By.CSS_SELECTOR, 'button.mt-24')
    SAVE_BUTTON = (By.CSS_SELECTOR, 'button.active')
    PROFILE_BUTTON = (By.CSS_SELECTOR, 'div.name')
    LOG_OUT_BUTTON = (By.CLASS_NAME, 'svg-inline--fa.fa-right-from-bracket')
    SETTINGS_BUTTON = (By.CLASS_NAME, 'svg-inline--fa.fa-gear.fa-fw')
    OPEN_PROFILE_BUTTON = (By.CSS_SELECTOR, "div.user-block > div > div.body > ul > li:nth-child(1) > a")

class ProfileSettingsLocators:
    FIRST_NAME_FIELD = (By.CSS_SELECTOR, 'input#reg-firstname')
    LAST_NAME_FIELD = (By.CSS_SELECTOR, 'input#reg-lastname')
    USERNAME_FIELD = (By.CSS_SELECTOR, 'input#reg-username')
    EMAIL_FIELD = (By.CSS_SELECTOR, 'input#reg-email')
    COUNTRY_FIELD = (By.CSS_SELECTOR, '#vs1__combobox > div.vs__selected-options > input')
    CITY_FIELD = (By.CSS_SELECTOR, '#vs2__combobox > div.vs__selected-options > input')
    CLUB_FIELD = (By.CSS_SELECTOR, '#vs3__combobox > div.vs__selected-options > input')
    CLEAR_COUNTRY_BUTTON = (By.CSS_SELECTOR, '#vs1__combobox > div.vs__actions > button')
    CLEAR_CITY_BUTTON = (By.CSS_SELECTOR, '#vs2__combobox > div.vs__actions > button')
    CLEAR_CLUB_BUTTON = (By.CSS_SELECTOR, '#vs3__combobox > div.vs__actions > button')
    CHANGE_PASSWORD_BUTTON = (By.CSS_SELECTOR, 'div.form > div:nth-child(5) > button')
    SAVE_BUTTON = (By.CSS_SELECTOR, 'button.active')
