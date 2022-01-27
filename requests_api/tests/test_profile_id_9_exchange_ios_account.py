import time
import allure
import pytest
import shared_vars

from allure_commons.types import Severity
from requests_api.core.request import Request


time_now = str(int(time.time()) * 1000 + 999)


@pytest.mark.id_9
@pytest.mark.api
@pytest.mark.smoke
@pytest.mark.regres
@pytest.mark.incremental
@pytest.mark.usefixtures("start_session")
@allure.title('[API] Проверка профиля')
@allure.severity(Severity.MINOR)
@allure.feature('[API] Профиль')
@allure.description('[API] Проверка добавления, назначения, удаления профиля Exchange аккаунт iOS')
class TestExchangeIOSAccount:

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

    @allure.title('[API] Сохранение профиля Exchange аккаунт iOS')
    def test_add_profile_exchange_ios_account(self):
        id_profile = Request(method='post',
                             endpoint='/api/v1/profile?_dc=' + time_now,
                             template='profiles_exchange_ios_account',
                             name_profile='Exchange аккаунт iOS',
                             ip_value='https://' + str(shared_vars.APPLICATION_PROPERTIES),
                             name='Сохранение профиля Exchange аккаунт iOS') \
            .fire()

        shared_vars.COMMON_VAR = id_profile

    @allure.title('[API] Назначение профиля Exchange аккаунт iOS')
    def test_purpose_profile_exchange_ios_account(self):
        Request(method='put',
                endpoint='/api/v1/profile/' +
                         str(shared_vars.COMMON_VAR.response.json()["data"]["id"]) + '/assignment/',
                template='profile_root_put',
                name='Назначение профиля Exchange аккаунт iOS') \
            .fire()

    @allure.title('[API] Удаление профиля Exchange аккаунт iOS')
    def test_delete_profile_exchange_ios_account(self):
        Request(method='delete',
                endpoint='/api/v1/profile/' +
                         str(shared_vars.COMMON_VAR.response.json()["data"]["id"]) + '?_dc=' + time_now,
                name='Удаление профиля Exchange аккаунт iOS')\
            .fire()
