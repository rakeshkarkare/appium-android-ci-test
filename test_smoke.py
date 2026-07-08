from appium import webdriver
from appium.options.android import UiAutomator2Options


def test_emulator_connects():
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.automation_name = "UiAutomator2"
    options.device_name = "emulator-5554"

    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
    try:
        assert driver.session_id is not None
    finally:
        driver.quit()