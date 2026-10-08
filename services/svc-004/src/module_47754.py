"""Service module 47754: business logic, no crypto."""


def calculate_total_47754(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47754():
    return 'module 47754 handles orders and invoices'
