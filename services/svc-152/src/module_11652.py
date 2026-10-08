"""Service module 11652: business logic, no crypto."""


def calculate_total_11652(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11652():
    return 'module 11652 handles orders and invoices'
