import random
import allure
import pytest
import shared_vars


from allure_commons.types import Severity
from ui.steps import common_steps


TEST = ['Администратор баз данных', 'Архитектор программного обеспечения', 'Менеджер по информационным технологиям',
        'Программист', 'Руководитель разработки программного обеспечения',
        'Специалист по автоматизированным системам управления производством', 'Ведущий специалист']

SURNAME = 'Surname_' + str(random.randint(10000, 1000000))
NAME = 'Name_' + str(random.randint(10000, 1000000))
PATRONYMIC = 'Patronymic_' + str(random.randint(10000, 1000000))
POST = random.choice(TEST)
EMAIL_DOMAIN = 'Orudenko' + str(random.randint(10000, 1000000)) + '@niisokb.ru'
EMAIL_LOGIN = 'Orudenko' + str(random.randint(10000, 1000000))
EMAIL = 'Orudenko@niisokb.ru' + str(random.randint(10000, 1000000))

ANOTHER_SURNAME = 'AnotherSurname_' + str(random.randint(10000, 1000000))
ANOTHER_NAME = 'AnotherName_' + str(random.randint(10000, 1000000))
ANOTHER_PATRONYMIC = 'Patronymic_' + str(random.randint(10000, 1000000))
ANOTHER_POST = random.choice(TEST)
ANOTHER_EMAIL_DOMAIN = 'Orudenko' + str(random.randint(10000, 1000000)) + '@niisokb.ru'
ANOTHER_EMAIL_LOGIN = 'Orudenko' + str(random.randint(10000, 1000000))
ANOTHER_EMAIL = 'Orudenko@niisokb.ru' + str(random.randint(10000, 1000000))


@pytest.mark.ui
@pytest.mark.smoke
@pytest.mark.regress
@pytest.mark.id_19
@pytest.mark.incremental
@pytest.mark.usefixtures("start_browser")
@allure.title('[UI] Проверка сотрудника')
@allure.severity(Severity.CRITICAL)
@allure.feature('[UI] Staff')
@allure.description('[UI] Проверка создания, редактирования, удаления сотрудника')
class TestCheckStaff:

    @allure.title('[UI] Добавление Сотрудника')
    def test_add_staff(self):
        common_steps.auth()
        page = shared_vars.set_page(name="Главная страница")
        page.click_button(locator=page.get_locator_by_name(name="Сотрудники"))
        page = shared_vars.set_page(name="Сотрудники")
        page.fill_field(locator=page.get_locator_by_name(name="Фамилия"), value=SURNAME)
        page.fill_field(locator=page.get_locator_by_name(name="Имя"), value=NAME)
        page.fill_field(locator=page.get_locator_by_name(name="Отчество"), value=PATRONYMIC)
        page.fill_field(locator=page.get_locator_by_name(name="Должность"), value=POST)
        page.fill_field(locator=page.get_locator_by_name(name="E-mail Домен"), value=EMAIL_DOMAIN)
        page.fill_field(locator=page.get_locator_by_name(name="Е-mail Логин"), value=EMAIL_LOGIN)
        page.fill_field(locator=page.get_locator_by_name(name="E-mail"), value=EMAIL)
        page.click_button(locator=page.get_locator_by_name(name="root"))
        page.click_button(locator=page.get_locator_by_name(name="Сохранить"))
        page.click_button(locator=page.format_locator(page.UNIVERSAL_DIV_XPATH,
                                                      div_text=SURNAME + " " + NAME + " " + PATRONYMIC))

    @allure.title('[UI] Редактирование сотрудника')
    def test_editing_staff(self):
        page = shared_vars.set_page(name="Сотрудники")
        page.fill_field(locator=page.get_locator_by_name(name="Фамилия"), value=ANOTHER_SURNAME)
        page.fill_field(locator=page.get_locator_by_name(name="Имя"), value=ANOTHER_NAME)
        page.fill_field(locator=page.get_locator_by_name(name="Отчество"), value=ANOTHER_PATRONYMIC)
        page.fill_field(locator=page.get_locator_by_name(name="Должность"), value=ANOTHER_POST)
        page.fill_field(locator=page.get_locator_by_name(name="E-mail Домен"), value=ANOTHER_EMAIL_DOMAIN)
        page.fill_field(locator=page.get_locator_by_name(name="Е-mail Логин"), value=ANOTHER_EMAIL_LOGIN)
        page.fill_field(locator=page.get_locator_by_name(name="E-mail"), value=ANOTHER_EMAIL)
        page.click_button(locator=page.get_locator_by_name(name="root"))
        page.click_button(locator=page.get_locator_by_name(name="Сохранить"))
        page.click_button(locator=page.format_locator(page.UNIVERSAL_DIV_XPATH,
                                                      div_text=ANOTHER_SURNAME+" "+ANOTHER_NAME+" "+ANOTHER_PATRONYMIC))

    @allure.title('[UI] Удаление сотрудника')
    def test_delete_staff(self):
        page = shared_vars.set_page(name="Сотрудники")
        page.click_button(locator=page.get_locator_by_name(name="Удалить"))
        page.click_button(locator=page.get_locator_by_name(name="Да"))
