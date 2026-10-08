"""Service module 2754: business logic, no crypto."""


def calculate_total_2754(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2754():
    return 'module 2754 handles orders and invoices'
