import allure
import pytest
import shared_vars


from allure_commons.types import Severity
from ui.steps import common_steps


"""
Добавление и удаление некорпоративного приложения для Android
Шаги:

1.Нажимаем на кнопку "Добавить", выбираем некорпоративное приложение, выбираем платформу Android, в поле "Приложение"
пишем "Luchshiy", в UID пишем com.luchshiy.ru, пишем "Текст" в поле Описание ---> нажимаем "Сохранить"
2.Нажимаем "Создать правило", проверяем под UID текст, - "Приложение: "Luchshiy"", 
в поле "Описание" добавлям "Текст", нажимаем "Сохранить"
3.Удаляем созданный ПУП и созданное некорпоративное приложение
"""


@pytest.mark.smoke
@pytest.mark.ui
@pytest.mark.regress
@pytest.mark.id_29
@pytest.mark.incremental
@pytest.mark.usefixtures("start_browser")
@allure.title('[UI] Проверка Приложения')
@allure.severity(Severity.CRITICAL)
@allure.feature('[UI] Приложения')
@allure.description('Добавление и удаление некорпоративного приложения для Android')
class TestAppAndroid:

    @allure.title('Нажимаем на кнопку "Добавить", выбираем некорпоративное приложение, '
                  'выбираем платформу Android, в поле "Приложение" пишем "Luchshiy", '
                  'в UID пишем com.luchshiy.ru, пишем "Текст" в поле Описание ---> нажимаем "Сохранить"')
    def test_apps_android_ui_1(self):
        common_steps.auth()
        page = shared_vars.set_page(name="Главная страница")
        page.click_button(locator=page.get_locator_by_name(name="Приложения(Объекты учёта)"))
        page = shared_vars.set_page(name="Приложения")
        page.click_button(locator=page.get_locator_by_name(name="Добавить"))
        page.click_button(locator=page.get_locator_by_name(name="Тип приложения"))
        page.click_button(locator=page.get_locator_by_name(name="Некорпоративное"))
        page.click_button(locator=page.get_locator_by_name(name="Платформа"))
        page.click_button(locator=page.get_locator_by_name(name="Платформа Android"))
        page.fill_field(locator=page.get_locator_by_name(name="Приложение"), value="Luchshiy")
        page.fill_field(locator=page.get_locator_by_name(name="UID"), value="com.luchshiy.ru")
        page.fill_field(locator=page.get_locator_by_name(name="Описание"), value="Текст")
        page.click_button(locator=page.get_locator_by_name(name="Сохранить"))

    @allure.title('Нажимаем "Создать правило", проверяем под UID текст, - "Приложение: "Luchshiy"", '
                  'в поле "Описание" добавлям "Текст", нажимаем "Сохранить"')
    def test_apps_android_ui_2(self):
        page = shared_vars.set_page(name="Приложения")
        page.click_button(locator=page.get_locator_by_name(name="Создать правило"))
        page = shared_vars.set_page(name="Правила управления(Приложения)")
        page.get_element(locator=page.get_locator_by_name(name="Текст под UID android"))
        page.fill_field(locator=page.get_locator_by_name(name="Описание"), value="Текст")
        page.click_button(locator=page.get_locator_by_name(name="Сохранить"))

    @allure.title('Удаляем созданный ПУП и созданное некорпоративное приложение')
    def test_apps_android_ui_3(self):
        page = shared_vars.set_page(name="Правила управления(Приложения)")
        page.click_button(locator=page.get_locator_by_name(name="Удалить"))
        page.click_button(locator=page.get_locator_by_name(name="Да"))
        page = shared_vars.set_page(name="Главная страница")
        page.click_button(locator=page.get_locator_by_name(name="Приложения(Объекты учёта)"))
        page = shared_vars.set_page(name="Приложения")
        page.click_button(locator=page.format_locator(page.UNIVERSAL_DIV_XPATH,
                                                      div_text="Luchshiy"))
        page.click_button(locator=page.get_locator_by_name(name="Удалить"))
        page.click_button(locator=page.get_locator_by_name(name="Да"))
        page = shared_vars.set_page(name="Главная страница")
        page.error_checking(locator=page.get_locator_by_name(name="Внутренняя ошибка"))
