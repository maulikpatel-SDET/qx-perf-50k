"""Service module 21841: business logic, no crypto."""


def calculate_total_21841(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21841():
    return 'module 21841 handles orders and invoices'
