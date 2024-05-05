"""Test the TodoJournal data type."""
# pylint: disable=missing-function-docstring
# pylint: disable=redefined-outer-name
# pylint: disable=protected-access
import json
import pytest
from src.TodoJournal import TodoJournal

@pytest.fixture
def tmpdir():
    filename = '../task4.json'
    with open(filename, "w", encoding="utf-8") as file:
        data = {"name": "test",
                "todos": []
                }
        json.dump(data, file)
    return filename

@pytest.fixture
def json_prepare():
    filename = '../task4.json'
    with open(filename, "w", encoding="utf-8") as file:
        data = {"name": "cosa io viglio fare oggi",
                "todos": [
                    "dormire",
                    "andare in chiesa",
                    "indulgere",
                    "lavare via i peccati",
                    "fare scherzi",
                    "litigare"]
                }
        json.dump(data, file)
    return filename




def test_len(json_prepare):
    """_len должен проверить количество задач"""
    filename = json_prepare
    journal = TodoJournal(filename)
    assert journal.__len__() == 6


def test_addentry(json_prepare):
    """_addentry должен показать, что новая задача была добавлена"""
    filename = json_prepare
    journal = TodoJournal(filename)
    journal.add_entry("comprare videogioco")
    assert journal._parse()["todos"][len(journal._parse()["todos"]) - 1] == "comprare videogioco"


def test_removeentry(json_prepare):
    """_removeentry должен показать, что задача была удалена"""
    filename = json_prepare
    journal = TodoJournal(filename)
    journal.remove_entry(len(journal._parse()["todos"]) - 1)
    assert len(journal._parse()["todos"]) == 5


def test_parse(json_prepare):
    """_parse должен получать данные о задачах из объекта TodoJournal"""
    filename = json_prepare
    arr = ["dormire",
        "andare in chiesa",
        "indulgere",
        "lavare via i peccati",
        "fare scherzi",
        "litigare"]
    journal = TodoJournal(filename)
    data = journal._parse()
    assert arr == data["todos"]


def test_init(json_prepare):
    """Проверка корректности инициализации TodoJournal"""
    expected_entries = ["dormire",
                    "andare in chiesa",
                    "indulgere",
                    "lavare via i peccati",
                    "fare scherzi",
                    "litigare"]
    expected_name = "cosa io viglio fare oggi"
    filename = json_prepare
    todo = TodoJournal(filename)
    entries = todo.entries
    name = todo.name

    assert entries == expected_entries
    assert name == expected_name


def test_create_journal(tmpdir):
    filename = tmpdir
    todo = TodoJournal(filename)

    expected_todo = {
            'name': 'test',
            'todos': []
        }

    TodoJournal.create(filename, "test")

    assert expected_todo == todo._parse()