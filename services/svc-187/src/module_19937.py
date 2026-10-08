"""Service module 19937: business logic, no crypto."""


def calculate_total_19937(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19937():
    return 'module 19937 handles orders and invoices'
