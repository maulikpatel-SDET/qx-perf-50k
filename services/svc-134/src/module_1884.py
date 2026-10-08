"""Service module 1884: business logic, no crypto."""


def calculate_total_1884(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1884():
    return 'module 1884 handles orders and invoices'
