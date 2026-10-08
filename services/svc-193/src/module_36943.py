"""Service module 36943: business logic, no crypto."""


def calculate_total_36943(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36943():
    return 'module 36943 handles orders and invoices'
