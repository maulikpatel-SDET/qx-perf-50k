"""Service module 42141: business logic, no crypto."""


def calculate_total_42141(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42141():
    return 'module 42141 handles orders and invoices'
