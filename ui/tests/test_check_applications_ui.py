import os
import random
import allure
import pytest
import shared_vars


from shared_vars import PAGE as page
from allure_commons.types import Severity
from ui.steps import common_steps


APPLICATION_NAME = 'Monitor' + str(random.randint(100, 10000))


@pytest.mark.smoke
@pytest.mark.ui
@pytest.mark.regress
@pytest.mark.id_11
@pytest.mark.incremental
@pytest.mark.usefixtures("start_browser")
@allure.title('[UI] Проверка Приложения')
@allure.severity(Severity.CRITICAL)
@allure.feature('[UI] Application')
@allure.description('[UI] Проверка создания, удаления Приложения')
class TestApplication:

    @allure.title('[UI] Добавление приложения')
    def test_save_application_ui(self):
        common_steps.auth()
        common_steps.menu_item(item_name="Приложения(Объекты учёта)")
        page.click_button(locator=page.get_locator_by_name(name="Добавить"))
        page.click_button(locator=page.get_locator_by_name(name="Тип приложения"))
        page.click_button(locator=page.get_locator_by_name(name="Корпоротивное"))
        path = os.path.dirname(__file__)
        final_path = os.path.join(path, 'files\Monitor-4.5.0.19_ui.apk')
        page.upload_file(locator=page.get_locator_by_name(name="Загрузить файл"), file_absolute_path=final_path)
        page.fill_field(locator=page.get_locator_by_name(name="Приложение"), value=APPLICATION_NAME)
        page.click_button(locator=page.get_locator_by_name(name="Сохранить"))

    @allure.title('[UI] Удаление приложения')
    def test_delete_application_ui(self):
        shared_vars.set_page(name="Главная страница")
        page.click_button(locator=page.get_locator_by_name(name="Приложения"))
        shared_vars.set_page(name="Приложения")
        page.click_button(locator=page.format_locator(page.UNIVERSAL_DIV_XPATH,
                                                      div_text=APPLICATION_NAME))
        page.click_button(locator=page.get_locator_by_name(name="Удалить"))
        page.click_button(locator=page.get_locator_by_name(name="Да"))
