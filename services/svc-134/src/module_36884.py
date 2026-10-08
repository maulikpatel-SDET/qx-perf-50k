"""Service module 36884: business logic, no crypto."""


def calculate_total_36884(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36884():
    return 'module 36884 handles orders and invoices'
