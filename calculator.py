это наш комментарий

class Calculator:
    def __init__(self):
        self.last_result = None  # Переменная для хранения последнего результата

    def multiply(self, a: float, b: float) -> float:
        """Умножение двух чисел."""
        self.last_result = a * b
        return self.last_result

    def add(self, a, b):
        """Сложение двух чисел."""
        self.last_result = a + b
        return self.last_result

    def divide(self, a: float, b: float) -> float:
        """Деление двух чисел."""
        if b == 0:
            raise ValueError("Деление на ноль невозможно.")
        self.last_result = a / b
        return self.last_result

    def subtract(self, a: float, b: float) -> float:
        """Вычитание двух чисел."""
        self.last_result = a - b
        return self.last_result

    def print_last_res(self):
        """Печать последнего результата."""
        if self.last_result is not None:
            print(f"Последний результат: {self.last_result}")
        else:
            print("Никаких вычислений еще не было.")