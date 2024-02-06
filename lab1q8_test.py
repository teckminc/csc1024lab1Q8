import lab1q8
from io import StringIO
from sys import stderr
def test_case1(monkeypatch, capsys):
    number_inputs = StringIO('5\n')

    monkeypatch.setattr('sys.stdin', number_inputs)
    lab1q8.main()
    captured_stdout, captured_stderr = capsys.readouterr()

    assert captured_stdout.strip().find(f'{75}') != -1


def test_case2(monkeypatch, capsys):
    number_inputs = StringIO('15\n')

    monkeypatch.setattr('sys.stdin', number_inputs)
    lab1q8.main()
    captured_stdout, captured_stderr = capsys.readouterr()

    assert captured_stdout.strip().find(f'{300}') != -1
