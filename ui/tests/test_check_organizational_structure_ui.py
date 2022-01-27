import random
import allure
import pytest
import shared_vars


from allure_commons.types import Severity
from ui.steps import common_steps


COMPANY_1 = 'Company_1_' + str(random.randint(100, 1000000))
COMPANY_2 = 'Company_2_' + str(random.randint(100, 1000000))
COMPANY_3 = 'Company_3_' + str(random.randint(100, 1000000))
COMPANY_4 = 'Company_4_' + str(random.randint(100, 1000000))
COMPANY_5 = 'Company_5_' + str(random.randint(100, 1000000))
COMPANY_6 = 'Company_6_' + str(random.randint(100, 1000000))
COMPANY_7 = 'Company_7_' + str(random.randint(100, 1000000))
COMPANY_8 = 'Company_8_' + str(random.randint(100, 1000000))
COMPANY_9 = 'Company_9_' + str(random.randint(100, 1000000))
COMPANY_10 = 'Company_10_' + str(random.randint(100, 1000000))


@pytest.mark.ui
@pytest.mark.smoke
@pytest.mark.regress
@pytest.mark.id_17
@pytest.mark.incremental
@pytest.mark.usefixtures("start_browser")
@allure.title('[UI] Проверка ОСШ')
@allure.severity(Severity.MINOR)
@allure.feature('[UI] Organizational Structure')
@allure.description('[UI] Проверка создания, редактирования, удаления ОШС (Организационно-штатная структура)')
class TestOrganizationalStructure:

    if shared_vars.APPLICATION_PROPERTIES["stand_version"] == "4.5":
        @allure.title('[UI] Добавление ОШС')
        def test_add_organizational_structure(self):
            common_steps.auth()
            page = shared_vars.set_page(name="Главная страница")
            page.click_button(locator=page.get_locator_by_name(name="ОШС"))
            page = shared_vars.set_page(name="ОСШ")
            page.click_button(locator=page.get_locator_by_name(name="root"))
            page.click_button(locator=page.get_locator_by_name(name="Добавить"))
            page.fill_field(locator=page.get_locator_by_name(name="Введите имя нового объекта ОШС (Добавление)"),
                            value=COMPANY_1)
            page.click_button(locator=page.get_locator_by_name(name="ОК"))

        @allure.title('[UI] Изменить ОШС')
        def test_editing_organizational_structure(self):
            page = shared_vars.set_page(name="ОСШ")
            page.click_button(locator=page.get_locator_by_name(name="Изменить"))
            page.fill_field(locator=page.get_locator_by_name(name="Введите новое имя объекта ОШС (Редактирование)"),
                            value=COMPANY_2)
            page.click_button(locator=page.get_locator_by_name(name="ОК"))

        @allure.title('[UI] Удаление ОШС')
        def test_delete_organizational_structure(self):
            page = shared_vars.set_page(name="ОСШ")
            page.click_button(locator=page.get_locator_by_name(name="Удалить"))
            page.click_button(locator=page.get_locator_by_name(name="Да"))
            page.wait_invisibility_of_element(locator=page.format_locator(page.UNIVERSAL_ELEMENT_WITH_TEXT, text=COMPANY_2))

    if shared_vars.APPLICATION_PROPERTIES["stand_version"] == "5.0":
        @allure.title('[UI] Добавление ОШС Автоматический выбор управления')
        def test_add_organizational_structure_1(self):
            common_steps.auth()
            page = shared_vars.set_page(name="Главная страница")
            page.click_button(locator=page.get_locator_by_name(name="ОШС"))
            page = shared_vars.set_page(name="ОСШ")
            page.click_button(locator=page.get_locator_by_name(name="root"))
            page.click_button(locator=page.get_locator_by_name(name="Добавить"))
            page.fill_field(locator=page.get_locator_by_name(name="Введите имя нового объекта ОШС 5.0"),
                            value=COMPANY_1)
            page.click_button(locator=page.get_locator_by_name(name="Стратегия"))
            page.click_button(locator=page.get_locator_by_name(name="Автоматический выбор управления"))
            page.click_button(locator=page.get_locator_by_name(name="ОК"))

        @allure.title('[UI] Добавление ОШС Только устройство (Android 5.0+)')
        def test_add_organizational_structure_2(self):
            page = shared_vars.set_page(name="ОСШ")
            page.click_button(locator=page.get_locator_by_name(name="root"))
            page.click_button(locator=page.get_locator_by_name(name="Добавить"))
            page.fill_field(locator=page.get_locator_by_name(name="Введите имя нового объекта ОШС 5.0"),
                            value=COMPANY_2)
            page.click_button(locator=page.get_locator_by_name(name="Стратегия"))
            page.click_button(locator=page.get_locator_by_name(name="Только устройство (Android 5.0+)"))
            page.click_button(locator=page.get_locator_by_name(name="ОК"))

        @allure.title('[UI] Добавление ОШС Устройство и контейнер KNOX (Samsung 4.4 - 9)')
        def test_add_organizational_structure_3(self):
            page = shared_vars.set_page(name="ОСШ")
            page.click_button(locator=page.get_locator_by_name(name="root"))
            page.click_button(locator=page.get_locator_by_name(name="Добавить"))
            page.fill_field(locator=page.get_locator_by_name(name="Введите имя нового объекта ОШС 5.0"),
                            value=COMPANY_3)
            page.click_button(locator=page.get_locator_by_name(name="Стратегия"))
            page.click_button(locator=page.get_locator_by_name(name="Устройство и контейнер KNOX (Samsung 4.4 - 9)"))
            page.click_button(locator=page.get_locator_by_name(name="ОК"))

        @allure.title('[UI] Добавление ОШС Устройство и контейнер KNOX (Samsung 4.4 - 9)')
        def test_add_organizational_structure_4(self):
            page = shared_vars.set_page(name="ОСШ")
            page.click_button(locator=page.get_locator_by_name(name="root"))
            page.click_button(locator=page.get_locator_by_name(name="Добавить"))
            page.fill_field(locator=page.get_locator_by_name(name="Введите имя нового объекта ОШС 5.0"),
                            value=COMPANY_4)
            page.click_button(locator=page.get_locator_by_name(name="Стратегия"))
            page.click_button(locator=page.get_locator_by_name(name="Корпоративный рабочий профиль (Samsung 5.1+)"))
            page.click_button(locator=page.get_locator_by_name(name="ОК"))

        @allure.title('[UI] Добавление ОШС Устройство и контейнер KNOX (Samsung 4.4 - 9)')
        def test_add_organizational_structure_5(self):
            page = shared_vars.set_page(name="ОСШ")
            page.click_button(locator=page.get_locator_by_name(name="root"))
            page.click_button(locator=page.get_locator_by_name(name="Добавить"))
            page.fill_field(locator=page.get_locator_by_name(name="Введите имя нового объекта ОШС 5.0"),
                            value=COMPANY_5)
            page.click_button(locator=page.get_locator_by_name(name="Стратегия"))
            page.click_button(locator=page.get_locator_by_name(name="Персональный рабочий профиль (Samsung 5.1+)"))
            page.click_button(locator=page.get_locator_by_name(name="ОК"))

        @allure.title('[UI] Изменить ОШС Автоматический выбор управления')
        def test_editing_organizational_structure_1(self):
            page = shared_vars.set_page(name="ОСШ")
            page.click_button(locator=page.format_locator(page.UNIVERSAL_SPAN_XPATH, span_text=COMPANY_1))
            page.click_button(locator=page.get_locator_by_name(name="Изменить"))
            page.fill_field(locator=page.get_locator_by_name(name="Введите новое имя объекта ОШС 5.0"),
                            value=COMPANY_6)
            page.click_button(locator=page.get_locator_by_name(name="Стратегия"))
            page.click_button(locator=page.get_locator_by_name(name="Только устройство (Android 5.0+)"))
            page.click_button(locator=page.get_locator_by_name(name="ОК"))

        @allure.title('[UI] Изменить ОШС Только устройство (Android 5.0+)')
        def test_editing_organizational_structure_2(self):
            page = shared_vars.set_page(name="ОСШ")
            page.click_button(locator=page.format_locator(page.UNIVERSAL_SPAN_XPATH, span_text=COMPANY_2))
            page.click_button(locator=page.get_locator_by_name(name="Изменить"))
            page.fill_field(locator=page.get_locator_by_name(name="Введите новое имя объекта ОШС 5.0"),
                            value=COMPANY_7)
            page.click_button(locator=page.get_locator_by_name(name="Стратегия"))
            page.click_button(locator=page.get_locator_by_name(name="Устройство и контейнер KNOX (Samsung 4.4 - 9)"))
            page.click_button(locator=page.get_locator_by_name(name="ОК"))

        @allure.title('[UI] Изменить ОШС Устройство и контейнер KNOX (Samsung 4.4 - 9)')
        def test_editing_organizational_structure_3(self):
            page = shared_vars.set_page(name="ОСШ")
            page.click_button(locator=page.format_locator(page.UNIVERSAL_SPAN_XPATH, span_text=COMPANY_3))
            page.click_button(locator=page.get_locator_by_name(name="Изменить"))
            page.fill_field(locator=page.get_locator_by_name(name="Введите новое имя объекта ОШС 5.0"),
                            value=COMPANY_8)
            page.click_button(locator=page.get_locator_by_name(name="Стратегия"))
            page.click_button(locator=page.get_locator_by_name(name="Корпоративный рабочий профиль (Samsung 5.1+)"))
            page.click_button(locator=page.get_locator_by_name(name="ОК"))

        @allure.title('[UI] Изменить ОШС Корпоративный рабочий профиль (Samsung 5.1+)')
        def test_editing_organizational_structure_4(self):
            page = shared_vars.set_page(name="ОСШ")
            page.click_button(locator=page.format_locator(page.UNIVERSAL_SPAN_XPATH, span_text=COMPANY_4))
            page.click_button(locator=page.get_locator_by_name(name="Изменить"))
            page.fill_field(locator=page.get_locator_by_name(name="Введите новое имя объекта ОШС 5.0"),
                            value=COMPANY_9)
            page.click_button(locator=page.get_locator_by_name(name="Стратегия"))
            page.click_button(locator=page.get_locator_by_name(name="Персональный рабочий профиль (Samsung 5.1+)"))
            page.click_button(locator=page.get_locator_by_name(name="ОК"))

        @allure.title('[UI] Изменить ОШС Персональный рабочий профиль (Samsung 5.1+)')
        def test_editing_organizational_structure_5(self):
            page = shared_vars.set_page(name="ОСШ")
            page.click_button(locator=page.format_locator(page.UNIVERSAL_SPAN_XPATH, span_text=COMPANY_5))
            page.click_button(locator=page.get_locator_by_name(name="Изменить"))
            page.fill_field(locator=page.get_locator_by_name(name="Введите новое имя объекта ОШС 5.0"),
                            value=COMPANY_10)
            page.click_button(locator=page.get_locator_by_name(name="Стратегия"))
            page.click_button(locator=page.get_locator_by_name(name="Автоматический выбор управления"))
            page.click_button(locator=page.get_locator_by_name(name="ОК"))

        @allure.title(f'[UI] Удаление ОШС {COMPANY_6}')
        def test_delete_organizational_structure_1(self):
            page = shared_vars.set_page(name="ОСШ")
            page.click_button(locator=page.format_locator(page.UNIVERSAL_SPAN_XPATH, span_text=COMPANY_6))
            page.click_button(locator=page.get_locator_by_name(name="Удалить"))
            page.click_button(locator=page.get_locator_by_name(name="Да"))
            page.wait_invisibility_of_element(
                locator=page.format_locator(page.UNIVERSAL_ELEMENT_WITH_TEXT, text=COMPANY_6))

        @allure.title(f'[UI] Удаление ОШС {COMPANY_7}')
        def test_delete_organizational_structure_2(self):
            page = shared_vars.set_page(name="ОСШ")
            page.click_button(locator=page.format_locator(page.UNIVERSAL_SPAN_XPATH, span_text=COMPANY_7))
            page.click_button(locator=page.get_locator_by_name(name="Удалить"))
            page.click_button(locator=page.get_locator_by_name(name="Да"))
            page.wait_invisibility_of_element(
                locator=page.format_locator(page.UNIVERSAL_ELEMENT_WITH_TEXT, text=COMPANY_7))

        @allure.title(f'[UI] Удаление ОШС {COMPANY_8}')
        def test_delete_organizational_structure_3(self):
            page = shared_vars.set_page(name="ОСШ")
            page.click_button(locator=page.format_locator(page.UNIVERSAL_SPAN_XPATH, span_text=COMPANY_8))
            page.click_button(locator=page.get_locator_by_name(name="Удалить"))
            page.click_button(locator=page.get_locator_by_name(name="Да"))
            page.wait_invisibility_of_element(
                locator=page.format_locator(page.UNIVERSAL_ELEMENT_WITH_TEXT, text=COMPANY_8))

        @allure.title(f'[UI] Удаление ОШС {COMPANY_9}')
        def test_delete_organizational_structure_4(self):
            page = shared_vars.set_page(name="ОСШ")
            page.click_button(locator=page.format_locator(page.UNIVERSAL_SPAN_XPATH, span_text=COMPANY_9))
            page.click_button(locator=page.get_locator_by_name(name="Удалить"))
            page.click_button(locator=page.get_locator_by_name(name="Да"))
            page.wait_invisibility_of_element(
                locator=page.format_locator(page.UNIVERSAL_ELEMENT_WITH_TEXT, text=COMPANY_9))

        @allure.title(f'[UI] Удаление ОШС {COMPANY_10}')
        def test_delete_organizational_structure_5(self):
            page = shared_vars.set_page(name="ОСШ")
            page.click_button(locator=page.format_locator(page.UNIVERSAL_SPAN_XPATH, span_text=COMPANY_10))
            page.click_button(locator=page.get_locator_by_name(name="Удалить"))
            page.click_button(locator=page.get_locator_by_name(name="Да"))
            page.wait_invisibility_of_element(
                locator=page.format_locator(page.UNIVERSAL_ELEMENT_WITH_TEXT, text=COMPANY_10))
            page = shared_vars.set_page(name="Главная страница")
            page.click_button(locator=page.get_locator_by_name(name="Обновить"))
            page.error_checking(locator=page.get_locator_by_name(name="Внутренняя ошибка"))
