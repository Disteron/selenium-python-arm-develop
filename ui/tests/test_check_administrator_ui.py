import random
import allure
import pytest
import shared_vars


from allure_commons.types import Severity
from ui.steps import common_steps


POST = ['Администратор баз данных', 'Архитектор программного обеспечения', 'Менеджер по информационным технологиям',
        'Программист', 'Руководитель разработки программного обеспечения',
        'Специалист по автоматизированным системам управления производством', 'Ведущий специалист']
POST_2 = random.choice(POST)

SURNAME = 'Surname_' + str(random.randint(10000, 1000000))
NAME = 'Name_' + str(random.randint(10000, 1000000))
PATRONYMIC = 'Patronymic_' + str(random.randint(10000, 1000000))
MAIL = 'orudenko@niisokb.ru'
NAME_ADMIN = 'admin_' + str(random.randint(100, 100000))
TIME = '2025-09-25 0:00'
PASSWORD = 'test'
NEW_PASSWORD = 'P@ssw0rd'
REPEAT_THE_INPUT = NEW_PASSWORD


@pytest.mark.ui
@pytest.mark.smoke
@pytest.mark.regress
@pytest.mark.id_15
@pytest.mark.incremental
@pytest.mark.usefixtures("start_browser")
@allure.title('[UI] Проверка Администраторы')
@allure.severity(Severity.MINOR)
@allure.feature('[UI] Administrator')
@allure.description('[UI] Проверка создания, редактирования, блокировки, '
                    'разблокировки, удаления Администратора и изменение его пароля')
class TestCheckAdministrators:

    @allure.title('[UI] Добавление Администратора')
    def test_add_check_administrators(self):
        common_steps.auth()
        page = shared_vars.set_page(name="Базовая страница")
        page.wait_invisibility_of_element(locator=page.get_locator_by_name(name='Загрузка'))
        page = shared_vars.set_page(name="Главная страница")
        page.click_button(locator=page.get_locator_by_name(name="Администраторы"))
        page = shared_vars.set_page(name="Администраторы")
        page.click_button(locator=page.get_locator_by_name(name="Добавить"))
        page.fill_field(locator=page.get_locator_by_name(name="Фамилия"), value=SURNAME)
        page.fill_field(locator=page.get_locator_by_name(name="Имя"), value=NAME)
        page.fill_field(locator=page.get_locator_by_name(name="Отчество"), value=PATRONYMIC)
        page.fill_field(locator=page.get_locator_by_name(name="Имя администратора"), value=NAME_ADMIN)
        page.fill_field(locator=page.get_locator_by_name(name="Электронная почта"), value=MAIL)
        page.fill_field(locator=page.get_locator_by_name(name="Должность"), value=POST_2)
        page.fill_field(locator=page.get_locator_by_name(name="Срок действия учётной записи"), value=TIME)
        page.fill_field(locator=page.get_locator_by_name(name="Пароль"), value=NEW_PASSWORD)
        page.click_button(locator=page.get_locator_by_name(name="Администратор ИТ"))
        page.click_button(locator=page.get_locator_by_name(name="Место работы root"))
        page.click_button(locator=page.get_locator_by_name(name="Область управления"))
        page.click_button(locator=page.get_locator_by_name(name="Область управления root"))
        page.click_button(locator=page.get_locator_by_name(name="Сохранить"))

    @allure.title('[UI] Проверка созданного Администратора')
    def test_check_administrators(self):
        page = shared_vars.set_page(name="Администраторы")
        page.click_button(locator=page.format_locator(page.UNIVERSAL_DIV_XPATH, div_text=NAME_ADMIN))
        page.click_button(locator=page.get_locator_by_name(name="root"))
        page.click_button(locator=page.get_locator_by_name(name="Выход"))
        page = shared_vars.set_page(name="Форма авторизации")
        page.fill_field(locator=page.get_locator_by_name(name="Имя пользователя"), value=NAME_ADMIN)
        page.fill_field(locator=page.get_locator_by_name(name="Пароль"), value=NEW_PASSWORD)
        page.click_button(locator=page.get_locator_by_name(name="Войти"))
        page = shared_vars.set_page(name="Базовая страница")
        page.wait_invisibility_of_element(locator=page.get_locator_by_name(name='Загрузка'))
        page = shared_vars.set_page(name="Администраторы")
        page.click_button(locator=page.format_locator(page.UNIVERSAL_SPAN_XPATH, span_text=NAME_ADMIN))
        page.click_button(locator=page.get_locator_by_name(name="Выход"))

    @allure.title('[UI] Проверка заблокированного Администратора')
    def test_check_blocking_administrators(self):
        page = shared_vars.set_page(name="Форма авторизации")
        page.fill_field(locator=page.get_locator_by_name(name="Имя пользователя"), value='root')
        page.fill_field(locator=page.get_locator_by_name(name="Пароль"), value=NEW_PASSWORD)
        page.click_button(locator=page.get_locator_by_name(name="Войти"))
        page = shared_vars.set_page(name="Базовая страница")
        page.wait_invisibility_of_element(locator=page.get_locator_by_name(name='Загрузка'))
        page = shared_vars.set_page(name="Главная страница")
        page.click_button(locator=page.get_locator_by_name(name="Администраторы"))
        page = shared_vars.set_page(name="Администраторы")
        page.click_button(locator=page.format_locator(page.UNIVERSAL_DIV_XPATH,
                                                      div_text=NAME_ADMIN))
        page.click_button(locator=page.get_locator_by_name(name="Заблокировать"))
        page.click_button(locator=page.format_locator(page.UNIVERSAL_DIV_XPATH,
                                                      div_text=NAME_ADMIN))
        page.click_button(locator=page.get_locator_by_name(name="root"))
        page.click_button(locator=page.get_locator_by_name(name="Выход"))
        page = shared_vars.set_page(name="Форма авторизации")
        page.fill_field(locator=page.get_locator_by_name(name="Имя пользователя"), value=NAME_ADMIN)
        page.fill_field(locator=page.get_locator_by_name(name="Пароль"), value=NEW_PASSWORD)
        page.click_button(locator=page.get_locator_by_name(name="Войти"))
        page = shared_vars.set_page(name="Администраторы")
        page.get_element(locator=page.get_locator_by_name(name='Администратор заблокирован'))

    @allure.title('[UI] Проверка Разблокированного Администратора')
    def test_check_unblock_administrators(self):
        page = shared_vars.set_page(name="Форма авторизации")
        page.fill_field(locator=page.get_locator_by_name(name="Имя пользователя"), value='root')
        page.fill_field(locator=page.get_locator_by_name(name="Пароль"), value=NEW_PASSWORD)
        page.click_button(locator=page.get_locator_by_name(name="Войти"))
        page = shared_vars.set_page(name="Базовая страница")
        page.wait_invisibility_of_element(locator=page.get_locator_by_name(name='Загрузка'))
        page = shared_vars.set_page(name="Главная страница")
        page.click_button(locator=page.get_locator_by_name(name="Администраторы"))
        page = shared_vars.set_page(name="Администраторы")
        page.click_button(locator=page.format_locator(page.UNIVERSAL_DIV_XPATH,
                                                      div_text=NAME_ADMIN))
        page.click_button(locator=page.get_locator_by_name(name="Разблокировать"))
        page.click_button(locator=page.format_locator(page.UNIVERSAL_DIV_XPATH,
                                                      div_text=NAME_ADMIN))
        page.click_button(locator=page.get_locator_by_name(name="root"))
        page.click_button(locator=page.get_locator_by_name(name="Выход"))
        page = shared_vars.set_page(name="Форма авторизации")
        page.fill_field(locator=page.get_locator_by_name(name="Имя пользователя"), value=NAME_ADMIN)
        page.fill_field(locator=page.get_locator_by_name(name="Пароль"), value=NEW_PASSWORD)
        page.click_button(locator=page.get_locator_by_name(name="Войти"))
        page = shared_vars.set_page(name="Базовая страница")
        page.wait_invisibility_of_element(locator=page.get_locator_by_name(name='Загрузка'))

    @allure.title('[UI] Удаление Администратора')
    def test_delete_check_administrators(self):
        page = shared_vars.set_page(name="Главная страница")
        page.click_button(locator=page.format_locator(page.UNIVERSAL_SPAN_XPATH, span_text=NAME_ADMIN))
        page.click_button(locator=page.get_locator_by_name(name="Выход"))
        page = shared_vars.set_page(name="Форма авторизации")
        page.fill_field(locator=page.get_locator_by_name(name="Имя пользователя"), value='root')
        page.fill_field(locator=page.get_locator_by_name(name="Пароль"), value=NEW_PASSWORD)
        page.click_button(locator=page.get_locator_by_name(name="Войти"))
        page = shared_vars.set_page(name="Базовая страница")
        page.wait_invisibility_of_element(locator=page.get_locator_by_name(name='Загрузка'))
        page = shared_vars.set_page(name="Главная страница")
        page.click_button(locator=page.get_locator_by_name(name="Администраторы"))
        page = shared_vars.set_page(name="Администраторы")
        page.click_button(locator=page.format_locator(page.UNIVERSAL_DIV_XPATH,
                                                      div_text=NAME_ADMIN))
        page.click_button(locator=page.get_locator_by_name(name="Удалить"))
        page.click_button(locator=page.get_locator_by_name(name="Да"))
        page = shared_vars.set_page(name="Главная страница")
        page.error_checking(locator=page.get_locator_by_name(name="Внутренняя ошибка"))
