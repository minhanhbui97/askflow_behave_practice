from webdriver.chromedriver import get_driver
from behave import fixture


@fixture
def browser_asker(context, timeout=30, **kwargs):
    # -- SETUP-FIXTURE PART: get_driver default argument (headless_mode=False)
    context.asker_browser = get_driver()
    yield context.asker_browser
    # -- CLEANUP-FIXTURE PART:
    context.asker_browser.quit()


@fixture
def browser_expert(context, timeout=30, **kwargs):
    # -- SETUP-FIXTURE PART: get_driver default argument (headless_mode=False)
    context.expert_browser = get_driver()
    yield context.expert_browser
    # -- CLEANUP-FIXTURE PART:
    context.expert_browser.quit()


