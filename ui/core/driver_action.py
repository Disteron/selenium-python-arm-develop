import time
import allure
import shared_vars

from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from ui.core.decorators import retry
from ui.exception.TestFailException import TestFailException


class DriverAction:

    def __init__(self):
        self.driver = shared_vars.DRIVER

    def _silent_scroll_to(self, element, x=None, y=None):
        """Перемещение к элементу
        В случае ошибки она игнорируется

        :param element: элемент на странице
        :param x: координат x на элементе
        :param y: координат y на элементе
        :return: возвращает этот же элемент
        """
        try:
            action_chains = ActionChains(self.driver)
            if x and y:
                action_chains.move_to_element_with_offset(element.wrapped_element, x, y).click().perform()
            else:
                action_chains.move_to_element(element.wrapped_element).perform()
        except Exception:
            pass
        return element

    @retry
    def click_button(self, locator):
        """Клик по элементу на странице

        :param locator: элемент на странице в виде имени(name) и расположения(xpath)
        """
        with allure.step(f'нажать на элемент "{locator["name"]}:{locator["xpath"]}"'):
            self._silent_scroll_to(element=self.driver.find_element_by_xpath(xpath=locator["xpath"])).click()

    @retry
    def click_button_with_offset(self, locator, x, y):
        """Клик по элементу на странице

        :param locator: элемент на странице в виде имени(name) и расположения(xpath)
        :param x: координат x на элементе
        :param y: координат y на элементе
        """
        with allure.step(f'нажать на элемент "{locator["name"]}:{locator["xpath"]}",'
                         f' координат X: "{x}", координат Y: "{y}"'):
            self._silent_scroll_to(element=self.driver.find_element_by_xpath(xpath=locator["xpath"]),
                                   x=x, y=y)

    @retry
    def fill_field(self, locator, value, button=None):
        """Заполнение значения в поле

        :param locator: элемент на странице в виде имени(name) и расположения(xpath)
        :param value: значение
        """
        with allure.step(f'ввести значение "{value}" в поле "{locator["name"]}:{locator["xpath"]}"'):
            field = self.driver.find_element_by_xpath(locator["xpath"])
            field.clear()
            field.send_keys(value)
            field.send_keys(Keys.TAB)
            if button:
                field.send_keys(button)

    @retry
    def fill_field_enter(self, locator, value):
        """Заполнение значения в поле

        :param locator: элемент на странице в виде имени(name) и расположения(xpath)
        :param value: значение
        """
        with allure.step(f'ввести значение "{value}" в поле "{locator["name"]}:{locator["xpath"]}"'):
            field = self.driver.find_element_by_xpath(locator["xpath"])
            field.clear()
            field.send_keys(value)
            field.send_keys(Keys.TAB)
            field.send_keys(Keys.ENTER)

    @retry
    def get_element(self, locator):
        """Найти и вернуть элемент

        :param locator: элемент на странице в виде имени(name) и расположения(xpath)
        :return: элемент
        """
        with allure.step(f'получить элемент "{locator["name"]}:{locator["xpath"]}"'):
            return self._silent_scroll_to(self.driver.find_element_by_xpath(locator["xpath"]))

    @retry
    def go_to_url(self, url):
        """Перейти на страницу по адресу
        
        :param url: адрес
        """
        with allure.step(f'перейти на страницу "{url}"'):
            self.driver.get(url)

    @retry
    def switch_window(self, i=1):
        """Переход на вкладку по номеру

        :param i: номер новой вкладки
        """
        with allure.step(f'перейти на вкладку под номером {i}'):
            self.driver.wrapped_driver.switch_to.window(self.driver.wrapped_driver.window_handles[i])

    @retry
    def switch_frame(self, locator):
        with allure.step(f'перейти на фрейм "{locator["name"]}: {locator["xpath"]}"'):
            it = expected_conditions.frame_to_be_available_and_switch_to_it(locator['xpath'])
            it(self.driver)

    @retry
    def switch_to_default_content(self):
        with allure.step('перейти на контент по умолчанию'):
            self.driver.wrapped_driver.switch_to_default_content()

    def wait_visibility_of_any_elements(self, locator):
        with allure.step(f'ждать видимости любого из элементов {locator["name"]}:{locator["xpath"]}'):
            located = expected_conditions.visibility_of_any_elements_located((By.XPATH, locator['xpath']))
            located(self.driver)

    @retry
    def wait_invisibility_of_element(self, locator):
        with allure.step(f'ждать невидимости элемента {locator["name"]}:{locator["xpath"]}'):
            located = expected_conditions.invisibility_of_element_located((By.XPATH, locator['xpath']))
            located(self.driver)

    @retry
    def wait_dom_not_changed(self):
        """Ожидание загрузки DOM модели, и проверка, что количество элементов не меняется на отрезке времени.
        """
        with allure.step('Загрузка страницы'):
            all_elements1 = self.driver.find_elements_by_xpath(xpath='//*')
            all_elements2 = self.driver.find_elements_by_xpath(xpath='//*')
            difference = len(all_elements1) - len(all_elements2)
            print(f"Изменение страницы - {difference}")
            if difference != 0:
                raise RuntimeError

    @retry
    def upload_file(self, locator, file_absolute_path):
        """
        В локатор нужно подавать ссылку на input с типом file
        path собирается так:
        path = os.getcwd()
        final_path = os.path.join(os.getcwd(), 'путь к файлу в проекте')
        """
        with allure.step(f'Прикрепление файла {locator["name"]}:{file_absolute_path}'):
            return self.driver.find_element_by_xpath(locator['xpath']).send_keys(file_absolute_path)

    @retry
    def error_checking(self, locator):
        """
        Проверка на "Внутреннюю Ошибку" в конце теста
        :param locator: элемент на странице в виде имени(name) и расположения(xpath)
        """
        with allure.step(f'Проверка ошибки {locator["name"]}'):
            end = time.time() + 3
            while end > time.time():
                elements = self.driver.find_elements_by_xpath(locator['xpath'])
                if len(elements) != 0:
                    raise TestFailException(msg='Внутренняя ошибка')

    @retry
    def element_error_checking(self, locator):
        """
        Выбрасывает ошибку если элемент находится на странице
        :param locator: элемент на странице в виде имени(name) и расположения(xpath)
        """
        with allure.step(f'Проверка элемента {locator["name"]} на странице'):
            elements = self.driver.find_elements_by_xpath(locator['xpath'])
            if len(elements) != 0:
                raise TestFailException(msg=f'Элемент {locator["name"]} присутствует на странице')
