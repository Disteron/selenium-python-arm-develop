from ui.pages.base_page import BasePage


class AdministratorPage(BasePage):
    """
    Страница Администраторы
    """
    BUTTON_1 = {"name": "Добавить", "xpath": "//div[contains(@id, 'sp-adminsgrid')]//span[text()='Добавить']"}
    BUTTON_2 = {"name": "Удалить", "xpath": "//div[contains(@id, 'sp-adminsgrid')]//span[text()='Удалить']"}
    BUTTON_3 = {"name": "Заблокировать", "xpath": "//div[contains(@id, 'sp-adminsgrid')]//span[text()='Заблокировать']"}
    BUTTON_4 = {"name": "Разблокировать", "xpath": "//div[contains(@id, 'sp-adminsgrid')]"
                                                   "//span[text()='Разблокировать']"}
    BUTTON_5 = {"name": "Администратор", "xpath": "//div[contains(@id, 'sp-adminsform')]//span[text()='Администратор']"}
    BUTTON_6 = {"name": "Область управления", "xpath": "//div[contains(@id, 'sp-adminsform')]"
                                                       "//span[text()=' Область управления']"}
    BUTTON_7 = {"name": "Фамилия", "xpath": "//input[@name='adm_surname']"}
    BUTTON_8 = {"name": "Имя", "xpath": "//input[@name='adm_name']"}
    BUTTON_9 = {"name": "Отчество", "xpath": "//input[@name='adm_patronymic']"}
    BUTTON_10 = {"name": "Имя администратора", "xpath": "//input[@name='id']"}
    BUTTON_11 = {"name": "Электронная почта", "xpath": "//input[@name='adm_email']"}
    BUTTON_12 = {"name": "Должность", "xpath": "//input[@name='adm_position']"}
    BUTTON_13 = {"name": "Срок действия учётной записи", "xpath": "//input[@name='account_expiration_date']"}
    BUTTON_14 = {"name": "Пароль", "xpath": "//div[contains(@id, 'sp-adminsform')]//input[@name='password']"}
    BUTTON_16 = {"name": "Администратор ИТ", "xpath": "//td[@role='gridcell']//div[text()='Администратор ИТ']"}
    BUTTON_17 = {"name": "Администратор ИБ", "xpath": "//td[@role='gridcell']//div[text()='Администратор ИБ']"}
    BUTTON_18 = {"name": "Место работы root", "xpath": "//td[contains(@id, 'sp-admin-unittreefield')]//span[text()='root']"}
    BUTTON_20 = {"name": "Область управления root", "xpath": "//img[@class=' x-tree-icon x-tree-icon- "
                                                             "icon-org-management-area-parent']"}
    BUTTON_21 = {"name": "Да", "xpath": "//span[text()='Да']/../../.."}
    BUTTON_22 = {"name": "Сохранить", "xpath": "//div[contains(@id, 'sp-adminsform')]//span[text()='Сохранить']"}
    BUTTON_15 = {"name": "Изменить пароль", "xpath": "//span[text()='Изменить пароль']"}
    BUTTON_23 = {"name": "root", "xpath": "//div[contains(@id, 'toolbar')]//span[text()='root']"}
    BUTTON_24 = {"name": "Выход", "xpath": "//div[contains(@id, 'menuitem')]//span[text()='Выход']"}
    BUTTON_25 = {"name": "Администратор заблокирован", "xpath": "//div[text()='Администратор заблокирован']"}
    BUTTON_26 = {"name": "Роль SafeLife", "xpath": "//div[contains(@id, 'sp-adminsform-')]//div[text()='SafeLife_{random}']"}
    BUTTON_27 = {"name": "Место работы SafeLife", "xpath": "//td[contains(@id, 'sp-admin-unittreefield')]//span[text()='SafeLife_{random}']"}
    BUTTON_28 = {"name": "Раскрыть root в области управления", "xpath": "//table[contains(@id, 'sp-sdmins-managementareatreepanel-')]//span[text()='root']/../img[contains(@class, 'x-tree-elbow-img')]"}
    BUTTON_29 = {"name": "Чек - бокс область управления SafeLife", "xpath": "//table[contains(@id, 'sp-sdmins-managementareatreepanel-')]//span[text()='SafeLife_{random}']/../img[contains(@class, 'x-tree-icon')]"}
    BUTTON_30 = {"name": "Раскрыть место работы root", "xpath": "//div[contains(@id, 'sp-admin-tree-')]//span[text()='root']/../img[contains(@class, 'x-tree-elbow-img')]"}

