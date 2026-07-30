from src.calculator import add, subtract, multiply, divide, main
from unittest.mock import patch
import io

def test_add():
    assert add(10, 5) == 15
    assert add(-1, 1) == 0
    assert add(-1, -1) == -2
    assert add(1.5, 2.5) == 4.0

def test_subtract():
    assert subtract(10, 5) == 5
    assert subtract(5, 10) == -5
    assert subtract(-1, -1) == 0

def test_multiply():
    assert multiply(10, 5) == 50
    assert multiply(-2, 3) == -6
    assert multiply(-2, -3) == 6
    assert multiply(0, 10) == 0

def test_divide():
    assert divide(10, 5) == 2
    assert divide(10, 4) == 2.5
    assert divide(10, 0) == "Error! Division by zero."

@patch('builtins.input')
@patch('sys.stdout', new_callable=io.StringIO)
def test_main_quit(mock_stdout, mock_input):
    mock_input.side_effect = ['q']
    main()
    assert "Exiting calculator. Goodbye!" in mock_stdout.getvalue()

@patch('builtins.input')
@patch('sys.stdout', new_callable=io.StringIO)
def test_main_add(mock_stdout, mock_input):
    mock_input.side_effect = ['1', '10', '5', 'q']
    main()
    assert "10.0 + 5.0 = 15.0" in mock_stdout.getvalue()

@patch('builtins.input')
@patch('sys.stdout', new_callable=io.StringIO)
def test_main_subtract(mock_stdout, mock_input):
    mock_input.side_effect = ['2', '10', '5', 'q']
    main()
    assert "10.0 - 5.0 = 5.0" in mock_stdout.getvalue()

@patch('builtins.input')
@patch('sys.stdout', new_callable=io.StringIO)
def test_main_multiply(mock_stdout, mock_input):
    mock_input.side_effect = ['3', '10', '5', 'q']
    main()
    assert "10.0 * 5.0 = 50.0" in mock_stdout.getvalue()

@patch('builtins.input')
@patch('sys.stdout', new_callable=io.StringIO)
def test_main_divide(mock_stdout, mock_input):
    mock_input.side_effect = ['4', '10', '5', 'q']
    main()
    assert "10.0 / 5.0 = 2.0" in mock_stdout.getvalue()

@patch('builtins.input')
@patch('sys.stdout', new_callable=io.StringIO)
def test_main_divide_by_zero(mock_stdout, mock_input):
    mock_input.side_effect = ['4', '10', '0', 'q']
    main()
    assert "10.0 / 0.0 = Error! Division by zero." in mock_stdout.getvalue()

@patch('builtins.input')
@patch('sys.stdout', new_callable=io.StringIO)
def test_main_invalid_number(mock_stdout, mock_input):
    # Test invalid numeric input then a valid one to ensure it continues
    # Correct sequence: Choice '1' -> Invalid Num1 -> Choice '1' -> Valid Num1 -> Valid Num2 -> Quit
    mock_input.side_effect = ['1', 'abc', '1', '10', '5', 'q']
    main()
    assert "Invalid input. Please enter numeric values." in mock_stdout.getvalue()
    assert "10.0 + 5.0 = 15.0" in mock_stdout.getvalue()

@patch('builtins.input')
@patch('sys.stdout', new_callable=io.StringIO)
def test_main_invalid_choice(mock_stdout, mock_input):
    mock_input.side_effect = ['5', 'q']
    main()
    assert "Invalid Input" in mock_stdout.getvalue()