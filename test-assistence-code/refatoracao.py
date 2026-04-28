from typing import List, Tuple


def calculate_statistics(numbers: List[float]) -> Tuple[float, float, float, float]:
    """Retorna soma, média, maior e menor valor de uma lista de números."""
    if not numbers:
        raise ValueError("A lista de números não pode estar vazia.")

    total = sum(numbers)
    average = total / len(numbers)
    maximum = max(numbers)
    minimum = min(numbers)

    return total, average, maximum, minimum


if __name__ == "__main__":
    values = [23, 7, 45, 2, 67, 12, 89, 34, 56, 11]
    total, average, maximum, minimum = calculate_statistics(values)

    print("total:", total)
    print("media:", average)
    print("maior:", maximum)
    print("menor:", minimum)
