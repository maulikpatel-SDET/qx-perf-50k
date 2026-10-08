"""Service module 44396: business logic, no crypto."""


def calculate_total_44396(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44396():
    return 'module 44396 handles orders and invoices'
