"""Service module 38396: business logic, no crypto."""


def calculate_total_38396(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38396():
    return 'module 38396 handles orders and invoices'
