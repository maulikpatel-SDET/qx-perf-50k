"""Service module 48884: business logic, no crypto."""


def calculate_total_48884(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48884():
    return 'module 48884 handles orders and invoices'
