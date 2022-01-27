import allure
import pytest
import shared_vars


from allure_commons.types import Severity
from ui.steps import common_steps


LICENSE = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiLQntCe0J4g0J3QmNCYINCh0J7QmtCRIiwiYXVkIjoi0J7QntCeINCd0J" \
          "jQmCDQodCe0JrQkSIsImp0aSI6ImI1MTBkOGQ0LTJkNjEtNDc1MS04MzYyLTAyZjZiNmJlNGExMCIsImlzcyI6Ik9PTyDCq9Cd0JjQm" \
          "CDQodCe0JrQkcK7IiwiaWF0IjoxNjQwNjkxMzUyLCJuYmYiOjE2NDA5ODQ0MDAsImV4cCI6MTY3MjUyMDM5OSwibWNjLWxpbWl0Ijox" \
          "MDAwfQ.Z_AAUH5sJwF7jyoWXof9PPdsvrUDeJrYRTNelLiDTqBOYG-b2j5tnTAYHuqPzgWFXDPYGN2hmfsHuTaLjtS03NfSgflHboSn" \
          "rVXD59RMDfu2L4pVih7ltSUUSvJtUYXHkZXqKm58EGM3YM7EjeFUfYiKIvgBBcLyExro5VaeyLqXicpsMxNf3AJYFn5srnn4Put_UeO" \
          "l-6fGBoZnDH4mP4XKPGfSWeUuCPiKDWV44RLMcaoPouhkThcPNv7sfh2HVJ1PUndSr87sf1xsisbyKM4V7M-AAAHdhIH4LVGu40tMcx" \
          "nNPzdbzOwlBKT3of0u0p6jM_4MTzRd5j-YJ6yeqA"

LICENSE_TEST = 'test'


@pytest.mark.ui
@pytest.mark.smoke
@pytest.mark.regress
@pytest.mark.id_16
@pytest.mark.incremental
@pytest.mark.usefixtures("start_browser")
@allure.title('Проверка лицензии')
@allure.severity(Severity.MINOR)
@allure.feature('[UI] License')
class TestCheckLicense:

    @allure.title('[UI] Добавление лицензии')
    def test_check_license(self):
        common_steps.auth()
        page = shared_vars.set_page(name="Главная страница")
        page.click_button(locator=page.get_locator_by_name(name="Лицензия"))
        page = shared_vars.set_page(name="Лицензия")
        page.fill_field(locator=page.get_locator_by_name(name="Поле ввода лицензии"), value=LICENSE)
        page.click_button(locator=page.get_locator_by_name(name="Сохранить"))
        page.get_element(locator=page.get_locator_by_name(name="Срок действия лицензии"))

    @allure.title('[UI] Проверка нарушения целостности лицензии')
    def test_integrity_is_broken_license(self):
        page = shared_vars.set_page(name="Лицензия")
        page.fill_field(locator=page.get_locator_by_name(name="Поле ввода лицензии"), value=LICENSE_TEST)
        page.click_button(locator=page.get_locator_by_name(name="Сохранить"))
        page.click_button(locator=page.get_locator_by_name(name="Целостность лицензии"))
        page = shared_vars.set_page(name="Главная страница")
        page.error_checking(locator=page.get_locator_by_name(name="Внутренняя ошибка"))
