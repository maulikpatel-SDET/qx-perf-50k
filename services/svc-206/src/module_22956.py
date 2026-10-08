"""Service module 22956: business logic, no crypto."""


def calculate_total_22956(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22956():
    return 'module 22956 handles orders and invoices'
