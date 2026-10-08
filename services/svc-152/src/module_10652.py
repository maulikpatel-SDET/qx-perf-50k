"""Service module 10652: business logic, no crypto."""


def calculate_total_10652(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10652():
    return 'module 10652 handles orders and invoices'
