"""Service module 38545: business logic, no crypto."""


def calculate_total_38545(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38545():
    return 'module 38545 handles orders and invoices'
