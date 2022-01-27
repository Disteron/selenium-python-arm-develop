import random
import allure
import pytest
import shared_vars


from allure_commons.types import Severity
from ui.steps import common_steps


VERSION = str(random.randint(100, 10000000))


@pytest.mark.ui
@pytest.mark.smoke
@pytest.mark.regress
@pytest.mark.id_23
@pytest.mark.incremental
@pytest.mark.usefixtures("start_browser")
@allure.title('[UI] Проверка операционной системы SafeLife')
@allure.severity(Severity.MINOR)
@allure.feature('[UI] OperationSystemSafeLife')
@allure.description('[UI] Проверка создания, удаления операционной системы SL')
class TestOperationSystemsSafeLife:

    @allure.title('[UI] Добавление SafeLife')
    def test_add_safe_life(self):
        common_steps.auth()
        page = shared_vars.set_page(name="Главная страница")
        page.click_button(locator=page.get_locator_by_name(name="Операционные системы"))
        page = shared_vars.set_page(name="Операционные системы")
        page.click_button(locator=page.get_locator_by_name(name="Добавить"))
        page.click_button(locator=page.get_locator_by_name(name="Платформа"))
        page.click_button(locator=page.get_locator_by_name(name="Платформа SafeLife"))
        page.fill_field(locator=page.get_locator_by_name(name='Версия'), value=VERSION)
        page.click_button(locator=page.get_locator_by_name(name="Сохранить"))

    @allure.title('[UI] Удаление SafeLife')
    def test_delete_safe_life(self):
        page = shared_vars.set_page(name="Операционные системы")
        page.fill_field_enter(locator=page.get_locator_by_name(name="Отображение"), value="999")
        page.click_button(locator=page.format_locator(page.UNIVERSAL_DIV_XPATH,
                                                      div_text='SafeLife ' + VERSION))
        page.click_button(locator=page.get_locator_by_name(name="Удалить"))
        page.click_button(locator=page.get_locator_by_name(name="Да"))
