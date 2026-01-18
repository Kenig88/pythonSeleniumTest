import pytest
import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function", autouse=True)
def driver(request):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--incognito")
    options.add_argument("--window-size=1920,1080")
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(options=options)
    request.cls.driver = driver
    yield driver
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when in ("setup", "call", "teardown") and rep.failed:
        driver = item.funcargs.get("driver", None)

        # Фоллбек: если тест в классе, driver мог быть сохранён в request.cls.driver
        if driver is None:
            cls = getattr(item, "cls", None)
            driver = getattr(cls, "driver", None) if cls else None

        if driver:
            try:
                allure.attach(
                    driver.get_screenshot_as_png(),
                    name=f"failure_screenshot_{rep.when}",
                    attachment_type=AttachmentType.PNG
                )
            except Exception:
                pass

            try:
                allure.attach(
                    driver.current_url,
                    name=f"current_url_{rep.when}",
                    attachment_type=AttachmentType.TEXT
                )
            except Exception:
                pass


# import pytest
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
#
#
# @pytest.fixture(scope='function', autouse=True)
# def driver(request):
#     options = Options()
#     # options.add_argument('--headless')
#     options.add_argument('--incognito')
#     # options.add_argument('--no-sandbox')
#     # options.add_argument('--disable-dev-shm-usage')
#     options.add_argument('--window-size=1920,1080')
#     driver = webdriver.Chrome(options=options)
#     request.cls.driver = driver
#     yield driver
#     driver.quit()












# import pytest
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
#
#
# @pytest.fixture(scope='function', autouse=True)
# def driver(request):
#     options = Options()
#     # options.add_argument('--headless')
#     options.add_argument('--incognito')
#     # options.add_argument('--no-sandbox')
#     # options.add_argument('--disable-dev-shm-usage')
#     options.add_argument('--window-size=1920,1080')
#     driver = webdriver.Chrome(options=options)
#     request.cls.driver = driver
#     yield driver
#     driver.quit()
