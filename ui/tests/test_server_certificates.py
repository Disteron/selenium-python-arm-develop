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
1. Перейти на вкладку "Серверные сертификаты" и нажимаем кнопку “Обновить” в верхней части стенда.
2. Выполняем сортировку по “Тип сервера”, “URL”, “Сертификаты”.
3. Выбираем MDMServer и нажимаем "Необходимо загрузить серверный сертификат"
4. Добавляем сертификат
5. Перейти на вкладку "Подключение к серверам" и нажимаем кнопку “Обновить”
11. Выполняем повторную сортировку по “Тип сервера”, “URL”, “Сертификаты”. Нажимаем кнопку “Обновить” в верхней 
    части стенда.
13. Переходим на вкладку "Серверные сертификаты" и удаляем сертификат.

"""


RANDOM = str(random.randint(1, 999999))


@pytest.mark.regress
@pytest.mark.ui
@pytest.mark.id_25
@pytest.mark.incremental
@pytest.mark.usefixtures("start_browser")
@allure.title('[UI] Серверные сертификаты')
@allure.severity(Severity.CRITICAL)
@allure.feature('[UI] Серверные сертификаты')
@allure.description('[UI] Серверные сертификаты')
class TestServerCertificates:

    @allure.title('Перейти на вкладку "Серверные сертификаты" и нажимаем кнопку “Обновить” в верхней части стенда.')
    def test_connecting_to_servers_1(self):
        common_steps.auth()
        page = shared_vars.set_page(name="Главная страница")
        page.click_button(locator=page.get_locator_by_name(name="Серверные сертификаты"))
        page.click_button(locator=page.get_locator_by_name(name="Обновить"))

    @allure.title('Выполняем сортировку по “Наименование”, “Формат файла”,'
                  ' “Субъект”, “Издатель”, “Период действия, не позднее”. '
                  'Нажимаем кнопку “Обновить” в верхней части стенда.')
    def test_connecting_to_servers_2(self):
        page = shared_vars.set_page(name="Серверные сертификаты")
        page.click_button(locator=page.get_locator_by_name(name="Сортировка", text='Наименование'))
        page.click_button(locator=page.get_locator_by_name(name="Сортировка", text='Формат файла'))
        page.click_button(locator=page.get_locator_by_name(name="Сортировка", text='Субъект'))
        page.click_button(locator=page.get_locator_by_name(name="Сортировка", text='Издатель'))
        page.click_button(locator=page.get_locator_by_name(name="Сортировка", text='Период действия, не позднее'))

    @allure.title('Добавляем сертификат')
    def test_connecting_to_servers_4(self):
        page = shared_vars.set_page(name="Серверные сертификаты")
        path = os.path.dirname(__file__)
        final_path = os.path.join(path, 'files/ca.pem')
        page.upload_file(locator=page.get_locator_by_name(name="Загрузить файл"), file_absolute_path=final_path)
        page.fill_field(locator=page.get_locator_by_name(name="Наименование"), value='ca.pem_' + RANDOM)
        page.click_button(locator=page.get_locator_by_name(name="Сохранить"))

    @allure.title('Выполняем повторную сортировку по “Наименование”, “Формат файла”,'
                  ' “Субъект”, “Издатель”, “Период действия, не позднее”. '
                  'Нажимаем кнопку “Обновить” в верхней части стенда.')
    def test_connecting_to_servers_11(self):
        page = shared_vars.set_page(name="Серверные сертификаты")
        page.click_button(locator=page.get_locator_by_name(name="Сортировка", text='Наименование'))
        page.click_button(locator=page.get_locator_by_name(name="Сортировка", text='Формат файла'))
        page.click_button(locator=page.get_locator_by_name(name="Сортировка", text='Субъект'))
        page.click_button(locator=page.get_locator_by_name(name="Сортировка", text='Издатель'))
        page.click_button(locator=page.get_locator_by_name(name="Сортировка", text='Период действия, не позднее'))
        page = shared_vars.set_page(name="Главная страница")
        page.click_button(locator=page.get_locator_by_name(name="Обновить"))

    @allure.title('Переходим на вкладку "Серверные сертификаты" и удаляем сертификат и '
                  'нажимаем кнопку “Обновить” в верхней части стенда.')
    def test_connecting_to_servers_12(self):
        page = shared_vars.set_page(name="Серверные сертификаты")
        page.click_button(locator=page.get_locator_by_name(name='ca_pem', random=RANDOM))
        page.click_button(locator=page.get_locator_by_name(name="Удалить"))
        page.click_button(locator=page.get_locator_by_name(name="Да"))
        page = shared_vars.set_page(name="Главная страница")
        page.click_button(locator=page.get_locator_by_name(name="Обновить"))
        page.error_checking(locator=page.get_locator_by_name(name="Внутренняя ошибка"))
