"""Service module 4652: business logic, no crypto."""


def calculate_total_4652(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4652():
    return 'module 4652 handles orders and invoices'
