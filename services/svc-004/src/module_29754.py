"""Service module 29754: business logic, no crypto."""


def calculate_total_29754(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29754():
    return 'module 29754 handles orders and invoices'
