from ui.pages.base_page import BasePage


class OwnerDelegationPage(BasePage):
    """
    Разделы Владелец и Делегирование
    """

    BUTTON_1 = {"name": "Владелец плюс root",
                "xpath": "//div[contains(@id, 'sp-common-ownerpanel-')]//span[text()='root']//.."
                         "//img[contains(@class, 'x-tree-expander')]"}

    BUTTON_2 = {"name": "Владелец плюс отдел тестирования",
                "xpath": "//div[contains(@id, 'sp-common-ownerpanel-')]"
                         "//span[text()='Отдел тестирования_{random}']//..//img[contains(@class, 'x-tree-expander')]"}

    BUTTON_3 = {"name": "Владелец ошс отдел тестирования",
                "xpath": "//div[contains(@id, 'sp-common-ownerpanel-')]//"
                         "span[text()='Отдел тестирования_{random}']//..//img[contains(@class, 'x-tree-icon')]"}

    BUTTON_4 = {"name": "Владелец отменить",
                "xpath": "//div[contains(@id, 'sp-common-ownerpanel-')]//span[text()='Отменить']"}

    BUTTON_5 = {"name": "Владелец сохранить",
                "xpath": "//div[contains(@id, 'sp-common-ownerpanel-')]//span[text()='Сохранить']"}

    BUTTON_6 = {"name": "Делегирование android",
                "xpath": "//div[contains(@id, 'sp-common-delegationpanel-')]"
                         "//span[text()='Android_{random}']//..//img[contains(@class, 'x-tree-icon')]"}

    BUTTON_7 = {"name": "Делегирование финансовый отдел",
                "xpath": "//div[contains(@id, 'sp-common-delegationpanel-')]"
                         "//span[text()='Финансовый отдел_{random}']//..//img[contains(@class, 'x-tree-icon')]"}

    BUTTON_8 = {"name": "Делегирование отдел тестирования",
                "xpath": "//div[contains(@id, 'sp-common-delegationpanel-')]"
                         "//span[text()='Отдел тестирования_{random}']//..//img[contains(@class, 'x-tree-icon')]"}

    BUTTON_9 = {"name": "Делегирование отменить",
                "xpath": "//div[contains(@id, 'sp-common-delegationpanel-')]//span[text()='Отменить']"}

    BUTTON_10 = {"name": "Делегирование сохранить",
                 "xpath": "//div[contains(@id, 'sp-common-delegationpanel-')]"
                          "//span[text()='Сохранить' and contains(@class, 'x-btn-inner-center')]"}
