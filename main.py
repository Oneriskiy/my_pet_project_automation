from pathlib import Path
import logging
import time
from datetime import datetime as d

# Необходимые пути
try:
    my_home_path = Path.home() / "Desktop" / "my_tasks"
    my_home_path.mkdir(exist_ok=True)
except FileNotFoundError:
    print("путь не найден!")
    exit()

# настройка логгирования
debug_h = logging.FileHandler(filename=my_home_path / "logs.log", mode="a")
debug_h.setLevel(level=logging.DEBUG)
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
debug_h.setFormatter(formatter)
logging.basicConfig(level=logging.DEBUG, handlers=[debug_h])


def menu():
    """Основное меню"""
    asc_menu = int(
        input(
            """
    Добро пожаловать! Выберите действие:
    1 - Посмотреть задачи
    2 - Добавить новую
    """.strip()
        )
    )
    if asc_menu == 1:
        logging.debug("открытие списка задач")
        check_tasks()
    if asc_menu == 2:
        logging.debug("открытие инструмента создания новых задач")
        creation_task()


def check_tasks():
    """Вывод всех задач"""
    with open(my_home_path / "tasks.txt") as file:
        logging.debug("открытие списка задач")
        print(file.read())


def creation_task():
    """создание файла и записывание информации"""
    asc_user_task = input("вставь название задачи: ")
    asc_user_description_task = input("вставь описание задачи: ")
    logging.debug("записываю информацию...")
    with open(my_home_path / "tasks.txt", "a") as file:
        file.write(
            time_now + " - " + asc_user_task + " - " + asc_user_description_task + "\n"
        )
        time.sleep(0.5)
    try:
        asc_ = int(
            input(
                """
        Желаете добавить доп.информацию?"
        1 - добавить дедлайн                         
        2 - добавить ключевые слова
                                 """.strip()
            )
        )
    except ValueError:
        logging.debug("информация записанна")
        exit()
    if asc_ == 1:
        creation_deadline()
    if asc_ == 2:
        creation_words()


def creation_deadline():
    """Добавление дедлайна"""
    deadline = input("Введите дедлайн в формате - ДД.ММ.ГГ: ")
    with open(my_home_path / "tasks.txt", "a") as file:
        file.write(f"Дедлайн - {deadline}\n")
        logging.debug("добавлен дедлайн")


def creation_words():
    """Добавление ключевых слов"""
    words = input("Введите ключевые слова: ")
    with open(my_home_path / "tasks.txt", "a") as file:
        file.write(f"Ключевые слова - {words}\n")
        logging.debug("добавлены ключевые слова")


if __name__ == "__main__":
    time_now = d.now().strftime("%m.%d %H:%M")
    menu()
