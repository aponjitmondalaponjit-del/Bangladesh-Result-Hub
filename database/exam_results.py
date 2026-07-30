RESULTS = {}


def save_result(exam, data):
    RESULTS[exam] = data


def get_result(exam):
    return RESULTS.get(exam)


def result_available(exam):
    return exam in RESULTS


def delete_result(exam):
    RESULTS.pop(exam, None)


def all_results():
    return RESULTS.values()
