import os
import random
import time
import allure
import pytest
import shared_vars


from allure_commons.types import Severity
from requests_api.core.request import Request
from ui.steps import common_steps


"""
Предуслове:
1. Добавление лицензии


Шаги:
1. Перейти на вкладку "Подключение к серверам" и нажимаем кнопку “Обновить” в верхней части стенда.
2. Выполняем сортировку по “Тип сервера”, “URL”, “Сертификаты”.
3. Выбираем MDMServer и нажимаем "Необходимо загрузить серверный сертификат"
4. Добавляем сертификат
5. Перейти на вкладку "Подключение к серверам" и нажимаем кнопку “Обновить”
6. Для "MDMServer" в поле "URL" вводим ip, и добавляем чекбокс серверного сертификата и нажимаем "Сохранить".
   Убираем чекбокс и нажимаем "Сохранить".
7. Для "SCEPServer" в поле "URL" вводим ip, и добавляем чекбокс серверного сертификата и нажимаем "Сохранить".
   Убираем чекбокс и нажимаем "Сохранить".
8. Для "SocketServer" в поле "URL" вводим ip, и добавляем чекбокс серверного сертификата и нажимаем "Сохранить".
   Убираем чекбокс и нажимаем "Сохранить".
9. Для "WinMDM Enrollment" в поле "URL" вводим ip, и добавляем чекбокс серверного сертификата и нажимаем "Сохранить".
   Убираем чекбокс и нажимаем "Сохранить".
10. Для "WinMDM Management" в поле "URL" вводим ip, и добавляем чекбокс серверного сертификата и нажимаем "Сохранить".
    Убираем чекбокс и нажимаем "Сохранить".
11. Выполняем повторную сортировку по “Тип сервера”, “URL”, “Сертификаты”. Нажимаем кнопку “Обновить” в верхней 
    части стенда.
13. Переходим на вкладку "Серверные сертификаты" и удаляем сертификат.

"""

time_now = str(int(time.time()) * 1000 + 999)
RANDOM = str(random.randint(1, 999999))
shared_vars.COMMON_VAR["RANDOM"] = RANDOM

URL_MDM = "https://" + shared_vars.APPLICATION_PROPERTIES["url"] + ":443"
URL_SCEP = "https://" + shared_vars.APPLICATION_PROPERTIES["url"] + ":8082"
URL_SOCKET = shared_vars.APPLICATION_PROPERTIES["url"] + ":50001"
URL_ENROLLMENT = "https://" + shared_vars.APPLICATION_PROPERTIES["url"],
URL_MANAGEMENT = "https://" + shared_vars.APPLICATION_PROPERTIES["url"] + ":8444"


@pytest.mark.regress
@pytest.mark.ui
@pytest.mark.id_25
@pytest.mark.incremental
@pytest.mark.usefixtures("start_browser")
@allure.title('[UI] Подключение к серверамй')
@allure.severity(Severity.CRITICAL)
@allure.feature('[UI] Подключение к серверам')
@allure.description('[UI] Подключение к серверам')
class TestConnectingToServer:

    @allure.title('Предусловие')
    @pytest.mark.usefixtures("start_function")
    def test_precondition(self):
        api_user = shared_vars.APPLICATION_PROPERTIES["api_user"]
        api_password = shared_vars.APPLICATION_PROPERTIES["api_password"]

        Request(method='post',
                endpoint='/login',
                template='auth',
                name='Авторизация',
                api_user=api_user,
                api_password=api_password) \
            .fire()

        Request(method='post',
                endpoint='/api/v1/license',
                template='license',
                name='Добавление Лицензии') \
            .fire()

    @allure.title('Перейти на вкладку "Подключение к серверам" и нажимаем кнопку “Обновить” в верхней части стенда.')
    def test_connecting_to_servers_1(self):
        common_steps.auth()
        page = shared_vars.set_page(name="Главная страница")
        page.click_button(locator=page.get_locator_by_name(name="Подключения к серверам"))
        page.click_button(locator=page.get_locator_by_name(name="Обновить"))

    @allure.title('Выполняем сортировку по “Тип сервера”, “URL”, “Сертификаты”.')
    def test_connecting_to_servers_2(self):
        page = shared_vars.set_page(name="Подключения к серверам")
        page.click_button(locator=page.get_locator_by_name(name="Сортировка(Тип сервера)"))
        page.click_button(locator=page.get_locator_by_name(name="Сортировка(URL)"))
        page.click_button(locator=page.get_locator_by_name(name="Сортировка(Сертификаты)"))

    @allure.title('Выбираем MDMServer и нажимаем "Необходимо загрузить серверный сертификат"')
    def test_connecting_to_servers_3(self):
        page = shared_vars.set_page(name="Подключения к серверам")
        page.click_button(locator=page.get_locator_by_name(name="Тип сервера(MDMServer)"))
        page = shared_vars.set_page(name="Главная страница")
        page.click_button(locator=page.get_locator_by_name(name="Серверные сертификаты"))

    @allure.title('Добавляем сертификат')
    def test_connecting_to_servers_4(self):
        page = shared_vars.set_page(name="Серверные сертификаты")
        path = os.path.dirname(__file__)
        final_path = os.path.join(path, 'files/ca.pem')
        page.upload_file(locator=page.get_locator_by_name(name="Загрузить файл"), file_absolute_path=final_path)
        page.fill_field(locator=page.get_locator_by_name(name="Наименование"), value='ca.pem_' + RANDOM)
        page.click_button(locator=page.get_locator_by_name(name="Сохранить"))

    @allure.title('Перейти на вкладку "Подключение к серверам" и нажимаем кнопку “Обновить”')
    def test_connecting_to_servers_5(self):
        page = shared_vars.set_page(name="Главная страница")
        page.click_button(locator=page.get_locator_by_name(name="Подключения к серверам"))
        page.click_button(locator=page.get_locator_by_name(name="Обновить"))

    @allure.title('Для "MDMServer" в поле "URL" вводим ip, и добавляем чекбокс серверного сертификата '
                  'и нажимаем "Сохранить". Убираем чекбокс и нажимаем "Сохранить".')
    def test_connecting_to_servers_6(self):
        page = shared_vars.set_page(name="Подключения к серверам")
        page.click_button(locator=page.get_locator_by_name(name="Тип сервера(MDMServer)"))
        page.fill_field(locator=page.get_locator_by_name(name="Поле(URL)"), value='https://10.17.7.' + RANDOM + ':443')
        page.click_button(locator=page.format_locator(page.UNIVERSAL_DIV_XPATH, div_text="ca.pem_" + RANDOM))
        page.click_button(locator=page.get_locator_by_name(name="Сохранить"))
        page.fill_field(locator=page.get_locator_by_name(name="Поле(URL)"), value=URL_MDM)
        page.click_button(locator=page.format_locator(page.UNIVERSAL_DIV_XPATH, div_text="ca.pem_" + RANDOM))
        page.click_button(locator=page.get_locator_by_name(name="Сохранить"))

    @allure.title('Для "SCEPServer" в поле "URL" вводим ip, и добавляем чекбокс серверного сертификата '
                  'и нажимаем "Сохранить". Убираем чекбокс и нажимаем "Сохранить".')
    def test_connecting_to_servers_7(self):
        page = shared_vars.set_page(name="Подключения к серверам")
        page.click_button(locator=page.get_locator_by_name(name="Тип сервера(SCEPServer)"))
        page.fill_field(locator=page.get_locator_by_name(name="Поле(URL)"), value='https://10.17.7.' + RANDOM + ':8082')
        page.click_button(locator=page.format_locator(page.UNIVERSAL_DIV_XPATH, div_text="ca.pem_" + RANDOM))
        page.click_button(locator=page.get_locator_by_name(name="Сохранить"))
        page.fill_field(locator=page.get_locator_by_name(name="Поле(URL)"), value=URL_SCEP)
        page.click_button(locator=page.format_locator(page.UNIVERSAL_DIV_XPATH, div_text="ca.pem_" + RANDOM))
        page.click_button(locator=page.get_locator_by_name(name="Сохранить"))

    @allure.title('Для "SocketServer" в поле "URL" вводим ip, и добавляем чекбокс серверного сертификата '
                  'и нажимаем "Сохранить". Убираем чекбокс и нажимаем "Сохранить".')
    def test_connecting_to_servers_8(self):
        page = shared_vars.set_page(name="Подключения к серверам")
        page.click_button(locator=page.get_locator_by_name(name="Тип сервера(SocketServer)"))
        page.fill_field(locator=page.get_locator_by_name(name="Поле(URL)"), value='10.17.7.' + RANDOM + ':50001')
        page.click_button(locator=page.format_locator(page.UNIVERSAL_DIV_XPATH, div_text="ca.pem_" + RANDOM))
        page.click_button(locator=page.get_locator_by_name(name="Сохранить"))
        page.fill_field(locator=page.get_locator_by_name(name="Поле(URL)"), value=URL_SOCKET)
        page.click_button(locator=page.format_locator(page.UNIVERSAL_DIV_XPATH, div_text="ca.pem_" + RANDOM))
        page.click_button(locator=page.get_locator_by_name(name="Сохранить"))

    @allure.title('Для "WinMDM Enrollment" в поле "URL" вводим ip, и добавляем чекбокс серверного сертификата '
                  'и нажимаем "Сохранить". Убираем чекбокс и нажимаем "Сохранить".')
    def test_connecting_to_servers_9(self):
        page = shared_vars.set_page(name="Подключения к серверам")
        page.click_button(locator=page.get_locator_by_name(name="Тип сервера(WinMDM Enrollment)"))
        page.fill_field(locator=page.get_locator_by_name(name="Поле(URL)"), value='https://10.17.7.' + RANDOM)
        page.click_button(locator=page.format_locator(page.UNIVERSAL_DIV_XPATH, div_text="ca.pem_" + RANDOM))
        page.click_button(locator=page.get_locator_by_name(name="Сохранить"))
        page.fill_field(locator=page.get_locator_by_name(name="Поле(URL)"), value=URL_ENROLLMENT)
        page.click_button(locator=page.format_locator(page.UNIVERSAL_DIV_XPATH, div_text="ca.pem_" + RANDOM))
        page.click_button(locator=page.get_locator_by_name(name="Сохранить"))

    @allure.title('Для "WinMDM Management" в поле "URL" вводим ip, и добавляем чекбокс серверного сертификата '
                  'и нажимаем "Сохранить". Убираем чекбокс и нажимаем "Сохранить".')
    def test_connecting_to_servers_10(self):
        page = shared_vars.set_page(name="Подключения к серверам")
        page.click_button(locator=page.get_locator_by_name(name="Тип сервера(WinMDM Management)"))
        page.fill_field(locator=page.get_locator_by_name(name="Поле(URL)"), value='https://10.17.7.' + RANDOM + ':8444')
        page.click_button(locator=page.format_locator(page.UNIVERSAL_DIV_XPATH, div_text="ca.pem_" + RANDOM))
        page.click_button(locator=page.get_locator_by_name(name="Сохранить"))
        page.fill_field(locator=page.get_locator_by_name(name="Поле(URL)"), value=URL_MANAGEMENT)
        page.click_button(locator=page.format_locator(page.UNIVERSAL_DIV_XPATH, div_text="ca.pem_" + RANDOM))
        page.click_button(locator=page.get_locator_by_name(name="Сохранить"))

    @allure.title('Выполняем повторную сортировку по “Тип сервера”, “URL”, “Сертификаты”. '
                  'Нажимаем кнопку “Обновить” в верхней части стенда.')
    def test_connecting_to_servers_11(self):
        page = shared_vars.set_page(name="Подключения к серверам")
        page.click_button(locator=page.get_locator_by_name(name="Сортировка(Тип сервера)"))
        page.click_button(locator=page.get_locator_by_name(name="Сортировка(URL)"))
        page.click_button(locator=page.get_locator_by_name(name="Сортировка(Сертификаты)"))
        page = shared_vars.set_page(name="Главная страница")
        page.click_button(locator=page.get_locator_by_name(name="Обновить"))

    @allure.title('Переходим на вкладку "Серверные сертификаты" и удаляем сертификат.')
    def test_connecting_to_servers_12(self):
        page = shared_vars.set_page(name="Главная страница")
        page.click_button(locator=page.get_locator_by_name(name="Серверные сертификаты"))
        page = shared_vars.set_page(name="Серверные сертификаты")
        page.click_button(locator=page.get_locator_by_name(name='ca_pem', random=RANDOM))
        page.click_button(locator=page.get_locator_by_name(name="Удалить"))
        page.click_button(locator=page.get_locator_by_name(name="Да"))
        page = shared_vars.set_page(name="Главная страница")
        page.error_checking(locator=page.get_locator_by_name(name="Внутренняя ошибка"))
