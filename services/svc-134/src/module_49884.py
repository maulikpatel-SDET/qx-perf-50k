"""Service module 49884: business logic, no crypto."""


def calculate_total_49884(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49884():
    return 'module 49884 handles orders and invoices'
