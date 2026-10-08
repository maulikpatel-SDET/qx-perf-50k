"""Service module 29396: business logic, no crypto."""


def calculate_total_29396(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29396():
    return 'module 29396 handles orders and invoices'
