"""Service module 42908: business logic, no crypto."""


def calculate_total_42908(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42908():
    return 'module 42908 handles orders and invoices'
