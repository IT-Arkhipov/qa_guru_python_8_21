from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have

from config import settings

options = UiAutomator2Options().load_capabilities({
    # Specify device and os_version for testing
    # "platformName": "android",
    "platformVersion": "9.0",
    "deviceName": "Google Pixel 3",

    # Set URL of the application under test
    "app": settings.bs_app,

    # Set other BrowserStack capabilities
    'bstack:options': {
        "projectName": "Wikipedia app",
        "buildName": "browserstack-build",
        "sessionName": "BStack tests",

        # Set your access credentials
        "userName": settings.user_name,
        "accessKey": settings.access_key
    }
})

browser.config.driver = webdriver.Remote("http://hub.browserstack.com/wd/hub", options=options)
browser.config.timeout = 10.0

browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_skip_button")).click()
browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type('BrowserStack')
browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title')).should(have.size_greater_than(0))
browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title')).first.should(have.text('BrowserStack'))

browser.quit()
