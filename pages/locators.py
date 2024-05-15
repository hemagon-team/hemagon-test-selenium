from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_BUTTON = (By.CSS_SELECTOR, ".user-block .btn.small")
    USER_NAME = (By.CLASS_NAME, "name")
    MY_TOURNAMENTS_BUTTON = (By.CSS_SELECTOR, ".user-block .popover li:nth-child(4) a")
    CLOSE_COOKIES_BUTTON = (By.CLASS_NAME, "cookies-alert__button")


class MainPageLocators:
    # Tabs
    TOURNAMENTS_TAB = (By.CSS_SELECTOR, ".menu-main > li:nth-of-type(1) > a")
    RATING_TAB = (By.CSS_SELECTOR, ".menu-main > li:nth-of-type(2) > a")
    FIGHTERS_TAB = (By.CSS_SELECTOR, ".menu-main > li:nth-of-type(3) > a")
    CLUBS_TAB = (By.CSS_SELECTOR, ".menu-main > li:nth-of-type(4) > a")
    ACHIEVEMENTS_TAB = (By.CSS_SELECTOR, ".menu-main > li:nth-of-type(5) > a")
    ABOUT_TAB = (By.CSS_SELECTOR, ".menu-main > li:nth-of-type(6) > a")
    CONTACT_TAB = (By.CSS_SELECTOR, ".menu-main > li:nth-of-type(7) > a")
    # Tournament tab
    TOURNAMENT_STATUS_TITLE = (By.CLASS_NAME, "tournaments-status-title")
    # Rating tab
    RATING_TITLE = (By.XPATH, "//h1[text()='Rating']")
    RATING_OVERALL_BUTTON = (By.CSS_SELECTOR, ".overall-rating > div > div > div > a")
    RATING_FULL_BUTTON = (By.CSS_SELECTOR, ".weapon-block > div > div > a")
    RATING_OVERALL_TABLE_USER = (By.XPATH, "//div[@class='column-title' and text()='User']")
    # Longsword tab
    RATING_LONGSWORD = (By.CSS_SELECTOR, ".weapon-type-selector > button:nth-of-type(1)")
    RATING_LONGSWORD_TITLE = (By.XPATH, "//div[@class='weapon-title' and text()='Longsword ']")
    RATING_LONGSWORD_OVERALL_TITLE = (By.XPATH, "//h1[text()='Overall rating: Longsword']")
    # Saber tab
    RATING_SABER = (By.CSS_SELECTOR, ".weapon-type-selector > button:nth-of-type(2)")
    RATING_SABER_TITLE = (By.XPATH, "//div[@class='weapon-title' and text()='Saber ']")
    RATING_SABER_OVERALL_TITLE = (By.XPATH, "//h1[text()='Overall rating: Saber']")
    # Rapier tab
    RATING_RAPIER = (By.CSS_SELECTOR, ".weapon-type-selector > button:nth-of-type(3)")
    RATING_RAPIER_TITLE = (By.XPATH, "//div[@class='weapon-title' and text()='Rapier ']")
    RATING_RAPIER_OVERALL_TITLE = (By.XPATH, "//h1[text()='Overall rating: Rapier']")
    # Rapier and dagger tab
    RATING_RAPIER_DAGGER = (By.CSS_SELECTOR, ".weapon-type-selector > button:nth-of-type(4)")
    RATING_RAPIER_DAGGER_TITLE = (By.XPATH, "//div[@class='weapon-title' and text()='Rapier and Dagger ']")
    RATING_RAPIER_DAGGER_OVERALL_TITLE = (By.XPATH, "//h1[text()='Overall rating: Rapier & Dagger']")
    # Dussak tab
    RATING_DUSSAK = (By.CSS_SELECTOR, ".weapon-type-selector > button:nth-of-type(5)")
    RATING_DUSSAK_TITLE = (By.XPATH, "//div[@class='weapon-title' and text()='Dussak  ']")
    RATING_DUSSAK_OVERALL_TITLE = (By.XPATH, "//h1[text()='Overall rating: Dussak']")
    # Spear tab
    RATING_SPEAR = (By.CSS_SELECTOR, ".weapon-type-selector > button:nth-of-type(6)")
    RATING_SPEAR_TITLE = (By.XPATH, "//div[@class='weapon-title' and text()='Spear ']")
    RATING_SPEAR_OVERALL_TITLE = (By.XPATH, "//h1[text()='Overall rating: Spear']")
    # Sword and buckler tab
    RATING_SWORD_BUCKLER = (By.CSS_SELECTOR, ".weapon-type-selector > button:nth-of-type(7)")
    RATING_SWORD_BUCKLER_TITLE = (By.XPATH, "//div[@class='weapon-title' and text()='Sword and Buckler - Open ']")
    RATING_SWORD_BUCKLER_OVERALL_TITLE = (By.XPATH, "//h1[text()='Overall rating: Sword & Buckler']")
    # Sidesword tab
    RATING_SIDESWORD = (By.CSS_SELECTOR, ".weapon-type-selector > button:nth-of-type(8)")
    RATING_SIDESWORD_TITLE = (By.XPATH, "//div[@class='weapon-title' and text()='Sidesword ']")
    RATING_SIDESWORD_OVERALL_TITLE = (By.XPATH, "//h1[text()='Overall rating: Sidesword']")
    # Triathlon tab
    RATING_TRIATHLON = (By.CSS_SELECTOR, ".weapon-type-selector > button:nth-of-type(9)")
    RATING_TRIATHLON_TITLE = (By.XPATH, "//div[@class='weapon-title' and text()='Triathlon ']")
    RATING_TRIATHLON_OVERALL_TITLE = (By.XPATH, "//h1[text()='Overall rating: Triathlon']")
    # Fighter tab
    FIGHTERS_TITLE = (By.XPATH, "//h1[text()='Fighters']")
    # Clubs tab
    CLUBS_TITLE = (By.XPATH, "//h1[text()='Clubs']")
    # Achievements tab
    ACHIEVEMENTS_TITLE = (By.XPATH, "//h1[text()='Achievements']")
    # About tab
    ABOUT_TITLE = (By.XPATH, "//h3[text()='Still have questions?']")
    # Contact tab
    CONTACT_TITLE = (By.XPATH, "//h1[text()='Contact us']")


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

class FightPageLocators:
    HTML = (By.TAG_NAME, 'html')
    SCORE_LEFT = (By.CSS_SELECTOR, 'div.sides > div:nth-child(1) > div.scores')
    SCORE_RIGHT = (By.CSS_SELECTOR, 'div.sides > div:nth-child(2) > div.scores')
    ADD_LEFT_BUTTON = (By.CSS_SELECTOR, 'div.scores-buttons-left > div:nth-child(1) > button')
    ADD_RIGHT_BUTTON = (By.CSS_SELECTOR, 'div.scores-buttons-right > div:nth-child(1) > button')
    FINISH_BUTTON = (By.CSS_SELECTOR, 'div.bottom > button.btn.active')

class StagePageLocators:
    POOLS_NUMBER = (By.CSS_SELECTOR, 'div.pool')
    NEXT_STAGE_BUTTON = (By.ID, 'btn-stage-0-build-next-stage')
    NEXT_PLAYOFF_STAGE_BUTTON = (By.ID, 'btn-stage-1-build-next-round-playoff')
    LEFT_BRANCH_RUN_BUTTON = (By.ID, 'btn-stage-1-side-0-build-next-playoff-round')
    RIGHT_BRANCH_RUN_BUTTON = (By.ID, 'btn-stage-1-side-1-build-next-playoff-round')
    FINALS_RUN_BUTTON = (By.ID, 'btn-stage-1-side-0-run-playoff-round')