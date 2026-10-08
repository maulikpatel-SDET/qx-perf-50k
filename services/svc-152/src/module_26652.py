"""Service module 26652: business logic, no crypto."""


def calculate_total_26652(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26652():
    return 'module 26652 handles orders and invoices'
