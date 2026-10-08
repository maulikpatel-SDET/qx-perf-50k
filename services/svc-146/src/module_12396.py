"""Service module 12396: business logic, no crypto."""


def calculate_total_12396(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12396():
    return 'module 12396 handles orders and invoices'
