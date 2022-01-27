from ui.pages.base_page import BasePage


class OperationSystem(BasePage):
    """
    Страница ОШС (Организационно-штатная структура)
    """
    BUTTON_1 = {"name": "Добавить", "xpath": "//div[contains(@id, 'sp-osgrid-')]//span[text()='Добавить']"}
    BUTTON_2 = {"name": "Платформа", "xpath": "//input[@name='platform']"}
    BUTTON_3 = {"name": "Платформа Android",
                "xpath": "//li[@class='x-boundlist-item x-boundlist-selected x-boundlist-item-over' "
                         "and text()='Android']"}
    BUTTON_4 = {"name": "Платформа iPhone OS", "xpath": "//li[@class='x-boundlist-item' and text()='iPhone OS']"}
    BUTTON_5 = {"name": "Платформа Windows", "xpath": "//li[@class='x-boundlist-item' and text()='Windows']"}
    BUTTON_6 = {"name": "Платформа SafeLife", "xpath": "//li[@class='x-boundlist-item' and text()='SafeLife']"}
    BUTTON_7 = {"name": "Платформа AuroraOS", "xpath": "//li[@class='x-boundlist-item' and text()='AuroraOS']"}
    BUTTON_8 = {"name": "Версия", "xpath": "//input[@name='version']"}
    BUTTON_9 = {"name": "Сохранить", "xpath": "//div[contains(@id, 'sp-osform-')]//span[text()='Сохранить']"}
    BUTTON_12 = {"name": "Удалить", "xpath": "//div[contains(@id, 'sp-osgrid-')]//span[text()='Удалить']"}
    BUTTON_13 = {"name": "Да", "xpath": "//span[text()='Да']/../../.."}
    BUTTON_14 = {"name": "Отображение", "xpath": "//div[contains(@id, 'sp-osgrid-')]//input[@value='40']"}
