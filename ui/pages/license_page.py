from ui.pages.base_page import BasePage


class LicensePage(BasePage):
    """
    Страница Лицензия
    """
    BUTTON_1 = {"name": "Поле ввода лицензии",
                "xpath": "//textarea[@name='token']"}

    BUTTON_2 = {"name": "Сохранить",
                "xpath": "//div[contains(@id, 'license-form')]//span[text()='Сохранить']"}

    BUTTON_3 = {"name": "Срок действия лицензии",
                "xpath": "//div[contains(text(), 'Лицензия для ООО НИИ СОКБ на 1') "
                         "and contains(text(), '000 устройств(а) действует с 31.12.2021 по 31.12.2022')]"}

    BUTTON_4 = {"name": "Целостность лицензии",
                "xpath": "//label[contains(@id, 'label-') "
                         "and contains(text(), 'Возможно, нарушена целостность лицензии.')]"}
