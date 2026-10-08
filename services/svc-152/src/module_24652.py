"""Service module 24652: business logic, no crypto."""


def calculate_total_24652(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24652():
    return 'module 24652 handles orders and invoices'
