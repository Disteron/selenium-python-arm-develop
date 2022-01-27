from ui.pages.base_page import BasePage


class MainPage(BasePage):
    """
    Главная страница
    """

    BUTTON_1 = {"name": "Информация об устройствах",
                "xpath": "//div[contains(@id, 'sp-mainmenu-')]//span[text()='Информация об устройствах']"}

    BUTTON_2 = {"name": "Данные об устройстве",
                "xpath": "//div[contains(@id, 'sp-mainmenu-')]//span[text()='Данные об устройстве']"}

    BUTTON_3 = {"name": "Сообщения",
                "xpath": "//div[contains(@id, 'sp-mainmenu-')]//span[text()='Сообщения']"}

    BUTTON_4 = {"name": "Звонки",
                "xpath": "//div[contains(@id, 'sp-mainmenu-')]//span[text()='Звонки']"}

    BUTTON_5 = {"name": "Местоположения",
                "xpath": "//div[contains(@id, 'sp-mainmenu-')]//span[text()='Местоположения']"}

    BUTTON_6 = {"name": "Действия",
                "xpath": "//div[contains(@id, 'sp-mainmenu-')]//span[text()='Действия']"}

    BUTTON_7 = {"name": "События",
                "xpath": "//div[contains(@id, 'sp-mainmenu-')]//span[text()='События']"}

    # Управление устройствами
    BUTTON_8 = {"name": "Управление устройствами",
                "xpath": "//div[contains(@id, 'sp-mainmenu-')]//span[text()='Управление устройствами']"}

    BUTTON_9 = {"name": "Команды",
                "xpath": "//div[contains(@id, 'sp-mainmenu-')]//span[text()='Команды']"}

    BUTTON_10 = {"name": "Профили(Управление устройствами)",
                 "xpath": "//div[contains(@id, 'sp-mainmenu-')]//span[text()='Установленные приложения']"
                          "/../../../preceding-sibling::tr//span[text()='Профили']"}

    # Приложения
    BUTTON_11 = {"name": "Приложения(Приложения)",
                 "xpath": "//div[contains(@id, 'sp-mainmenu-')]//span[text()='Установленные приложения']"
                          "/../../../preceding-sibling::tr//span[text()='Приложения']"}

    BUTTON_12 = {"name": "Установленные приложения",
                 "xpath": "//div[contains(@id, 'sp-mainmenu-')]//span[text()='Установленные приложения']"}

    BUTTON_13 = {"name": "Правила управления(Приложения)",
                 "xpath": "//div[contains(@id, 'sp-mainmenu-')]//span[text()='Конфигурации']"
                          "/../../../preceding-sibling::tr//span[text()='Правила управления']"}

    BUTTON_14 = {"name": "Конфигурации",
                 "xpath": "//div[contains(@id, 'sp-mainmenu-')]//span[text()='Конфигурации']"}

    # Отчёты
    BUTTON_15 = {"name": "Отчёты",
                 "xpath": "//div[contains(@id, 'sp-mainmenu-')]//span[text()='Отчёты']"}

    BUTTON_16 = {"name": "Аудит",
                 "xpath": "//div[contains(@id, 'sp-mainmenu-')]//span[text()='Аудит']"}

    BUTTON_17 = {"name": "Звонки и SMS",
                 "xpath": "//div[contains(@id, 'sp-mainmenu-')]//span[text()='Звонки и SMS']"}

    BUTTON_18 = {"name": "События ИБ",
                 "xpath": "//div[contains(@id, 'sp-mainmenu-')]//span[text()='События ИБ']"}

    BUTTON_47 = {"name": "Перемещения",
                 "xpath": "//div[contains(@id, 'sp-mainmenu-')]//span[text()='Перемещения']"}

    BUTTON_20 = {"name": "Профили(Отчеты)",
                 "xpath": "//div[contains(@id, 'sp-mainmenu-')]//span[text()='Отчёты']"
                          "/../../../following-sibling::tr//span[text()='Профили']"}

    BUTTON_21 = {"name": "Правила управления(Отчеты)",
                 "xpath": "//div[contains(@id, 'sp-mainmenu-')]//span[text()='Отчёты']"
                          "/../../../following-sibling::tr//span[text()='Правила управления']"}

    BUTTON_22 = {"name": "Геозоны(Отчёты)",
                 "xpath": "//div[contains(@id, 'sp-mainmenu-')]//span[text()='Объекты учёта']"
                          "/../../../preceding-sibling::tr//span[text()='Геозоны']"}

    BUTTON_23 = {"name": "SafeLife",
                 "xpath": "//div[contains(@id, 'sp-mainmenu-')]//span[text()='SafeLife']"}

    # Объекты учёта
    BUTTON_24 = {"name": "Объекты учёта",
                 "xpath": "//div[contains(@id, 'sp-mainmenu-')]//span[text()='Объекты учёта']"}

    BUTTON_25 = {"name": "ОШС",
                 "xpath": "//div[contains(@id, 'sp-mainmenu-')]//span[text()='ОШС']"}

    BUTTON_26 = {"name": "Сотрудники",
                 "xpath": "//div[contains(@id, 'sp-mainmenu-')]//span[text()='Сотрудники']"}

    BUTTON_27 = {"name": "Роли",
                 "xpath": "//div[contains(@id, 'sp-mainmenu-')]//span[text()='Роли']"}

    BUTTON_28 = {"name": "Администраторы",
                 "xpath": "//div[contains(@id, 'sp-mainmenu-')]//span[text()='Администраторы']"}

    BUTTON_29 = {"name": "Парольные политики АРМ",
                 "xpath": "//div[contains(@id, 'sp-mainmenu-')]//span[text()='Парольные политики АРМ']"}

    BUTTON_30 = {"name": "Операционные системы",
                 "xpath": "//div[contains(@id, 'sp-mainmenu-')]//span[text()='Операционные системы']"}

    BUTTON_31 = {"name": "Приложения(Объекты учёта)",
                 "xpath": "//div[contains(@id, 'sp-mainmenu-')]//span[text()='Объекты учёта']"
                          "/../../../following-sibling::tr//span[text()='Приложения']"}

    BUTTON_32 = {"name": "SIM-карты",
                 "xpath": "//div[contains(@id, 'sp-mainmenu-')]//span[text()='SIM-карты']"}

    BUTTON_33 = {"name": "Комплекты",
                 "xpath": "//div[contains(@id, 'sp-mainmenu-')]//span[text()='Комплекты']"}

    BUTTON_34 = {"name": "Геозоны(Объекты учёта)",
                 "xpath": "//div[contains(@id, 'sp-mainmenu-')]//span[text()='Объекты учёта']"
                          "/../../../following-sibling::tr//span[text()='Геозоны']"}

    BUTTON_35 = {"name": "Серверные сертификаты",
                 "xpath": "//div[contains(@id, 'sp-mainmenu-')]//span[text()='Серверные сертификаты']"}

    BUTTON_36 = {"name": "Подключения к серверам",
                 "xpath": "//div[contains(@id, 'sp-mainmenu-')]//span[text()='Подключения к серверам']"}

    BUTTON_37 = {"name": "Настройки SCEP",
                 "xpath": "//div[contains(@id, 'sp-mainmenu-')]//span[text()='Настройки SCEP']"}

    BUTTON_38 = {"name": "Клиентские сертификаты",
                 "xpath": "//div[contains(@id, 'sp-mainmenu-')]//span[text()='Клиентские сертификаты']"}

    # Дополнительно
    BUTTON_39 = {"name": "Загрузчик",
                 "xpath": "//div[contains(@id, 'sp-mainmenu-')]//span[text()='Загрузчик']"}

    BUTTON_40 = {"name": "Календарь",
                 "xpath": "//div[contains(@id, 'sp-mainmenu-')]//span[text()='Календарь']"}

    BUTTON_41 = {"name": "Адресная книга",
                 "xpath": "//div[contains(@id, 'sp-mainmenu-')]//span[text()='Адресная книга']"}

    BUTTON_42 = {"name": "Лицензия",
                 "xpath": "//div[contains(@id, 'sp-mainmenu-')]//span[text()='Лицензия']"}

    BUTTON_43 = {"name": "Пользовательское соглашение",
                 "xpath": "//div[contains(@id, 'sp-mainmenu-')]//span[text()='Пользовательское соглашение']"}

    # Сообщение
    BUTTON_44 = {"name": "Внутренняя ошибка",
                 "xpath": "//div[contains(@id, 'messagebox-')]//span[text()='Сообщение']"}

    # Верхняя панель
    BUTTON_45 = {"name": "Администратор root",
                 "xpath": "//div[contains(@id, 'toolbar-')]//span[text()='root']"}

    BUTTON_46 = {"name": "Выход",
                 "xpath": "//div[contains(@id, 'menu-')]//span[text()='Выход']"}

    BUTTON_48 = {"name": "Обновить",
                 "xpath": "//div[contains(@id, 'rootPanel')]//span[text()='Обновить']"}
