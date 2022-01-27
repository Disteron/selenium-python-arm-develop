from ui.pages.base_page import BasePage


class CalenderPage(BasePage):
    """
    Страница Приложения
    """
    BUTTON_1 = {"name": "root", "xpath": "(//span[text()='root'])[8]"}
    BUTTON_2 = {"name": "Показать правила", "xpath": "//span[text()='Показать правила']"}
    BUTTON_3 = {"name": "Добавить", "xpath": "(//span[text()='Добавить'])[15]"}
    # BUTTON_4 = {"name": "Добавить", "xpath": "(//span[text()='Добавить'])[8]"}
    # BUTTON_5 = {"name": "Добавить", "xpath": "(//span[text()='Добавить'])[8]"}