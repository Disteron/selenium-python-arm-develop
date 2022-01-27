import json
import os
import re

import allure

import shared_vars

from datetime import datetime


class Request:
    def __init__(self, method, endpoint, template=None, body=None, data=None, name=None, files=None, headers=None, **kwargs):
        """Класс, реализующий логику запроса, а именно -
        - создание, выполнение, проверка ответа, логирование(allure, печать в console)

        :param method: метод запроса (get, post ...etc)
        :param endpoint: эндпоинт хоста (сервера) на какой ресурс сходить

        Используются для отправки в теле запроса (post, delete, put)
        :param template: название шаблона из папки json_bodies (в **kwargs передаются поля для замены)
        :param body: готовый json объект для отправки в теле
        :param data: словарь, список кортежей, байтов или файловый (то есть не обязательно json)

        :param name: название запроса (например, запрос на авторизацию)
        :param files: используется для передачи файла в запросе (post)
        :param headers: заголовки HTTP запроса или ответа
        :param kwargs: параметры для вставки значений в template
        """

        self.session = shared_vars.SESSION
        self.host = 'https://' + shared_vars.APPLICATION_PROPERTIES["host"] + ':8443'
        self.url = self.host + endpoint
        self.method = method.lower()
        self.kwargs = kwargs
        self.body = body
        if body is None and template is not None:
            self.body = open(os.path.join(shared_vars.PROJECT_ROOT, "requests_api", "json_bodies", template + ".json"),
                             encoding='UTF-8').read()
            for key, value in self.kwargs.items():
                self.body = self.body.replace('%' + key, str(value))
            self.body = json.loads(self.body)
        self.name = name
        self.data = data
        self.files = None
        if files is not None:
            with open(os.path.join(shared_vars.PROJECT_ROOT, "requests_api", "files", files["path"]), 'rb') as f:
                self.files = {files["name"]: (files["path"], f.read(), files["content-type"])}
                if "password" in files:
                    self.files["password"] = files["password"]
        self.headers = {'Content-type': 'application/json'} if not headers else headers
        self.response = None

    def fire(self):
        """Метод исполняет запрос типа "get", "post" или "delete".

        Returns:
            self: возвращает объект класса со всеми полями.
        """
        self.print_log()
        if self.method == 'get':
            self.response = self.session.get(url=self.url,
                                             verify=False)
        elif self.method == 'post':
            self.response = self.session.post(url=self.url,
                                              verify=False,
                                              json=self.body,
                                              data=self.data,
                                              files=self.files,
                                              headers=self.headers if not self.files else None)
        elif self.method == 'put':
            self.response = self.session.put(url=self.url,
                                             verify=False,
                                             json=self.body,
                                             headers=self.headers)
        else:
            self.response = self.session.delete(url=self.url,
                                                verify=False,
                                                json=self.body,
                                                headers=self.headers)
        self.print_result()
        self.check_result()

        return self

    def print_log(self):
        """Метод выводит информацию о запросе.
        """
        print_body = "{}"
        if self.body is not None and not issubclass(type(self.body), dict) and not issubclass(type(self.body), list):
            print_body = json.dumps(json.loads(self.body), indent=4, sort_keys=True)
        elif self.body and (issubclass(type(self.body), dict) or issubclass(type(self.body), list)):
            print_body = json.dumps(self.body, indent=4, sort_keys=True)

        log = f'\nRequest  ({datetime.today().time()}):' \
              f'\nname - {self.name}' \
              f'\nmethod - {self.method}' \
              f'\nurl - {self.url}' \
              f'\nbody:\n{print_body}\n'
        with allure.step(f"Запрос\n{log}"):
            print(log)

    def print_result(self):
        """Метод выводит результат запроса.
        """
        if 'content-type' in self.response.headers and self.response.headers['content-type'].find('application/json') == 0:
            with allure.step(f"Результат запроса: Status code - {self.response.status_code}\n"
                             f"Response Body:\n{json.dumps(self.response.json(), indent=4, sort_keys=True)}"):
                print(f'Status code - {self.response.status_code}')
                print(f'Response Body:\n{json.dumps(self.response.json(), indent=4, sort_keys=True)}')
        else:
            with allure.step(f"Результат запроса: Status code - {self.response.status_code}"):
                print(f"method - {self.method}\n" +
                      f"url - {self.url}\n" +
                      f"status code - {self.response.status_code}")

    def check_result(self):
        """Метод проверяет результат запроса.
        """
        msg_error = "Неуспешный ответ от сервера" + " - " + str(self.response.status_code)
        response_json = None

        if 'content-type' in self.response.headers and self.response.headers['content-type'].find('application/json') == 0:
            response_json = self.response.json()
        with allure.step(f"Проверка результата запроса: \n" +
                         f"method - {self.method}" +
                         f"url - {self.url}" +
                         f"status code - {self.response.status_code}"):

            if self.method == "get":
                assert self.response.status_code == 200, msg_error
            elif response_json and "success" in response_json:
                assert response_json["success"] is True, msg_error
            elif response_json and "status" in response_json:
                assert response_json["status"] == "OK" or "CHANGE_PASSWORD", msg_error
            elif self.response.status_code == 200 or 201:
                return
            else:
                raise RuntimeError(msg_error)

        if bool(re.fullmatch(r'[45]\d{2}', str(self.response.status_code))):
            raise RuntimeError(msg_error)
