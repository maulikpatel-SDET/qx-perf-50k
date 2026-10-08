"""Service module 14754: business logic, no crypto."""


def calculate_total_14754(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14754():
    return 'module 14754 handles orders and invoices'
