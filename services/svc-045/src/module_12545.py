"""Service module 12545: business logic, no crypto."""


def calculate_total_12545(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12545():
    return 'module 12545 handles orders and invoices'
