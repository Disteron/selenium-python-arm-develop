import time
import allure
import pytest
import shared_vars

from allure_commons.types import Severity
from requests_api.core.request import Request


time_now = str(int(time.time()) * 1000 + 999)


@pytest.mark.id_7
@pytest.mark.api
@pytest.mark.smoke
@pytest.mark.regres
@pytest.mark.incremental
@pytest.mark.usefixtures("start_session")
@allure.title('[API] Проверка профиля')
@allure.severity(Severity.MINOR)
@allure.feature('[API] Профиль')
@allure.description('[API] Проверка добавления, назначения, удаления профиля '
                    'Парольные политики контейнера Samsung Knox Android')
class TestSamsungKnoxAndroidContainerPasswordPolicies:

    @allure.title('[API] Открытие Сессии')
    def test_open_session(self):
        api_user = shared_vars.APPLICATION_PROPERTIES["api_user"]
        api_password = shared_vars.APPLICATION_PROPERTIES["api_password"]

        Request(method='post',
                endpoint='/login',
                template='auth',
                name='Авторизация',
                api_user=api_user,
                api_password=api_password) \
            .fire()

    @allure.title('[API] Сохранение профиля Парольные политики контейнера Samsung Knox Android')
    def test_add_profile_samsung_knox_android_container_password_policies(self):
        id_profile = Request(method='post',
                             endpoint='/api/v1/profile?_dc=' + time_now,
                             template='profiles_samsung_knox_android_container_password_policies',
                             name_profile='Парольные политики контейнера Samsung Knox Android',
                             name='Сохранение профиля Парольные политики контейнера Samsung Knox Android', ) \
            .fire()

        shared_vars.COMMON_VAR = id_profile

    @allure.title('[API] Назначение профиля Парольные политики контейнера Samsung Knox Android на ветку root')
    def test_purpose_profile_samsung_knox_android_container_password_policies(self):
        Request(method='put',
                endpoint='/api/v1/profile/' +
                         str(shared_vars.COMMON_VAR.response.json()["data"]["id"]) + '/assignment/',
                template='profile_root_put',
                name='Назначение профиля Парольные политики контейнера Samsung Knox Android на ветку root') \
            .fire()

    @allure.title('[API] Удаление профиля Парольные политики контейнера Samsung Knox Android')
    def test_delete_profile_samsung_knox_android_container_password_policies(self):
        Request(method='delete',
                endpoint='/api/v1/profile/' +
                         str(shared_vars.COMMON_VAR.response.json()["data"]["id"]) + '?_dc=' + time_now,
                name='Удаление профиля Парольные политики контейнера Samsung Knox Android')\
            .fire()
