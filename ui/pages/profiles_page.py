from ui.pages.base_page import BasePage


class ProfilesPage(BasePage):
    """
    Вкладка Профили
    """

    BUTTON_1 = {"name": "Обновить верх",
                "xpath": "//div[contains(@id, 'rootPanel')]//span[text()='Обновить']"}

    BUTTON_2 = {"name": "Обновить низ 1",
                "xpath": "//div[contains(@id, 'sp-profilespanel')]//a[@data-qtip='Обновить']"}

    BUTTON_3 = {"name": "Отображение",
                "xpath": "//div[contains(@id, 'sp-profilespanel')]//input[@value='40']"}

    BUTTON_4 = {"name": "Следующая страница", 
                "xpath": "//div[contains(@id, 'sp-profilespanel')]//a[@data-qtip='Следующая страница']"}

    BUTTON_5 = {"name": "Последняя страница", 
                "xpath": "//div[contains(@id, 'sp-profilespanel')]//a[@data-qtip='Последняя страница']"}

    BUTTON_6 = {"name": "Предыдущая страница", 
                "xpath": "//div[contains(@id, 'sp-profilespanel')]//a[@data-qtip='Предыдущая страница']"}

    BUTTON_7 = {"name": "Первая страница", 
                "xpath": "//div[contains(@id, 'sp-profilespanel')]//a[@data-qtip='Первая страница']"}

    BUTTON_9 = {"name": "Наименование сортировка", 
                "xpath": "//div[contains(@id, 'sp-profilespanel')]//span[text()='Наименование']"}

    BUTTON_10 = {"name": "Тип 1",
                 "xpath": "//div[contains(@id, 'sp-profilespanel')]//span[text()='Тип']"}

    BUTTON_11 = {"name": "Платформа 1",
                 "xpath": "//div[contains(@id, 'sp-profilespanel')]//span[text()='Платформа']"}

    BUTTON_12 = {"name": "Сущность",
                 "xpath": "//div[contains(@id, 'sp-profilespanel')]//span[text()='Сущность']"}

    BUTTON_13 = {"name": "Добавить",
                 "xpath": "//div[contains(@id, 'sp-profilespanel')]//span[text()='Добавить']"}

    BUTTON_14 = {"name": "Тип 2",
                 "xpath": "//div[contains(@id, 'sp-profiletypesgrid')]//span[text()='Тип']"}

    BUTTON_15 = {"name": "Платформа 2",
                 "xpath": "//div[contains(@id, 'sp-profiletypesgrid')]//span[text()='Платформа']"}

    BUTTON_16 = {"name": "Настройки монитора Android",
                 "xpath": "//div[contains(@id, 'sp-profiletypesgrid')]//div[text()='Настройки монитора Android']"}

    BUTTON_17 = {"name": "Ок",
                 "xpath": "//div[contains(@id, 'ext-comp')]//span[text()='ОК']/.."}

    BUTTON_18 = {"name": "Наименование поле",
                 "xpath": "//div[contains(@id, 'sp-profilespanel-')]//input[@name='profileName']"}

    BUTTON_19 = {"name": "Сохранить",
                 "xpath": "//div[contains(@id, 'sp-profilespanel-')]//span[text()='Сохранить']"}

    BUTTON_20 = {"name": "Условия (не заданы)",
                 "xpath": "//div[contains(@id, 'sp-profilespanel-')]//span[text()='Условия (не заданы)']"}

    BUTTON_21 = {"name": "Назначения",
                 "xpath": "//div[contains(@id, 'sp-profilespanel-')]//span[text()='Назначения']"}

    BUTTON_22 = {"name": "Плюс root",
                 "xpath": "//div[contains(@id, 'sp-profiles-unitemployeetreepanel-')]"
                          "//span[text()='root']//..//img[contains(@class, 'x-tree-expander')]"}

    BUTTON_23 = {"name": "Плюс Отдел тестирования",
                 "xpath": "//div[contains(@id, 'sp-profiles-unitemployeetreepanel-')]"
                          "//span[text()='Отдел тестирования_{random}']//..//img[contains(@class, 'x-tree-expander')]"}

    BUTTON_24 = {"name": "Плюс Android",
                 "xpath": "//div[contains(@id, 'sp-profiles-unitemployeetreepanel-')]"
                          "//span[text()='Android_{random}']//..//img[contains(@class, 'x-tree-expander')]"}

    BUTTON_25 = {"name": "Плюс IOS",
                 "xpath": "//div[contains(@id, 'sp-profiles-unitemployeetreepanel-')]"
                          "//span[text()='IOS_{random}']//..//img[contains(@class, 'x-tree-expander')]"}

    BUTTON_26 = {"name": "ОШС Android",
                 "xpath": "//div[contains(@id, 'sp-profiles-unitemployeetreepanel-')]"
                          "//span[text()='Android_{random}']//..//input"}

    BUTTON_27 = {"name": "Сотрудник ios 1",
                 "xpath": "//div[contains(@id, 'sp-profiles-unitemployeetreepanel-')]"
                          "//span[text()='IOS QA1 QA1_{random}']//..//input"}

    BUTTON_28 = {"name": "Сотрудник ios 2",
                 "xpath": "//div[contains(@id, 'sp-profiles-unitemployeetreepanel-')]"
                          "//span[text()='IOS QA2 QA2_{random}']//..//input"}

    BUTTON_29 = {"name": "Сохранить назначения",
                 "xpath": "//div[contains(@id, 'sp-profilespanel')]//div[contains(@id,"
                          " 'sp-profiles-assignmentpanel')]//span[text()='Сохранить']"}

    BUTTON_30 = {"name": "mcc",
                 "xpath": "//div[contains(@id, 'sp-profiles-mobilegrid-')]//span[text()='mcc']"}

    BUTTON_31 = {"name": "Телефон",
                 "xpath": "//div[contains(@id, 'sp-profiles-mobilegrid-')]//span[text()='Телефон']"}

    BUTTON_32 = {"name": "Сотрудник",
                 "xpath": "//div[contains(@id, 'sp-profiles-mobilegrid-')]//span[text()='Сотрудник']"}

    BUTTON_33 = {"name": "Должность",
                 "xpath": "//div[contains(@id, 'sp-profiles-mobilegrid-')]//span[text()='Должность']"}

    BUTTON_34 = {"name": "Отдел Группа",
                 "xpath": "//div[contains(@id, 'sp-profiles-mobilegrid-')]//span[text()='Отдел/Группа']"}

    BUTTON_35 = {"name": "Статус",
                 "xpath": "//div[contains(@id, 'sp-profiles-mobilegrid-')]//span[text()='Статус']"}

    BUTTON_36 = {"name": "Обновить низ 2",
                 "xpath": "//div[contains(@id, 'sp-profiles-mobilegrid-')]//a[@data-qtip='Обновить']"}

    BUTTON_37 = {"name": "Владелец",
                 "xpath": "//div[contains(@id, 'sp-profilespanel-')]"
                          "//div[contains(@id, 'tabpanel-')]//span[text()='Владелец']"}

    BUTTON_38 = {"name": "Делегирование",
                 "xpath": "//div[contains(@id, 'sp-profilespanel-')]"
                          "//div[contains(@id, 'tabpanel-')]//span[text()='Делегирование']"}

    BUTTON_39 = {"name": "Да",
                 "xpath": "//div[contains(@id, 'messagebox-')]//span[text()='Да']/.."}

    BUTTON_40 = {"name": "Удалить",
                 "xpath": "//div[contains(@id, 'sp-profilespanel-')]//span[text()='Удалить']"}
