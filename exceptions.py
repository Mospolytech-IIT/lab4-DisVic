"""
Этот модуль демонстрирует работу с пользовательскими исключениями,
обработкой файлов и различными техниками обработки исключений.
"""

# 6. Пользовательские исключения
class NegativeValueError(Exception):
    """Пользовательское исключение для отрицательных значений."""

    def __init__(self, value):
        super().__init__(f"Значение {value} является отрицательным, что недопустимо.")
        self.value = value


class DivisionByZeroError(Exception):
    """Пользовательское исключение для деления на ноль."""

    def __init__(self):
        super().__init__("Попытка деления на ноль, что недопустимо.")


class EmptyDataError(Exception):
    """Пользовательское исключение для пустых данных."""

    def __init__(self, file_path):
        super().__init__(f"Файл '{file_path}' пуст.")
        self.file_path = file_path

# 1 и 8. Минимум 2 разные функции, выбрасывающие исключения без обработчиков
def power(base, exponent):
    """
    Возводит число в степень.

    Args:
        base (int/float): Основание степени.
        exponent (int): Показатель степени.

    Returns:
        float: Результат возведения числа в степень.

    Raises:
        NegativeValueError: Если показатель степени отрицательный.
    """
    # Если закомментировать две следующих строки, то будут выдаваться ошибки в консоль при выполнении программы
    if exponent < 0:
        raise NegativeValueError(exponent)
    return base ** exponent

# 1 и 8
def divide(a, b):
    """
    Делит два числа.

    Args:
        a (int/float): Числитель.
        b (int/float): Знаменатель.

    Returns:
        float: Результат деления.

    Raises:
        DivisionByZeroError: Если знаменатель равен нулю.
    """
    #Если закомментировать две следующих строки, то будут выдаваться ошибки в консоль при выполнении программы
    if b == 0:
        raise DivisionByZeroError()
    return a / b

#  2 и 8. Функция с одним обработчиком исключений общего типа
def safe_divide(a, b):
    """
    Безопасно делит два числа с обработкой исключений.

    Args:
        a (int/float): Числитель.
        b (int/float): Знаменатель.

    Returns:
        float or None: Результат деления или None, если возникла ошибка.
    """
    try:
        return divide(a, b)
    except DivisionByZeroError as error:
        print(f"Ошибка: {error}")
        return None

# 3. Функция с одним обработчиком исключений и блоком finally
def open_and_read_file(file_path):
    """
    Читает содержимое файла.

    Args:
        file_path (str): Путь к файлу.

    Returns:
        str: Содержимое файла.

    Raises:
        FileNotFoundError: Если файл не существует.
        EmptyDataError: Если файл пуст.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            if not content:
                raise EmptyDataError(file_path)
            return content
    except FileNotFoundError as error:
        print(f"Ошибка файла: {error}")
    except EmptyDataError as error:
        print(f"Ошибка данных: {error}")
    return None

# 4. Три функции с обработкой различных типов исключений
def read_integer(value):
    """
    Преобразует значение в целое число.

    Args:
        value: Входное значение.

    Returns:
        int or None: Целое число или None, если возникла ошибка.

    Raises:
        NegativeValueError: Если значение отрицательное.
    """
    try:
        number = int(value)
        if number < 0:
            raise NegativeValueError(number)
        return number
    except (ValueError, TypeError) as error:
        print(f"Ошибка преобразования: {error}")
        return None
    except NegativeValueError as error:
        print(f"Ошибка проверки: {error}")
        return None

def compute_operations(a, b, exponent):
    """
    Выполняет деление и возводит результат в степень.

    Args:
        a (int/float): Числитель.
        b (int/float): Знаменатель.
        exponent (int): Показатель степени.

    Returns:
        float or None: Результат или None, если возникла ошибка.
    """
    try:
        division_result = divide(a, b)
        return power(division_result, exponent)
    except (DivisionByZeroError, NegativeValueError) as error:
        print(f"Ошибка операции: {error}")
        return None

# 5 и 4. Функция с генерацией и обработкой исключений
def complex_calculation(x, y):
    """
    Выполняет сложное вычисление, связанное с делением.

    Args:
        x (int/float): Делимое.
        y (int/float): Делитель.

    Returns:
        float or None: Результат или None, если возникла ошибка.

    Raises:
        NegativeValueError: Если x отрицательное.
    """
    try:
        if x < 0:
            raise NegativeValueError(x)
        return divide(x, y)
    except (NegativeValueError, DivisionByZeroError) as error:
        print(f"Ошибка вычисления: {error}")
        return None

# 7. Функция, выбрасывающая пользовательское исключение
def process_value(value):
    """
    Обрабатывает значение путем выполнения деления.

    Args:
        value (int/float): Входное значение.

    Returns:
        float or None: Результат или None, если возникла ошибка.
    """
    try:
        if value < 0:
            raise NegativeValueError(value)
        if value == 0:
            raise DivisionByZeroError()
        return 100 / value
    except (NegativeValueError, DivisionByZeroError) as error:
        print(f"Ошибка обработки значения: {error}")
        return None

# 9. Функция, которая последовательно вызывает ВСЕ выше созданные функции
def execute_all_functions():
    """
    Последовательно выполняет все ранее определенные функции.
    """
    try:
        print("Результат возведения в степень:", power(2, 3))
    except NegativeValueError as error:
        print(error)

    try:
        print("Результат деления:", divide(10, 2))
    except DivisionByZeroError as error:
        print(error)

    print("Результат безопасного деления:", safe_divide(10, 0))
    print("Результат чтения числа:", read_integer("123"))

    try:
        print("Содержимое файла:", open_and_read_file("example.txt"))
    except (FileNotFoundError, EmptyDataError) as error:
        print(error)

    print("Результат вычислений:", compute_operations(10, 2, 3))
    print("Результат сложного вычисления:", complex_calculation(10, 5))
    print("Результат обработки значения:", process_value(5))
