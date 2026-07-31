from providers.educationboard import get_education_result
from providers.madrasaboard import get_madrasa_result
from providers.technicalboard import get_technical_result


def get_result(exam, board, roll, registration):
    exam = exam.lower()

    if exam in ["ssc", "hsc"]:
        return get_education_result(
            exam,
            board,
            roll,
            registration,
        )

    if exam in ["dakhil", "alim"]:
        return get_madrasa_result(
            exam,
            board,
            roll,
            registration,
        )

    return get_technical_result(
        exam,
        board,
        roll,
        registration,
    )
