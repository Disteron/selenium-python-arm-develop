from ui.pages.base_page import BasePage


class StaffPage(BasePage):
    """
    Страница Сотрудники
    """
    BUTTON_1 = {"name": "Фамилия", "xpath": "//input[@name='surname']"}
    BUTTON_2 = {"name": "Имя", "xpath": "//input[@name='name']"}
    BUTTON_3 = {"name": "Отчество", "xpath": "//input[@name='patronymic']"}
    BUTTON_4 = {"name": "Должность", "xpath": "//input[@name='job']"}
    BUTTON_5 = {"name": "E-mail Домен", "xpath": "//input[@name='domain']"}
    BUTTON_6 = {"name": "Е-mail Логин", "xpath": "//input[@name='login']"}
    BUTTON_7 = {"name": "E-mail", "xpath": "//input[@name='email']"}
    BUTTON_8 = {"name": "Сохранить", "xpath": "(//span[text()='Сохранить'])[4]"}
    BUTTON_9 = {"name": "root", "xpath": "//div[contains(@id, 'sp-employeeform')]/.//span[text()='root']"}
    BUTTON_10 = {"name": "Удалить", "xpath": "//div[contains(@id, 'sp-employeepanel')]/.//span[text()='Удалить']"}
    BUTTON_11  = {"name": "Да", "xpath": "//span[text()='Да']/../../.."}
    BUTTON_12  = {"name": "Внутренняя ошибка", "xpath": "//span[text()='Внутренняя ошибка']"}
