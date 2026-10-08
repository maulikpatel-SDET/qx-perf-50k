"""Service module 21652: business logic, no crypto."""


def calculate_total_21652(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21652():
    return 'module 21652 handles orders and invoices'
