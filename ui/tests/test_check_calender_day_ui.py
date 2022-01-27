import random
import allure
import pytest
import shared_vars


from allure_commons.types import Severity
from ui.steps import common_steps


NAME = 'NAME_' + str(random.randint(10000, 1000000))
SURNAME = 'SURNAME_' + str(random.randint(10000, 1000000))
PATRONYMIC = 'PATRONYMIC_' + str(random.randint(10000, 1000000))


@pytest.mark.ui
@pytest.mark.smoke
@pytest.mark.regress
@pytest.mark.id_14
@pytest.mark.incremental
@pytest.mark.usefixtures("start_browser")
@allure.title('[UI] Проверка календаря')
@allure.severity(Severity.MINOR)
@allure.feature('[UI] Calendar')
@allure.description('[UI] Проверка создания calendar')
class TestCalendarDay:

    @allure.title('[UI] Добавление календаря на день')
    def test_add_calendar_day(self):
        common_steps.auth()
        page = shared_vars.set_page(name="Главная страница")
        page.click_button(locator=page.get_locator_by_name(name="Календарь"))
        page = shared_vars.set_page(name="Календарь")
        page.click_button(locator=page.get_locator_by_name(name="root"))
        page.click_button(locator=page.get_locator_by_name(name="Показать правила"))
        page.click_button(locator=page.get_locator_by_name(name="Добавить"))
        # page.click_button(locator=page.format_locator(page.UNIVERSAL_DIV_XPATH,
        #                                               div_text=SURNAME + " " + NAME + " " + PATRONYMIC))
