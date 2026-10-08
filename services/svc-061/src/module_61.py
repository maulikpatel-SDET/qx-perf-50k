"""Service module 61: business logic, no crypto."""


def calculate_total_61(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_61():
    return 'module 61 handles orders and invoices'
