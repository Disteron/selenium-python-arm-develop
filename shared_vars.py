import os
import allure

from ui.pages.administrator_page import AdministratorPage
from ui.pages.applications_page import ApplicationsPage
from ui.pages.auth_page import AuthPage
from ui.pages.base_page import BasePage
from ui.pages.calender_page import CalenderPage
from ui.pages.configurations_page import ConfigurationsPage
from ui.pages.connecting_to_servers_page import ConnectionToServers
from ui.pages.license_page import LicensePage
from ui.pages.main_page import MainPage
from ui.pages.management_rules_page import ManagementRulesPage
from ui.pages.operating_systems_page import OperationSystem
from ui.pages.organizational_structure_page import OrganizationalStructurePage
from ui.pages.owner_delegation_page import OwnerDelegationPage
from ui.pages.roles_page import RolesPage
from ui.pages.server_certificates_page import ServerCertificates
from ui.pages.staff_page import StaffPage
from ui.pages.profiles_page import ProfilesPage

DRIVER = None
PAGE = None
SESSION = None
COMMON_VAR = {}
APPLICATION_PROPERTIES = {}

PROJECT_ROOT = os.path.dirname(__file__)


PAGES = {
    'Базовая страница': BasePage,
    'Главная страница': MainPage,
    'Форма авторизации': AuthPage,
    'Профили': ProfilesPage,
    'Правила управления(Приложения)': ManagementRulesPage,
    'Конфигурации': ConfigurationsPage,
    'ОСШ': OrganizationalStructurePage,
    'Сотрудники': StaffPage,
    'Роли': RolesPage,
    'Администраторы': AdministratorPage,
    'Операционные системы': OperationSystem,
    'Календарь': CalenderPage,
    'Приложения': ApplicationsPage,
    'Серверные сертификаты': ServerCertificates,
    'Подключения к серверам': ConnectionToServers,
    'Лицензия': LicensePage,
    'Владелец и делегирование': OwnerDelegationPage,
}


def set_page(name):
    PAGE = PAGES[name]()
    with allure.step(f"Установлена страница - {name}"):
        return PAGE


CHROME_DRIVER_DICT = {
    'linux': os.path.join(PROJECT_ROOT, 'ui/webdrivers/chrome/chromedriver_linux64'),
    'darwin': os.path.join(PROJECT_ROOT, 'ui/webdrivers/chrome/chromedriver_mac'),
    'win32': os.path.join(PROJECT_ROOT, 'ui/webdrivers/chrome/chromedriver_win32_64.exe'),
    'win64': os.path.join(PROJECT_ROOT, 'ui/webdrivers/chrome/chromedriver_win32_64.exe')
}

OPERA_DRIVER_DICT = {
    'linux': os.path.join(PROJECT_ROOT, 'ui/webdrivers/opera/operadriver_linux64'),
    'darwin': os.path.join(PROJECT_ROOT, 'ui/webdrivers/opera/operadriver_mac64'),
    'win32': os.path.join(PROJECT_ROOT, 'ui/webdrivers/opera/operadriver_win32.exe'),
    'win64': os.path.join(PROJECT_ROOT, 'ui/webdrivers/opera/operadriver_win64.exe'),
}

YANDEX_DRIVER_DICT = {
    'linux': os.path.join(PROJECT_ROOT, 'ui/webdrivers/yandex/yandexdriver-21.2.1.94-linux'),
    'darwin': os.path.join(PROJECT_ROOT, 'ui/webdrivers/chrome/chromedriver_mac'),
    'win32': os.path.join(PROJECT_ROOT, 'ui/webdrivers/yandex/yandexdriver-21.3.0.673-win.exe'),
    'win64': os.path.join(PROJECT_ROOT, 'ui/webdrivers/yandex/yandexdriver-21.3.0.673-win.exe'),
}
