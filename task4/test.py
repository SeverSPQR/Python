import Task4
def test_passing():
    assert (1, 2, 3) == (1, 2, 3)


def test_Len():
    myFirstJournal = Task4.TodoJournal('./task4.json','cosa io viglio fare oggi')
    assert len(myFirstJournal._parse()["todos"]) == 6

def test_AddEntry():
    myFirstJournal = Task4.TodoJournal('./task4.json','cosa io viglio fare oggi')
    myFirstJournal.add_entry("comprare videogioco")
    assert myFirstJournal._parse()["todos"][len(myFirstJournal._parse()["todos"]) - 1] == "comprare videogioco"

def test_RemoveEntryTest():
    myFirstJournal = Task4.TodoJournal('./task4.json','cosa io viglio fare oggi')
    myFirstJournal.remove_entry(len(myFirstJournal._parse()["todos"]) - 1)
    assert len(myFirstJournal._parse()["todos"]) == 6
