"""Service module 2545: business logic, no crypto."""


def calculate_total_2545(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2545():
    return 'module 2545 handles orders and invoices'
