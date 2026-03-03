from pathlib import Path

#Необходимые пути
my_home_path = Path.home() / "Desktop" / 'my_tasks'
my_home_path.mkdir(exist_ok=True)

#создание файла и записывание информации
with open(my_home_path / 'tasks.txt', 'w') as file:
    file.write('привет')
