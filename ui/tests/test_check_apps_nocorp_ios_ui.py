import allure
import pytest
import shared_vars


from selenium.webdriver.common.keys import Keys
from allure_commons.types import Severity
from ui.steps import common_steps


"""
Добавление и удаление некорпоративного приложения для IPhone OS
Шаги:

1.Нажимаем на кнопку "Добавить", выбираем некорпоративное приложение, выбираем платформу IPhone OS, в поле "Приложение"
пишем "Signal" и выбираем его из списка, нажимаем "Сохранить"
2.Нажимаем "Создать правило", проверяем под UID текст, - "Приложение: "Signal - приватный мессенджер"", 
в поле "Описание" добавлям "Текст", нажимаем "Сохранить"
3.Удаляем созданный ПУП и созданное некорпоративное приложение
"""


@pytest.mark.smoke
@pytest.mark.ui
@pytest.mark.regress
@pytest.mark.id_28
@pytest.mark.incremental
@pytest.mark.usefixtures("start_browser")
@allure.title('[UI] Проверка Приложения')
@allure.severity(Severity.CRITICAL)
@allure.feature('[UI] Приложения')
@allure.description('Добавление и удаление некорпоративного приложения для IPhone OS')
class TestAppIOs:

    @allure.title('Нажимаем на кнопку "Добавить", выбираем некорпоративное приложение, выбираем платформу IPhone OS, '
                  'в поле "Приложение" пишем "Signal" и выбираем его из списка, нажимаем "Сохранить"')
    def test_apps_ios_ui_1(self):
        common_steps.auth()
        page = shared_vars.set_page(name="Главная страница")
        page.click_button(locator=page.get_locator_by_name(name="Приложения(Объекты учёта)"))
        page = shared_vars.set_page(name="Приложения")
        page.click_button(locator=page.get_locator_by_name(name="Добавить"))
        page.click_button(locator=page.get_locator_by_name(name="Тип приложения"))
        page.click_button(locator=page.get_locator_by_name(name="Некорпоративное"))
        page.click_button(locator=page.get_locator_by_name(name="Платформа"))
        page.click_button(locator=page.get_locator_by_name(name="Платформа IPhone OS"))
        page.fill_field(locator=page.get_locator_by_name(name="Приложение"), value="Signal", button=Keys.SPACE)
        page.click_button(locator=page.get_locator_by_name(name="Выбор приложения из списка"))
        page.click_button(locator=page.get_locator_by_name(name="Сохранить"))

    @allure.title('Нажимаем "Создать правило", проверяем под UID текст, - "Приложение: "Signal - приватный мессенджер",'
                  ' в поле "Описание" добавлям "Текст", нажимаем "Сохранить"')
    def test_apps_ios_ui_2(self):
        page = shared_vars.set_page(name="Приложения")
        page.click_button(locator=page.get_locator_by_name(name="Создать правило"))
        page = shared_vars.set_page(name="Правила управления(Приложения)")
        page.get_element(locator=page.get_locator_by_name(name="Текст под UID ios"))
        page.fill_field(locator=page.get_locator_by_name(name="Описание"), value="Текст")
        page.click_button(locator=page.get_locator_by_name(name="Сохранить"))

    @allure.title('Удаляем созданный ПУП и созданное некорпоративное приложение')
    def test_apps_ios_ui_3(self):
        page = shared_vars.set_page(name="Правила управления(Приложения)")
        page.click_button(locator=page.get_locator_by_name(name="Удалить"))
        page.click_button(locator=page.get_locator_by_name(name="Да"))
        page = shared_vars.set_page(name="Главная страница")
        page.click_button(locator=page.get_locator_by_name(name="Приложения(Объекты учёта)"))
        page = shared_vars.set_page(name="Приложения")
        page.click_button(locator=page.format_locator(page.UNIVERSAL_DIV_XPATH,
                                                      div_text="Signal — приватный мессенджер"))
        page.click_button(locator=page.get_locator_by_name(name="Удалить"))
        page.click_button(locator=page.get_locator_by_name(name="Да"))
        page = shared_vars.set_page(name="Главная страница")
        page.error_checking(locator=page.get_locator_by_name(name="Внутренняя ошибка"))
