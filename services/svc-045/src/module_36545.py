"""Service module 36545: business logic, no crypto."""


def calculate_total_36545(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36545():
    return 'module 36545 handles orders and invoices'
