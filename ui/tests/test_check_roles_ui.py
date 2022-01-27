import random
import allure
import pytest
import shared_vars


from allure_commons.types import Severity
from ui.steps import common_steps


NAME = 'Admin_' + str(random.randint(10000, 1000000))
ANOTHER_NAME = 'AdminRU' + str(random.randint(10000, 1000000))


@pytest.mark.ui
@pytest.mark.smoke
@pytest.mark.regress
@pytest.mark.id_18
@pytest.mark.incremental
@pytest.mark.usefixtures("start_browser")
@allure.title('[UI] Проверка Роли')
@allure.severity(Severity.CRITICAL)
@allure.feature('[UI] Roles')
@allure.description('[UI] Проверка создания, редактирования, удаления Роли')
class TestCheckRoles:

    @allure.title('[UI] Добавление Роли')
    def test_add_check_roles(self):
        common_steps.auth()
        page = shared_vars.set_page(name="Главная страница")
        page.click_button(locator=page.get_locator_by_name(name="Роли"))
        page = shared_vars.set_page(name="Роли")
        page.click_button(locator=page.get_locator_by_name(name="Добавить"))
        page.fill_field(locator=page.get_locator_by_name(name="Введите имя новой Роли (Добавление)"), value=NAME)

    @allure.title('[UI] Добавление полномочий для роли')
    def test_add_authority_check_roles(self):
        page = shared_vars.set_page(name="Роли")
        page.click_button(locator=page.get_locator_by_name(
            name="Чек-бокс полномочие новой роли",
            text='Информация об устройствах'))
        page.click_button(locator=page.get_locator_by_name(
            name="Чек-бокс полномочие новой роли",
            text="Управление устройствами"))
        page.click_button(locator=page.get_locator_by_name(
            name="Чек-бокс полномочие новой роли",
            text="Приложения"))
        page.click_button(locator=page.get_locator_by_name(
            name="Чек-бокс полномочие новой роли",
            text="Отчёты"))
        page.click_button(locator=page.get_locator_by_name(
            name="Чек-бокс полномочие новой роли",
            text="Календарь рабочего времени"))
        page.click_button(locator=page.get_locator_by_name(
            name="Чек-бокс полномочие новой роли",
            text="Адресная книга"))
        page.click_button(locator=page.get_locator_by_name(
            name="Чек-бокс полномочие новой роли",
            text="Объекты учёта"))
        page.click_button(locator=page.get_locator_by_name(
            name="Чек-бокс полномочие новой роли",
            text="Загрузчик"))
        page.click_button(locator=page.get_locator_by_name(
            name="Чек-бокс полномочие новой роли",
            text="Лицензия"))
        page.click_button(locator=page.get_locator_by_name(
            name="Чек-бокс полномочие новой роли",
            text="Пользовательское соглашение"))
        page.click_button(locator=page.get_locator_by_name(name="Создать новую роль"))

    @allure.title('[UI] Редактирование роли')
    def test_editing_check_roles(self):
        page = shared_vars.set_page(name="Роли")
        page.click_button(locator=page.format_locator(page.UNIVERSAL_DIV_XPATH, div_text=NAME))
        page.click_button(locator=page.get_locator_by_name(name="Изменить"))
        page.fill_field(locator=page.get_locator_by_name(name="Введите имя новой Роли (Редактирование)"),
                        value=ANOTHER_NAME)
        page.click_button(locator=page.get_locator_by_name(name="ОК"))

    @allure.title('[UI] Удаление полномочий для роли')
    def test_remove_authority_check_roles(self):
        page = shared_vars.set_page(name="Роли")
        page.click_button(locator=page.format_locator(page.UNIVERSAL_DIV_XPATH, div_text=ANOTHER_NAME))
        page.click_button(locator=page.get_locator_by_name(name='Чек-бокс полномочие',
                                                           text="Информация об устройствах"))
        page.click_button(locator=page.get_locator_by_name(name='Чек-бокс полномочие',
                                                           text="Управление устройствами"))
        page.click_button(locator=page.get_locator_by_name(name='Чек-бокс полномочие',
                                                           text="Приложения"))
        page.click_button(locator=page.get_locator_by_name(name='Чек-бокс полномочие',
                                                           text="Отчёты"))
        page.click_button(locator=page.get_locator_by_name(name='Чек-бокс полномочие',
                                                           text="Календарь рабочего времени"))
        page.click_button(locator=page.get_locator_by_name(name='Чек-бокс полномочие',
                                                           text="Адресная книга"))
        page.click_button(locator=page.get_locator_by_name(name='Чек-бокс полномочие',
                                                           text="Объекты учёта"))
        page.click_button(locator=page.get_locator_by_name(name='Чек-бокс полномочие',
                                                           text="Загрузчик"))
        page.click_button(locator=page.get_locator_by_name(name='Чек-бокс полномочие',
                                                           text="Лицензия"))
        page.click_button(locator=page.get_locator_by_name(name='Чек-бокс полномочие',
                                                           text="Пользовательское соглашение"))
        page.click_button(locator=page.get_locator_by_name(name="Сохранить полномочия"))

    @allure.title('[UI] Удаление роли')
    def test_delete_check_roles(self):
        page = shared_vars.set_page(name="Роли")
        page.click_button(locator=page.format_locator(page.UNIVERSAL_DIV_XPATH, div_text=ANOTHER_NAME))
        page.click_button(locator=page.get_locator_by_name(name="Удалить"))
        page.click_button(locator=page.get_locator_by_name(name="Да"))
        page = shared_vars.set_page(name="Главная страница")
        page.error_checking(locator=page.get_locator_by_name(name="Внутренняя ошибка"))
