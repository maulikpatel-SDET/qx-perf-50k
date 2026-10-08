"""Service module 45652: business logic, no crypto."""


def calculate_total_45652(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45652():
    return 'module 45652 handles orders and invoices'
