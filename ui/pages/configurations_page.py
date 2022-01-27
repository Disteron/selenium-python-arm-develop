from ui.pages.base_page import BasePage


class ConfigurationsPage(BasePage):
    """
    Страница Конфигурации
    """

    BUTTON_1 = {"name": "Обновить низ 1",
                "xpath": "//div[contains(@id, 'sp-configurationsgrid-')]//a[@data-qtip='Обновить']"}

    BUTTON_2 = {"name": "Добавить(Кнопка вниз)",
                "xpath": "//div[contains(@id, 'sp-configurationsgrid-')]//span[text()='Добавить']/../../.."}

    BUTTON_3 = {"name": "Создать пустую конфигурацию",
                "xpath": "//a[contains(@id, 'menuitem-')]//span[text()='Создать пустую конфигурацию']"}

    BUTTON_4 = {"name": "Создать конфигурацию из шаблона",
                "xpath": "//a[contains(@id, 'menuitem-')]//span[text()='Создать конфигурацию из шаблона']"}

    BUTTON_5 = {"name": "Сортировка(Наименование)",
                "xpath": "//div[contains(@id, 'sp-configurationsgrid-')]//span[text()='Наименование']"}

    BUTTON_6 = {"name": "Сортировка(UID)",
                "xpath": "//div[contains(@id, 'sp-configurationsgrid-')]//span[text()='UID']"}

    BUTTON_7 = {"name": "Сортировка(Место установки)",
                "xpath": "//div[contains(@id, 'sp-configurationsgrid-')]//span[text()='Место установки']"}

    BUTTON_8 = {"name": "Сортировка(Платформа)",
                "xpath": "//div[contains(@id, 'sp-configurationsgrid-')]//span[text()='Платформа']"}

    BUTTON_9 = {"name": "Сортировка(Сущность)",
                "xpath": "//div[contains(@id, 'sp-configurationsgrid-')]//span[text()='Сущность']"}

    BUTTON_10 = {"name": "Создание конфигурации приложения(Сортировка)(UID)",
                 "xpath": "//div[contains(@id, 'sp-configurationtemplatesgrid-')]//span[text()='UID']"}

    BUTTON_11 = {"name": "Создание конфигурации приложения(Сортировка)(Платформа)",
                 "xpath": "//div[contains(@id, 'sp-configurationtemplatesgrid-')]//span[text()='Платформа']"}

    BUTTON_12 = {"name": "Создание конфигурации приложения(com.microsoft.office.outlook)",
                 "xpath": "//div[contains(@id, 'sp-configurationtemplatesgrid-')]"
                          "//div[text()='com.microsoft.office.outlook']"}

    BUTTON_13 = {"name": "Ок",
                 "xpath": "(//div[contains(@id, 'ext-comp-')]//span[text()='ОК']/..)[last()]"}

    BUTTON_14 = {"name": "Название",
                 "xpath": "//div[contains(@id, 'sp-configurations-form-')]//input[@name='title']"}

    BUTTON_15 = {"name": "Сохранить(Настройки)",
                 "xpath": "(//div[contains(@id, 'sp-configurationspanel-')]//span[text()='Сохранить'])[1]"}

    BUTTON_16 = {"name": "Создание конфигурации приложения(com.google.android.gm)",
                 "xpath": "//div[contains(@id, 'sp-configurationtemplatesgrid-')]"
                          "//div[text()='com.google.android.gm']"}

    BUTTON_17 = {"name": "Платформа",
                 "xpath": "//div[contains(@id, 'sp-configurationspanel-')]//input[@name='platformId']"}

    BUTTON_18 = {"name": "Платформа(Android)",
                 "xpath": "//div[contains(@id, 'boundlist-')]//li[text()='Android']"}

    BUTTON_19 = {"name": "Место установки",
                 "xpath": "//div[contains(@id, 'sp-configurationspanel-')]//input[@name='location']"}

    BUTTON_20 = {"name": "Место установки(Устройство)",
                 "xpath": "//div[contains(@id, 'boundlist-')]//li[text()='Устройство']"}

    BUTTON_21 = {"name": "UID",
                 "xpath": "//div[contains(@id, 'sp-configurationspanel-')]//input[@name='uid']"}

    BUTTON_22 = {"name": "Описание",
                 "xpath": "//div[contains(@id, 'sp-configurationspanel-')]//textarea[@name='description']"}

    BUTTON_23 = {"name": "SafePhone SDK",
                 "xpath": "//table[contains(@id, 'togglefield-')]"}

    BUTTON_24 = {"name": "Создание настройки конфигураци(Добавить)",
                 "xpath": "//div[contains(@id, 'tabpanel-')]//span[text()='Добавить']"}

    BUTTON_25 = {"name": "Создание настройки конфигураци(Ключ)",
                 "xpath": "//div[contains(@id, 'ext-comp-')]//input[@name='id']"}

    BUTTON_26 = {"name": "Создание настройки конфигураци(Название)",
                 "xpath": "//div[contains(@id, 'ext-comp-')]//input[@name='label']"}

    BUTTON_27 = {"name": "Создание настройки конфигураци(Описание)",
                 "xpath": "//div[contains(@id, 'ext-comp-')]//textarea[@name='description']"}

    BUTTON_28 = {"name": "Создание настройки конфигураци(Тип значений)(Строка)",
                 "xpath": "//div[contains(@id, 'ext-comp-')]//input[@name='type']"}

    BUTTON_29 = {"name": "Поле key_random",
                 "xpath": "//div[contains(@id, 'sp-configurationspanel-')]//input[@name='Key_{random}']"}

    BUTTON_69 = {"name": "Условия (не заданы)",
                 "xpath": "//div[contains(@id, 'sp-configurationspanel-')]//span[text()='Условия (не заданы)']"}

    BUTTON_70 = {"name": "Назначения",
                 "xpath": "//div[contains(@id, 'sp-configurationspanel-')]//span[text()='Назначения']"}

    BUTTON_71 = {"name": "Плюс root",
                 "xpath": "//div[contains(@id, 'sp-configurations-assignmententitiestreepanel-')]//span[text()='root']"
                          "//..//img[contains(@class, 'x-tree-expander')]"}

    BUTTON_72 = {"name": "Плюс Отдел тестирования",
                 "xpath": "//div[contains(@id, 'sp-configurations-assignmententitiestreepanel-')]"
                          "//span[text()='Отдел тестирования_{random}']//..//img[contains(@class, 'x-tree-expander')]"}

    BUTTON_73 = {"name": "Плюс Android",
                 "xpath": "//div[contains(@id, 'sp-configurations-assignmententitiestreepanel-')]"
                          "//span[text()='Android_{random}']//..//img[contains(@class, 'x-tree-expander')]"}
    BUTTON_74 = {"name": "Плюс IOS",
                 "xpath": "//div[contains(@id, 'sp-configurations-assignmententitiestreepanel-')]"
                          "//span[text()='IOS_{random}']//..//img[contains(@class, 'x-tree-expander')]"}
    BUTTON_75 = {"name": "ОШС Android",
                 "xpath": "//div[contains(@id, 'sp-configurations-assignmententitiestreepanel-')]"
                          "//span[text()='Android_{random}']//..//input"}
    BUTTON_30 = {"name": "Сотрудник ios 1",
                 "xpath": "//div[contains(@id, 'sp-configurations-assignmententitiestreepanel-')]"
                          "//span[text()='IOS QA1 QA1_{random}']//..//input"}
    BUTTON_31 = {"name": "Сотрудник ios 2",
                 "xpath": "//div[contains(@id, 'sp-configurations-assignmententitiestreepanel-')]"
                          "//span[text()='IOS QA2 QA2_{random}']//..//input"}

    BUTTON_32 = {"name": "Сохранить(Назначения)",
                 "xpath": "//div[contains(@id, 'sp-configurationspanel-')]//div[contains(@id,"
                          " 'sp-configurations-assignmentpanel-')]//span[text()='Сохранить']"}

    BUTTON_33 = {"name": "mcc",
                 "xpath": "//div[contains(@id, 'sp-configurations-mobilegrid-')]//span[text()='mcc']"}

    BUTTON_34 = {"name": "Телефон",
                 "xpath": "//div[contains(@id, 'sp-configurations-mobilegrid-')]//span[text()='Телефон']"}

    BUTTON_35 = {"name": "Сотрудник",
                 "xpath": "//div[contains(@id, 'sp-configurations-mobilegrid-')]//span[text()='Сотрудник']"}

    BUTTON_36 = {"name": "Должность",
                 "xpath": "//div[contains(@id, 'sp-configurations-mobilegrid-')]//span[text()='Должность']"}

    BUTTON_37 = {"name": "Отдел Группа",
                 "xpath": "//div[contains(@id, 'sp-configurations-mobilegrid-')]//span[text()='Отдел/Группа']"}

    BUTTON_38 = {"name": "Статус",
                 "xpath": "//div[contains(@id, 'sp-configurations-mobilegrid-')]//span[text()='Статус']"}

    BUTTON_39 = {"name": "Обновить низ 2",
                 "xpath": "//div[contains(@id, 'sp-configurations-mobilegrid-')]//a[@data-qtip='Обновить']"}

    BUTTON_40 = {"name": "Владелец",
                 "xpath": "//div[contains(@id, 'sp-configurationspanel-')]"
                          "//div[contains(@id, 'tabpanel-')]//span[text()='Владелец']"}

    BUTTON_46 = {"name": "Делегирование",
                 "xpath": "//div[contains(@id, 'sp-configurationspanel-')]"
                          "//div[contains(@id, 'tabpanel-')]//span[text()='Делегирование']"}

    BUTTON_54 = {"name": "Отображение",
                 "xpath": "//div[contains(@id, 'sp-configurationsgrid-')]//input[@value='40']"}

    BUTTON_55 = {"name": "Следующая страница",
                 "xpath": "//div[contains(@id, 'sp-configurationsgrid-')]//a[@data-qtip='Следующая страница']"}

    BUTTON_56 = {"name": "Последняя страница",
                 "xpath": "//div[contains(@id, 'sp-configurationsgrid-')]//a[@data-qtip='Последняя страница']"}

    BUTTON_57 = {"name": "Предыдущая страница",
                 "xpath": "//div[contains(@id, 'sp-configurationsgrid-')]//a[@data-qtip='Предыдущая страница']"}

    BUTTON_58 = {"name": "Первая страница",
                 "xpath": "//div[contains(@id, 'sp-configurationsgrid-')]//a[@data-qtip='Первая страница']"}

    BUTTON_52 = {"name": "Да",
                 "xpath": "//div[contains(@id, 'messagebox-')]//span[text()='Да']/.."}

    BUTTON_53 = {"name": "Удалить",
                 "xpath": "//div[contains(@id, 'sp-configurationsgrid-')]//span[text()='Удалить']"}

    BUTTON_60 = {"name": "ru_niisokb_mcc_safemessages",
                 "xpath": "//div[contains(@id, 'boundlist-')]//td[text()='ru.niisokb.mcc.safemessages']"}
