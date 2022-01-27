from ui.pages.base_page import BasePage


class ConnectionToServers(BasePage):
    """
    Страница Подключение к серверам
    """
    BUTTON_1 = {"name": "Сортировка(Тип сервера)",
                "xpath": "//div[contains(@id, 'sp-server-conn-grid-')]//span[text()='Тип сервера']"}

    BUTTON_2 = {"name": "Сортировка(URL)",
                "xpath": "//div[contains(@id, 'sp-server-conn-grid-')]//span[text()='URL']"}

    BUTTON_3 = {"name": "Сортировка(Сертификаты)",
                "xpath": "//div[contains(@id, 'sp-server-conn-grid-')]//span[text()='Сертификаты']"}

    BUTTON_4 = {"name": "Тип сервера(MDMServer)",
                "xpath": "//div[contains(@id, 'sp-server-conn-grid-')]//div[text()='MDMServer']"}

    BUTTON_5 = {"name": "Тип сервера(SCEPServer)",
                "xpath": "//div[contains(@id, 'sp-server-conn-grid-')]//div[text()='SCEPServer']"}

    BUTTON_6 = {"name": "Тип сервера(SocketServer)",
                "xpath": "//div[contains(@id, 'sp-server-conn-grid-')]//div[text()='SocketServer']"}

    BUTTON_7 = {"name": "Тип сервера(WinMDM Enrollment)",
                "xpath": "//div[contains(@id, 'sp-server-conn-grid-')]//div[text()='WinMDM Enrollment']"}

    BUTTON_8 = {"name": "Тип сервера(WinMDM Management)",
                "xpath": "//div[contains(@id, 'sp-server-conn-grid-')]//div[text()='WinMDM Management']"}

    BUTTON_9 = {"name": "Поле(URL)",
                "xpath": "//input[@name='server_connection_url']"}

    BUTTON_10 = {"name": "Сохранить",
                 "xpath": "//div[contains(@id, 'sp-serverconn-panel-')]//a[@class='x-btn x-unselectable x-btn-toolbar"
                          " x-box-item x-toolbar-item x-btn-default-toolbar-small x-icon-text-left x-btn-icon-text-left"
                          " x-btn-default-toolbar-small-icon-text-left']//span[text()='Сохранить']"}

    BUTTON_11 = {"name": "Необходимо загрузить серверный сертификат",
                 "xpath": "//div[contains(@id, 'sp-serverconn-panel-')]"
                          "//a[text()='Необходимо загрузить серверный сертификат']"}
