"""Service module 31840: business logic, no crypto."""


def calculate_total_31840(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31840():
    return 'module 31840 handles orders and invoices'
