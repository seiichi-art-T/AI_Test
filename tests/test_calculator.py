from calculator import add, subtract, multiply, divide

def test_calculator():
    assert add(10, 5) == 15, "Addition failed"
    assert subtract(10, 5) == 5, "Subtraction failed"
    assert multiply(10, 5) == 50, "Multiplication failed"
    assert divide(10, 5) == 2, "Division failed"
    assert divide(10, 0) == "Error! Division by zero.", "Divide by zero failed"
    print("All tests passed!")

if __name__ == "__main__":
    test_calculator()