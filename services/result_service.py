EXAMS = [
    "SSC",
    "HSC",
    "Dakhil",
    "Alim",
]


def get_exam_list():
    return EXAMS


def is_supported_exam(exam):
    return exam in EXAMS


def future_result_sheet():
    return False


def future_university():
    return False
