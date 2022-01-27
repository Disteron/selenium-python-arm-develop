from ui.pages.base_page import BasePage


class ManagementRulesPage(BasePage):
    """
    Страница ПУП (Правила управления(Приложения))
    """

    BUTTON_2 = {"name": "Обновить низ 1",
                "xpath": "//div[contains(@id, 'sp-apprules-grid-')]//a[@data-qtip='Обновить']"}

    BUTTON_3 = {"name": "Отображение",
                "xpath": "//div[contains(@id, 'sp-apprules-grid-')]//input[@value='40']"}

    BUTTON_4 = {"name": "Следующая страница",
                "xpath": "//div[contains(@id, 'sp-apprules-grid-')]//a[@data-qtip='Следующая страница']"}

    BUTTON_5 = {"name": "Последняя страница",
                "xpath": "//div[contains(@id, 'sp-apprules-grid-')]//a[@data-qtip='Последняя страница']"}

    BUTTON_6 = {"name": "Предыдущая страница",
                "xpath": "//div[contains(@id, 'sp-apprules-grid-')]//a[@data-qtip='Предыдущая страница']"}

    BUTTON_7 = {"name": "Первая страница",
                "xpath": "//div[contains(@id, 'sp-apprules-grid-')]//a[@data-qtip='Первая страница']"}

    BUTTON_9 = {"name": "Сортировка(Наименование)",
                "xpath": "//div[contains(@id, 'sp-apprules-grid-')]//span[text()='Наименование']"}

    BUTTON_10 = {"name": "Сортировка(Приложение)",
                 "xpath": "//div[contains(@id, 'sp-apprules-grid-')]//span[text()='Приложение']"}

    BUTTON_11 = {"name": "Сортировка(Версия)",
                 "xpath": "//div[contains(@id, 'sp-apprules-grid-')]//span[text()='Версия']"}

    BUTTON_12 = {"name": "Сортировка(Платформа)",
                 "xpath": "//div[contains(@id, 'sp-apprules-grid-')]//span[text()='Платформа']"}

    BUTTON_14 = {"name": "Сортировка(Монитор)",
                 "xpath": "//div[contains(@id, 'sp-apprules-grid-')]//span[text()='Монитор']"}

    BUTTON_15 = {"name": "Сортировка(Место установки)",
                 "xpath": "//div[contains(@id, 'sp-apprules-grid-')]//span[text()='Место установки']"}

    BUTTON_16 = {"name": "Сортировка(Сущность)",
                 "xpath": "//div[contains(@id, 'sp-apprules-grid-')]//span[text()='Сущность']"}

    BUTTON_13 = {"name": "Добавить",
                 "xpath": "//div[contains(@id, 'sp-apprules-grid-')]//span[text()='Добавить']"}

    BUTTON_18 = {"name": "Название",
                 "xpath": "//div[contains(@id, 'sp-apprules-form-')]//input[@name='title']"}

    BUTTON_54 = {"name": "Платформа",
                 "xpath": "//div[contains(@id, 'sp-apprules-form-')]//input[@name='platformId']"}

    BUTTON_55 = {"name": "Платформа(iPhone OS)",
                 "xpath": "//div[contains(@id, 'boundlist-')]//li[text()='iPhone OS']"}

    BUTTON_56 = {"name": "Платформа(Android)",
                 "xpath": "//div[contains(@id, 'boundlist-')]//li[text()='Android']"}

    BUTTON_57 = {"name": "Платформа(Windows)",
                 "xpath": "//div[contains(@id, 'boundlist-')]//li[text()='Windows']"}

    BUTTON_58 = {"name": "Место установки",
                 "xpath": "//div[contains(@id, 'sp-apprules-form-')]//input[@name='location']"}

    BUTTON_59 = {"name": "Место установки(Устройство)",
                 "xpath": "//div[contains(@id, 'boundlist-')]//li[text()='Устройство']"}

    BUTTON_60 = {"name": "Тип приложения",
                 "xpath": "//div[contains(@id, 'sp-apprules-form-')]//input[@name='app_type']"}

    BUTTON_61 = {"name": "Тип приложения(Корпоративное)",
                 "xpath": "//div[contains(@id, 'boundlist-')]//li[text()='Корпоративное']"}

    BUTTON_62 = {"name": "UID",
                 "xpath": "//div[contains(@id, 'sp-apprules-form-')]//input[@name='app_id']"}

    BUTTON_64 = {"name": "UID(Android)",
                 "xpath": "//div[contains(@id, 'boundlist-')]//td[text()='ru.niisokb.mcc']"}

    BUTTON_65 = {"name": "UID(iPhone OS)",
                 "xpath": "//div[contains(@id, 'boundlist-')]//td[text()='ru.safe-phone.SafeMail']"}

    BUTTON_66 = {"name": "UID(Windows)",
                 "xpath": "//div[contains(@id, 'boundlist-')]//td[text()='Far Manager 2 x64 2.0.1420']"}

    BUTTON_63 = {"name": "Описание",
                 "xpath": "//div[contains(@id, 'sp-apprules-form-')]//textarea[@name='description']"}

    BUTTON_19 = {"name": "Сохранить",
                 "xpath": "(//div[contains(@id, 'sp-apprules-panel-')]//span[text()='Сохранить'])[1]"}

    BUTTON_17 = {"name": "Ок",
                 "xpath": "//div[contains(@id, 'ext-comp')]//span[text()='ОК']/.."}

    BUTTON_20 = {"name": "Условия (не заданы)",
                 "xpath": "//div[contains(@id, 'sp-apprules-panel-')]//span[text()='Условия (не заданы)']"}

    BUTTON_21 = {"name": "Назначения",
                 "xpath": "//div[contains(@id, 'sp-apprules-panel-')]//span[text()='Назначения']"}

    BUTTON_22 = {"name": "Плюс root",
                 "xpath": "//div[contains(@id, 'sp-apprules-assignmententitiestreepanel-')]"
                          "//span[text()='root']//..//img[contains(@class, 'x-tree-expander')]"}

    BUTTON_23 = {"name": "Плюс Отдел тестирования",
                 "xpath": "//div[contains(@id, 'sp-apprules-assignmententitiestreepanel-')]"
                          "//span[text()='Отдел тестирования_{random}']//..//img[contains(@class, 'x-tree-expander')]"}

    BUTTON_24 = {"name": "Плюс Android",
                 "xpath": "//div[contains(@id, 'sp-apprules-assignmententitiestreepanel-')]"
                          "//span[text()='Android_{random}']//..//img[contains(@class, 'x-tree-expander')]"}
    BUTTON_26 = {"name": "Плюс IOS",
                 "xpath": "//div[contains(@id, 'sp-apprules-assignmententitiestreepanel-')]"
                          "//span[text()='IOS_{random}']//..//img[contains(@class, 'x-tree-expander')]"}
    BUTTON_29 = {"name": "ОШС Android",
                 "xpath": "//div[contains(@id, 'sp-apprules-assignmententitiestreepanel-')]"
                          "//span[text()='Android_{random}']//..//input"}
    BUTTON_30 = {"name": "Сотрудник ios 1",
                 "xpath": "//div[contains(@id, 'sp-apprules-assignmententitiestreepanel-')]"
                          "//span[text()='IOS QA1 QA1_{random}']//..//input"}
    BUTTON_31 = {"name": "Сотрудник ios 2",
                 "xpath": "//div[contains(@id, 'sp-apprules-assignmententitiestreepanel-')]"
                          "//span[text()='IOS QA2 QA2_{random}']//..//input"}

    BUTTON_32 = {"name": "Сохранить(Назначения)",
                 "xpath": "//div[contains(@id, 'sp-apprules-panel-')]//div[contains(@id,"
                          " 'sp-apprules-assignmentpanel-')]//span[text()='Сохранить']"}

    BUTTON_33 = {"name": "mcc",
                 "xpath": "//div[contains(@id, 'sp-apprules-mobilegrid-')]//span[text()='mcc']"}

    BUTTON_34 = {"name": "Телефон",
                 "xpath": "//div[contains(@id, 'sp-apprules-mobilegrid-')]//span[text()='Телефон']"}

    BUTTON_35 = {"name": "Сотрудник",
                 "xpath": "//div[contains(@id, 'sp-apprules-mobilegrid-')]//span[text()='Сотрудник']"}

    BUTTON_36 = {"name": "Должность",
                 "xpath": "//div[contains(@id, 'sp-apprules-mobilegrid-')]//span[text()='Должность']"}

    BUTTON_37 = {"name": "Отдел Группа",
                 "xpath": "//div[contains(@id, 'sp-apprules-mobilegrid-')]//span[text()='Отдел/Группа']"}

    BUTTON_38 = {"name": "Статус",
                 "xpath": "//div[contains(@id, 'sp-apprules-mobilegrid-')]//span[text()='Статус']"}

    BUTTON_39 = {"name": "Обновить низ 2",
                 "xpath": "//div[contains(@id, 'sp-apprules-mobilegrid-')]//a[@data-qtip='Обновить']"}

    BUTTON_40 = {"name": "Владелец",
                 "xpath": "//div[contains(@id, 'sp-apprules-panel-')]"
                          "//div[contains(@id, 'tabpanel-')]//span[text()='Владелец']"}

    BUTTON_46 = {"name": "Делегирование",
                 "xpath": "//div[contains(@id, 'sp-apprules-panel-')]"
                          "//div[contains(@id, 'tabpanel-')]//span[text()='Делегирование']"}

    BUTTON_52 = {"name": "Да",
                 "xpath": "//div[contains(@id, 'messagebox-')]//span[text()='Да']/.."}

    BUTTON_53 = {"name": "Удалить",
                 "xpath": "//div[contains(@id, 'sp-apprules-panel-')]//span[text()='Удалить']"}

    BUTTON_67 = {"name": "Поиск",
                 "xpath": "//div[contains(@id, 'sp-apprules-grid-')]//input[contains(@name, 'customtrigger-')]"}

    BUTTON_68 = {"name": "Настройки",
                 "xpath": "//div[contains(@id, 'sp-apprules-panel-')]//span[text()='Настройки']"}

    BUTTON_69 = {"name": "Текст под UID ios",
                 "xpath": """//label[text()='Приложение: "Signal — приватный мессенджер"']"""}

    BUTTON_70 = {"name": "Текст под UID android",
                 "xpath": """//label[text()='Приложение: "Luchshiy"']"""}
