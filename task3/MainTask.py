import json
import sys


class TodoJournal:
    """
    Класс для представления журнала тудушек.
    ...
    Атрибуты
    --------
    name : str
        название тудушки
    path_todo : str
        путь к журналу

    Методы
    ------
    create(self):
        Создание тудушки
    add_entry(self, new_entry):
        Добавление тудушки
   remove_entry(self, index):
        Удаление тудушки
   _update(self, new_data):
        Обновление данных о тудушках
   _parse(self):
        Получение данных о тудушках
    """
    def __init__(self, path_todo, name):
        """
        Устанавливает все необходимые атрибуты для объекта TodoJournal.
        Параметры
        ---------
        name : str
            название тудушки
        path_todo : str
            путь к журналу
        """
        self.path_todo = path_todo
        self.name = name

    def create(self):
        """
        Копирует данные из объекта в json файл
        """
        try:
            with open(self.path_todo, "w", encoding='utf-8') as todo_file:
                json.dump(
                    {"name": self.name, "todos": []},
                    todo_file,
                    sort_keys=True,
                    indent=4,
                    ensure_ascii=False,
                )
        except FileNotFoundError as error:
            print(f"{error}")
            print(f"Не существует такой тудушки: {self.path_todo}")
            sys.exit(1)

        except PermissionError as error:
            # Обработка ошибок, связанных с разрешением на доступ к файлу
            print(f"{error}")
            print(f"У Вас нет прав на открытие данного файла! {self.path_todo}")
            sys.exit(2)

    def add_entry(self, new_entry):
        """
        добавляет новую тудушку в json файл

        Параметры
        ---------
        new_entry : str
            новая задача
        """
        data = self._parse()

        name = data["name"]
        todos = data["todos"]

        todos.append(new_entry)

        new_data = {
            "name": name,
            "todos": todos,
        }

        self._update(new_data)

    def remove_entry(self, index):
        """
        удаляет тудушку из json файла

        Параметры
        ---------
        index : int
            индекс удаляемой тудушки
        """
        data = self._parse()
        name = data["name"]
        todos = data["todos"]

        todos.remove(todos[index])

        new_data = {
            "name": name,
            "todos": todos,
        }

        self._update(new_data)

    def _update(self, new_data):
        """
        заполняет json файл новыми данными

        Параметры
        ---------
        new_data : str
            новые тудушки
        """
        try:
            with open(self.path_todo, "w", encoding='utf-8') as todo_file:
                json.dump(
                    new_data,
                    todo_file,
                    sort_keys=True,
                    indent=4,
                    ensure_ascii=False,
                )
        except FileNotFoundError as error:
            print(f"{error}")
            print(f"Не существует такой тудушки: {self.path_todo}")
            sys.exit(1)
        except PermissionError as error:
            # Обработка ошибок, связанных с разрешением на доступ к файлу
            print(f"{error}")
            print(f"У Вас нет прав на открытие данного файла! {self.path_todo}")
            sys.exit(2)

    def _parse(self):
        """
        чтение json файла
        Возвращаемое значение
        ---------------------
        str
        """
        try:
            with open(self.path_todo, 'r') as todo_file:
                data = json.load(todo_file)
            return data
        except FileNotFoundError as error:
            print(f"{error}")
            print(f"Не существует такой тудушки: {self.path_todo}")
            sys.exit(1)
        except PermissionError as error:
            # Обработка ошибок, связанных с разрешением на доступ к файлу
            print(f"{error}")
            print(f"У Вас нет прав на открытие данного файла! {self.path_todo}")
            sys.exit(2)


def main():
    pass

if __name__ == '__main__':
    main()
