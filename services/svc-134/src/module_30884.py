"""Service module 30884: business logic, no crypto."""


def calculate_total_30884(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30884():
    return 'module 30884 handles orders and invoices'
