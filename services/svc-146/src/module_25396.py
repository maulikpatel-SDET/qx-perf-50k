"""Service module 25396: business logic, no crypto."""


def calculate_total_25396(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25396():
    return 'module 25396 handles orders and invoices'
