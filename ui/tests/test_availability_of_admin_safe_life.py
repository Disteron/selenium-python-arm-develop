import random
import time
import allure
import pytest
import shared_vars


from allure_commons.types import Severity
from requests_api.core.request import Request
from ui.steps import common_steps


"""
Предуслове:
1. Создать ОШС SafeLife


Шаги:
1. Перейти на вкладку "Роли", нажимаем "Добавить", в поле вводим название роли, нажимаем "Ок"
2. Выбираем созданную роль и выбираем полномочия для SafeLife(
-Информация об устройствах(Данные об устройстве, Местоположения, События)
-Отчёты(Аудит, Перемещения, Геозоны, SafeLife)
-Объекты учёта(ОШС, Сотрудники, Комплекты, Геозоны)
) и нажимаем кнопку "Сохранить полномочия"
3. Преходим на вкладку "Администраторы", нажимаем кнопку "Добавить", заполняем поля и выбираем ранее созданную роль, 
выбираем область управления и нажимаем кнопку "Сохранить"
4. Залогинится под администратором SafeLife
5. Проверить наполнение АРМ согласно набору ролей
6. Перейти в раздел Отчёты - SafeLife

"""

time_now = str(int(time.time()) * 1000 + 999)
RANDOM = str(random.randint(1, 10000000))
shared_vars.COMMON_VAR["RANDOM"] = RANDOM


@pytest.mark.regress
@pytest.mark.ui
@pytest.mark.id_10
@pytest.mark.incremental
@pytest.mark.usefixtures("start_browser")
@allure.title('[UI] Проверка админа SafeLife')
@allure.severity(Severity.CRITICAL)
@allure.feature('[UI] Админ SafeLife')
@allure.description('[UI] Проверка админа SafeLife')
class TestAdminSafeLife:

    @allure.title('Предусловие')
    @pytest.mark.usefixtures("start_function")
    def test_precondition(self):
        api_user = shared_vars.APPLICATION_PROPERTIES["api_user"]
        api_password = shared_vars.APPLICATION_PROPERTIES["api_password"]

        Request(method='post',
                endpoint='/login',
                template='auth',
                name='Авторизация',
                api_user=api_user,
                api_password=api_password) \
            .fire()

        Request(method='post',
                endpoint='/api/v1/license',
                template='license',
                name='Добавление Лицензии') \
            .fire()

        Request(method='post',
                endpoint='/api/v1/unit?_dc=' + time_now + '&lazy=false&employee=false',
                template='organizational_structure',
                name='Добавление SafeLife на ветку root',
                company_name='SafeLife_' + RANDOM,
                structure_number=-1) \
            .fire()

    @allure.title('Перейти на вкладку "Роли", нажимаем "Добавить", в поле вводим название роли, '
                  'выбираем полномочия для SafeLife(Информация об устройствах '
                  '(Данные об устройстве, Местоположения, События) -Отчёты(Аудит, Перемещения, Геозоны, SafeLife) '
                  '- Объекты учёта(ОШС, Сотрудники, Комплекты, Геозоны) и нажимаем кнопку "Сохранить полномочия"')
    def test_safelife_1(self):
        common_steps.auth()
        page = shared_vars.set_page(name="Главная страница")
        page.click_button(locator=page.get_locator_by_name(name="Роли"))
        page = shared_vars.set_page(name="Роли")
        page.click_button(locator=page.get_locator_by_name(name="Добавить"))
        page.fill_field(locator=page.get_locator_by_name(name="Введите имя новой Роли (Добавление)"),
                        value='SafeLife_' + RANDOM)
        page.click_button(locator=page.get_locator_by_name(
            name="Раскратие/Закрытие полномочие новой роли",
            text='Информация об устройствах'))
        page.click_button(locator=page.get_locator_by_name(
            name="Чек-бокс полномочие новой роли",
            text='Данные об устройстве'))
        page.click_button(locator=page.get_locator_by_name(
            name="Чек-бокс полномочие новой роли",
            text='Местоположения'))
        page.click_button(locator=page.get_locator_by_name(
            name="Чек-бокс полномочие новой роли",
            text='События'))
        page.click_button(locator=page.get_locator_by_name(
            name="Раскратие/Закрытие полномочие новой роли",
            text='Информация об устройствах'))
        page.click_button(locator=page.get_locator_by_name(
            name="Раскратие/Закрытие полномочие новой роли",
            text='Отчёты'))
        page.click_button(locator=page.get_locator_by_name(
            name="Чек-бокс полномочие новой роли",
            text='Аудит'))
        page.click_button(locator=page.get_locator_by_name(
            name="Чек-бокс полномочие новой роли",
            text='Перемещения'))
        page.click_button(locator=page.get_locator_by_name(
            name="Чек-бокс полномочие новой роли",
            text='Геозоны'))
        page.click_button(locator=page.get_locator_by_name(
            name="Чек-бокс полномочие новой роли",
            text='SafeLife'))
        page.click_button(locator=page.get_locator_by_name(
            name="Раскратие/Закрытие полномочие новой роли",
            text='Отчёты'))
        page.click_button(locator=page.get_locator_by_name(
            name="Раскратие/Закрытие полномочие новой роли",
            text='Объекты учёта'))
        page.click_button(locator=page.get_locator_by_name(
            name="Чек-бокс полномочие новой роли",
            text='ОШС'))
        page.click_button(locator=page.get_locator_by_name(
            name="Чек-бокс полномочие новой роли",
            text='Сотрудники'))
        page.click_button(locator=page.get_locator_by_name(
            name="Чек-бокс полномочие новой роли",
            text='Комплекты'))
        page.click_button(locator=page.get_locator_by_name(
            name="Чек-бокс полномочие новой роли",
            text='Геозоны'))
        page.click_button(locator=page.get_locator_by_name(
            name="Раскратие/Закрытие полномочие новой роли",
            text='Объекты учёта'))
        page.click_button(locator=page.get_locator_by_name(name="Создать новую роль"))

    @allure.title('Преходим на вкладку "Администраторы", '
                  'нажимаем кнопку "Добавить", заполняем поля и выбираем ранее созданную роль, '
                  'выбираем область управления и нажимаем кнопку "Сохранить"')
    def test_safelife_3(self):
        page = shared_vars.set_page(name="Главная страница")
        page.click_button(locator=page.get_locator_by_name(name="Администраторы"))
        page = shared_vars.set_page(name="Администраторы")
        page.click_button(locator=page.get_locator_by_name(name="Добавить"))
        page.fill_field(locator=page.get_locator_by_name(name="Фамилия"), value="SafeLife")
        page.fill_field(locator=page.get_locator_by_name(name="Имя"), value="SafeLife")
        page.fill_field(locator=page.get_locator_by_name(name="Отчество"), value="SafeLife")
        page.fill_field(locator=page.get_locator_by_name(name="Имя администратора"), value="SafeLife_" + RANDOM)
        page.fill_field(locator=page.get_locator_by_name(name="Должность"), value="SafeLife")
        page.fill_field(locator=page.get_locator_by_name(name="Пароль"), value="P@ssw0rd")
        page.click_button(locator=page.get_locator_by_name(name="Роль SafeLife", random=RANDOM))
        page.click_button(locator=page.get_locator_by_name(name="Раскрыть место работы root"))
        page.click_button(locator=page.get_locator_by_name(name="Место работы SafeLife", random=RANDOM))
        page.click_button(locator=page.get_locator_by_name(name="Область управления"))
        page.click_button(locator=page.get_locator_by_name(name="Раскрыть root в области управления"))
        page.click_button(locator=page.get_locator_by_name(name="Чек - бокс область управления SafeLife",
                                                           random=RANDOM))
        page.click_button(locator=page.get_locator_by_name(name="Сохранить"))
        page = shared_vars.set_page(name="Главная страница")
        page.click_button(locator=page.get_locator_by_name(name="Администратор root"))
        page.click_button(locator=page.get_locator_by_name(name="Выход"))
        page = shared_vars.set_page(name="Форма авторизации")
        page.fill_field(locator=page.get_locator_by_name(name="Имя пользователя"), value="SafeLife_" + RANDOM)
        page.fill_field(locator=page.get_locator_by_name(name="Пароль"), value="P@ssw0rd")
        page.click_button(locator=page.get_locator_by_name(name="Войти"))

    @allure.title('Проверить наполнение АРМ согласно набору ролей')
    def test_safelife_4(self):
        page = shared_vars.set_page(name="Главная страница")
        page.get_element(locator=page.get_locator_by_name(name="Информация об устройствах"))
        page.get_element(locator=page.get_locator_by_name(name="Данные об устройстве"))
        page.get_element(locator=page.get_locator_by_name(name="Местоположения"))
        page.get_element(locator=page.get_locator_by_name(name="События"))
        page.get_element(locator=page.get_locator_by_name(name="Отчёты"))
        page.get_element(locator=page.get_locator_by_name(name="Аудит"))
        page.get_element(locator=page.get_locator_by_name(name="Перемещения"))
        page.get_element(locator=page.get_locator_by_name(name="Геозоны(Отчёты)"))
        page.get_element(locator=page.get_locator_by_name(name="SafeLife"))
        page.get_element(locator=page.get_locator_by_name(name="Объекты учёта"))
        page.get_element(locator=page.get_locator_by_name(name="ОШС"))
        page.get_element(locator=page.get_locator_by_name(name="Сотрудники"))
        page.get_element(locator=page.get_locator_by_name(name="Комплекты"))
        page.get_element(locator=page.get_locator_by_name(name="Геозоны(Объекты учёта)"))
        page.get_element(locator=page.get_locator_by_name(name="Пользовательское соглашение"))
        page.element_error_checking(locator=page.get_locator_by_name(name="Управление устройствами"))
        page.element_error_checking(locator=page.get_locator_by_name(name="Команды"))
        page.element_error_checking(locator=page.get_locator_by_name(name="Профили(Управление устройствами)"))
        page.element_error_checking(locator=page.get_locator_by_name(name="Приложения(Приложения)"))
        page.element_error_checking(locator=page.get_locator_by_name(name="Конфигурации"))
        page.element_error_checking(locator=page.get_locator_by_name(name="Звонки и SMS"))
        page.element_error_checking(locator=page.get_locator_by_name(name="События ИБ"))
        page.element_error_checking(locator=page.get_locator_by_name(name="Профили(Отчеты)"))
        page.element_error_checking(locator=page.get_locator_by_name(name="Правила управления(Отчеты)"))
        page.element_error_checking(locator=page.get_locator_by_name(name="Загрузчик"))
        page.element_error_checking(locator=page.get_locator_by_name(name="Календарь"))
        page.element_error_checking(locator=page.get_locator_by_name(name="Адресная книга"))
        page.element_error_checking(locator=page.get_locator_by_name(name="Лицензия"))
        page.click_button(locator=page.get_locator_by_name(name="SafeLife"))
        page.error_checking(locator=page.get_locator_by_name(name="Внутренняя ошибка"))
