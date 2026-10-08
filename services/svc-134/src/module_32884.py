"""Service module 32884: business logic, no crypto."""


def calculate_total_32884(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32884():
    return 'module 32884 handles orders and invoices'
