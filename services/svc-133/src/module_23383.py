"""Service module 23383: business logic, no crypto."""


def calculate_total_23383(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23383():
    return 'module 23383 handles orders and invoices'
