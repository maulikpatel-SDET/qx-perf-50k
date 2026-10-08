"""Service module 49545: business logic, no crypto."""


def calculate_total_49545(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49545():
    return 'module 49545 handles orders and invoices'
