"""Service module 10952: business logic, no crypto."""


def calculate_total_10952(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10952():
    return 'module 10952 handles orders and invoices'
