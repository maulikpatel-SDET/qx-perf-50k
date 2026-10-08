"""Service module 16125: business logic, no crypto."""


def calculate_total_16125(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16125():
    return 'module 16125 handles orders and invoices'
