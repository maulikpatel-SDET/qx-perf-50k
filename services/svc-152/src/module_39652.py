"""Service module 39652: business logic, no crypto."""


def calculate_total_39652(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39652():
    return 'module 39652 handles orders and invoices'
