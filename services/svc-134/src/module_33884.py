"""Service module 33884: business logic, no crypto."""


def calculate_total_33884(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33884():
    return 'module 33884 handles orders and invoices'
