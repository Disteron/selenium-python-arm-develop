import json
import time
import shared_vars
import allure
import pytest

from allure_commons.types import Severity
from requests_api.core.request import Request


time_now = str(int(time.time()) * 1000 + 999)

COMPANY_NAME = ['Служба оперативного управления производством', 'Отдел технического контроля',
                'Технический отдел', 'Финансовый отдел', 'Транспортный цех']

NAME_STAFF = ['QA1', 'QA2', 'QA3', 'QA4', 'QA5']

NAME_ROLE = 'full_roles'

time_start = int(time.time()) * 1000 - 500000000
time_end = int(time.time()) * 1000 + 2500000000
time1 = str(int(time.time()))

ID_CONNECT = [2, 1, 3, 4, 5]
SERVER_TYPE = ["MDMServer", "SCEPServer", "SocketServer", "WinMDM Enrollment", "WinMDM Management"]
URL_SERVER = ["https://" + shared_vars.APPLICATION_PROPERTIES["host"] + ":443",
              "https://" + shared_vars.APPLICATION_PROPERTIES["host"] + ":8082",
              shared_vars.APPLICATION_PROPERTIES["host"] + ":50001",
              "https://" + shared_vars.APPLICATION_PROPERTIES["host"],
              "https://" + shared_vars.APPLICATION_PROPERTIES["host"] + ":8444"]


@pytest.mark.filling
@pytest.mark.usefixtures("start_session")
@pytest.mark.skipif(shared_vars.APPLICATION_PROPERTIES["stand_version"] != "5.0", reason="version is not 5.0")
@allure.title('[API] Наполнение стенда данными')
@allure.severity(Severity.MINOR)
@allure.feature('[API] Наполнение стенда данными')
@allure.description('[API] Наполнение стенда данными')
class TestFilling50:

    @allure.title('[API] Открытие сессии')
    def test_filling_open_session(self):
        api_user = shared_vars.APPLICATION_PROPERTIES["api_user"]

        Request(method='post',
                endpoint='/login',
                template='auth',
                name='Авторизация',
                api_user=api_user,
                api_password='change_on_install') \
            .fire()

    @allure.title('[API] Смена пароля')
    def test_filling_changing_password(self):
        api_password = shared_vars.APPLICATION_PROPERTIES["api_password"]

        Request(method='post',
                endpoint='/change-pass',
                name='Смена пароля',
                data='pass-old=change_on_install&pass-new=' + api_password + '&pass-new=' + api_password,
                headers={'Content-type': 'application/x-www-form-urlencoded'}) \
            .fire()

    @allure.title('[API] Добавление лицензии')
    def test_filling_add_license(self):
        Request(method='post',
                endpoint='/api/v1/license',
                template='license',
                name='Добавление Лицензии') \
            .fire()

    @allure.title('[API] Добавление ОШС Отдел тестирования на ветку root')
    def test_filling_add_oss(self):
        Request(method='post',
                endpoint='/api/v1/unit?_dc=' + time_now + '&lazy=false&employee=false',
                template='organizational_structure_46',
                name='Добавление ОШС Отдел тестирования на ветку root',
                company_name='Отдел тестирования',
                structure_number=-1) \
            .fire()

        shared_vars.COMMON_VAR["id_department"] = 1

    @allure.title('[API] Добавление ОШС android на ветку Отдел тестирования')
    def test_filling_add_oss_android(self):
        Request(method='post',
                endpoint='/api/v1/unit?_dc=' + time_now + '&lazy=false&employee=false',
                template='organizational_structure_46',
                name='Добавление ОШС Android',
                company_name='Android',
                structure_number=int(shared_vars.COMMON_VAR["id_department"])) \
            .fire()

        shared_vars.COMMON_VAR["id_oss_android"] = 2

    @allure.title('[API] Добавление ОШС ios на ветку Отдел тестирования')
    def test_filling_add_oss_ios(self):
        Request(method='post',
                endpoint='/api/v1/unit?_dc=' + time_now + '&lazy=false&employee=false',
                template='organizational_structure_46',
                name='Добавление ОШС IOS',
                company_name='IOS',
                structure_number=int(shared_vars.COMMON_VAR["id_department"])) \
            .fire()

        shared_vars.COMMON_VAR["id_oss_ios"] = 3

    @allure.title('[API] Добавление ОШС aurora на ветку Отдел тестирования')
    def test_filling_add_oss_aurora(self):
        Request(method='post',
                endpoint='/api/v1/unit?_dc=' + time_now + '&lazy=false&employee=false',
                template='organizational_structure_46',
                name='Добавление ОШС Aurora',
                company_name='Aurora',
                structure_number=int(shared_vars.COMMON_VAR["id_department"])) \
            .fire()

        shared_vars.COMMON_VAR["id_oss_aurora"] = 4

    @allure.title('[API] Добавление ОШС windows на ветку Отдел тестирования')
    def test_filling_add_oss_windows(self):
        Request(method='post',
                endpoint='/api/v1/unit?_dc=' + time_now + '&lazy=false&employee=false',
                template='organizational_structure_46',
                name='Добавление ОШС Windows',
                company_name='Windows',
                structure_number=int(shared_vars.COMMON_VAR["id_department"])) \
            .fire()

        shared_vars.COMMON_VAR["id_oss_windows"] = 5

    @allure.title('[API] Добавление ОШС SafeLife на ветку Отдел тестирования')
    def test_filling_add_oss_safe_life(self):
        Request(method='post',
                endpoint='/api/v1/unit?_dc=' + time_now + '&lazy=false&employee=false',
                template='organizational_structure_46',
                name='Добавление ОШС SafeLife',
                company_name='SafeLife',
                structure_number=int(shared_vars.COMMON_VAR["id_department"])) \
            .fire()

        shared_vars.COMMON_VAR["id_oss_safe_life"] = 6

    @allure.title('[API] Добавление различных ОШС')
    def test_filling_add_various_oss(self):
        for i in range(5):
            Request(method='post',
                    endpoint='/api/v1/unit?_dc=' + time_now + '&lazy=false&employee=false',
                    template='organizational_structure_46',
                    name='Добавление различных ОШС',
                    company_name=COMPANY_NAME[i],
                    structure_number=-1) \
                .fire()

    @allure.title('[API] Добавление сотрудников на ветку Android')
    def test_filling_add_staff_android(self):
        for i in range(5):
            staff_android = Request(method='post',
                                    endpoint='/api/v1/employee?_dc=' + time_now + '&filter=%5B%7B%22property'
                                                                                  '%22%3A%22liveSearch%22%2C%2'
                                                                                  '2value%22%3A%22%22%7D%5D',
                                    template='staff',
                                    name='Добавление сотрудников Android',
                                    surname='Android',
                                    name_staff=NAME_STAFF[i],
                                    patronymic=NAME_STAFF[i],
                                    position='Android_' + NAME_STAFF[i],
                                    email_domain='niisokb',
                                    email_login='Android_' + NAME_STAFF[i],
                                    email='Android_' + NAME_STAFF[i] + '@niisikb.ru',
                                    staff_number=int(shared_vars.COMMON_VAR["id_oss_android"])) \
                .fire()

            shared_vars.COMMON_VAR["id_staff_android"] = []
            shared_vars.COMMON_VAR["id_staff_android"].append(staff_android)

    @allure.title('[API] Добавление сотрудников на ветку IOS')
    def test_filling_add_staff_ios(self):
        for i in range(5):
            staff_ios = Request(method='post',
                                endpoint='/api/v1/employee?_dc=' + time_now + '&filter=%5B%7B%22property'
                                                                              '%22%3A%22liveSearch%22%2C%22value'
                                                                              '%22%3A%22%22%7D%5D',
                                template='staff',
                                name='Добавление сотрудников IOS',
                                surname='IOS',
                                name_staff=NAME_STAFF[i],
                                patronymic=NAME_STAFF[i],
                                position='IOS' + NAME_STAFF[i],
                                email_domain='niisokb',
                                email_login='IOS_' + NAME_STAFF[i],
                                email='IOS_' + NAME_STAFF[i] + '@niisikb.ru',
                                staff_number=int(shared_vars.COMMON_VAR["id_oss_ios"])) \
                .fire()

            shared_vars.COMMON_VAR["id_staff_ios"] = []
            shared_vars.COMMON_VAR["id_staff_ios"].append(staff_ios)

    @allure.title('[API] Добавление сотрудников на ветку Aurora')
    def test_filling_add_staff_aurora(self):
        for i in range(5):
            Request(method='post',
                    endpoint='/api/v1/employee?_dc=' + time_now + '&filter=%5B%7B%22property%22%3A%22liveSe'
                                                                  'arch%22%2C%22value%22%3A%22%22%7D%5D',
                    template='staff',
                    name='Добавление сотрудников Aurora',
                    surname='Aurora',
                    name_staff=NAME_STAFF[i],
                    patronymic=NAME_STAFF[i],
                    position='Aurora' + NAME_STAFF[i],
                    email_domain='niisokb',
                    email_login='Aurora_' + NAME_STAFF[i],
                    email='Aurora_' + NAME_STAFF[i] + '@niisikb.ru',
                    staff_number=int(shared_vars.COMMON_VAR["id_oss_aurora"])) \
                .fire()

    @allure.title('[API] Добавление сотрудников на ветку Windows')
    def test_filling_add_staff_windows(self):
        for i in range(5):
            Request(method='post',
                    endpoint='/api/v1/employee?_dc=' + time_now + '&filter=%5B%7B%22property%22%3A%22liveSe'
                                                                  'arch%22%2C%22value%22%3A%22%22%7D%5D',
                    template='staff',
                    name='Добавление сотрудников Windows',
                    surname='Windows',
                    name_staff=NAME_STAFF[i],
                    patronymic=NAME_STAFF[i],
                    position='Windows' + NAME_STAFF[i],
                    email_domain='niisokb',
                    email_login='Windows_' + NAME_STAFF[i],
                    email='Windows_' + NAME_STAFF[i] + '@niisikb.ru',
                    staff_number=int(shared_vars.COMMON_VAR["id_oss_windows"])) \
                .fire()

    @allure.title('[API] Добавление сотрудников на ветку safe_life')
    def test_filling_add_staff_safe_life(self):
        for i in range(5):
            Request(method='post',
                    endpoint='/api/v1/employee?_dc=' + time_now + '&filter=%5B%7B%22property%22%3A%22liveSe'
                                                                  'arch%22%2C%22value%22%3A%22%22%7D%5D',
                    template='staff',
                    name='Добавление сотрудников SafeLife',
                    surname='SafeLife',
                    name_staff=NAME_STAFF[i],
                    patronymic=NAME_STAFF[i],
                    position='SafeLife' + NAME_STAFF[i],
                    email_domain='niisokb',
                    email_login='SafeLife_' + NAME_STAFF[i],
                    email='SafeLife_' + NAME_STAFF[i] + '@niisikb.ru',
                    staff_number=int(shared_vars.COMMON_VAR["id_oss_safe_life"])) \
                .fire()

    @allure.title('[API] Добавление всех кодов сотрудников')
    def test_filling_add_loaders(self):
        Request(method='post',
                endpoint='/api/v1/bootstrap/codes?validTill=' + time_now + '&ownership=corporate&deviceManagementStrate'
                                                                           'gy=auto&depId=-1&isRecursive=true',
                name='Добавление Загрузчика') \
            .fire()

    @allure.title('[API] Подключение к серверам')
    def test_filling_connection_to_server(self):
        for i in range(5):
            Request(method='put',
                    endpoint='/api/v1/server-connection/' + str(ID_CONNECT[i]) + '?_dc=' + time_now,
                    template='connecting_to_server',
                    id_server=int(ID_CONNECT[i]),
                    server_type=SERVER_TYPE[i],
                    url_server=URL_SERVER[i],
                    name='Подключение к серверам') \
                .fire()

    @allure.title('[API] Добавление профиля Настройки монитора Android без ключа KNOX')
    def test_filling_add_profile_1(self):
        profile_android = Request(method='post',
                                  endpoint='/api/v1/profile?_dc=' + time_now,
                                  template='profiles_android_monitor_settings5_0',
                                  name_profile='Настройки монитора Android без ключа KNOX',
                                  key_knox='',
                                  name='Сохранение профиля Настройки монитора Android без ключа KNOX') \
            .fire()

        shared_vars.COMMON_VAR["id_profile"] = profile_android

    @allure.title('[API] Назначение профиля Настройки монитора Android без ключа KNOX на сотрудников Android ')
    def test_filling_purpose_profile_2(self):
        for personal in shared_vars.COMMON_VAR["id_staff_android"]:
            Request(method='put',
                    endpoint='/api/v1/profile/' + str(shared_vars.COMMON_VAR["id_profile"].response.json()["data"]
                                                      ["id"]) + '/assignment/',
                    template='profile_personal_put',
                    id=int(personal.response.json()["id"]),
                    name='Назначение профиля Настройки монитора Android без ключа KNOX на сотрудников Android') \
                .fire()

    @allure.title('[API] Добавление профиля Настройки монитора Android с ключом KNOX')
    def test_filling_add_profile_3(self):
        Request(method='post',
                endpoint='/api/v1/profile?_dc=' + time_now,
                template='profiles_android_monitor_settings5_0',
                name_profile='Настройки монитора Android с ключом KNOX',
                key_knox='KLM09-N5C61-H0DS6-10JQD-QUAAB-DDQXU',
                name='Сохранение профиля Настройки монитора Android с ключом KNOX') \
            .fire()

    @allure.title('[API] Добавление профиля Парольные политики Android')
    def test_filling_add_profile_4(self):
        Request(method='post',
                endpoint='/api/v1/profile?_dc=' + time_now,
                template='profiles_android_password_policies',
                name_profile='Парольные политики Android',
                name='Сохранение профиля Парольные политики Android') \
            .fire()

    @allure.title('[API] Добавление профиля Защита устройства от угроз Android без ключа')
    def test_filling_add_profile_5(self):
        profile_android = Request(method='post',
                                  endpoint='/api/v1/profile?_dc=' + time_now,
                                  template='profiles_protecting_your_device_from_android_threats',
                                  name_profile='Защита устройства от угроз Android без ключа',
                                  key='',
                                  name='Сохранение профиля Защита устройства от угроз Android без ключа') \
            .fire()

        shared_vars.COMMON_VAR["id_profile"] = profile_android

    @allure.title('[API] Назначение профиля Защита устройства от угроз Android без ключа на сотрудников Android ')
    def test_filling_purpose_profile_6(self):
        for personal in shared_vars.COMMON_VAR["id_staff_android"]:
            Request(method='put',
                    endpoint='/api/v1/profile/' + str(shared_vars.COMMON_VAR["id_profile"].response.json()["data"]
                                                      ["id"]) + '/assignment/',
                    template='profile_personal_put',
                    id=int(personal.response.json()["id"]),
                    name='Назначение профиля Защита устройства от угроз Android без ключа на сотрудников Android') \
                .fire()

    @allure.title('[API] Добавление профиля Защита устройства от угроз Android с ключом')
    def test_filling_add_profile_7(self):
        Request(method='post',
                endpoint='/api/v1/profile?_dc=' + time_now,
                template='profiles_protecting_your_device_from_android_threats',
                name_profile='Защита устройства от угроз Android с ключом',
                key='1JXRM-2J4UG-KGB8H-S3DPN',
                name='Сохранение профиля Защита устройства от угроз Android с ключом') \
            .fire()

    @allure.title('[API] Добавление профиля Режим киоска Android')
    def test_filling_add_profile_8(self):
        Request(method='post',
                endpoint='/api/v1/profile?_dc=' + time_now,
                template='profiles_android_kiosk_mode',
                name='Сохранение профиля Режим киоска Android') \
            .fire()

    @allure.title('[API] Добавление профиля Режим киоска Samsung Knox Android')
    def test_filling_add_profile_9(self):
        Request(method='post',
                endpoint='/api/v1/profile?_dc=' + time_now,
                template='profiles_samsung_knox_android_kiosk_mode',
                name='Сохранение профиля Режим киоска Samsung Knox Android') \
            .fire()

    @allure.title('[API] Добавление профиля Политики ограничений Android')
    def test_filling_add_profile_10(self):
        Request(method='post',
                endpoint='/api/v1/profile?_dc=' + time_now,
                template='profiles_android_restriction_policies',
                name_profile='Политики ограничений Android',
                name='Сохранение профиля Политики ограничений Android') \
            .fire()

    @allure.title('[API] Добавление профиля Политики ограничений Samsung Knox Android')
    def test_filling_add_profile_11(self):
        Request(method='post',
                endpoint='/api/v1/profile?_dc=' + time_now,
                template='profiles_samsung_knox_android_restriction_policies',
                name_profile='Политики ограничений Samsung Knox Android',
                name='Сохранение профиля Политики ограничений Samsung Knox Android') \
            .fire()

    @allure.title('[API] Добавление профиля Политики ограничений ОС Аврора')
    def test_filling_add_profile_12(self):
        Request(method='post',
                endpoint='/api/v1/profile?_dc=' + time_now,
                template='profiles_aurora_os_restriction_policies',
                name='Сохранение профиля Политики ограничений ОС Аврора') \
            .fire()

    @allure.title('[API] Добавление профиля Настройки браслета SafeLife')
    def test_filling_add_profile_13(self):
        Request(method='post',
                endpoint='/api/v1/profile?_dc=' + time_now,
                template='profiles_safeLife_bracelet_settings',
                name='Сохранение профиля Настройки браслета SafeLife') \
            .fire()

    @allure.title('[API] Добавление профиля Настройки монитора iOS')
    def test_filling_add_profile_14(self):
        profile_ios = Request(method='post',
                              endpoint='/api/v1/profile?_dc=' + time_now,
                              template='profiles_ios_monitor_settings',
                              name='Сохранение профиля Настройки монитора iOS') \
            .fire()

        shared_vars.COMMON_VAR["id_profile"] = profile_ios

    @allure.title('[API] Назначение профиля Настройки монитора iOS')
    def test_filling_purpose_profile_15(self):
        for personal in shared_vars.COMMON_VAR["id_staff_ios"]:
            Request(method='put',
                    endpoint='/api/v1/profile/' + str(shared_vars.COMMON_VAR["id_profile"].response.json()["data"]
                                                      ["id"]) + '/assignment/',
                    template='profile_personal_put',
                    id=int(personal.response.json()["id"]),
                    name='Назначение профиля Настройки монитора iOS') \
                .fire()

    @allure.title('[API] Добавление профиля Парольные политики iOS')
    def test_filling_add_profile_16(self):
        Request(method='post',
                endpoint='/api/v1/profile?_dc=' + time_now,
                template='profiles_ios_password_policies',
                name_profile='Парольные политики iOS',
                name='Сохранение профиля Парольные политики iOS') \
            .fire()

    @allure.title('[API] Добавление профиля Режим киоска iOS')
    def test_filling_add_profile_17(self):
        Request(method='post',
                endpoint='/api/v1/profile?_dc=' + time_now,
                template='profiles_ios_kiosk_mode',
                name='Сохранение профиля Режим киоска iOS') \
            .fire()

    @allure.title('[API] Добавление профиля Политики ограничений Windows')
    def test_filling_add_profile_18(self):
        Request(method='post',
                endpoint='/api/v1/profile?_dc=' + time_now,
                template='profiles_windows_restriction_policies',
                name='Сохранение профиля Политики ограничений Windows') \
            .fire()

    @allure.title('[API] Добавление профиля Политики использования камеры Windows')
    def test_filling_add_profile_19(self):
        Request(method='post',
                endpoint='/api/v1/profile?_dc=' + time_now,
                template='profiles_windows_camera_usage_policies',
                name='Сохранение профиля Политики использования камеры Windows') \
            .fire()

    @allure.title('[API] Добавление профиля Настройки bluetooth Windows')
    def test_filling_add_profile_20(self):
        Request(method='post',
                endpoint='/api/v1/profile?_dc=' + time_now,
                template='profiles_windows_bluetooth_settings',
                name='Сохранение профиля Настройки bluetooth Windows') \
            .fire()

    @allure.title('[API] Добавление Календаря')
    def test_filling_add_calender(self):
        Request(method='post',
                endpoint='/api/v1/schedule/rule/create-and-bind/unit/-1',
                template='calender_week',
                name='Добавление календаря на неделю',
                name_calender='Календарь_' + time1,
                time_start=time_start,
                time_end=time_end) \
            .fire()

    @allure.title('[API] Добавление геолокации НИИ СОКБ')
    def test_filling_add_geolocation_niisokb(self):
        geolocation = Request(method='post',
                              endpoint='/api/v1/geofence?_dc=' + time_now,
                              template='geolocation_niisokb',
                              name_geolocation='НИИ СОКБ',
                              name='Добавление геолокации НИИ СОКБ') \
            .fire()

        shared_vars.COMMON_VAR["geolocation"] = geolocation

    @allure.title('[API] Активация геолокации НИИ СОКБ')
    def test_filling_activation_geolocation_niisokb(self):
        Request(method='put',
                endpoint='/api/v1/geofence/' +
                         str(shared_vars.COMMON_VAR["geolocation"].response.json()["data"]["id"]) + '/activate',
                name='Добавление геолокации НИИ СОКБ') \
            .fire()

    @allure.title('[API] Добавление геолокации ГБОУ школа №15 дошкольный корпус 1')
    def test_filling_add_geolocation_schoolmini_15_1(self):
        geolocation = Request(method='post',
                              endpoint='/api/v1/geofence?_dc=' + time_now,
                              template='geolocation_school_15_1',
                              name_geolocation='ГБОУ школа №15 дошкольный корпус 1',
                              name='Добавление геолокации ГБОУ школа №15 дошкольный корпус 1') \
            .fire()

        shared_vars.COMMON_VAR["geolocation"] = geolocation

    @allure.title('[API] Активация геолокации ГБОУ школа №15 дошкольный корпус 1')
    def test_filling_activation_geolocation_schoolmini_15_1(self):
        Request(method='put',
                endpoint='/api/v1/geofence/' +
                         str(shared_vars.COMMON_VAR["geolocation"].response.json()["data"]["id"]) + '/activate',
                name='Добавление геолокации НИИ СОКБ') \
            .fire()

    @allure.title('[API] Добавление геолокации Smart Park')
    def test_filling_add_geolocation_smartpark(self):
        geolocation = Request(method='post',
                              endpoint='/api/v1/geofence?_dc=' + time_now,
                              template='geolocation_smartpark',
                              name_geolocation='Smart Park',
                              name='Добавление геолокации Smart Park') \
            .fire()

        shared_vars.COMMON_VAR["geolocation"] = geolocation

    @allure.title('[API] Активация геолокации Smart Park')
    def test_filling_activation_geolocation_smartpark(self):
        Request(method='put',
                endpoint='/api/v1/geofence/' +
                         str(shared_vars.COMMON_VAR["geolocation"].response.json()["data"]["id"]) + '/activate',
                name='Добавление геолокации Smart Park') \
            .fire()

    @allure.title('[API] Добавление пользовательского соглашения')
    def test_filling_add_user_agreement(self):
        Request(method='post',
                endpoint='/api/v1/agreement',
                template='user_agreement',
                name='Добавление пользовательского соглашения',
                text='Пожалуйста, примите пользовательское соглашение!') \
            .fire()

    @allure.title('[API] Добавление роли')
    def test_filling_add_role(self):
        Request(method='post',
                endpoint='/api/v1/roles/',
                template='role_name',
                role_name=NAME_ROLE,
                name='Добавление роли') \
            .fire()

    @allure.title('[API] Просмотр списка ролей')
    def test_filling_get_role(self):
        role = Request(method='get',
                       endpoint='/api/v1/roles?_dc=' + time_now,
                       name='Добавление роли') \
            .fire()

        for i in json.loads(role.response.text)["data"]:
            if i["name"] == NAME_ROLE:
                shared_vars.COMMON_VAR["id_role"] = i["id"]

    @allure.title('[API] Добавление полномочий')
    def test_filling_add_privileges(self):
        Request(method='post',
                endpoint='/api/v1/roles/' + str(shared_vars.COMMON_VAR["id_role"]) + '/privileges/change',
                template='privileges_all',
                name='Добавление полномочий') \
            .fire()

    @allure.title('[API] Добавление администратора')
    def test_filling_add_admin(self):
        Request(method='post',
                endpoint='/api/v1/admin',
                template='admin',
                role_id=int(shared_vars.COMMON_VAR["id_role"]),
                name='Добавление администратора') \
            .fire()

    @allure.title('[API] Добавление роли Safe Life')
    def test_filling_add_role_safe_life(self):
        Request(method='post',
                endpoint='/api/v1/roles/',
                template='role_name',
                role_name='SafeLife',
                name='Добавление роли') \
            .fire()

    @allure.title('[API] Просмотр списка ролей')
    def test_filling_get_role_safe_life(self):
        role = Request(method='get',
                       endpoint='/api/v1/roles?_dc=' + time_now,
                       name='Добавление роли') \
            .fire()

        for i in json.loads(role.response.text)["data"]:
            if i["name"] == 'SafeLife':
                shared_vars.COMMON_VAR["id_role"] = i["id"]

    @allure.title('[API] Добавление полномочий SafeLife')
    def test_filling_add_privileges_safe_life(self):
        Request(method='post',
                endpoint='/api/v1/roles/' + str(shared_vars.COMMON_VAR["id_role"]) + '/privileges/change',
                template='privileges_safe_life',
                name='Добавление полномочий') \
            .fire()

    @allure.title('[API] Добавление администратора SafeLife')
    def test_filling_add_admin_safe_life(self):
        Request(method='post',
                endpoint='/api/v1/admin',
                template='admin_safe_life',
                role_id=int(shared_vars.COMMON_VAR["id_role"]),
                name='Добавление администратора') \
            .fire()

    @allure.title('[API] Добавление Операционной системы Android 11')
    def test_filling_add_os_android11(self):
        Request(method='post',
                endpoint='/api/v1/os',
                template='operating_systems',
                platform='Android',
                id=2,
                version_name="11",
                name='Добавление Операционной системы Android 11') \
            .fire()

    @allure.title('[API] Добавление Операционной системы Android 12')
    def test_filling_add_os_android12(self):
        Request(method='post',
                endpoint='/api/v1/os',
                template='operating_systems',
                platform='Android',
                id=2,
                version_name="12",
                name='Добавление Операционной системы Android 12') \
            .fire()

    @allure.title('[API] Добавление Операционной системы Android 13')
    def test_filling_add_os_android13(self):
        Request(method='post',
                endpoint='/api/v1/os',
                template='operating_systems',
                platform='Android',
                id=2,
                version_name="13",
                name='Добавление Операционной системы Android 13') \
            .fire()

    @allure.title('[API] Добавление Операционной системы iPhone OS 14.8.1')
    def test_filling_add_os_ios14(self):
        Request(method='post',
                endpoint='/api/v1/os',
                template='operating_systems',
                platform='iPhone OS',
                id=1,
                version_name="14.8.1",
                name='Добавление Операционной системы iPhone OS 14.8.1') \
            .fire()

    @allure.title('[API] Добавление Операционной системы iPhone OS 15.1')
    def test_filling_add_os_ios15(self):
        Request(method='post',
                endpoint='/api/v1/os',
                template='operating_systems',
                platform='iPhone OS',
                id=1,
                version_name="15.1",
                name='Добавление Операционной системы iPhone OS 15.1') \
            .fire()

    @allure.title('[API] Добавление всех комплектов сотрудников узла android')
    def test_filling_kits(self):
        for kits in shared_vars.COMMON_VAR["id_staff_android"]:
            Request(method='post',
                    endpoint='/api/v1/kit/add',
                    template='kit',
                    emp_id=int(kits.response.json()["id"]),
                    name='Добавление всех комплектов сотрудников узла android') \
                .fire()
