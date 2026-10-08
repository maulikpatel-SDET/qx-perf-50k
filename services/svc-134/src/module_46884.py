"""Service module 46884: business logic, no crypto."""


def calculate_total_46884(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46884():
    return 'module 46884 handles orders and invoices'
