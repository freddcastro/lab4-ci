from fib import fibonacci


# Casos de prueba para la función de Fibonacci
def test_first_fibonacci():
    assert fibonacci(1) == 1


def test_zero_fibonacci():
    assert fibonacci(0) == 0

def test_second_fibonacci():
    assert fibonacci(2) == 1
