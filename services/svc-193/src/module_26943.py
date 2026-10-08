"""Service module 26943: business logic, no crypto."""


def calculate_total_26943(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26943():
    return 'module 26943 handles orders and invoices'
