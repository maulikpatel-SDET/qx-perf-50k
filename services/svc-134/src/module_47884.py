"""Service module 47884: business logic, no crypto."""


def calculate_total_47884(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47884():
    return 'module 47884 handles orders and invoices'
