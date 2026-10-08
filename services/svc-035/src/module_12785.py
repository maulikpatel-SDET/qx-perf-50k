"""Service module 12785: business logic, no crypto."""


def calculate_total_12785(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12785():
    return 'module 12785 handles orders and invoices'
