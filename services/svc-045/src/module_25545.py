"""Service module 25545: business logic, no crypto."""


def calculate_total_25545(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25545():
    return 'module 25545 handles orders and invoices'
