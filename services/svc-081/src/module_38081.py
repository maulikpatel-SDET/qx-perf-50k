"""Service module 38081: business logic, no crypto."""


def calculate_total_38081(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38081():
    return 'module 38081 handles orders and invoices'
