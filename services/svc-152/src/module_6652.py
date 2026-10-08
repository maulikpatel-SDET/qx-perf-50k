"""Service module 6652: business logic, no crypto."""


def calculate_total_6652(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6652():
    return 'module 6652 handles orders and invoices'
