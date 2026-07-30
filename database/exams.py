EXAMS = {}


def add_exam(exam, data):
    EXAMS[exam] = data


def get_exam(exam):
    return EXAMS.get(exam)


def update_exam(exam, data):
    EXAMS[exam] = data


def all_exams():
    return EXAMS.values()


def exam_exists(exam):
    return exam in EXAMS


def remove_exam(exam):
    EXAMS.pop(exam, None)
