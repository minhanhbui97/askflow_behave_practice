import time
import os
from behave.fixture import use_fixture_by_tag
from features.fixtures import browser_asker
from features.fixtures import browser_expert


fixture_registry = {
    "fixture.browser.asker": browser_asker,
    "fixture.browser.expert": browser_expert
}


def before_tag(context, tag):
    if tag == "fixture.browser.asker":
        return use_fixture_by_tag(tag, context, fixture_registry)
    elif tag == "fixture.browser.expert":
        return use_fixture_by_tag(tag, context, fixture_registry)


def before_scenario(context, scenario):
    context.scenario = scenario


def before_step(context, step):
    context.step = step


def after_step(context, step):
    if step.status == "failed":
        try:
            script_directory = os.path.dirname(os.path.realpath('__file__'))
            screenshot_directory = "/screenshot/"

            dest_directory = script_directory + screenshot_directory
            if not os.path.exists(dest_directory):
                os.makedirs(dest_directory)

            if hasattr(context, 'expert_browser'):
                expert_file_name = time.strftime("%H%M%S_%d_%m_%Y") + "_ExpertBrowser_" + context.scenario.name.replace(" ", "_") + "_" + context.step.name.replace(" ", "_") + "." + "png"

                expert_rel_filename = screenshot_directory + expert_file_name
                expert_dest_filename = script_directory + expert_rel_filename
                context.expert_driver.save_screenshot(expert_dest_filename)

            elif hasattr(context, 'asker_browser'):
                asker_file_name = time.strftime("%H%M%S_%d_%m_%Y") + "_AskerBrowser_" + context.scenario.name.replace(" ", "_") + "_" + context.step.name.replace(" ", "_") + "." + "png"
                asker_rel_filename = screenshot_directory + asker_file_name
                asker_dest_filename = script_directory + asker_rel_filename
                context.asker_driver.save_screenshot(asker_dest_filename)
        except:
            print("Exception occurs. Can not take screenshot")
