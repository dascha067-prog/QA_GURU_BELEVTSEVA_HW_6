# Создать функцию отправки письма с базовой валидацией адресов и логикой выбора отправителя recipien
from tests.hw6_part_a import get_correct_email, check_empty_fields, clean_body_text, create_email, add_send_date, \
    extract_login_domain, mask_sender_email, add_short_body


def build_sent_text(email: dict) -> str:
    return f"""Кому: {email['recipient']}, от {email['sender']}
Тема: {email['subject']}, дата {email['date']}
{email['clean_body']}"""


def sender_email(recipient_list: list[str], subject: str, message: str, *, sender="default@study.com") -> list[dict]:
    # 1. список получателей не пуст
    if not recipient_list:
        return []

    # 2. валидирую адреса отправителя и получателей
    valid_sender = get_correct_email([sender])
    valid_recipients = get_correct_email(recipient_list)
    if not valid_sender or not valid_recipients:
        return []

    sender = valid_sender[0]

    # 3. тема и тело не пустые
    is_subject_empty, is_body_empty = check_empty_fields({"subject": subject, "body": message})
    if is_subject_empty or is_body_empty:
        return []

    # 4. исключаю отправку самому себе
    valid_recipients = [r for r in valid_recipients if r != sender]
    if not valid_recipients:
        return []

    # 5. нормализую текст (адреса мы уже нормализовали через get_correct_email)
    clean_subject = clean_body_text(subject)
    clean_body = clean_body_text(message)

    emails: list[dict] = []

    for r in valid_recipients:
        # 6. создаю базовое письмо
        email = create_email(sender=sender, recipient=r, subject=clean_subject, body=clean_body)

        # 7. добавляю дату
        email = add_send_date(email)

        # 8. маска отправителя
        login, domain = extract_login_domain(sender)
        email["masked_sender"] = mask_sender_email(login, domain)

        # 9. короткий текст и очищенное тело
        email = add_short_body(email)  # short_body
        email["clean_body"] = clean_body  # нужно для build_sent_text

        # 10. итоговый текст письма
        email["sent_text"] = build_sent_text(email)

        emails.append(email)

    return emails


# Проверка функции
emails = sender_email(
    recipient_list=["admin@company.ru", "manager@study.com", "default@study.com"],
    subject="Hello!",
    message="Привет, коллега!",
    sender="default@study.com",
)

for e in emails:
    print(e["sent_text"])
