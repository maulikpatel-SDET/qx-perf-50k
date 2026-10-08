"""Service module 46652: business logic, no crypto."""


def calculate_total_46652(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46652():
    return 'module 46652 handles orders and invoices'
