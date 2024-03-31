import Task4


def test_passing():
    assert (1, 2, 3) == (1, 2, 3)


def test_len():
    journal = Task4.TodoJournal('./task4.json','cosa io viglio fare oggi')
    assert len(journal._parse()["todos"]) == 6


def test_addentry():
    journal = Task4.TodoJournal('./task4.json','cosa io viglio fare oggi')
    journal.add_entry("comprare videogioco")
    assert journal._parse()["todos"][len(journal._parse()["todos"]) - 1] == "comprare videogioco"


def test_removeentrytest():
    journal = Task4.TodoJournal('./task4.json','cosa io viglio fare oggi')
    journal.remove_entry(len(journal._parse()["todos"]) - 1)
    assert len(journal._parse()["todos"]) == 6
