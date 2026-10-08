"""Service module 42133: business logic, no crypto."""


def calculate_total_42133(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42133():
    return 'module 42133 handles orders and invoices'
