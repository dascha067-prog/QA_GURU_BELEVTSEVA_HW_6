from datetime import date

# 1. Нормализация email адресов

# Создаю словарь письма
email = {
    "subject": "Project meeting",
    "from": " Manager@Example.com ",  # специально добавила пробелы и разные буквы
    "to": " Daria@Example.com ",
    "body": "Hi Daria! Reminder: meeting at 15:00. See you!"
}


# Создаю функцию нормализации email-адресов
def normalize_addresses(email: dict) -> dict:
    normalized_email = email.copy()  # создаю копию, чтобы не менять оригинал
    normalized_email["from"] = email["from"].strip().lower()
    normalized_email["to"] = email["to"].strip().lower()
    return normalized_email


#  Вызываю функцию
normalized_email = normalize_addresses(email)

#  Проверяю результат
print(normalized_email)


# 2. Сокращенная версия тела письма
def add_short_body(email: dict) -> dict:
    short_email = email.copy()  # создаю копию, чтобы не портить оригинал
    short_email["short_body"] = email["body"][:10] + "..."  # добавляю новое поле
    return short_email  # возвращаю новый словарь


email_with_short = add_short_body(email)

print(email_with_short)


# 3. Очистка текста письма
def clean_body_text(body: str) -> str:
    clean_text = body.replace("\n", " ").replace("\t", " ")
    return clean_text


# Добавляю очищенный текст
email["clean_body"] = clean_body_text(email["body"])

# Проверяю результат
print(email)


# 4. Формирование итогового текста письма
def build_sent_text(email: dict) -> str:
    sent_text = f"""Кому: {email["to"]}, от {email["from"]}    # создаю многострочную f-строку для красивого вывода письма
    Тема: {email["subject"]}, дата {email["date"]} {email["clean_body"]}"""
    return sent_text


# Добавляю дату вручную
email["date"] = "2025-11-05"

# Формирую итоговое письмо
email["sent_text"] = build_sent_text(email)

# Вывожу финальный результат
print(email["sent_text"])


# 5. Проверка пустоты темы и тела
def check_empty_fields(email: dict) -> tuple[bool, bool]:
    # убираю пробелы по краям и проверяю: если строка пустая → True
    is_subject_empty = not email["subject"].strip()  # проверяю тему
    is_body_empty = not email["body"].strip()  # проверяю тело

    # возвращаю оба результата как пару (кортеж)
    return is_subject_empty, is_body_empty


is_subject_empty, is_body_empty = check_empty_fields(email)

# вывожу результаты проверки
print("Пустая тема письма:", is_subject_empty)
print("Пустое тело письма:", is_body_empty)


# 6. Маска email отправителя
def mask_sender_email(login: str, domain: str) -> str:
    # беру первые 2 буквы логина и добавляю маску
    masked_email = login[:2] + "***@" + domain
    return masked_email


# Пример работы функции маски
sender = "manager@example.com"  # исходный адрес
login, domain = sender.split("@")  # разделяю логин и домен
masked = mask_sender_email(login, domain)  # создаю маску через функцию
print("Маска отправителя:", masked)


# 7. Проверка корректности email адресов
def get_correct_email(email_list: list[str]) -> list[str]:
    correct_emails = []  # создаю пустой список для корректных адресов

    for email in email_list:
        # убираю пробелы и перевожу в нижний регистр
        clean_email = email.strip().lower()

        # проверяю наличие '@' и корректное окончание
        if "@" in clean_email and clean_email.endswith((".com", ".ru", ".net")):
            correct_emails.append(clean_email)  # добавляю валидный адрес

    return correct_emails


# Проверка функции
test_emails = [
    "user@gmail.com",
    "admin@company.ru",
    "test_123@service.net",
    "Example.User@domain.com",
    "user@domain.org",  # неправильный домен
    "usergmail.com",  # нет символа @
    "@mail.ru",  # странный, но по условию пройдёт
    "name@.com",  # странный, но тоже пройдёт
    "",  # пустая строка
]

correct_list = get_correct_email(test_emails)
print("Корректные email-адреса:", correct_list)


# 8. Создание словаря письма
def create_email(sender: str, recipient: str, subject: str, body: str) -> dict:
    email = {
        "sender": sender,  # адрес отправителя
        "recipient": recipient,  # адрес получателя
        "subject": subject,  # тема письма
        "body": body  # текст письма
    }

    # возвращаю готовый словарь письма
    return email


# Проверка
my_email = create_email(
    sender="manager@example.com",
    recipient="daria@example.com",
    subject="Project update",
    body="Hi Daria! The report is ready. Please check it."
)

# вывожу результат
print(my_email)


# 9. Добавление даты отправки
def add_send_date(email: dict) -> dict:
    # создаю переменную с текущей датой и перевожу её в нужный формат
    send_date = date.today().strftime("%Y-%m-%d")

    # добавляю новую пару "date": дата в словарь email
    email["date"] = send_date

    # возвращаю обновлённый словарь
    return email


#  Проверка
email = {
    "sender": "manager@example.com",
    "recipient": "daria@example.com",
    "subject": "Project update",
    "body": "Hi Daria! The report is ready. Please check it."
}

# вызываю функцию и сохраняю результат
email = add_send_date(email)

# вывожу результат
print(email)


# 10. Получение логина и домена
def extract_login_domain(address: str) -> tuple[str, str]:
    """
    Возвращает логин и домен отправителя.
    Пример: "user@mail.ru" -> ("user", "mail.ru")
    """
    # делю адрес на две части: логин (до @) и домен (после @)
    login, domain = address.split("@")

    # возвращаю обе части как кортеж (два значения)
    return login, domain


#  Проверка
email = {"from": "manager@example.com"}  # пример письма

# получаю логин и домен из адреса отправителя
login, domain = extract_login_domain(email["from"])

print("Логин отправителя:", login)
print("Домен отправителя:", domain)
