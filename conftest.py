import os
import sys
import allure
import pytest
import requests
import shared_vars

from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver
from ui.core.logger_listener import LoggedListener
from shared_vars import PROJECT_ROOT
from requests_api.report import miro, telegram, slackbot


def pytest_addoption(parser):
    """Запускается один раз перед началом тестового набора(теста)
    Используется для настройки тестового окружения
    set_application_props() - Устанавливает значения переменных из app.properties в словарь APPLICATION_PROPERTIES

    :param parser: парсер используется для парсинга параметров командной строки
    """
    set_application_props()
    parser.addoption('--browser', action='store', help='available browser: chrome, yandex, opera')
    parser.addoption('--ip', action='store', help='available IP')
    parser.addoption('--headless', action='store', help='фоновый режим')
    parser.addoption('--stand-version', action='store', help='stand-version')


def pytest_configure(config):
    stand_version = config.getoption('--stand-version')
    if stand_version:
        shared_vars.APPLICATION_PROPERTIES["stand_version"] = stand_version

    headless = config.getoption('--headless')
    if headless:
        shared_vars.APPLICATION_PROPERTIES["headless"] = headless

    ip = config.getoption('--ip')
    if ip:
        shared_vars.APPLICATION_PROPERTIES["url"] = ip
        shared_vars.APPLICATION_PROPERTIES["host"] = ip

    browser_name = config.getoption('--browser')
    if browser_name:
        shared_vars.APPLICATION_PROPERTIES['browser'] = browser_name.lower()


@pytest.fixture(scope="class")
def start_browser():
    """Фикстура для UI тестов
    Перед началом теста поднимает браузер с настройками, после закрывает браузер (делает скриншот, если тест упал)
    """
    browser_name = shared_vars.APPLICATION_PROPERTIES["browser"]
    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-gpu')
    if shared_vars.APPLICATION_PROPERTIES["headless"] == "true":
        options.add_argument('--headless')
    options.add_argument('--window-size=1920,1080')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('lang=ru')
    options.add_argument('--ignore-ssl-errors=yes')
    options.add_argument('--ignore-certificate-errors')

    if browser_name == 'chrome':
        driver = webdriver.Chrome(executable_path=shared_vars.CHROME_DRIVER_DICT[sys.platform], options=options)
    elif browser_name == 'opera':
        driver = webdriver.Opera(executable_path=shared_vars.OPERA_DRIVER_DICT[sys.platform], options=options)
    elif browser_name == 'yandex':
        driver = webdriver.Opera(executable_path=shared_vars.YANDEX_DRIVER_DICT[sys.platform], options=options)
    else:
        driver = webdriver.Chrome(executable_path=shared_vars.CHROME_DRIVER_DICT[sys.platform], options=options)
    driver.maximize_window()

    listener = LoggedListener()
    shared_vars.DRIVER = EventFiringWebDriver(driver=driver, event_listener=listener)

    yield

    shared_vars.DRIVER.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Исполняется после прохода каждого автотеста, если тест упал, то делает скриншот и следующие тесты в классе skip
    """
    if "incremental" in item.keywords:
        if call.excinfo is not None:
            parent = item.parent
            parent._previousfailed = item

    outcome = yield
    result = outcome.get_result()
    if result.outcome == "failed" and shared_vars.DRIVER is not None:
        allure.attach(body=shared_vars.DRIVER.get_screenshot_as_png(),
                      name='screenshot',
                      attachment_type=AttachmentType.PNG)


def pytest_runtest_setup(item):
    """Используется для пропуска тестов в классе, если предыдущий failed
    """
    previousfailed = getattr(item.parent, "_previousfailed", None)
    if previousfailed is not None:
        pytest.skip("previous test failed (%s)" % previousfailed.name)


@pytest.fixture(scope="class")
def start_session():
    """Фикстура для API тестов
    Создает сессию через которую отправляются запросы
    """
    session = requests.Session()
    shared_vars.SESSION = session

    yield

    session.close()


@pytest.fixture(scope="function")
def start_function():
    """Фикстура для API тестов
    Создает сессию через которую отправляются запросы в рамках одного метода
    """
    session = requests.Session()
    shared_vars.SESSION = session

    yield

    session.close()


def set_application_props():
    """Устанавливает значения переменных из app.properties в словарь shared_vars.APPLICATION_PROPERTIES
    перед началом прогона тестового набора
    """
    with open(os.path.join(PROJECT_ROOT, 'app.properties')) as properties:
        for line in properties:
            key, value = line.split("=", 1)
            shared_vars.APPLICATION_PROPERTIES[key.strip()] = value.strip()


# TODO: Исправить условие по отправке отчетов по маркам. Добавить новый отчет для марки filling, id, api, ui
def pytest_terminal_summary(terminalreporter, config):
    """Запускается один раз после прогона тестового набора

    miro.after_pytest_report_on_miro(...) - отправка результатов прогона в Miro
    telegram.telegram_bot_send_text(report) - отправка результатов прогона в Telegram

    :param terminalreporter: хранит список статусов по тестам (passed, failed ...etc)
    :param config: данные конфига теста (какие марки использовались или параметры при запуске)
    """
    if "regress" or "smoke" == config.option.markexpr:
        report = miro.after_pytest_report_on_miro(terminalreporter, config)
        # telegram.telegram_bot_send_text(report)
        # slackbot.slack_bot_send_text(report)
