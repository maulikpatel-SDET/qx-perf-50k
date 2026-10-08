"""Service module 13652: business logic, no crypto."""


def calculate_total_13652(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13652():
    return 'module 13652 handles orders and invoices'
