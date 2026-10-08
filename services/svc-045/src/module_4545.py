"""Service module 4545: business logic, no crypto."""


def calculate_total_4545(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4545():
    return 'module 4545 handles orders and invoices'
