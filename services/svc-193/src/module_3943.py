"""Service module 3943: business logic, no crypto."""


def calculate_total_3943(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3943():
    return 'module 3943 handles orders and invoices'
