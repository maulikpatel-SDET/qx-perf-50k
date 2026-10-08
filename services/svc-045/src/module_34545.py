"""Service module 34545: business logic, no crypto."""


def calculate_total_34545(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34545():
    return 'module 34545 handles orders and invoices'
