"""Service module 46396: business logic, no crypto."""


def calculate_total_46396(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46396():
    return 'module 46396 handles orders and invoices'
