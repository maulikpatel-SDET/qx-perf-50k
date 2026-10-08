"""Service module 32652: business logic, no crypto."""


def calculate_total_32652(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32652():
    return 'module 32652 handles orders and invoices'
