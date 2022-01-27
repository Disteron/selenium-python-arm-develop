from ui.pages.base_page import BasePage


class RolesPage(BasePage):
    """
    Страница Роли
    """
    BUTTON_1 = {"name": "Добавить",
                "xpath": "//div[contains(@id, 'sp-rolespanel-')]//span[text()='Добавить']"}

    BUTTON_2 = {"name": "Введите имя новой Роли (Добавление)",
                "xpath": "//label[text()='Введите имя новой Роли']/..//input"}

    BUTTON_3 = {"name": "ОК",
                "xpath": "//div[contains(@id, 'messagebox-')]//span[text()='ОК']/.."}

    BUTTON_4 = {"name": "Да",
                "xpath": "//div[contains(@id, 'messagebox-')]//span[text()='Да']/.."}

    BUTTON_5 = {"name": "Раскратие/Закрытие полномочие новой роли",
                "xpath": "//div[contains(@id, 'window-')]//span[text()='{text}']"
                        "/../img[contains(@class, ' x-tree-elbow-img')]"}

    BUTTON_6 = {"name": "Чек-бокс полномочие новой роли",
                "xpath": "//div[contains(@id, 'window-')]//span[text()='{text}']"
                        "/../input[@role='checkbox']"}

    BUTTON_7 = {"name": "Чек-бокс полномочие",
                "xpath": "//div[contains(@id, 'sp-rolespanel-')]"
                         "//span[text()='{text}']/../input[@role='checkbox']"}

    BUTTON_8 = {"name": "Раскратие/Закрытие полномочий",
                "xpath": "//div[contains(@id, 'sp-rolespanel-')]"
                         "//span[text()='{text}']/../img[contains(@class, ' x-tree-elbow-img')]"}

    BUTTON_9 = \
        {"name": "Введите имя новой Роли (Редактирование)",
         "xpath": "//div[text()='Введите новое имя Роли']/ancestor::table/following-sibling::table//input"
         }

    BUTTON_10 = {"name": "Удалить",
                 "xpath": "//div[contains(@id, 'sp-rolespanel-')]//span[text()='Удалить']"}

    BUTTON_11 = {"name": "Создать новую роль",
                 "xpath": "//div[contains(@id, 'window-')]//span[text()='Создать']/.."}

    BUTTON_27 = {"name": "Сохранить полномочия",
                 "xpath": "//div[contains(@id, 'sp-rolespanel-')]//span[text()='Сохранить полномочия']"}

    BUTTON_28 = {"name": "Изменить", "xpath": "//div[contains(@id, 'sp-rolespanel-')]//span[text()='Изменить']"}
