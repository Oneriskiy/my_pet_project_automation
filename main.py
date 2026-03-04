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


class Status:
    def __init__(self, asc_user_task, asc_user_description_task):
        self.asc_user_task = asc_user_task
        self.asc_user_description_task = asc_user_description_task

    def __str__(self):
        return f" Название задачи: {self.asc_user_task} | Описание задачи: {self.asc_user_description_task}"


list_tasks = []


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


def load_tasks():
    """загрузка задач из файла в список"""
    global my_home_path
    path = my_home_path / "tasks.txt"
    if not path.exists():
        return
    with open(path, "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            parts = line.split("|")
            if len(parts) != 3:
                continue
            time_now, task_name, task_desc = parts
            list_tasks.append(Status(task_name, task_desc))


def check_tasks():
    if not list_tasks: print("Список задач пуст!")

    """Вывод всех задач"""
    for i in list_tasks:
        print(i)



def creation_task():
    """создание файла и записывание информации"""
    time_now = d.now().strftime("%m.%d %H:%M")
    asc_user_task = input("вставь название задачи: ")
    asc_user_description_task = input("вставь описание задачи: ")
    list_tasks.append(Status(asc_user_task, asc_user_description_task))
    logging.debug("записываю информацию...")
    with open(my_home_path / "tasks.txt", "a") as file:
        file.write(f"{time_now}|{asc_user_task}|{asc_user_description_task}\n")
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
    key_words = input("Введите ключевые слова: ")
    with open(my_home_path / "tasks.txt", "a") as file:
        file.write(f"Ключевые слова - {key_words}\n")
        logging.debug("добавлены ключевые слова")


if __name__ == "__main__":
    load_tasks()
    menu()
