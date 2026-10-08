"""Service module 35396: business logic, no crypto."""


def calculate_total_35396(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35396():
    return 'module 35396 handles orders and invoices'
