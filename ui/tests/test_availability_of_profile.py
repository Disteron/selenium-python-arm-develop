import json
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
1. Создать ОШС Отдел тестирования, Android, IOS, Финаносовый отдел
2. Создать 2 сотрудника для ветки Android, IOS
3. Создать несколько профилей 

Шаги:
1.	Переходим на вкладку “Профили” и нажимаем кнопку “Обновить” в верхней части стенда и в нижней части стенда
2.	В поле “Отображение” вводим параметр 5 и нажимаем enter, нажимаем на “Следующая страница”, нажимаем на “Последняя”,
    нажимаем на “Предыдущая страница”, нажимаем на “Первая страница”.
3.	Выполняем сортировку по “Наименование”, “Тип”, “Платформа”, “Сущность”.
4.	Нажимаем на кнопку “Добавить”, выполняем сортировку по столбцам “Тип”, “Платформа”, выбираем профиль 
    “Парольные политики iOS”, нажимаем “ОК”, в поле наименование пишем “Парольные политики iOS”,
     нажимаем “Сохранить”.
5.	Выполняем повторную сортировку по “Наименование”, “Тип”, “Платформа”, “Сущность”.
6.	Переход на вкладку “Условия”.
7.	Переход на вкладку “Назначения” и раскрываем все узлы ОШС, выбираем узел Android и выбираем 2 сотрудника авроры,
    нажимаем “Сохранить”, нажимаем "Да".
8.	Выполняем сортировку по “mcc”, “Телефон”, “Сотрудник”, “Должность”, “Отдел/Группа”, “Статус”.
    Нажимаем на кнопку обновить в нижней части стенда.
9.	Закрыть все узлы ОШС.
10.	Переходим на вкладку “Владелец”, раскрываем все ОШС, выбираем “Отдел тестирования” и нажимаем “Отмена”,
    выбираем “Отдел тестирования” и нажимаем “Сохранить”
11.	Переходим на вкладку “Делегирование”, выбираем “Android”, “Финансовый отдел”, нажимаем “Отмена”,
    выбираем “Отдел тестирования”, нажимаем “Сохранить”, нажимаем “Да”
12.	В поле “Отображение” вводим параметр 1 и нажимаем enter, нажимаем на “Следующая страница”,
    нажимаем на “Последняя”, нажимаем на “Предыдущая страница”, нажимаем на “Первая страница”.
13.	Удаляем созданный профиль ранее 
14.	Нажимаем кнопку “Обновить” в верхней части стенда и в нижней части стенда

"""

time_now = str(int(time.time()) * 1000 + 999)
RANDOM = str(random.randint(1, 10000000))
shared_vars.COMMON_VAR["RANDOM"] = RANDOM
TESTING_DEPARTMENT = 'Отдел тестирования_' + RANDOM
ANDROID = 'Android_' + RANDOM
IOS = 'IOS_' + RANDOM


@pytest.mark.ui
@pytest.mark.smoke
@pytest.mark.regress
@pytest.mark.id_13
@pytest.mark.incremental
@pytest.mark.usefixtures("start_browser")
@allure.title('[UI] Проверка Профиля')
@allure.severity(Severity.CRITICAL)
@allure.feature('[UI] Профили')
@allure.description('[UI] Проверка доступоности всех форм во вкладке профили')
class TestProfile:

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
                name='Добавление ОШС Отдел тестирования на ветку root',
                company_name='Отдел тестирования_' + RANDOM,
                structure_number=-1) \
            .fire()

        oss = Request(method='get',
                      endpoint='/api/v1/unit/-1?_dc=' + time_now + '&count=true&node=-1',
                      name='Просмотр списка ошс на ветке root') \
            .fire()

        for i in json.loads(oss.response.text)["children"]:
            if i["text"] == TESTING_DEPARTMENT:
                shared_vars.COMMON_VAR["id_testing_departament"] = i["id"]

        Request(method='post',
                endpoint='/api/v1/unit?_dc=' + time_now + '&lazy=false&employee=false',
                template='organizational_structure',
                name='Добавление ОШС Android',
                company_name='Android_' + RANDOM,
                structure_number=int(shared_vars.COMMON_VAR["id_testing_departament"])) \
            .fire()

        Request(method='post',
                endpoint='/api/v1/unit?_dc=' + time_now + '&lazy=false&employee=false',
                template='organizational_structure',
                name='Добавление ОШС IOS',
                company_name='IOS_' + RANDOM,
                structure_number=int(shared_vars.COMMON_VAR["id_testing_departament"])) \
            .fire()

        android = Request(method='get',
                          endpoint='/api/v1/unit/' + str(shared_vars.COMMON_VAR["id_testing_departament"])
                                   + '?_dc=' + time_now + '&count=true&node='
                                   + str(shared_vars.COMMON_VAR["id_testing_departament"]) + '',
                          name='Просмотр списка ошс на ветке android') \
            .fire()

        for i in json.loads(android.response.text)["children"]:
            if i["text"] == ANDROID:
                shared_vars.COMMON_VAR["android"] = i["id"]

        ios = Request(method='get',
                      endpoint='/api/v1/unit/' + str(shared_vars.COMMON_VAR["id_testing_departament"])
                               + '?_dc=' + time_now + '&count=true&node='
                               + str(shared_vars.COMMON_VAR["id_testing_departament"]) + '',
                      name='Просмотр списка ошс на ветке android') \
            .fire()

        for i in json.loads(ios.response.text)["children"]:
            if i["text"] == IOS:
                shared_vars.COMMON_VAR["ios"] = i["id"]

        Request(method='post',
                endpoint='/api/v1/employee?_dc=' + time_now + '&filter=%5B%7B%22property'
                                                              '%22%3A%22liveSearch%22%2C%22value%22%3A%22%22%7D%5D',
                template='staff',
                name='Добавление сотрудников Android',
                surname='Android',
                name_staff='QA1',
                patronymic='QA1_' + RANDOM,
                position='Android_QA1_' + RANDOM,
                email_domain='niisokb',
                email_login='Android_QA1_' + RANDOM,
                email='Android_QA1_@niisikb.ru' + RANDOM,
                staff_number=int(shared_vars.COMMON_VAR["android"])) \
            .fire()

        Request(method='post',
                endpoint='/api/v1/employee?_dc=' + time_now + '&filter=%5B%7B%22property'
                                                              '%22%3A%22liveSearch%22%2C%22value%22%3A%22%22%7D%5D',
                template='staff',
                name='Добавление сотрудников Android',
                surname='Android',
                name_staff='QA2',
                patronymic='QA2_' + RANDOM,
                position='Android_QA2_' + RANDOM,
                email_domain='niisokb',
                email_login='Android_QA2_' + RANDOM,
                email='Android_QA2_@niisikb.ru' + RANDOM,
                staff_number=int(shared_vars.COMMON_VAR["android"])) \
            .fire()

        Request(method='post',
                endpoint='/api/v1/employee?_dc=' + time_now + '&filter=%5B%7B%22property'
                                                              '%22%3A%22liveSearch%22%2C%22value%22%3A%22%22%7D%5D',
                template='staff',
                name='Добавление сотрудников IOS',
                surname='IOS',
                name_staff='QA1',
                patronymic='QA1_' + RANDOM,
                position='IOS_' + RANDOM,
                email_domain='niisokb',
                email_login='IOS_QA1' + RANDOM,
                email='IOS_QA1_@niisikb.ru' + RANDOM,
                staff_number=int(shared_vars.COMMON_VAR["ios"])) \
            .fire()

        Request(method='post',
                endpoint='/api/v1/employee?_dc=' + time_now + '&filter=%5B%7B%22property'
                                                              '%22%3A%22liveSearch%22%2C%22value%22%3A%22%22%7D%5D',
                template='staff',
                name='Добавление сотрудников IOS',
                surname='IOS',
                name_staff='QA2',
                patronymic='QA2_' + RANDOM,
                position='IOS_' + RANDOM,
                email_domain='niisokb',
                email_login='IOS_QA2' + RANDOM,
                email='IOS_QA2_@niisikb.ru' + RANDOM,
                staff_number=int(shared_vars.COMMON_VAR["ios"])) \
            .fire()

        Request(method='post',
                endpoint='/api/v1/profile?_dc=' + time_now,
                template='profiles_android_password_policies',
                name_profile='Парольные политики Android_' + RANDOM,
                name='Сохранение профиля Парольные политики Android') \
            .fire()

        Request(method='post',
                endpoint='/api/v1/profile?_dc=' + time_now,
                template='profiles_android_restriction_policies',
                name_profile='Политики ограничений Android_' + RANDOM,
                name='Сохранение профиля Политики ограничений Android') \
            .fire()

    @allure.title('Переходим на вкладку “Профили” и нажимаем кнопку “Обновить” в верхней части стенда '
                  'и в нижней части стенда')
    def test_profile_1(self):
        common_steps.auth()
        page = shared_vars.set_page(name="Главная страница")
        page.click_button(locator=page.get_locator_by_name(name="Профили(Управление устройствами)"))
        page.click_button(locator=page.get_locator_by_name(name="Обновить"))
        page = shared_vars.set_page(name="Профили")
        page.click_button(locator=page.get_locator_by_name(name="Обновить низ 1"))

    @allure.title('В поле “Отображение” вводим параметр 5 и нажимаем enter, '
                  'нажимаем на “Следующая страница”, нажимаем на “Последняя”, '
                  'нажимаем на “Предыдущая страница”, нажимаем на “Первая страница”.')
    def test_profile_2(self):
        page = shared_vars.set_page(name="Профили")
        page.fill_field_enter(locator=page.get_locator_by_name(name="Отображение"), value="1")
        page.click_button(locator=page.get_locator_by_name(name="Следующая страница"))
        page.click_button(locator=page.get_locator_by_name(name="Последняя страница"))
        page.click_button(locator=page.get_locator_by_name(name="Предыдущая страница"))
        page.click_button(locator=page.get_locator_by_name(name="Первая страница"))

    @allure.title('Выполняем сортировку по “Наименование”, “Тип”, “Платформа”, “Сущность”.')
    def test_profile_3(self):
        page = shared_vars.set_page(name="Профили")
        page.click_button(locator=page.get_locator_by_name(name="Наименование сортировка"))
        page.click_button(locator=page.get_locator_by_name(name="Тип 1"))
        page.click_button(locator=page.get_locator_by_name(name="Платформа 1"))
        page.click_button(locator=page.get_locator_by_name(name="Сущность"))

    @allure.title('Нажимаем на кнопку “Добавить”, выполняем сортировку по столбцам “Тип”, “Платформа”,'
                  ' выбираем профиль “Парольные политики iOS”, нажимаем “ОК”, в поле наименование пишем'
                  ' “Парольные политики iOS”, нажимаем “Сохранить”.')
    def test_profile_4(self):
        page = shared_vars.set_page(name="Профили")
        page.click_button(locator=page.get_locator_by_name(name="Добавить"))
        page.click_button(locator=page.get_locator_by_name(name="Тип 2"))
        page.click_button(locator=page.get_locator_by_name(name="Платформа 2"))
        page.click_button(locator=page.format_locator(page.UNIVERSAL_DIV_XPATH, div_text='Парольные политики iOS'))
        page.click_button(locator=page.get_locator_by_name(name="Ок"))
        page.fill_field(locator=page.get_locator_by_name(name="Наименование поле"),
                        value='Парольные политики iOS_' + RANDOM)
        page.click_button(locator=page.get_locator_by_name(name="Сохранить"))

    @allure.title('Выполняем повторную сортировку по “Наименование”, “Тип”, “Платформа”, “Сущность”.')
    def test_profile_5(self):
        page = shared_vars.set_page(name="Профили")
        page.click_button(locator=page.get_locator_by_name(name="Наименование сортировка"))
        page.click_button(locator=page.get_locator_by_name(name="Тип 1"))
        page.click_button(locator=page.get_locator_by_name(name="Платформа 1"))
        page.click_button(locator=page.get_locator_by_name(name="Сущность"))

    @allure.title('Переход на вкладку “Условия”.')
    def test_profile_6(self):
        page = shared_vars.set_page(name="Профили")
        page.click_button(locator=page.get_locator_by_name(name="Условия (не заданы)"))

    @allure.title('Переход на вкладку “Назначения” и раскрываем все узлы ОШС, '
                  'выбираем узел Android и выбираем 2 сотрудника авроры, нажимаем “Сохранить”, нажимаем "Да".')
    def test_profile_7(self):
        page = shared_vars.set_page(name="Профили")
        page.click_button(locator=page.get_locator_by_name(name="Назначения"))
        page.click_button(locator=page.get_locator_by_name(name="Плюс root"))
        page.click_button(locator=page.get_locator_by_name(name="Плюс Отдел тестирования",
                                                           random=RANDOM))
        page.click_button(locator=page.get_locator_by_name(name="Плюс Android",
                                                           random=RANDOM))
        page.click_button(locator=page.get_locator_by_name(name="Плюс IOS",
                                                           random=RANDOM))
        page.click_button(locator=page.get_locator_by_name(name="ОШС Android",
                                                           random=RANDOM))
        page.click_button(locator=page.get_locator_by_name(name="Сотрудник ios 1",
                                                           random=RANDOM))
        page.click_button(locator=page.get_locator_by_name(name="Сотрудник ios 2",
                                                           random=RANDOM))
        page.click_button(locator=page.get_locator_by_name(name="Сохранить назначения"))
        page.click_button(locator=page.get_locator_by_name(name="Да"))

    @allure.title('Выполняем сортировку по “Телефон”, “Сотрудник”, “Должность”, “Отдел/Группа”, “Статус”.'
                  ' Нажимаем на кнопку обновить в нижней части стенда.')
    def test_profile_8(self):
        page = shared_vars.set_page(name="Профили")
        page.click_button(locator=page.get_locator_by_name(name="Телефон"))
        page.click_button(locator=page.get_locator_by_name(name="Сотрудник"))
        page.click_button(locator=page.get_locator_by_name(name="Должность"))
        page.click_button(locator=page.get_locator_by_name(name="Отдел Группа"))
        page.click_button(locator=page.get_locator_by_name(name="Статус"))
        page.click_button(locator=page.get_locator_by_name(name="Обновить низ 2"))

    @allure.title('Закрыть все узлы ОШС')
    def test_profile_9(self):
        page = shared_vars.set_page(name="Профили")
        page.click_button(locator=page.get_locator_by_name(name="Плюс IOS",
                                                           random=RANDOM))
        page.click_button(locator=page.get_locator_by_name(name="Плюс Android",
                                                           random=RANDOM))
        page.click_button(locator=page.get_locator_by_name(name="Плюс Отдел тестирования",
                                                           random=RANDOM))
        page.click_button(locator=page.get_locator_by_name(name="Плюс root"))

    @allure.title('Переходим на вкладку “Владелец”, раскрываем все ОШС, выбираем “Отдел тестирования”'
                  ' и нажимаем “Отмена”, выбираем “Отдел тестирования” и нажимаем “Сохранить”')
    def test_profile_10(self):
        page = shared_vars.set_page(name="Профили")
        page.click_button(locator=page.get_locator_by_name(name="Владелец"))
        page = shared_vars.set_page(name="Владелец и делегирование")
        page.click_button(locator=page.get_locator_by_name(name="Владелец плюс root"))
        page.click_button(locator=page.get_locator_by_name(name="Владелец плюс отдел тестирования",
                                                           random=RANDOM))
        page.click_button(locator=page.get_locator_by_name(name="Владелец ошс отдел тестирования",
                                                           random=RANDOM))
        page.click_button(locator=page.get_locator_by_name(name="Владелец отменить"))
        page.click_button(locator=page.get_locator_by_name(name="Владелец ошс отдел тестирования",
                                                           random=RANDOM))
        page.click_button(locator=page.get_locator_by_name(name="Владелец сохранить"))
        page = shared_vars.set_page(name="Профили")
        page.click_button(locator=page.get_locator_by_name(name="Да"))

    @allure.title('Переходим на вкладку “Делегирование”, выбираем “Android”, “Финансовый отдел”,'
                  ' нажимаем “Отмена”, выбираем “Отдел тестирования”, нажимаем “Сохранить”, нажимаем “Да”.')
    def test_profile_11(self):
        page = shared_vars.set_page(name="Профили")
        page.click_button(locator=page.get_locator_by_name(name="Делегирование"))
        page = shared_vars.set_page(name="Владелец и делегирование")
        page.click_button(locator=page.get_locator_by_name(name="Делегирование android",
                                                           random=RANDOM))
        page.click_button(locator=page.get_locator_by_name(name="Делегирование отменить"))
        page.click_button(locator=page.get_locator_by_name(name="Делегирование android",
                                                           random=RANDOM))
        page.click_button(locator=page.get_locator_by_name(name="Делегирование сохранить"))
        page = shared_vars.set_page(name="Профили")
        page.click_button(locator=page.get_locator_by_name(name="Да"))

    @allure.title('В поле “Отображение” вводим параметр 1 и нажимаем enter, нажимаем на “Следующая страница”, '
                  'нажимаем на “Последняя”, нажимаем на “Предыдущая страница”, нажимаем на “Первая страница”.')
    def test_profile_12(self):
        page = shared_vars.set_page(name="Профили")
        page.fill_field_enter(locator=page.get_locator_by_name(name="Отображение"), value="1")
        page.click_button(locator=page.get_locator_by_name(name="Следующая страница"))
        page.click_button(locator=page.get_locator_by_name(name="Последняя страница"))
        page.click_button(locator=page.get_locator_by_name(name="Предыдущая страница"))
        page.click_button(locator=page.get_locator_by_name(name="Первая страница"))
        page.fill_field_enter(locator=page.get_locator_by_name(name="Отображение"), value="999")

    @allure.title('Удаляем созданный профиль ранее')
    def test_profile_13(self):
        page = shared_vars.set_page(name="Профили")
        page.click_button(locator=page.format_locator(page.UNIVERSAL_DIV_XPATH,
                                                      div_text='Парольные политики iOS_' + RANDOM))
        page.click_button(locator=page.get_locator_by_name(name="Удалить"))
        page.click_button(locator=page.get_locator_by_name(name="Да"))
        page.click_button(locator=page.format_locator(page.UNIVERSAL_DIV_XPATH,
                                                      div_text='Парольные политики Android_' + RANDOM))
        page.click_button(locator=page.get_locator_by_name(name="Удалить"))
        page.click_button(locator=page.get_locator_by_name(name="Да"))
        page.click_button(locator=page.format_locator(page.UNIVERSAL_DIV_XPATH,
                                                      div_text='Политики ограничений Android_' + RANDOM))
        page.click_button(locator=page.get_locator_by_name(name="Удалить"))
        page.click_button(locator=page.get_locator_by_name(name="Да"))

    @allure.title('Нажимаем кнопку “Обновить” в верхней части стенда и в нижней части стенда')
    def test_profile_14(self):
        page = shared_vars.set_page(name="Профили")
        page.click_button(locator=page.get_locator_by_name(name="Обновить низ 1"))
        page.click_button(locator=page.get_locator_by_name(name="Обновить верх"))
        page = shared_vars.set_page(name="Главная страница")
        page.error_checking(locator=page.get_locator_by_name(name="Внутренняя ошибка"))
