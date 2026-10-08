"""Service module 47396: business logic, no crypto."""


def calculate_total_47396(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47396():
    return 'module 47396 handles orders and invoices'
