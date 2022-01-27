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
1. Добавляем приложения для Android, ios, windows.
2. Создать ОШС Отдел тестирования, Android, IOS, Финаносовый отдел
3. Создать 2 сотрудника для ветки Android, IOS

Шаги:
1.	Переходим на вкладку “Правила управления” и нажимаем кнопку “Обновить” в верхней части стенда и в нижней части стенда
2.  Выполняем сортировку по “Наименование”, “Приложение”, “Версия”, “Платформа”, “Монитор”, 
    “Место установки”, “Сущность”.
3.	Нажимаем "Добавить". В поле "Название" вводим "Android_app", выбираем платфоруму "Android",
    Место установки "Устройство",
    Тип приложения "Корпоративное", UID "ru.niisokb.mcc", Описание "test" и нажимаем кнопку сохранить
4.	Нажимаем "Добавить". В поле "Название" вводим "iPhone_os_app", выбираем платфоруму "iPhone_os",
    Тип приложения "Корпоративное", UID "ru.safe-phone.SafeMail", Описание "test" и нажимаем кнопку сохранить
5.	Нажимаем "Добавить". В поле "Название" вводим "Windows_app", выбираем платфоруму "Windows",
    Тип приложения "Корпоративное", 
    UID "{9201FC66-1329-424A-9647-13E35EF71860}", Описание "test" и нажимаем кнопку сохранить
6.	Выполняем повторную сортировку по “Наименование”, “Приложение”, “Версия”, “Платформа”, “Монитор”, 
    “Место установки”, “Сущность”.
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
14. В поиске вводим "iPhone_os_app" и просматриваем найденый ПУП  
15.	Удаляем созданный ПУПы ранее 
16.	Нажимаем кнопку “Обновить” в верхней части стенда и в нижней части стенда

"""


time_now = str(int(time.time()) * 1000 + 999)
RANDOM = str(random.randint(1, 10000000))
shared_vars.COMMON_VAR["RANDOM"] = RANDOM
TESTING_DEPARTMENT = 'Отдел тестирования_' + RANDOM
ANDROID = 'Android_' + RANDOM
IOS = 'IOS_' + RANDOM


@pytest.mark.ui
@pytest.mark.regress
@pytest.mark.id_27
@pytest.mark.incremental
@pytest.mark.usefixtures("start_browser")
@allure.title('[UI] Проверка ПУП')
@allure.severity(Severity.CRITICAL)
@allure.feature('[UI] Правила управления')
@allure.description('[UI] Проверка доступоности всех форм во вкладке правила управления')
class TestManagementRules:

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

        upload_response = Request(method='post',
                                  endpoint='/api/v1/application/upload',
                                  name='Запрос на загрузку файла приложения SafeMail_1.1.ipa',
                                  files={"name": "application",
                                         "content-type": "application/vnd.android.package-archive",
                                         "path": "SafeMail_1.1.ipa"}) \
            .fire()

        shared_vars.COMMON_VAR["IOS_app"] = upload_response

        Request(method='post',
                endpoint='/api/v1/application',
                name='Сохранение файла приложения SafeMail_1.1.ipa',
                body=shared_vars.COMMON_VAR["IOS_app"].response.json()["data"]) \
            .fire()

        if shared_vars.APPLICATION_PROPERTIES["stand_version"] == "4.5":
            upload_response = Request(method='post',
                                      endpoint='/api/v1/application/upload',
                                      name='Запрос на загрузку файла приложения Far20b1420.x64.20100225.msi',
                                      files={"name": "application",
                                             "content-type": "application/vnd.android.package-archive",
                                             "path": "Far20b1420.x64.20100225.msi"}) \
                .fire()

            shared_vars.COMMON_VAR["Windows_app"] = upload_response

            Request(method='post',
                    endpoint='/api/v1/application',
                    name='Сохранение файла приложения Far20b1420.x64.20100225.msi',
                    body=shared_vars.COMMON_VAR["Windows_app"].response.json()["data"]) \
                .fire()

        if shared_vars.APPLICATION_PROPERTIES["stand_version"] == "5.0":
            upload_response = Request(method='post',
                                      endpoint='/api/v1/application/upload',
                                      name='Запрос на загрузку файла приложения Far20b1420.x64.20100225.msi',
                                      files={"name": "application",
                                             "content-type": "application/vnd.android.package-archive",
                                             "path": "Far20b1420.x64.20100225.msi"}) \
                .fire()

            shared_vars.COMMON_VAR["Windows_app"] = upload_response

            Request(method='post',
                    endpoint='/api/v1/application',
                    template='windows_far_5_0',
                    name='Сохранение файла приложения Far20b1420.x64.20100225.msi') \
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

    @allure.title('Переходим на вкладку “Правила управления” и нажимаем кнопку '
                  '“Обновить” в верхней части стенда и в нижней части стенда')
    def test_forms_management_rules_1(self):
        common_steps.auth()
        page = shared_vars.set_page(name="Главная страница")
        page.click_button(locator=page.get_locator_by_name(name="Правила управления(Приложения)"))
        page.click_button(locator=page.get_locator_by_name(name="Обновить"))
        page = shared_vars.set_page(name="Правила управления(Приложения)")
        page.click_button(locator=page.get_locator_by_name(name="Обновить низ 1"))

    @allure.title('Выполняем сортировку по “Наименование”, “Приложение”, “Версия”, “Платформа”, “Монитор”, '
                  '“Место установки”, “Сущность”.')
    def test_forms_management_rules_2(self):
        page = shared_vars.set_page(name="Правила управления(Приложения)")
        page.click_button(locator=page.get_locator_by_name(name="Сортировка(Наименование)"))
        page.click_button(locator=page.get_locator_by_name(name="Сортировка(Приложение)"))
        page.click_button(locator=page.get_locator_by_name(name="Сортировка(Версия)"))
        page.click_button(locator=page.get_locator_by_name(name="Сортировка(Платформа)"))
        page.click_button(locator=page.get_locator_by_name(name="Сортировка(Монитор)"))
        page.click_button(locator=page.get_locator_by_name(name="Сортировка(Место установки)"))
        page.click_button(locator=page.get_locator_by_name(name="Сортировка(Сущность)"))

    @allure.title('Нажимаем на кнопку "Добавить". В поле "Название" вводим "Android_app",'
                  ' выбираем платфоруму "Android",Место установки "Устройство",Тип приложения "Корпоративное",'
                  ' UID "ru.niisokb.mcc", Описание "test" и нажимаем кнопку сохранить.')
    def test_forms_management_rules_3(self):
        page = shared_vars.set_page(name="Правила управления(Приложения)")
        page.click_button(locator=page.get_locator_by_name(name="Добавить"))
        page.fill_field(locator=page.get_locator_by_name(name="Название"), value="Android_" + RANDOM)
        page.click_button(locator=page.get_locator_by_name(name="Платформа"))
        page.click_button(locator=page.get_locator_by_name(name="Платформа(Android)"))
        page.click_button(locator=page.get_locator_by_name(name="Место установки"))
        page.click_button(locator=page.get_locator_by_name(name="Место установки(Устройство)"))
        page.click_button(locator=page.get_locator_by_name(name="Тип приложения"))
        page.click_button(locator=page.get_locator_by_name(name="Тип приложения(Корпоративное)"))
        page.click_button(locator=page.get_locator_by_name(name="UID"))
        page.click_button(locator=page.get_locator_by_name(name="UID(Android)"))
        page.fill_field(locator=page.get_locator_by_name(name="Описание"), value="test")
        page.click_button(locator=page.get_locator_by_name(name="Сохранить"))

    @allure.title('Нажимаем "Добавить". В поле "Название" вводим "iPhone_os_app",'
                  ' выбираем платфоруму "iPhone_os",Тип приложения "Корпоративное",'
                  ' UID "ru.safe-phone.SafeMail", Описание "test" и нажимаем кнопку сохранить')
    def test_forms_management_rules_4(self):
        page = shared_vars.set_page(name="Правила управления(Приложения)")
        page.click_button(locator=page.get_locator_by_name(name="Добавить"))
        page.fill_field(locator=page.get_locator_by_name(name="Название"), value="iPhone_OS_" + RANDOM)
        page.click_button(locator=page.get_locator_by_name(name="Платформа"))
        page.click_button(locator=page.get_locator_by_name(name="Платформа(iPhone OS)"))
        page.click_button(locator=page.get_locator_by_name(name="Тип приложения"))
        page.click_button(locator=page.get_locator_by_name(name="Тип приложения(Корпоративное)"))
        page.click_button(locator=page.get_locator_by_name(name="UID"))
        page.click_button(locator=page.get_locator_by_name(name="UID(iPhone OS)"))
        page.fill_field(locator=page.get_locator_by_name(name="Описание"), value="test")
        page.click_button(locator=page.get_locator_by_name(name="Сохранить"))

    @allure.title('Нажимаем "Добавить". В поле "Название" вводим "Windows_app", выбираем платфоруму "Windows",'
                  ' Тип приложения "Корпоративное", UID "9201FC66-1329-424A-9647-13E35EF71860",'
                  ' Описание "test" и нажимаем кнопку сохранить')
    def test_forms_management_rules_5(self):
        page = shared_vars.set_page(name="Правила управления(Приложения)")
        page.click_button(locator=page.get_locator_by_name(name="Добавить"))
        page.fill_field(locator=page.get_locator_by_name(name="Название"), value="Windows_" + RANDOM)
        page.click_button(locator=page.get_locator_by_name(name="Платформа"))
        page.click_button(locator=page.get_locator_by_name(name="Платформа(Windows)"))
        page.get_element(locator=page.get_locator_by_name(name="Тип приложения"))
        page.fill_field(locator=page.get_locator_by_name(name="UID"), value="{9201FC66-1329-424A-9647-13E35EF71860}")
        page.fill_field(locator=page.get_locator_by_name(name="Описание"), value="test")
        page.click_button(locator=page.get_locator_by_name(name="Сохранить"))

    @allure.title('Выполняем повторную сортировку по “Наименование”, “Приложение”, “Версия”,'
                  ' “Платформа”, “Монитор”, “Место установки”, “Сущность”.')
    def test_forms_management_rules_6(self):
        page = shared_vars.set_page(name="Правила управления(Приложения)")
        page.click_button(locator=page.get_locator_by_name(name="Сортировка(Наименование)"))
        page.click_button(locator=page.get_locator_by_name(name="Сортировка(Приложение)"))
        page.click_button(locator=page.get_locator_by_name(name="Сортировка(Версия)"))
        page.click_button(locator=page.get_locator_by_name(name="Сортировка(Платформа)"))
        page.click_button(locator=page.get_locator_by_name(name="Сортировка(Монитор)"))
        page.click_button(locator=page.get_locator_by_name(name="Сортировка(Место установки)"))
        page.click_button(locator=page.get_locator_by_name(name="Сортировка(Сущность)"))

    @allure.title('Переход на вкладку “Условия”.')
    def test_forms_management_rules_7(self):
        page = shared_vars.set_page(name="Правила управления(Приложения)")
        page.click_button(locator=page.get_locator_by_name(name="Условия (не заданы)"))

    @allure.title('Переход на вкладку “Назначения” и раскрываем все узлы ОШС, выбираем узел Android'
                  ' и выбираем 2 сотрудника авроры, нажимаем “Сохранить”, нажимаем "Да".')
    def test_forms_management_rules_8(self):
        page = shared_vars.set_page(name="Правила управления(Приложения)")
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

    @allure.title('Выполняем сортировку по “mcc”, “Телефон”, “Сотрудник”, “Должность”, “Отдел/Группа”, “Статус”.'
                  'Нажимаем на кнопку обновить в нижней части стенда.')
    def test_forms_management_rules_9(self):
        page = shared_vars.set_page(name="Правила управления(Приложения)")
        page.click_button(locator=page.get_locator_by_name(name="Телефон"))
        page.click_button(locator=page.get_locator_by_name(name="Сотрудник"))
        page.click_button(locator=page.get_locator_by_name(name="Должность"))
        page.click_button(locator=page.get_locator_by_name(name="Отдел Группа"))
        page.click_button(locator=page.get_locator_by_name(name="Статус"))
        page.click_button(locator=page.get_locator_by_name(name="Обновить низ 2"))

    @allure.title('Закрыть все узлы ОШС')
    def test_forms_management_rules_10(self):
        page = shared_vars.set_page(name="Правила управления(Приложения)")
        page.click_button(locator=page.get_locator_by_name(name="Плюс IOS",
                                                           random=RANDOM))
        page.click_button(locator=page.get_locator_by_name(name="Плюс Android",
                                                           random=RANDOM))
        page.click_button(locator=page.get_locator_by_name(name="Плюс Отдел тестирования",
                                                           random=RANDOM))
        page.click_button(locator=page.get_locator_by_name(name="Плюс root"))

    @allure.title('Переходим на вкладку “Владелец”, раскрываем все ОШС, выбираем “Отдел тестирования”'
                  ' и нажимаем “Отмена”, выбираем “Отдел тестирования” и нажимаем “Сохранить”')
    def test_forms_management_rules_11(self):
        page = shared_vars.set_page(name="Правила управления(Приложения)")
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
        page = shared_vars.set_page(name="Правила управления(Приложения)")
        page.click_button(locator=page.get_locator_by_name(name="Да"))

    @allure.title('Переходим на вкладку “Делегирование”, выбираем “Android”, “Финансовый отдел”,'
                  ' нажимаем “Отмена”, выбираем “Отдел тестирования”, нажимаем “Сохранить”, нажимаем “Да”')
    def test_forms_management_rules_12(self):
        page = shared_vars.set_page(name="Правила управления(Приложения)")
        page.click_button(locator=page.get_locator_by_name(name="Делегирование"))
        page = shared_vars.set_page(name="Владелец и делегирование")
        page.click_button(locator=page.get_locator_by_name(name="Делегирование android",
                                                           random=RANDOM))
        page.click_button(locator=page.get_locator_by_name(name="Делегирование отменить"))
        page.click_button(locator=page.get_locator_by_name(name="Делегирование android",
                                                           random=RANDOM))
        page.click_button(locator=page.get_locator_by_name(name="Делегирование сохранить"))
        page = shared_vars.set_page(name="Правила управления(Приложения)")
        page.click_button(locator=page.get_locator_by_name(name="Да"))

    @allure.title('В поле “Отображение” вводим параметр 1 и нажимаем enter, нажимаем на “Следующая страница”, '
                  'нажимаем на “Последняя”, нажимаем на “Предыдущая страница”, нажимаем на “Первая страница”')
    def test_forms_management_rules_13(self):
        page = shared_vars.set_page(name="Правила управления(Приложения)")
        page.fill_field_enter(locator=page.get_locator_by_name(name="Отображение"), value="1")
        page.click_button(locator=page.get_locator_by_name(name="Следующая страница"))
        page.click_button(locator=page.get_locator_by_name(name="Последняя страница"))
        page.click_button(locator=page.get_locator_by_name(name="Предыдущая страница"))
        page.click_button(locator=page.get_locator_by_name(name="Первая страница"))
        page.fill_field_enter(locator=page.get_locator_by_name(name="Отображение"), value="999")

    @allure.title('В поиске вводим "iPhone_os_app" и просматриваем найденый ПУП')
    def test_forms_management_rules_14(self):
        page = shared_vars.set_page(name="Правила управления(Приложения)")
        page.fill_field(locator=page.get_locator_by_name(name="Поиск"), value="iPhone_OS_" + RANDOM)
        page.get_element(locator=page.format_locator(page.UNIVERSAL_DIV_XPATH, div_text="iPhone_OS_" + RANDOM))
        page.fill_field(locator=page.get_locator_by_name(name="Поиск"), value="")

    @allure.title('Удаляем созданный ранее ПУПы ')
    def test_forms_management_rules_15(self):
        page = shared_vars.set_page(name="Правила управления(Приложения)")
        page.click_button(locator=page.format_locator(page.UNIVERSAL_DIV_XPATH, div_text="iPhone_OS_" + RANDOM))
        page.click_button(locator=page.get_locator_by_name(name="Удалить"))
        page.click_button(locator=page.get_locator_by_name(name="Да"))
        page.click_button(locator=page.format_locator(page.UNIVERSAL_DIV_XPATH, div_text="Windows_" + RANDOM))
        page.click_button(locator=page.get_locator_by_name(name="Удалить"))
        page.click_button(locator=page.get_locator_by_name(name="Да"))
        page.click_button(locator=page.format_locator(page.UNIVERSAL_DIV_XPATH, div_text="Android_" + RANDOM))
        page.click_button(locator=page.get_locator_by_name(name="Удалить"))
        page.click_button(locator=page.get_locator_by_name(name="Да"))

    @allure.title('Нажимаем кнопку “Обновить” в верхней части стенда и в нижней части стенда')
    def test_forms_management_rules_16(self):
        page = shared_vars.set_page(name="Главная страница")
        page.click_button(locator=page.get_locator_by_name(name="Правила управления(Приложения)"))
        page.click_button(locator=page.get_locator_by_name(name="Обновить"))
        page = shared_vars.set_page(name="Правила управления(Приложения)")
        page.click_button(locator=page.get_locator_by_name(name="Обновить низ 1"))
        page = shared_vars.set_page(name="Главная страница")
        page.error_checking(locator=page.get_locator_by_name(name="Внутренняя ошибка"))
