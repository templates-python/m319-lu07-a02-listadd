import main


def test_while_existing(capsys, monkeypatch):
    inputs = iter(['pineapple'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    main.while_else()
    output = capsys.readouterr().out
    assert 'Frucht bereits vorhanden' in output


def test_while_new(capsys, monkeypatch):
    inputs = iter(['apple'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    main.while_else()
    output = capsys.readouterr().out
    assert output == "Inhalt der Liste: ['papaya', 'banana', 'pineapple', 'mango', 'grapes', 'apple']\n"


def test_in_existing(capsys, monkeypatch):
    inputs = iter(['mango'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    main.if_in()
    output = capsys.readouterr().out
    assert 'Frucht bereits vorhanden' in output


def test_in_new(capsys, monkeypatch):
    inputs = iter(['pear'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    main.if_in()
    output = capsys.readouterr().out
    assert output == "Inhalt der Liste: ['papaya', 'banana', 'pineapple', 'mango', 'grapes', 'pear']\n"
