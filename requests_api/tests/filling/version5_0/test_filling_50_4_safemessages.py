import time
import shared_vars
import allure
import pytest

from allure_commons.types import Severity
from requests_api.core.request import Request


time_now = str(int(time.time()) * 1000 + 999)


@pytest.mark.filling
@pytest.mark.usefixtures("start_session")
@pytest.mark.skipif(shared_vars.APPLICATION_PROPERTIES["stand_version"] != "5.0", reason="version is not 5.0")
@allure.title('[API] Добавление приложения SafeMessages-2.7.5')
@allure.severity(Severity.MINOR)
@allure.feature('[API] Добавление приложения SafeMessages-2.7.5')
@allure.description('[API] Добавление приложения SafeMessages-2.7.5')
class TestFillingSafeMessages:

    @allure.title('[API] Открытие сессии')
    def test_filling_open_session(self):
        api_user = shared_vars.APPLICATION_PROPERTIES["api_user"]
        api_password = shared_vars.APPLICATION_PROPERTIES["api_password"]

        Request(method='post',
                endpoint='/login',
                template='auth',
                name='Авторизация',
                api_user=api_user,
                api_password=api_password) \
            .fire()

    @allure.title('[API] Добавление приложения SafeMessages-2.7.5')
    def test_filling_upload_application_6(self):
        upload_response = Request(method='post',
                                  endpoint='/api/v1/application/upload',
                                  name='Запрос на загрузку файла приложения Far Windows',
                                  files={"name": "application",
                                         "content-type": "application/vnd.android.package-archive",
                                         "path": "SafeMessages-2.7.5.apk"}) \
            .fire()

        shared_vars.COMMON_VAR = upload_response

    @allure.title('[API] Сохранение приложения SafeMessages-2.7.5')
    def test_filling_save_application_6(self):
        Request(method='post',
                endpoint='/api/v1/application',
                name='Сохранение файла приложения SafeMessages-2.7.5',
                body=shared_vars.COMMON_VAR.response.json()["data"]) \
            .fire()

    @allure.title('[API] Просмотр списка приложений')
    def test_filling_get_applications_6(self):
        end = time.time() + int(shared_vars.APPLICATION_PROPERTIES.get("timeout_api"))

        while end > time.time():
            time.sleep(1)
            applications = Request(method='get',
                                   endpoint='/api/v1/application',
                                   name='Просмотр приложений') \
                .fire()

            application_list = applications.response.json()["data"]

            if application_list:
                for application in application_list:
                    if application["name"] == "Messages":
                        shared_vars.COMMON_VAR = application["id"]
                        return

    @allure.title('[API] Добавление ПУП для SafeMessages-2.7.5')
    def test_filling_add_pyp_safemessages(self):
        Request(method='post',
                endpoint='/api/v1/app-rule?_dc=' + time_now + '&liveSearch=',
                template='safemessages',
                title='SafeMessages-2.7.5',
                app_id=shared_vars.COMMON_VAR,
                name='Добавление ПУП для SafeMessages-2.7.5') \
            .fire()
