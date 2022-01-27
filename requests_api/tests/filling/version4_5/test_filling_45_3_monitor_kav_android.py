import time
import shared_vars
import allure
import pytest

from allure_commons.types import Severity
from requests_api.core.request import Request


time_now = str(int(time.time()) * 1000 + 999)


@pytest.mark.filling
@pytest.mark.usefixtures("start_session")
@pytest.mark.skipif(shared_vars.APPLICATION_PROPERTIES["stand_version"] != "4.5", reason="version is not 4.5")
@allure.title('[API] Добавление приложения Monitor-4.5.2.0-kav')
@allure.severity(Severity.MINOR)
@allure.feature('[API] Добавление приложения Monitor')
@allure.description('[API] Добавление приложения Monitor')
class TestFillingMonitorKAVAndroid:

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

    @allure.title('[API] Добавление приложения Monitor')
    def test_filling_upload_application_3(self):
        upload_response = Request(method='post',
                                  endpoint='/api/v1/application/upload',
                                  name='Запрос на загрузку файла приложения Monitor',
                                  files={"name": "application",
                                         "content-type": "application/vnd.android.package-archive",
                                         "path": "Monitor-4.5.2.0-kav-release.apk"}) \
            .fire()

        shared_vars.COMMON_VAR = upload_response

    @allure.title('[API] Сохранение приложения Monitor')
    def test_filling_save_application_3(self):
        Request(method='post',
                endpoint='/api/v1/application',
                name='Сохранение файла приложения Monitor',
                body=shared_vars.COMMON_VAR.response.json()["data"]) \
            .fire()

    @allure.title('[API] Просмотр списка приложений')
    def test_filling_get_applications_3(self):
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
                    if application["version"] == "4.5.2.0-kav":
                        shared_vars.COMMON_VAR = application["id"]
                        return

    @allure.title('[API] Добавление ПУП для Monitor')
    def test_filling_add_pyp_monitor_kav_android(self):

        Request(method='post',
                endpoint='/api/v1/app-rule?_dc=' + time_now + '&liveSearch=',
                template='monitor_android',
                title='Monitor-4.5.2.0-kav',
                app_version='4.5.2.0-kav',
                app_id=shared_vars.COMMON_VAR,
                name='Добавление ПУП для Monitor') \
            .fire()
