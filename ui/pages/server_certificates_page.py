from ui.pages.base_page import BasePage


class ServerCertificates(BasePage):
    """
    Страница Серверные сертификаты
    """
    BUTTON_1 = {"name": "Загрузить файл",
                "xpath": "//div[contains(@id, 'sp-server-cert-form-')]//input[@name='cert_file']"}

    BUTTON_2 = {"name": "Наименование",
                "xpath": "//div[contains(@id, 'sp-server-cert-form-')]//input[@name='cert_title']"}

    BUTTON_3 = {"name": "Сохранить",
                "xpath": "(//div[contains(@id, 'ext-comp-')]//span[text()='Сохранить'])[1]"}

    BUTTON_4 = {"name": "Удалить",
                "xpath": "(//div[contains(@id, 'ext-comp-')]//span[text()='Удалить'])[1]"}

    BUTTON_5 = {"name": "Да",
                "xpath": "//div[contains(@id, 'messagebox-')]//span[text()='Да']/.."}

    BUTTON_6 = {"name": "ca_pem",
                "xpath": "//div[contains(@id, 'sp-certgrid-')]//div[text()='ca.pem_{random}']"}

    BUTTON_7 = {"name": "Сортировка",
                "xpath": "(//div[contains(@id, 'sp-certgrid-')]"
                         "//span[text()='{text}'])[1]"}
