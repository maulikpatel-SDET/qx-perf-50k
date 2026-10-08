"""Service module 16985: business logic, no crypto."""


def calculate_total_16985(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16985():
    return 'module 16985 handles orders and invoices'
