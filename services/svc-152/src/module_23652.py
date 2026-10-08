"""Service module 23652: business logic, no crypto."""


def calculate_total_23652(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23652():
    return 'module 23652 handles orders and invoices'
