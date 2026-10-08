"""Service module 41396: business logic, no crypto."""


def calculate_total_41396(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41396():
    return 'module 41396 handles orders and invoices'
