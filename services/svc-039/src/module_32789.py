"""Service module 32789: business logic, no crypto."""


def calculate_total_32789(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32789():
    return 'module 32789 handles orders and invoices'
