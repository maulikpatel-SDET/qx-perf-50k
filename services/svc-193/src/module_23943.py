"""Service module 23943: business logic, no crypto."""


def calculate_total_23943(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23943():
    return 'module 23943 handles orders and invoices'
