import allure

import shared_vars

"""
Общие шаги, которые часто используются в тестах
"""


def auth():
    """Авторизация на сайте
    """
    with allure.step("Авторизация на странице"):
        url = "https://" + shared_vars.APPLICATION_PROPERTIES.get("url") + ":8443/"
        login = shared_vars.APPLICATION_PROPERTIES.get("login")
        password = shared_vars.APPLICATION_PROPERTIES.get("password")
        page = shared_vars.set_page(name="Форма авторизации")
        page.go_to_url(url=url)
        page.fill_field(locator=page.get_locator_by_name(name="Имя пользователя"), value=login)
        page.fill_field(locator=page.get_locator_by_name(name="Пароль"), value=password)
        page.click_button(locator=page.get_locator_by_name(name="Войти"))


def menu_item(item_name):
    """Переход в раздел меню по имени
    """
    page = shared_vars.set_page(name="Главная страница")
    page.click_button(locator=page.get_locator_by_name(name=item_name))
    shared_vars.set_page(name=item_name)

