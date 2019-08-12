from behave import given, when, then
from cfg.staging import StagingConfigs
from pages.expert.expert_landingpage import ExpertLandingPage
from pages.expert.expert_homepage import ExpertHomePage
from pages.expert.expert_connectingpage import ExpertConnectingPage
from pages.asker.asker_landingpage import AskerLandingPage
from pages.asker.asker_login_modal import AskerLoginModal
from pages.asker.asker_homepage import AskerHomePage
from cfg.main_config import MainConfig
from pages.asker.asker_matching_modal import AskerMatchingModal
from pages.asker.asker_workspace import AskerWorkspace
from pages.expert.expert_workspace import ExpertWorkspace
from pages.expert.expert_intro_modal import ExpertIntroModal
from pages.asker.problem_expert_intro_modal import ProblemExpertIntroModal


@given("Expert is on Landing Page")
def step_impl(context):
    context.expert_browser.get(StagingConfigs.EXPERT_PORTAL)
    print(context.expert_browser.title)
    expert_landing_page = ExpertLandingPage(context.expert_browser)
    assert expert_landing_page.is_present()


@given("Expert logs in by email and password successfully")
def step_impl(context):
    expert_landingpage = ExpertLandingPage(context.expert_browser)
    expert_landingpage.click_login_link()
    expert_landingpage.enter_email_field(StagingConfigs.EXPERT_USERNAME)
    expert_landingpage.enter_password_field(StagingConfigs.EXPERT_PASSWORD)
    expert_landingpage.click_submit_login_button()


@then("Expert should be able to skip Intro Modal")
def step_impl(context):
    expert_expert_intro_modal = ExpertIntroModal(context.expert_browser)
    assert expert_expert_intro_modal.is_present()
    expert_expert_intro_modal.click_skip_button()


@then("Expert should enter Homepage")
def step_impl(context):
    expert_homepage = ExpertHomePage(context.expert_browser)
    assert expert_homepage.is_present()


@when("Expert clicks Start Working button")
def step_impl(context):
    expert_homepage = ExpertHomePage(context.expert_browser)
    expert_homepage.click_on_start_working_button()


@then("Expert should be in Connecting Area")
def step_impl(context):
    expert_connectingarea = ExpertConnectingPage(context.expert_browser)
    assert expert_connectingarea.is_present()


@given("Asker is on Landing Page")
def step_impl(context):
    # context.asker_browser = get_driver()
    context.asker_browser.get(StagingConfigs.ASKER_PORTAL)
    print(context.asker_browser.title)

    asker_landingpage = AskerLandingPage(context.asker_browser)
    assert asker_landingpage.is_present()


# @when("Asker logs in by Google account")
# def step_impl(context):
#     asker_landingpage = AskerLandingPage(context.asker_driver)
#     asker_landingpage.click_login_link()
#     asker_landingpage.verify_login_modal_appear()
#
#     asker_login_modal = AskerLoginModal(context.asker_driver)
#     asker_login_modal.switch_to_google_browser(StagingConfigs.ASKER_GEMAIL, StagingConfigs.ASKER_GPASSWORD)
#
#     time.sleep(10)


@when("Asker logs in by email and password successfully")
def step_impl(context):
    asker_landingpage = AskerLandingPage(context.asker_browser)
    asker_landingpage.click_login_link()

    asker_login_modal = AskerLoginModal(context.asker_browser)
    assert asker_login_modal.is_present()
    asker_login_modal.enter_email_field(StagingConfigs.ASKER_EMAIL)
    asker_login_modal.enter_password_field(StagingConfigs.ASKER_PASSWORD)
    asker_login_modal.click_submit_login_button()


@then("Asker should enter Homepage")
def step_impl(context):
    asker_homepage = AskerHomePage(context.asker_browser)
    assert asker_homepage.is_present()


@when("Asker posts a question with description and type successfully")
def step_impl(context):
    asker_homepage = AskerHomePage(context.asker_browser)
    asker_homepage.enter_question_description_field(MainConfig.QUESTION_DESC)
    asker_homepage.select_question_type(MainConfig.QUESTION_TYPE)
    asker_homepage.click_on_submit_question_button()
    

@then("Asker should see Matching Modal")
def step_impl(context):
    asker_matching_modal = AskerMatchingModal(context.asker_browser)
    assert asker_matching_modal.is_present()


@when("Expert claims Asker's question")
def step_impl(context):
    expert_biddingscreen = ExpertConnectingPage(context.expert_browser)
    expert_biddingscreen.click_claim_asker_question(MainConfig.QUESTION_DESC)


@then("Asker should be able to close Problem Expert Intro Modal")
def step_impl(context):
    problem_expert_intro_modal = ProblemExpertIntroModal(context.asker_browser)
    assert problem_expert_intro_modal.is_present()
    problem_expert_intro_modal.close_expert_intro_modal()


@then("Asker should enter Workspace")
def step_impl(context):
    asker_workspace = AskerWorkspace(context.asker_browser)
    assert asker_workspace.is_present()


@then("Expert should enter on Workspace")
def step_impl(context):
    expert_workspace = ExpertWorkspace(context.expert_browser)
    assert expert_workspace.is_present()


@when("Asker sends a chat message")
def step_impl(context):
    asker_workspace = AskerWorkspace(context.asker_browser)
    asker_workspace.send_chat_message(MainConfig.CHAT_MESSAGE)


@then("Expert should see Asker's chat message")
def step_impl(context):
    expert_workspace = ExpertWorkspace(context.expert_browser)
    assert expert_workspace.get_asker_last_message(MainConfig.CHAT_MESSAGE)
