"""Service module 42988: business logic, no crypto."""


def calculate_total_42988(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42988():
    return 'module 42988 handles orders and invoices'
