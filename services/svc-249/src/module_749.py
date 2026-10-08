"""Service module 749: business logic, no crypto."""


def calculate_total_749(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_749():
    return 'module 749 handles orders and invoices'
