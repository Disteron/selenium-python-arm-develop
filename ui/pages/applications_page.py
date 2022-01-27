from ui.pages.base_page import BasePage


class ApplicationsPage(BasePage):
    """
    Страница Приложения
    """
    BUTTON_1 = {"name": "Добавить",
                "xpath": "//div[contains(@id, 'sp-appgrid')]//span[text()='Добавить']"}

    BUTTON_2 = {"name": "Тип приложения",
                "xpath": "//input[@name='sourceType']"}

    BUTTON_3 = {"name": "Корпоротивное",
                "xpath": "//li[text()='Корпоративное']"}

    BUTTON_4 = {"name": "Некорпоративное",
                "xpath": "//li[text()='Некорпоративное']"}

    BUTTON_5 = {"name": "Загрузить файл",
                "xpath": "//input[@name='application']"}

    BUTTON_6 = {"name": "Сохранить",
                "xpath": "//div[contains(@id, 'sp-appform')]//span[text()='Сохранить']"}

    BUTTON_7 = {"name": "Приложение",
                "xpath": "//div[contains(@id, 'sp-appform')]//input[@name='name']"}

    BUTTON_8 = {"name": "UID",
                "xpath": "//div[contains(@id, 'sp-appform')]//input[@name='uid']"}

    BUTTON_9 = {"name": "Описание",
                "xpath": "//div[contains(@id, 'sp-appform')]//textarea[@name='description']"}

    BUTTON_10 = {"name": "Удалить",
                 "xpath": "//div[contains(@id, 'sp-appgrid')]//span[text()='Удалить']"}

    BUTTON_11 = {"name": "Да",
                 "xpath": "//div[contains(@id, 'messagebox-')]//span[text()='Да']/.."}

    BUTTON_12 = {"name": "Платформа",
                 "xpath": "//div[contains(@id, 'sp-appform-')]//input[@name='platformId']"}

    BUTTON_13 = {"name": "Платформа IPhone OS",
                 "xpath": "//li[text()='iPhone OS']"}

    BUTTON_14 = {"name": "Платформа Android",
                 "xpath": "//li[text()='Android']"}

    BUTTON_15 = {"name": "Создать правило",
                 "xpath": "//span[text()='Создать правило']"}

    BUTTON_16 = {"name": "Выбор приложения из списка",
                 "xpath": "//td[text()='Signal — приватный мессенджер']"}
