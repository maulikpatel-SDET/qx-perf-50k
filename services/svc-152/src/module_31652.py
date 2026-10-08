"""Service module 31652: business logic, no crypto."""


def calculate_total_31652(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31652():
    return 'module 31652 handles orders and invoices'
