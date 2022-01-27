import json
import random
import time
import allure
import pytest
import shared_vars


from requests_api.core.request import Request
from allure_commons.types import Severity
from ui.steps import common_steps


"""

Предуслове:
1. Создать ОШС Отдел тестирования, Android, IOS, Финаносовый отдел
2. Создать 2 сотрудника для ветки Android, IOS

Шаги:
1.	Переходим на вкладку “Конфигурации” и нажимаем кнопку “Обновить” в верхней части стенда и в нижней части стенда
2.  Выполняем сортировку по “Наименование”, “UID”, “Место установки”, “Платформа”, “Сущность”.
3.	Нажимаем "Добавить(Кнопка вниз)", нажимаем "Создать конфигурацию из шаблона".
    Выполняем сортировку по "UID", "Платформа". Выбираем "com.microsoft.office.outlook".
    В поле "Название" пишем "Outlook_random". Нажимаем "сохранить"
4.	Нажимаем "Добавить(Кнопка вниз)", нажимаем "Создать конфигурацию из шаблона".
    Выполняем сортировку по "UID", "Платформа". Выбираем "com.google.android.gm".
    В поле "Название" пишем "Android_gm_random". Нажимаем "сохранить"
5.	Нажимаем "Добавить(Кнопка вниз)", нажимаем "Создать пустую конфигурацию", В поле "Название" пишем
    "Configurations_random", "Платформа" выбираем "Android", "UID" пишем "Configuration_random",
    "Описание" пишем "test".
    Активируем "SafePhone SDK". Нажимаем "Добавить(Создание настройки конфигурации)". Ключ - Key_random
    Название - Name_random, Описание - test, Тип значений - "Строка", в поле "Key_random" вписываем значение,
    Нажимаем "Сохранить".
6.	Выполняем повторную сортировку по “Наименование”, “UID”, “Место установки”, “Платформа”, “Сущность”.
7.	Переход на вкладку “Условия”.
8.	Переход на вкладку “Назначения” и раскрываем все узлы ОШС, выбираем узел Android и выбираем 2 сотрудника авроры,
    нажимаем “Сохранить”, нажимаем "Да".
9.	Выполняем сортировку по “mcc”, “Телефон”, “Сотрудник”, “Должность”, “Отдел/Группа”, “Статус”.
    Нажимаем на кнопку обновить в нижней части стенда.
10.	Закрыть все узлы ОШС.
11.	Переходим на вкладку “Владелец”, раскрываем все ОШС, выбираем “Отдел тестирования” и нажимаем “Отмена”,
    выбираем “Отдел тестирования” и нажимаем “Сохранить”
12.	Переходим на вкладку “Делегирование”, выбираем “Android”, “Финансовый отдел”, нажимаем “Отмена”,
    выбираем “Отдел тестирования”, нажимаем “Сохранить”, нажимаем “Да”
13.	В поле “Отображение” вводим параметр 1 и нажимаем enter, нажимаем на “Следующая страница”,
    нажимаем на “Последняя”, нажимаем на “Предыдущая страница”, нажимаем на “Первая страница”.
14.	Удаляем созданные конфигурации 
15.	Нажимаем кнопку “Обновить” в верхней части стенда и в нижней части стенда

"""


time_now = str(int(time.time()) * 1000 + 999)
RANDOM = str(random.randint(1, 10000000))
shared_vars.COMMON_VAR["RANDOM"] = RANDOM
TESTING_DEPARTMENT = 'Отдел тестирования_' + RANDOM
ANDROID = 'Android_' + RANDOM
IOS = 'IOS_' + RANDOM


@pytest.mark.ui
@pytest.mark.regress
@pytest.mark.id_12
@pytest.mark.incremental
@pytest.mark.usefixtures("start_browser")
@allure.title('[UI] Проверка Конфигурации')
@allure.severity(Severity.CRITICAL)
@allure.feature('[UI] Конфигурации')
@allure.description('[UI] Проверка доступоности всех форм во вкладке Конфигурации')
class TestConfiguration:

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

        upload_response = Request(method='post',
                                  endpoint='/api/v1/application/upload',
                                  name='Запрос на загрузку файла приложения SafeMessages-2.7.5.apk',
                                  files={"name": "application",
                                         "content-type": "application/vnd.android.package-archive",
                                         "path": "SafeMessages-2.7.5.apk"}) \
            .fire()

        shared_vars.COMMON_VAR["Android_app"] = upload_response

        Request(method='post',
                endpoint='/api/v1/application',
                name='Сохранение файла приложения SafeMessages-2.7.5.apk',
                body=shared_vars.COMMON_VAR["Android_app"].response.json()["data"]) \
            .fire()

    @allure.title('Переходим на вкладку “Конфигурации” и нажимаем кнопку “Обновить” '
                  'в верхней части стенда и в нижней части стенда')
    def test_configurations_1(self):
        common_steps.auth()
        page = shared_vars.set_page(name="Главная страница")
        page.click_button(locator=page.get_locator_by_name(name="Конфигурации"))
        page.click_button(locator=page.get_locator_by_name(name="Обновить"))
        page = shared_vars.set_page(name="Конфигурации")
        page.click_button(locator=page.get_locator_by_name(name="Обновить низ 1"))

    @allure.title('Выполняем сортировку по “Наименование”, “UID”, “Место установки”, “Платформа”, “Сущность”.')
    def test_configurations_2(self):
        page = shared_vars.set_page(name="Конфигурации")
        page.click_button(locator=page.get_locator_by_name(name="Сортировка(Наименование)"))
        page.click_button(locator=page.get_locator_by_name(name="Сортировка(UID)"))
        page.click_button(locator=page.get_locator_by_name(name="Сортировка(Место установки)"))
        page.click_button(locator=page.get_locator_by_name(name="Сортировка(Платформа)"))
        page.click_button(locator=page.get_locator_by_name(name="Сортировка(Сущность)"))

    @allure.title('Нажимаем "Добавить(Кнопка вниз)", нажимаем "Создать конфигурацию из шаблона". '
                  'Выполняем сортировку по "UID", "Платформа". Выбираем "com.microsoft.office.outlook". '
                  'В поле "Название" пишем "Outlook_random". Нажимаем "сохранить"')
    def test_configurations_3(self):
        page = shared_vars.set_page(name="Конфигурации")
        page.click_button_with_offset(locator=page.get_locator_by_name(name="Добавить(Кнопка вниз)"), x=95, y=11)
        page.click_button(locator=page.get_locator_by_name(name="Создать конфигурацию из шаблона"))
        page.click_button(locator=page.get_locator_by_name(name="Создание конфигурации приложения(Сортировка)(UID)"))
        page.click_button(
            locator=page.get_locator_by_name(name="Создание конфигурации приложения(Сортировка)(Платформа)"))
        page.click_button(
            locator=page.get_locator_by_name(name="Создание конфигурации приложения(com.microsoft.office.outlook)"))
        page.click_button(locator=page.get_locator_by_name(name="Ок"))
        page.fill_field(locator=page.get_locator_by_name(name="Название"), value="microsoft_office_" + RANDOM)
        page.click_button(locator=page.get_locator_by_name(name="Сохранить(Настройки)"))

    @allure.title('Нажимаем "Добавить(Кнопка вниз)", нажимаем "Создать конфигурацию из шаблона". '
                  'Выполняем сортировку по "UID", "Платформа". Выбираем "com.google.android.gm". '
                  'В поле "Название" пишем "Android_gm_random". Нажимаем "сохранить')
    def test_configurations_4(self):
        page = shared_vars.set_page(name="Базовая страница")
        page.wait_invisibility_of_element(locator=page.get_locator_by_name(name='Загрузка'))
        page = shared_vars.set_page(name="Конфигурации")
        page.click_button_with_offset(locator=page.get_locator_by_name(name="Добавить(Кнопка вниз)"), x=95, y=11)
        page.click_button(locator=page.get_locator_by_name(name="Создать конфигурацию из шаблона"))
        page.click_button(locator=page.get_locator_by_name(name="Создание конфигурации приложения(Сортировка)(UID)"))
        page.click_button(
            locator=page.get_locator_by_name(name="Создание конфигурации приложения(Сортировка)(Платформа)"))
        page.click_button(
            locator=page.get_locator_by_name(name="Создание конфигурации приложения(com.google.android.gm)"))
        page.click_button(locator=page.get_locator_by_name(name="Ок"))
        page.fill_field(locator=page.get_locator_by_name(name="Название"), value="google_android_" + RANDOM)
        page.click_button(locator=page.get_locator_by_name(name="Сохранить(Настройки)"))

    @allure.title('Нажимаем "Добавить(Кнопка вниз)", нажимаем "Создать пустую конфигурацию", В поле "Название" '
                  'пишем "Configurations_random", "Платформа" выбираем "Android", "UID" пишем "Configuration_random",'
                  ' "Описание" пишем "test". Активируем "SafePhone SDK". Нажимаем "Добавить'
                  '(Создание настройки конфигурации)". Ключ - Key_random Название - Name_random, Описание - test,'
                  ' Тип значений - "Строка", в поле "Key_random" вписываем значение, Нажимаем "Сохранить"')
    def test_configurations_5(self):
        page = shared_vars.set_page(name="Базовая страница")
        page.wait_invisibility_of_element(locator=page.get_locator_by_name(name='Загрузка'))
        page = shared_vars.set_page(name="Конфигурации")
        page.click_button_with_offset(locator=page.get_locator_by_name(name="Добавить(Кнопка вниз)"), x=95, y=11)
        page.click_button(locator=page.get_locator_by_name(name="Создать пустую конфигурацию"))
        page.fill_field(locator=page.get_locator_by_name(name="Название"), value="Configurations_" + RANDOM)
        page.click_button(locator=page.get_locator_by_name(name="Платформа"))
        page.click_button(locator=page.get_locator_by_name(name="Платформа(Android)"))
        page.click_button(locator=page.get_locator_by_name(name="Место установки"))
        page.click_button(locator=page.get_locator_by_name(name="Место установки(Устройство)"))
        page.click_button(locator=page.get_locator_by_name(name="UID"))
        page.click_button(locator=page.get_locator_by_name(name="ru_niisokb_mcc_safemessages"))
        page.fill_field(locator=page.get_locator_by_name(name="Описание"), value="test" + RANDOM)
        page.click_button(locator=page.get_locator_by_name(name="SafePhone SDK"))
        page.click_button(locator=page.get_locator_by_name(name="Создание настройки конфигураци(Добавить)"))
        page.fill_field(locator=page.get_locator_by_name(name="Создание настройки конфигураци(Ключ)"),
                        value="Key_" + RANDOM)
        page.fill_field(locator=page.get_locator_by_name(name="Создание настройки конфигураци(Название)"),
                        value="Key_" + RANDOM)
        page.fill_field(locator=page.get_locator_by_name(name="Создание настройки конфигураци(Описание)"),
                        value="test_" + RANDOM)
        page.fill_field(locator=page.get_locator_by_name(name="Создание настройки конфигураци(Тип значений)(Строка)"),
                        value="Строка")
        page.click_button(locator=page.get_locator_by_name(name="Ок"))
        page.fill_field(locator=page.get_locator_by_name(name="Поле key_random", random=RANDOM), value="test" + RANDOM)
        page.click_button(locator=page.get_locator_by_name(name="Сохранить(Настройки)"))

    @allure.title('Выполняем повторную сортировку по “Наименование”, “UID”,'
                  ' “Место установки”, “Платформа”, “Сущность”.')
    def test_configurations_6(self):
        page = shared_vars.set_page(name="Конфигурации")
        page.click_button(locator=page.get_locator_by_name(name="Сортировка(Наименование)"))
        page.click_button(locator=page.get_locator_by_name(name="Сортировка(UID)"))
        page.click_button(locator=page.get_locator_by_name(name="Сортировка(Место установки)"))
        page.click_button(locator=page.get_locator_by_name(name="Сортировка(Платформа)"))
        page.click_button(locator=page.get_locator_by_name(name="Сортировка(Сущность)"))

    @allure.title('Переход на вкладку “Условия”.')
    def test_configurations_7(self):
        page = shared_vars.set_page(name="Конфигурации")
        page.click_button(locator=page.get_locator_by_name(name="Условия (не заданы)"))

    @allure.title('Переход на вкладку “Назначения” и раскрываем все узлы ОШС, '
                  'выбираем узел Android и выбираем 2 сотрудника авроры, нажимаем “Сохранить”, нажимаем "Да".')
    def test_configurations_8(self):
        page = shared_vars.set_page(name="Конфигурации")
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
        page.click_button(locator=page.get_locator_by_name(name="Сохранить(Назначения)"))
        page.click_button(locator=page.get_locator_by_name(name="Да"))

    @allure.title('Выполняем сортировку по “Телефон”, “Сотрудник”, “Должность”, “Отдел/Группа”, “Статус”.'
                  ' Нажимаем на кнопку обновить в нижней части стенда.')
    def test_configurations_9(self):
        page = shared_vars.set_page(name="Конфигурации")
        page.click_button(locator=page.get_locator_by_name(name="Телефон"))
        page.click_button(locator=page.get_locator_by_name(name="Сотрудник"))
        page.click_button(locator=page.get_locator_by_name(name="Должность"))
        page.click_button(locator=page.get_locator_by_name(name="Отдел Группа"))
        page.click_button(locator=page.get_locator_by_name(name="Статус"))
        page.click_button(locator=page.get_locator_by_name(name="Обновить низ 2"))

    @allure.title('Закрыть все узлы ОШС')
    def test_configurations_10(self):
        page = shared_vars.set_page(name="Конфигурации")
        page.click_button(locator=page.get_locator_by_name(name="Плюс IOS",
                                                           random=RANDOM))
        page.click_button(locator=page.get_locator_by_name(name="Плюс Android",
                                                           random=RANDOM))
        page.click_button(locator=page.get_locator_by_name(name="Плюс Отдел тестирования",
                                                           random=RANDOM))
        page.click_button(locator=page.get_locator_by_name(name="Плюс root"))

    @allure.title('Переходим на вкладку “Владелец”, раскрываем все ОШС, выбираем “Отдел тестирования”'
                  ' и нажимаем “Отмена”, выбираем “Отдел тестирования” и нажимаем “Сохранить”')
    def test_configurations_11(self):
        page = shared_vars.set_page(name="Конфигурации")
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
        page = shared_vars.set_page(name="Конфигурации")
        page.click_button(locator=page.get_locator_by_name(name="Да"))

    @allure.title('Переходим на вкладку “Делегирование”, выбираем “Android”, “Финансовый отдел”,'
                  ' нажимаем “Отмена”, выбираем “Отдел тестирования”, нажимаем “Сохранить”, нажимаем “Да”.')
    def test_configurations_12(self):
        page = shared_vars.set_page(name="Конфигурации")
        page.click_button(locator=page.get_locator_by_name(name="Делегирование"))
        page = shared_vars.set_page(name="Владелец и делегирование")
        page.click_button(locator=page.get_locator_by_name(name="Делегирование android",
                                                           random=RANDOM))
        page.click_button(locator=page.get_locator_by_name(name="Делегирование отменить"))
        page.click_button(locator=page.get_locator_by_name(name="Делегирование android",
                                                           random=RANDOM))
        page.click_button(locator=page.get_locator_by_name(name="Делегирование сохранить"))
        page = shared_vars.set_page(name="Конфигурации")
        page.click_button(locator=page.get_locator_by_name(name="Да"))

    @allure.title('В поле “Отображение” вводим параметр 1 и нажимаем enter, нажимаем на “Следующая страница”, '
                  'нажимаем на “Последняя”, нажимаем на “Предыдущая страница”, нажимаем на “Первая страница”.')
    def test_configurations_13(self):
        page = shared_vars.set_page(name="Конфигурации")
        page.fill_field_enter(locator=page.get_locator_by_name(name="Отображение"), value="1")
        page.click_button(locator=page.get_locator_by_name(name="Следующая страница"))
        page.click_button(locator=page.get_locator_by_name(name="Последняя страница"))
        page.click_button(locator=page.get_locator_by_name(name="Предыдущая страница"))
        page.click_button(locator=page.get_locator_by_name(name="Первая страница"))
        page.fill_field_enter(locator=page.get_locator_by_name(name="Отображение"), value="999")

    @allure.title('Удаляем созданный конфигурации ')
    def test_configurations_14(self):
        page = shared_vars.set_page(name="Конфигурации")
        page.click_button(locator=page.format_locator(page.UNIVERSAL_DIV_XPATH,
                                                      div_text='microsoft_office_' + RANDOM))
        page.click_button(locator=page.get_locator_by_name(name="Удалить"))
        page.click_button(locator=page.get_locator_by_name(name="Да"))
        page.click_button(locator=page.format_locator(page.UNIVERSAL_DIV_XPATH,
                                                      div_text='google_android_' + RANDOM))
        page.click_button(locator=page.get_locator_by_name(name="Удалить"))
        page.click_button(locator=page.get_locator_by_name(name="Да"))
        page.click_button(locator=page.format_locator(page.UNIVERSAL_DIV_XPATH,
                                                      div_text='Configurations_' + RANDOM))
        page.click_button(locator=page.get_locator_by_name(name="Удалить"))
        page.click_button(locator=page.get_locator_by_name(name="Да"))

    @allure.title('Нажимаем кнопку “Обновить” в верхней части стенда и в нижней части стенда')
    def test_configurations_15(self):
        page = shared_vars.set_page(name="Конфигурации")
        page.click_button(locator=page.get_locator_by_name(name="Обновить низ 1"))
        page = shared_vars.set_page(name="Главная страница")
        page.click_button(locator=page.get_locator_by_name(name="Обновить"))
        page.error_checking(locator=page.get_locator_by_name(name="Внутренняя ошибка"))
