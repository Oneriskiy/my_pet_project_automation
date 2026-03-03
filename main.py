from pathlib import Path
import logging

#Необходимые пути
try:
    my_home_path = Path.home() / "Desktop" / 'my_tasks'
    my_home_path.mkdir(exist_ok=True)
except FileNotFoundError:
    print('путь не найден!')
    exit()

#настройка логгирования
debug_h = logging.FileHandler(filename = my_home_path / 'logs.log', mode='a')
debug_h.setLevel(level=logging.DEBUG)
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
debug_h.setFormatter(formatter)
logging.basicConfig(level=logging.DEBUG, handlers=[debug_h])

#создание файла и записывание информации
def creation_task(asc_first, asc_second):
    logging.debug('записываю информацию...')
    with open(my_home_path / 'tasks.txt', 'a') as file:
        file.write(asc_first + ' - ' + asc_second + '\n')
        logging.debug('информация записана')

if __name__ == '__main__':
    asc_user_task = input('вставь название задачи: ')
    asc_user_description_task = input('вставь описание задачи: ')
    creation_task(asc_user_task, asc_user_description_task)