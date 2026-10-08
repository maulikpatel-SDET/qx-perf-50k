"""Service module 29652: business logic, no crypto."""


def calculate_total_29652(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29652():
    return 'module 29652 handles orders and invoices'
