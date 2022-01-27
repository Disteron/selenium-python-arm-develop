import time

import requests

from datetime import datetime


HEADERS = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": "Bearer wLDwd3uKg8jn6GwD7oIeFV9MuRE",
}


def after_pytest_report_on_miro(terminalreporter, config):
    passed = len(terminalreporter.stats['passed']) if 'passed' in terminalreporter.stats else "0"
    failed = len(terminalreporter.stats['failed']) if 'failed' in terminalreporter.stats else "0"
    skipped = len(terminalreporter.stats['skipped']) if 'skipped' in terminalreporter.stats else "0"
    xfailed = len(terminalreporter.stats['xfailed']) if 'xfailed' in terminalreporter.stats else "0"
    xpass = len(terminalreporter.stats['xpass']) if 'xpass' in terminalreporter.stats else "0"
    deselected = len(terminalreporter.stats['deselected']) if 'deselected' in terminalreporter.stats else "0"
    session_start_time = terminalreporter._sessionstarttime
    date_time_start = str(datetime.fromtimestamp(session_start_time).strftime("%Y-%m-%d %H:%M:%S"))
    duration = time.time() - session_start_time
    markexpr_ = config.option.markexpr if config.option.markexpr != '' else '-'

    report = 'Дата/время начала тестового прогона: ' + date_time_start + '\n' + \
             'Тестовый набор: ' + markexpr_ + '\n' + \
             'passed amount: ' + str(passed) + '\n' + \
             'failed amount: ' + str(failed) + '\n' + \
             'xfailed amount: ' + str(xfailed) + '\n' + \
             'xpass amount: ' + str(xpass) + '\n' + \
             'skipped amount: ' + str(skipped) + '\n' + \
             'deselected amount: ' + str(deselected) + '\n' + \
             "Время прогона: " + str(float('{:.3f}'.format(duration))) + " сек"
    report = report.replace("_", "\\_").replace("*", "\\*").replace("[", "\\[").replace("`", "\\`")
    print(report)

    payload = {
        "text": date_time_start
    }
    requests.patch(url="https://api.miro.com/v1/boards/o9J_l2-noe0%3D/widgets/3074457362822926651",
                   json=payload,
                   headers=HEADERS)

    payload = {
        "title": "Время прогона: " + str(float('{:.3f}'.format(duration))) + " сек",
    }
    requests.patch(url="https://api.miro.com/v1/boards/o9J_l2-noe0%3D/widgets/3074457362822161643",
                   json=payload,
                   headers=HEADERS)

    failed_payload = {"text": str(failed)}
    requests.patch(url="https://api.miro.com/v1/boards/o9J_l2-noe0%3D/widgets/3074457362821557188",
                   json=failed_payload,
                   headers=HEADERS)

    passed_payload = {"text": str(passed)}
    requests.patch(url="https://api.miro.com/v1/boards/o9J_l2-noe0%3D/widgets/3074457362821597682",
                   json=passed_payload,
                   headers=HEADERS)

    skipped_payload = {"text": str(skipped)}
    requests.patch(url="https://api.miro.com/v1/boards/o9J_l2-noe0%3D/widgets/3074457362821598004",
                   json=skipped_payload,
                   headers=HEADERS)

    xfailed_payload = {"text": str(xfailed)}
    requests.patch(url="https://api.miro.com/v1/boards/o9J_l2-noe0%3D/widgets/3074457362823330962",
                   json=xfailed_payload,
                   headers=HEADERS)

    xpass_payload = {"text": str(xpass)}
    requests.patch(url="https://api.miro.com/v1/boards/o9J_l2-noe0%3D/widgets/3074457362823330966",
                   json=xpass_payload,
                   headers=HEADERS)

    deselected_payload = {"text": str(deselected)}
    requests.patch(url="https://api.miro.com/v1/boards/o9J_l2-noe0%3D/widgets/3074457362823549991",
                   json=deselected_payload,
                   headers=HEADERS)

    return report
