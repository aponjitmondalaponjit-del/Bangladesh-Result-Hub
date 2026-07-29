FAQ = {
    "hello": "Hello! How can we help you?",
    "result": "Please select an exam from the Result menu.",
}


def auto_reply(message):
    return FAQ.get(message.lower())


def create_ticket(user_id):
    return {
        "user_id": user_id,
        "status": "open",
    }


def ticket_status(ticket):
    return ticket["status"]
