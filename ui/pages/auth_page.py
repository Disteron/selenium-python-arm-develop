from ui.pages.base_page import BasePage


class AuthPage(BasePage):
    """
    Страница Авторизации
    """
    LOGIN = {'name': 'Имя пользователя', 'xpath': "//input[@id='username']"}
    PASSWORD = {'name': 'Пароль', 'xpath': "//input[@id='password']"}
    ENTER = {'name': 'Войти', 'xpath': "//input[@value='Войти']"}
    OLD_PASSWORD = {'name': 'Старый пароль', 'xpath': "//input[@placeholder='Старый пароль']"}
    NEW_PASSWORD = {'name': 'Новый пароль', 'xpath': "//input[@placeholder='Новый пароль']"}
    REPEAT_THE_INPUT = {'name': 'Повторите ввод', 'xpath': "//input[@placeholder='Повторите ввод']"}
    CHANGE = {'name': 'Сменить', 'xpath': "//input[@value='Сменить']"}
    RUSSIAN_LANG = {"name": "ru", "xpath": "//button[text()='Русский']"}
    ENGLISH_LANG = {"name": "en", "xpath": "//button[text()='English']"}
