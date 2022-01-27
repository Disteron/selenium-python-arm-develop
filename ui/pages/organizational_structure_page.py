from ui.pages.base_page import BasePage


class OrganizationalStructurePage(BasePage):
    """
    Страница ОШС (Организационно-штатная структура)
    """
    BUTTON_1 = {"name": "root",
                "xpath": "//div[contains(@id, 'sp-unitpanel')]//span[text()='root']"}

    BUTTON_2 = {"name": "Добавить",
                "xpath": "//div[contains(@id, 'sp-unitpanel')]//span[text()='Добавить']"}

    BUTTON_3 = {"name": "Изменить",
                "xpath": "//div[contains(@id, 'sp-unitpanel')]//span[text()='Изменить']"}

    BUTTON_4 = {"name": "Удалить",
                "xpath": "//div[contains(@id, 'sp-unitpanel')]//span[text()='Удалить']"}

    BUTTON_5 = \
        {"name": "Введите имя нового объекта ОШС (Добавление)",
         "xpath": "//div[text()='Введите имя нового объекта ОШС']/ancestor::table/following-sibling::table//input"
         }

    BUTTON_11 = \
        {"name": "Введите имя нового объекта ОШС 5.0",
         "xpath": "(//label[text()='Введите имя нового объекта ОШС']"
                  "/following-sibling::table//input[contains(@id, 'textfield-')])[last()]"
         }

    BUTTON_17 = \
        {"name": "Введите новое имя объекта ОШС 5.0",
         "xpath": "(//label[text()='Введите новое имя объекта ОШС']"
                  "/following-sibling::table//input[contains(@id, 'textfield-')])[last()]"
         }

    BUTTON_10 = \
        {"name": "Стратегия",
         "xpath": "//label[text()='Стратегия']/following-sibling::table//input[contains(@id, 'combobox-')]"
         }

    BUTTON_6 = \
        {"name": "Введите новое имя объекта ОШС (Редактирование)",
         "xpath": "//div[text()='Введите новое имя объекта ОШС']/ancestor::table/following-sibling::table//input"
         }

    BUTTON_7 = {"name": "ОК",
                "xpath": "//div[contains(@id, 'window-')]//span[text()='ОК']/.."}

    BUTTON_8 = {"name": "Да",
                "xpath": "//div[contains(@id, 'messagebox-')]//span[text()='Да']/.."}

    BUTTON_9 = {"name": "Плюс",
                "xpath": "(//div[contains(@id, 'sp-unitpanel')]"
                         "//img[@class=' x-tree-elbow-img x-tree-elbow-end-plus x-tree-expander'])[last()]"}

    BUTTON_12 = {"name": "Автоматический выбор управления",
                 "xpath": "//div[contains(@id, 'boundlist-')]//li[text()='Автоматический выбор управления']"}

    BUTTON_13 = {"name": "Только устройство (Android 5.0+)",
                 "xpath": "//div[contains(@id, 'boundlist-')]//li[text()='Только устройство (Android 5.0+)']"}

    BUTTON_14 = {"name": "Устройство и контейнер KNOX (Samsung 4.4 - 9)",
                 "xpath": "//div[contains(@id, 'boundlist-')]"
                          "//li[text()='Устройство и контейнер KNOX (Samsung 4.4 - 9)']"}

    BUTTON_15 = {"name": "Корпоративный рабочий профиль (Samsung 5.1+)",
                 "xpath": "//div[contains(@id, 'boundlist-')]"
                          "//li[text()='Корпоративный рабочий профиль (Samsung 5.1+)']"}

    BUTTON_16 = {"name": "Персональный рабочий профиль (Samsung 5.1+)",
                 "xpath": "//div[contains(@id, 'boundlist-')]"
                          "//li[text()='Персональный рабочий профиль (Samsung 5.1+)']"}
