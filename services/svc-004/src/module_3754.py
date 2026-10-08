"""Service module 3754: business logic, no crypto."""


def calculate_total_3754(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3754():
    return 'module 3754 handles orders and invoices'
