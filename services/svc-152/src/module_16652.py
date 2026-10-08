"""Service module 16652: business logic, no crypto."""


def calculate_total_16652(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16652():
    return 'module 16652 handles orders and invoices'
