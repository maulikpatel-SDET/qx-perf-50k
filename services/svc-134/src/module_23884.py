"""Service module 23884: business logic, no crypto."""


def calculate_total_23884(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23884():
    return 'module 23884 handles orders and invoices'
