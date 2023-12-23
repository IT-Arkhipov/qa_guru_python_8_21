import os
import pytest
import allure
from config import settings
import allure_commons

from utils import attach
from appium.options.android import UiAutomator2Options
from selene import browser, support
from appium import webdriver


@pytest.fixture()
def android_mobile():
    options = UiAutomator2Options().load_capabilities({
        "platformVersion": "9.0",
        "deviceName": "Google Pixel 3",
        "app": "bs://sample.app",
        'bstack:options': {
            "projectName": "First Python project",
            "buildName": "browserstack-build-1",
            "sessionName": "BStack first_test",

            "userName": f'{settings.user_name}',
            "accessKey": f'{settings.access_key}'
        }
    })

    with allure.step('Initialization'):
        browser.config.driver = webdriver.Remote(
            "http://hub.browserstack.com/wd/hub",
            options=options
        )

    browser.config.timeout = float(os.getenv('timeout', '10.0'))
    browser.config._wait_decorator = support._logging.wait_with(context=allure_commons._allure.StepContext)

    yield

    attach.screenshot()
    attach.page_source()
    session_id = browser.driver.session_id
    with allure.step('Close application'):
        browser.quit()
    attach.video(session_id)
