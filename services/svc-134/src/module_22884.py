"""Service module 22884: business logic, no crypto."""


def calculate_total_22884(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22884():
    return 'module 22884 handles orders and invoices'
